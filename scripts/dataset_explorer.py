import pandas as pd

import re
from pprint import pprint


class SODataSetExplorer:
    """
    Helper class for loading stackoverflow datasets.
    """
    
    datasets = {}
    
    def __init__(self, years=[], format_col_names=True):
        """
        Class constructor.
        Args:
            - years: list of numbers representing years in the range [2011, 2020].
            - format_col_names: boolean. If true formats dataset columns to snake case.
        Return:
            - SODataSetExplorer instance.
        """
        self.datasets = self.load(years, format_col_names)


    def camel_to_snake(self, name: str):
        """
        Convert strings to snake case format
        Args: 
            - name: unformated string to be handled.
        Return:
            - None
        """
        # https://stackoverflow.com/a/1176023
        name = name.replace(' ', '_').replace("'", '').replace(':', '_').replace('?','')
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub('_+', r'_', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


    def load(self, years=[], format_col_names=True):
        """
        Import all stackoverflow datasets in dict-like manner (key: year, val: df).
        Args: 
            - years: list of dataframes to load. If none provided all datasets will be load
            - format_col_names: boolean. If True all column names will be format to snake_case
        Return:
            - key, value pair: year agains as key, load df as value.
        """
        years = years or list(range(2011,2021))
        dataset_base_file_name = 'stack_overflow_datasets/survey_results_'

        dfs = {}
        for year in years:
            name = f'{dataset_base_file_name}{year}.csv'
            # TODO: for the original datasets encoding should be "ISO-8859-1" to avoid errors
            df = pd.read_csv(name, dtype=object)
            if format_col_names:
                df.columns = map(lambda name: self.camel_to_snake(name), df.columns)
            df['year'] = year
            dfs[year] = df

        return dfs


    def dataset_cols_difference(self, base_year: int, years_against=[], display_difference=True):
        """
        Compares features present in a given year and its presence or absence in the other.
        Args:
            - base_year: features within this year are compare against other years.
            - years_against: list of year to compare with.
            - display_difference: boolean. Print the difference by default.
        Return:
            - key, value pair: year_compared agains as key, column difference as value.
        """
        df_to_compare_with = self.datasets

        if years_against:
            df_to_compare_with = { year: self.datasets[year] for year in years_against }

        columns_to_compare = set(self.datasets[base_year].columns.tolist())

        column_differences = {}
        for compared_year, compared_df in df_to_compare_with.items():
            if compared_year <= base_year: continue
            columns = compared_df.columns.tolist()
            difference = columns_to_compare - set(columns)

            column_differences[compared_year] = difference

            if display_difference:
                print(f'{base_year} columns not present in {compared_year}')
                pprint(difference)
                print('\n')
                
        return column_differences


    def similar_columns(self, columns: list, years=[], display_similar=True):
        """
        Given a list of features displays similar columns per year.
        Args:
            - columns: list of features to look for in each year.
            - years: list of years to compare with.
            - display_similar: boolean. Print the similar features by default.
        Return:
            - key, value pair: year as key, similar set as value.
        """
        df_to_compare_with = self.datasets

        if years:
            df_to_compare_with = { year: self.datasets[year] for year in years }
        
        similar_per_year = {}
        for year, df in df_to_compare_with.items():

            similar = set()
            for name in columns:
                similar.update([col for col in df.columns.tolist() if name in col])
                
            similar_per_year[year] = similar

            if display_similar and similar:
                print(year)
                pprint(similar)
                print('\n')
                
        return similar_per_year


    def rename_columns(self, column_rename: {}, by_year=False):
        """
        Rename df columns across years given a dict columns mapping.
        Args:
            - column_rename: dict with feature_name as key and new_feature_name as value.
            - by_year: When True, the column_rename dict should have the following structure: 
                {
                    'new_column_name': 'new_feature_name',
                    'year_map': {
                        [yeart]: 'feature_name',
                        ...
                    }
                }
        Return:
            - None. Modifies the SODataSetExplorer instance in place.
        """
        if by_year:
            new_column_name = column_rename['new_column_name']
            for year, column_name in column_rename['year_map'].items():
                self.datasets[year].rename(columns={column_name: new_column_name}, inplace=True) 
        else:
            for df in self.datasets.values():
                df.rename(columns=column_rename, inplace=True)


    def display_feature_across_years(
        self, feature: str, display_func=print, year_summary=True, 
        feature_per_year=False, total_value_counts=False
    ):
        """
        Display feature evolution across years.
        Args:
            - feature: feature name present in at least one year. Raise error if not found in any.
            - display_func: function that will print/show the feature summary. Default print since its supported if run as script.
                            Use display if within jupyter notebook.
            - year_summary: boolean. feature sumary per year including count and percentage distribution.
            - feature_per_year: displays just all the feature values present per year
            - total_value_counts: total count of each unique feature value independent of the year.
        Return:
            - feature values per year dataframe. 
        """
        dataframes_with_column = [ 
            df[['year', feature]] for df in self.datasets.values() if feature in df.columns.tolist()
        ]

        merged_df = pd.concat(dataframes_with_column)

        df = merged_df
        
        if year_summary or feature_per_year:
            feature_df = df.groupby(['year', feature])[feature].count().to_frame()
            feature_df.columns = ['count']
            feature_df['percentage'] = feature_df.groupby(level=0).apply(lambda x: x / float(x.sum())).round(4)

        if year_summary:
            display(feature_df)

        if feature_per_year:
            display_func(feature_df.reset_index()[['year', feature]])

        if total_value_counts:
            display_func(df[feature].value_counts().to_frame())
            
        return merged_df


    def get_feature_dummies_per_year(self, feature: str, years=[], keep_features=[]):
        """
        Get dummies for multiple choice categorical features. The feature pass as argument should be defined a semicolon separeted string.
        Args:
            - feature: feature from which to get the dummies
            - years: list of years to get the dummies from. If none all years will be operated upon.
            - remove_white_spaces: boolean. If true, all white spaces from values will be removed before the encoding.
            - keep_features: list of other features to preserve after the operation.
        Return:
            - key, value pair: year as key, dummies_df as value.
        """
        feature_per_year_dummies = {}
        years = years or list(self.datasets.keys())
        for year, df in self.datasets.items():
            if year not in years:
                continue
            # removing trailing white spaces with \s* and \s*' before getting dummies to avoid misleading feature repeatition
            dummies_df = df[feature].str.split('\s*;\s*').str.join('|').str.get_dummies()
            feature_per_year_dummies[year] = pd.concat([df[keep_features], dummies_df], axis=1)
        return feature_per_year_dummies
    
    
    def missing_values_percentage(self, feature:str, years=[]):
        years = years or list(self.datasets.keys())
        feature_per_year = {}
        for year, df in self.datasets.items():
            if year not in years:
                continue
            if feature not in df.columns.tolist():
                continue
            feature_per_year[year] = df[feature].isna().mean()
        return pd.DataFrame(feature_per_year.items(), columns=['year', feature])