#NB: This mapping is make over the openrefine initial operation results

column_rename_mapping = {
    'salary': 'annual_compensation',
    'annueal_compensation': 'annual_compensation',

    'org_size': 'company_size',

    'years_code': 'years_experience', 
    'years_coding': 'years_experience', 
    'years_program': 'years_experience', 

    'main_branch': 'occupation', 
    'professional': 'occupation',

    'training_and_education': 'education',
    'education_types': 'education',
    'ed_level': 'education',

    'remote': 'remote_status',
    'work_remote': 'remote_status',
    'home_remote': 'remote_status',

    'job_sat': 'job_satisfaction',

    'op_sys': 'os',
    'operating_system': 'os',
    'desktop_os': 'os',

    'age_range': 'age',
    'company_size_range': 'company_size',
    'experience_range': 'years_experience',
    'salary_range': 'annual_compensation',
    'team_size_range': 'team_size',

    'language_worked_with': 'programming_languages',
    'have_worked_language': 'programming_languages',
    'tech_do': 'programming_languages',
    'programming_lalnguages': 'programming_languages',
    'programming_language': 'programming_languages',
    'programming_languages_oher': 'programming_languages_other',
    'programming_language_other': 'programming_languages_other',

    'future_language_or_tech': 'want_work_language',
    'tech_want': 'want_work_language',
    'language_desire_next_year': 'want_work_language',
    'new_tech_interests': 'want_work_language',

    'have_worked_database': 'database_worked_with',
    'want_work_database': 'database_desire_work',
    'database_desire_next_year': 'database_desire_work',

    'major_undergrad': 'undergrad_mayor', 

    'so_visit1st': 'stack_overflow_visit1st',
    'so_visit_freq': 'stack_overflow_visit_freq',
    'so_visit_to': 'stack_overflow_visit_to',
    'so_find_answer': 'stack_overflow_find_answer',
    'so_time_saved': 'stack_overflow_time_saved',
    'so_how_much_time': 'stack_overflow_how_much_time',
    'so_account': 'stack_overflow_account',
    'so_part_freq': 'stack_overflow_part_freq',
    'so_jobs': 'stack_overflow_jobs',
    'so_comm': 'stack_overflow_comm',
    'so_new_content': 'stack_overflow_new_content',
    'so_region': 'stack_overflow_region',
    'newso_sites': 'new_stack_overflow_sites'
}