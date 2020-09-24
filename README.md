# Stack Overflow Survey Analysis
An analysis of the questions asked in the yearly surveys conducted by Stack Overflow focusing in **the evolution of the questions and its results throughout 10 years (2011-2020)**, taking a closer look to features like `top programming languages`, `job satisfaction`, and `developers' salaries`.  

I published a related post on Medium summarizing the results. You can find it [here](https://medium.com/@ismaelmasharo/10-years-of-stack-overflow-surveys-c8ff3f662b2f)


## Datasets 
- Sources can be found [here](https://insights.stackoverflow.com/survey/)
- Due to github repository size policies no dataset is attached. 
- Survey results from 2011 to 2015 are download and initially preprocessed using **OpenRefine**. The rest of the dataset is just directly downloaded from source. All files are renamed with its associated *year* as a suffix. 
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
ETL operations for datasets from 2011 to 2015.  
- Base operations: merging and rename related columns
- **Output:** 
    - `openrefine_operation_history`: json files describing etl transformations per survey dataset.
    - `stack_overflow_datasets`: csv files with the transformed survey datasets.
- To replicate datasets, load the original once into OpenRefine and apply the respective operation history json.
    

### Business Understanding
* **features_exploration.ipynb**  
    Identify features similarity and presence in surveys over years. Potential values normalization, feature types.

* [**business_understanding.md**](./business_understanding.md)  
    Defining questions and data requirements. Base features summary.


### Data Understanding, Preparation, and Evaluation
Each of the following notebooks addresses a question defined in the Business Understanding stage. Sections per notebook are `data understanding`, `data preparation` and `evaluation`.

* [**programming_languages_eda.ipynb**](./programming_languages_eda.ipynb)  
    Explores the programming languages over the years.
    - Only languages present as options are being analyzed. 
    - Other languages specified by the users are kept out.


* [**job_satisfaction_eda.ipynb**](./job_satisfaction_eda.ipynb)  
    Descriptive visualization comparing each year's job satisfaction compellingly. Analyzing the correlation between programming languages.  
    - Normalisation of values is performed per year dataset to consistently standardize this feature. Only 5 categories are kept, ranging from `very satisfied` to `very dissatisfied`. 
    - Mappings are located in `scripts/job_satisfaction_labeling.py`
    - Categorical associations are performed using Theil's U analysis. 

* [**compensation_dev_type_eda.ipynb**](./compensation_dev_type_eda.ipynb)   
    Analyzing compensation from 2017 onwards per each developer type.  
    - Compensation values are being cleaned up removing inter quartile outliers. 
    - The summarized values may differ from the ones presented by the analysis of Stack Overflow since they applied other types of strategy for removing these outliers (mainly setting up threshold values around 200k).


### Results Summary
* Javascript has remained on the top 5 programming languages throughout the years followed by related technologies such as HTML and CSS complementing the language of the web.
* Over the 10 years developers’ job satisfaction has kept high with a proportion of high satisfaction above 60% of professional developers that participated in the surveys.
* Regarding the features that could explain job satisfaction the possibility of working remotely slightly stands out among the reasons that could explain developers’ satisfaction together with the influence of the main branch (developer by profession or someone who writes code as part of their work).
* The shape of the compensation density plots per year remains similar, with a tendency of normalization in lower range salaries. Depending on the developer type, curves get skewed to lower salaries (Mobile Developers) or better approximating to normally distributed (DevOps).
* From 2018 to 2020 Engineer Managers have been reporting the highest annual compensations, with median salaries around 90k USD dollars per year. For the rest of professional developers, salaries range around 55k per year.


### Resources/Acknowledgements

* [Stack Overflow surveys](https://insights.stackoverflow.com/survey/)
* [Shaked Zychlinski - The Search for Categorical Correlation](https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9)