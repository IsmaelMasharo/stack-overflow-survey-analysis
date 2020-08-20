import re
import pandas as pd


def camel_to_snake(name):
    """
    Convert strings to snake case format
    """
    # https://stackoverflow.com/a/1176023
    name = name.replace(' ', '_').replace("'", '').replace(':', '_').replace('?','')
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('_+', r'_', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def load_datasets(years=[], format_col_names=True):
    """
    Import all stackoverflow datasets in year, df dict-like manner.
    Args: 
        - years: list of dataframes to load. If none provided all datasets will be load
        - format_col_names: boolean. If True all column names will be format to snake_case
    """
    years = years or list(range(2011,2021))
    dataset_base_file_name = 'stack_overflow_datasets/survey_results_'

    dfs = {}
    for year in years:
        name = f'{dataset_base_file_name}{year}.csv'
        df = pd.read_csv(name, dtype=object)
        if format_col_names:
            df.columns = map(lambda name: camel_to_snake(name), df.columns)
        df['year'] = str(year)
        dfs[year] = df

    return dfs