import pandas as pd

from scripts.developer_type_labeling import standarized_developer_type_column, selected_dev_type_columns


class CommonHandler:
    """
    Mixin class with common methods.
    """

    # https://stackoverflow.com/a/59366409
    @staticmethod
    def remove_iqr_outliers(df):
        """
        Remove interquartile outliers from numerical dataframe. Quartiles specified for the filtering: Q1=0.1, Q3=0.9.
        Args: 
            - df: dataframe with numerical columns.
        Return:
            - filtered dataframe.
        """
        Q1 = df.quantile(0.1)
        Q3 = df.quantile(0.9)
        IQR = Q3 - Q1
        return df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]


class DevTypeHandler(CommonHandler):
    """
    Helper namespaced class handler for developer type feature.
    """

    @staticmethod
    def identify_web_developer_type(developer_type, web_developer_type):
        """
        Helper function used to replace developer feature from 2017 survey identiying the web developer type (back, front, full-stack).
        Args: 
            - developer_type: string identifying the developer type.
            - web_developer_type: string identifying web developer type.
        Return:
            - string with the developer type and its kind (back, front, full-stack) if the type is web developer.
        """
        if (
            not(pd.isnull(developer_type) or pd.isnull(web_developer_type))
            and developer_type and web_developer_type
        ):
            return developer_type.replace('Web developer', web_developer_type)
        return developer_type

    @staticmethod
    def merge_dev_and_non_dev_types(developer_type, non_developer_type):
        """
        Helper function used to merge both developer_type and non_developer_type features from 2017 survey.
        Args: 
            - developer_type: string identifying the developer type.
            - non_developer_type: string identifying non developer type.
        Return:
            - semicolon separated string of both developer_type and non_developer_type feature.
        """
        if pd.isnull(developer_type):
            return non_developer_type
        elif pd.isnull(non_developer_type):
            return developer_type
        else:
            return f"{developer_type};{non_developer_type}"

    @classmethod
    def update_2017_developer_type_values(cls, datasets):
        """
        2017 survey developer type handler function.
        Args: 
            - datasets: dict with year, survey dataframe as key, value pairs.
        Return:
            - None. Inplace operation
        """
        df_2017 = datasets[2017]

        df_2017['developer_type'] = df_2017.apply(
            lambda x: cls.identify_web_developer_type(x['developer_type'], x['web_developer_type']), axis=1
        )

        df_2017['dev_type'] = df_2017.apply(
            lambda x: cls.merge_dev_and_non_dev_types(x['developer_type'], x['non_developer_type']), axis=1
        )


    @staticmethod
    def merge_dummies_data_science_ml_2017(datasets):
        """
        Merge Data scientist and Machine Learning specialist developer types into one feature for 2017 survey.
        Args: 
            - datasets: dict with year, survey dataframe as key, value pairs.
        Return:
            - None. Inplace operation
        """
        df_2017 = datasets[2017]
        df_2017["Data scientist or machine learning specialist"] = \
            df_2017[["Data scientist", "Machine learning specialist"]].any(axis='columns').astype(int)


    @staticmethod
    def rename_and_extract_selected_dev_type_columns(dev_type_per_year_dummies, keep_features=[]):
        """
        Standarize developer types names over years.
        Args: 
            - dev_type_per_year_dummies: survey dataframe with developer types dummy data as single features.
            - keep_features: features to be kept in the new dataframe besides developer types.
        Return:
            - dict: year, developer_dataframe as key value pairs.
        """
        dev_type_dfs = {}
        selected_dev_types = selected_dev_type_columns.keys()
        keep_features.extend(selected_dev_types)

        for year, df in dev_type_per_year_dummies.items():
            df.rename(columns=standarized_developer_type_column, inplace=True)
            dev_type_dfs[year] = df[keep_features]

        return dev_type_dfs



class CompensationHandler(CommonHandler):
    """
    Helper namespaced class handler for developer compensation feature.
    """

    @classmethod
    def extract_and_clean(cls, df_explorer, compensation_feature_name, keep_columns):
        """
        Extract and clean compensation feature.
        Args: 
            - df_explorer: SODataSetExplorer instance.
            - compensation_feature_name: name of the compensation feature.
            - keep_columns: features to be kept in the new dataframe besides developers' compensation.
        Return:
            - dict: year, compensation_dataframe as key value pairs.
        """
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
