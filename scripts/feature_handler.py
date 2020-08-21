import pandas as pd

from scripts.developer_type_column_rename import standarized_developer_type_column, selected_dev_type_columns

class CommonHandler:
    
    # https://stackoverflow.com/a/59366409
    @staticmethod
    def remove_iqr_outliers(df):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        return df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

class DevTypeHandler(CommonHandler):

    @staticmethod
    def identify_web_developer_type(developer_type, web_developer_type):
        if (
            not(pd.isnull(developer_type) or pd.isnull(web_developer_type))
            and developer_type and web_developer_type
        ):
            return developer_type.replace('Web developer', web_developer_type)
        return developer_type

    @staticmethod
    def merge_dev_and_non_dev_types(developer_type, non_developer_type):
        if pd.isnull(developer_type):
            return non_developer_type
        elif pd.isnull(non_developer_type):
            return developer_type
        else:
            return f"{developer_type};{non_developer_type}"

    @classmethod
    def update_2017_developer_type_values(cls, datasets):
        df_2017 = datasets[2017]

        df_2017['developer_type'] = df_2017.apply(
            lambda x: cls.identify_web_developer_type(x['developer_type'], x['web_developer_type']), axis=1
        )

        df_2017['dev_type'] = df_2017.apply(
            lambda x: cls.merge_dev_and_non_dev_types(x['developer_type'], x['non_developer_type']), axis=1
        )


    @staticmethod
    def merge_dummies_data_science_ml_2017(datasets):
        df_2017 = datasets[2017]
        df_2017["Data scientist or machine learning specialist"] = \
            df_2017[["Data scientist", "Machine learning specialist"]].any(axis='columns').astype(int)


    @staticmethod
    def rename_and_extract_selected_dev_type_columns(dev_type_per_year_dummies, keep_features=[]):
        dev_type_dfs = {}
        selected_dev_types = selected_dev_type_columns.keys()
        keep_features.extend(selected_dev_types)

        for year, df in dev_type_per_year_dummies.items():
            df.rename(columns=standarized_developer_type_column, inplace=True)
            dev_type_dfs[year] = df[keep_features]
            
        return dev_type_dfs



class CompensationHandler(CommonHandler):

    @classmethod
    def extract_and_clean(cls, df_explorer, compensation_feature_name, keep_columns):
        keep_columns.append(compensation_feature_name)
        compensation_datasets = {}
        for year, df in df_explorer.datasets.items():
            # set compensation feature as type float
            df[compensation_feature_name] = df[compensation_feature_name].astype(float)
            # remove iqr outliers
            compensation_datasets[year] = cls.remove_iqr_outliers(df[keep_columns])
            # remove nans from compensation
            compensation_datasets[year].dropna(subset=[compensation_feature_name], inplace=True)
        return compensation_datasets
