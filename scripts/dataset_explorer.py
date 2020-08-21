import pandas as pd

import re
from pprint import pprint

from .column_rename import column_rename_mapping

class SODataSetExplorer:
    """
    Helper for loading stackoverflow datasets
    """
    
    datasets = {}
    
    def __init__(self, years=[], format_col_names=True):
        self.datasets = self.load(years, format_col_names)


    def camel_to_snake(self, name):
        """
        Convert strings to snake case format
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
            df['year'] = str(year)
            dfs[year] = df

        return dfs


    def dataset_cols_difference(self, base_year, years_against=[], display_difference=True):
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


    def similar_columns(self, columns, years=[], display_similar=True):
        df_to_compare_with = self.datasets

        if years:
            df_to_compare_with = { year: dfs[year] for year in years }
        
        similar_per_year = {}
        for year, df in df_to_compare_with.items():

            similar = set()
            for name in columns:
                similar.update([col for col in df.columns.tolist() if name in col])
                
            similar_per_year[year] = similar

            if display_similar:
                print(year)
                pprint(similar)
                print('\n')
                
        return similar_per_year


    def rename_columns(self, column_rename=column_rename_mapping, by_year=False):
        if by_year:
            new_column_name = column_rename['new_column_name']
            for year, column_name in column_rename['year_map'].items():
                self.datasets[year].rename(columns={column_name: new_column_name}, inplace=True) 
        else:
            for df in self.datasets.values():
                df.rename(columns=column_rename, inplace=True)


    def display_feature_across_years(
        self, feature, display_func=print, year_summary=True, 
        feature_per_year=False, total_value_counts=False
    ):
        """
        Display feature evolution across years.
        Args:
            - df: dataframe with feature asociated.
            - display_func: function that will print/show the feature summary. Default print since its supported if run as script.
                            Use display if in jupyter notebook.
            - year_summary: boolean. feature sumary per year including count and percentage distribution.
            - feature_per_year: displays just all the feature values present per year
            - total_value_counts: total count of each unique feature value independent of the year. 
        """

        dataframes_with_column = [ 
            df[['year', feature]] for df in self.datasets.values() if feature in df.columns.tolist()
        ]

        merged_df = pd.concat(dataframes_with_column)

        df = merged_df

        feature_df = df.groupby(['year', feature])[feature].count().to_frame()
        if year_summary:
            feature_df.columns = ['count']
            feature_df['percentage'] = feature_df.groupby(level=0).apply(lambda x: x / float(x.sum())).round(4)
            display(feature_df)

        if feature_per_year:
            display_func(feature_df.reset_index())

        if total_value_counts:
            df_counts = df[feature].value_counts().to_frame()
            display_func(df_counts)

            
    def get_feature_dummies_per_year(self, feature, keep_features=[]):
        feature_per_year_dummies = {} 
        for year, df in self.datasets.items():
            dummies_df = df[feature].str.split(';').str.join('|').str.get_dummies()
            for keep in keep_features:
                dummies_df[keep] = df[keep]
            feature_per_year_dummies[year] = dummies_df
        return feature_per_year_dummies