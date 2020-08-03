# Stack Overflow Survey Analysis

Initial Clean up process

- [x]  Initial etl operations in open refine
    - Merge related columns → renaming
    - **Output:** 
        - `open refine history json files`
        - `stack_overflow_datasets csv files`

- [x]  Initial operations in jupyter
    - Column name formating to snake case
    - Datasets column name comparing and normalization
    - Basic feature engineering: 2018 occupation
    - Selecting features to work with based on its presence over the years
    - Feature column for tracking percetage of missing rows per year dataset
    - Merging all datasets with just the selected features
    - **Output:** `survey_report_concat_common_questions.csv`

- [x] Clustering values per feature with OpenRefine
    - **Output:** `open refine history json file survey_results_combined.json`
    - **Output:** `survey_report_combined.csv`
