import pandas as pd

from .job_satisfaction_constants import JobSatisfactionConstants


class JobSatisfactionHandler(JobSatisfactionConstants):

    @classmethod
    def rename_and_normalize(cls, df_explorer):
        df_explorer.rename_columns(cls.feature_rename)

        for year, df in df_explorer.datasets.items():
            df[cls.feature] = df[cls.feature].map(
                lambda x: cls.feature_values_mapping.get(x, x)
            )

            filtered_job_sat = df[cls.feature].isin(cls.feature_scale)
            # direct reasignation wont change the original dataframe from loop (df)
            # df = df[filtered_job_sat] (X)
            # so, doing this instead
            df_explorer.datasets[year] = df[filtered_job_sat]
            # for attributes works ok
            df[cls.feature] = pd.Categorical(df[cls.feature], cls.feature_scale)


    @classmethod
    def concat_over_years(cls, df_explorer, keep_features=[]):
        keep_features.extend([cls.feature])
        df_w_feature = [
            df[keep_features] for df in df_explorer.datasets.values() 
                if cls.feature in df.columns.tolist()
        ]
        concat_df = pd.concat(df_w_feature, ignore_index=True)
        # would be necesary to update to categorical only if the categories change across datasets
        # concat_df[cls.feature] = pd.Categorical(concat_df[cls.feature], cls.feature_scale)
        return concat_df
