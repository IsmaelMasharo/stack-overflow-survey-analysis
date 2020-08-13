# Stack Overflow Survey Analysis

Wrangling *StackOverflow Survey Results* over from 2011 till 2020. 

### Datasets
- No dataset is attached within this repo since the size of the overall datasets exceeds github maximum repo size policies.
- Original sources can be found [here](https://insights.stackoverflow.com/survey/)
- Survey results from 2011 to 2015 are download and initially procesed using **OpenRefine**. The rest of the dataset is just directly download from source. All files are renamed with its associated *year* as suffix. 
- Files hierarchy for the current analysis:

```
- stack_overflow_datasets   
    - survey_results_2011.csv  (OpenRefine Output)
    - survey_results_2012.csv  (OpenRefine Output)
    - survey_results_2013.csv  (OpenRefine Output)
    - survey_results_2014.csv  (OpenRefine Output)
    - survey_results_2015.csv  (OpenRefine Output)
    - survey_results_2015.csv  (OpenRefine Output)
    - survey_results_2016.csv  (Direct Survey download and renamed)
    - survey_results_2017.csv  (Direct Survey download and renamed)
    - survey_results_2018.csv  (Direct Survey download and renamed)
    - survey_results_2019.csv  (Direct Survey download and renamed)
    - survey_results_2020.csv  (Direct Survey download and renamed)
    ...
```

### Initial Clean up steps
Every step creates the input for the next step.

1. OpenRefine: Etl operations - datasets from 2011 to 2015
    - Merge related columns → renaming
    - **Output:** 
        - `openrefine_operation_history`: json files describing etl transformations per survey dataset.
        - `stack_overflow_datasets`: csv files with the transformed survey datasets.

2. Jupyter: *dataset_transformations.ipynb*
    - Column name formating to snake case
    - Datasets column name comparing and normalization
    - Basic feature engineering: 2018 occupation
    - Selecting features to work with based on its presence over the years
    - Feature column for tracking percetage of missing rows per year dataset
    - Merging all datasets with just the selected features
    - **Output:** 
        - `survey_report_concat_common_questions.csv`

3. OpenRefine: Clustering text values per feature
    - **Output:** 
        - `survey_results_combined.json`: json describing etl transformations for the concatenated datasets.
        - `survey_report_combined.csv`: csv with the transformed concatenated survey datasets.


### EDA
Interactive chart visualizations using plotly. The input for this files is the one from step 3 (`survey_report_combined.csv`)
- *programming_languages_eda.ipynb*
- *job_satisfaction_eda.ipynb*