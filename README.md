# Stack Overflow Survey Analysis

Wrangling *StackOverflow Survey Results* over from 2011 till 2020. 

### Datasets
- No dataset is attached within this repo since the size of the overall datasets exceeds github maximum repo size policies.
- Original sources can be found [here](https://insights.stackoverflow.com/survey/)
- Survey results from 2011 to 2015 are download and initially preprocesed using **OpenRefine**. The rest of the dataset is just directly download from source. All files are renamed with its associated *year* as suffix. 
- Files hierarchy for the current analysis:

```
- stack_overflow_datasets   
    - survey_results_2011.csv  (OpenRefine Output)
    - survey_results_2012.csv  (OpenRefine Output)
    - survey_results_2013.csv  (OpenRefine Output)
    - survey_results_2014.csv  (OpenRefine Output)
    - survey_results_2015.csv  (OpenRefine Output)
    - survey_results_2015.csv  (OpenRefine Output)
    - survey_results_2016.csv  (Direct Survey download)
    - survey_results_2017.csv  (Direct Survey download)
    - survey_results_2018.csv  (Direct Survey download)
    - survey_results_2019.csv  (Direct Survey download)
    - survey_results_2020.csv  (Direct Survey download)
```


### Initial Clean up steps
Every step creates the input for the next step.

1. OpenRefine: Etl operations - datasets from 2011 to 2015
    - Merge related columns → renaming
    - **Output:** 
        - `openrefine_operation_history`: json files describing etl transformations per survey dataset.
        - `stack_overflow_datasets`: csv files with the transformed survey datasets.
    - To replicate datasets, load the original once into OpenRefine and apply the respective operation history json.
    

### EDA

* **datasets_exploration.ipynb**  
    Exploring similar features over the years, potential values normalization, feature types, etc.

* **programming_languages_eda.ipynb**  
    Explores the programming languages over the years. 
    
* **job_satisfaction_eda.ipynb**  
    Descriptive visualization comparing each year job satisfaction in a compeling way.

* **compensation_dev_type_eda.ipynb**  
    Analyzing compensation from 2017 onwards per each developer type.
    
* **categorical_corr.ipynb**  
    Analyzing correlation between programming languages. Other categorical correlations. 