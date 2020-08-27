

class ProgrammingLanguagesHandler:
    feature_rename = {
        'tech_do': 'programming_languages',
        'have_worked_language': 'programming_languages',
        'language_worked_with': 'programming_languages',
    }

    @classmethod
    def rename_and_normalize(cls, df_explorer):
        df_explorer.rename_columns(cls.feature_rename)
