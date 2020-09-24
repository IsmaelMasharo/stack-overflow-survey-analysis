# Stack Overflow Survey Analysis
Wrangling *Stack Overflow Survey Results* from 2011 till 2020. Taking a closer look to features like `top programming languages`, `job satisfaction`, and `developers' salaries`.  

I published a post related to this analaysis on Medium and you can find it [here](https://medium.com/@ismaelmasharo/10-years-of-stack-overflow-surveys-c8ff3f662b2f).

## Datasets
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


### Initial clean up with OpenRefine
Etl operations for datasets from 2011 to 2015.  
- Base operations: merging and rename related columns
- **Output:** 
    - `openrefine_operation_history`: json files describing etl transformations per survey dataset.
    - `stack_overflow_datasets`: csv files with the transformed survey datasets.
- To replicate datasets, load the original once into OpenRefine and apply the respective operation history json.
    

### Business Understanding
* **features_exploration.ipynb**  
    Spot features similarity and presence in surveys over years. Potential values normalization, feature types.

* [**business_understanding.ipynb**](./business_understanding.ipynb)  
    Defining questions and data requirements. Base features summary.


### Data Understanding, Preparation and Evaluation
Each of the following notebooks address a question defined in the Business Understanding stage. Sections per notebook are `data understanding`, `data preparation` and `evaluation`.

* [**programming_languages_eda.ipynb**](./programming_languages_eda.ipynb)  
    Explores the programming languages over the years.
    - Only languages present as options are beign analyzed. 
    - Other languages specified by the users are kept out.


* [**job_satisfaction_eda.ipynb**](./job_satisfaction_eda.ipynb)  
    Descriptive visualization comparing each year job satisfaction in a compeling way. Analyzing correlation between programming languages.  
    - Normalisation of values are performed per year dataset to consistenly standarize this feature. Only 5 categories are kept, ranging from `very satisfied` to `very dissatisfied`. 
    - Mappings are located in `scripts/job_satisfaction_labeling.py`
    - Categorical associations are performed using Theil's U analysis. 

* [**compensation_dev_type_eda.ipynb**](./compensation_dev_type_eda.ipynb)   
    Analyzing compensation from 2017 onwards per each developer type.  
    - Compensation values are being cleaned up removing inter quartile outliers. 
    - The summaryze values may differ from the ones presented by the analysis of Stack Overflow since they applied other type of strategy for removing this outliers (mainly setting up threshold values around 200k).
