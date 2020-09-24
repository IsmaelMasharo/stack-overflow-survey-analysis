## Business Understanding

Stack Overflow has been conducting developer surveys for about a decade. In this notebook, we'll explore some of these features.  

Let's start by inspecting the feature presence over the years.

### Feature summary
One inmediate thing to point out is that over the years features have been changing. Some questions present in one year could be rephrased or leaved out the next year, furtheremore, feature types could change from one year to another. Bellow is a summary of some of the different features and its types over the years (build from [*features_exploration.ipynb* notebook)](./features_exploration.ipynb).

**Multiple choice categorical features**  
<pre>
<b>dev_type</b>                    2017-onwards         categorical. Previous years: <b>occupation</b>
<b>education</b>                   2015-2016
<b>education_types</b>             2017-2018
<b>job_factors</b>                 2019-2020
<b>ethnicity</b>                   2018-onwards
<b>gender</b>                      2017-onwards         From 2014 till 2016: categorical single choice
<b>sexuality</b>                   2018-onwards
<b>programming_languages</b>       2011-2020
<b>want_work_language</b>          2013-onwards
<b>database_desire_work</b>        2017-onwards
<b>database_worked_with</b>        2017-onwards
</pre>

**Categorical**
<pre>
<b>country</b>                     2011-2020
<b>occupation</b>                  2011-2016            Categorical. Forward years: <b>dev_type</b>. Multiple choice categorical
<b>job_satisfaction</b>            2011-2020 but 2014
<b>ed_level</b>                    2019-2020
<b>undergrad_major</b>             2017-onwards
<b>employment</b>                  2015-onwards
<b>professional</b>                2017                 Forward years 2019-2020: <b>main_branch</b>
<b>os</b>                          2011-2020 but 2017
<b>industry</b>                    2011-2017
<b>hobbyist</b>                    2018-onwards         Boolean
<b>trans</b>                       2019-2020            Boolean
<b>org_size</b>                    2017-onwards         Range
<b>years_coded_job</b>             2017                 Range
<b>years_coded_job_past</b>        2017                 Range
<b>remote</b>                      2014-2017, 2019      Indicate frequency of remote working
</pre>

**Continuous**
<pre>
<b>work_week_hrs</b>               2019-2020
<b>age</b>                         2019-2020            Before is defined as a categorical range
<b>age1st_code</b>                 2019-2020            Continuous with exceptions
<b>years_code</b>                  2019-2020            Continuous with exceptions
<b>years_code_pro</b>              2019-2020            Continuous with exceptions
</pre>

**Others**
<pre>
<b>Learning related feature</b>    Inconsistent over years
<b>years_experience</b>            Wrong format
</pre>

<br>

As we can see many features could be analyzed and further explore. However, `the goal here is the analysis of the features that could be continuously present over the years`. For this, one alternative would be to look if a feature is present in every single year. Unfortunately, that's not the case for most features. Another approach would be to look for features continuously present over a subset of years.  

Considering both options the features analyzed will be: developers' **top programming languages, job satisfaction and compensation**.

From these features we'll want to know the following:
### Top Programming Languages
* Over the 10 years surveys what have been the top 10 programming languages per year? 
* Is there any programming language that has remained on top over the years?

### Job Satisfaction
* How does developers' job satisfaction has evolved?
* Do developers feel more satisfied at job on average?
* What features could explained or be related to developers' satisfaction at job?

### Compensation
* From the last 3 years (2018-2020), how does developers' compensation has changed?
* Which developer type has the highest compensation on average?

These questions are related to a `descriptive` type of analysis, therefore, the question assessment can be met using tools like data visualization techniques and descriptive statistics. 