# Stack Overflow Survey Analysis

### Initial Clean up process
Every step creates the input for the next one.

- [x] Etl operations in open refine
    - Merge related columns → renaming
    - **Output:** 
        - `openrefine_operation_history`: json files describing etl transformations per survey dataset.
        - `stack_overflow_datasets`: csv files with the transformed survey datasets.

- [x]  Initial operations in jupyter
    - Column name formating to snake case
    - Datasets column name comparing and normalization
    - Basic feature engineering: 2018 occupation
    - Selecting features to work with based on its presence over the years
    - Feature column for tracking percetage of missing rows per year dataset
    - Merging all datasets with just the selected features
    - **Output:** 
        - `survey_report_concat_common_questions.csv`

- [x] Clustering values per feature with OpenRefine
    - **Output:** 
        - `survey_results_combined.json`: json describing etl transformations for the concatenated datasets.
        - `survey_report_combined.csv`: csv with the transformed concatenated survey datasets.
