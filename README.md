# Estimating Home Values

1. I used Miro to plan out my project. You can find it <a href="https://miro.com/app/board/o9J_lxwpzC0=/">here</a>.
2. You can find a copy of the slide presentation <a href="https://www.canva.com/design/DAEqDI-L6kc/P5eDAfxDdn1rNT6DVaamDg/view?utm_content=DAEqDI-L6kc&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton">here</a>.

2. Goal:
- Predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.
## Project Details
- Libraries
    - pandas
    - numpy
    - seaborn
    - matplotlib
    - scipy.stats
    - sklearn
- Individual modules
    - acquire.py (SQL data acquisition)
    - prepare.py (data cleaning)
    - explore.py (data exploration)
    - model.py (data modeling)
- Statistical Tests
    - chi2
    - pearsonr
    - ttest
- Exploration
    - Univariate
    - Bivariate
    - Multivariate
- Feature Engineering
    - rfe
    - kbest
- Modeling
    - LinearRegression (OLS)
    - LassoLars
    - TweedieRegressor (GLM)
    - Polynomial Regression
## Pipeline
My methodology follow is the data pipeline; plan, acquire, prepare, explore, model and deliver.
### Planning
I want to find out if tax values differ for each of the following scenarios:
- tax value to number of bathrooms
- tax value to number of bedrooms
- tax value to square footage
- tax value to county
### Acquire
Predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.
### Prepare
Based on the project details the following went into consideration:
- Calculated tax rate dividing taxamount by taxvaluedollarcnt
- Calculated age of home vice using year built by subtracting today's date by yearbuilt
- Filled all nulls with the respective mean values
- Dropped respective columns
- Converted all but tax_rate to integers. Left tax_rate as float.
### Explore
Data exploration used include univariate, bivariate and multivariate exploration.
### Model
Modeling the data included:
- Sampling
- Scaling
- Feature engineering 
- Regression modeling
- Modeling of test, validate, and test data samples.
### Delivery
A downloadable csv file has been created for future modeling.
## Hypothesis
Hypothesis testing concluded by accepting the alternate hypothesis of each tested hypothesis.
1. Do homes in 6059 have a higer tax values? (chi2)
    - Null: Tax value is independent of homes in 6059.
    - Alternate: Tax value is dependent of homes in 6059.

2. Do homes with three or more baths have a higher tax value? (chi2)
    - Null: Tax value is independentt of three or more baths.
    - Alternate: Tax value is dependent on three or more baths.
3. Do home with four or more bedrooms have a higher tax value? (chi2)
    - Null: Tax value is independentt of four or more bedrooms.
    - Alternate: Tax value is dependent on four or more bedrooms.

4. Linear correlation between tax value and square footage of the home. (pearsonr)
    - Null: Tax value and square footage are NOT lineraly correlated.
    - Alternate: Tax value and square footage are lineraly correlated.
## Key findings and takeaways
1. Initial takeaways:
- Average home is 3 bedroom, 2 baths, built in 1963, and with a square footage of 1934.
- Value of the average home is 535,000 dollars
- Home owners pay an average of 6,508 dollars in property tax
- Both tax_value and square_feet are right skewed
- Normal distributions amongst the other features
- Average home is between 2 and 3 bathrooms
3 - 4 bedrooms
- Average tax value is roughly 400K
- Average tax rate just above 1.2 percent
- Average square feet is just above 1500sqft
- The average age of homes in this dataset is 60
2. In univariate exploration I got a glimse into several possible drivers that led me to the aforementioned hypothesis:
- Homes in Los Angeles county make up 61% of the homes querried
- Homes in Ventura county make up 29.24% of the homes querried
- Homes in Orange county make up 9.63% of the homes querried
- Average bathroom count is 2
- Average bedroom count is 3
- Average tax value is 416,366 dollars
- Average square footage is 1,753 sqft
- Average home age is 58 years
- Average tax rate is 1.25%
3. Bivariate exploration takeaways:
- Homes in Orange county (6059) have the highest tax value average at 468,487 dollars
- Followed by homes in Ventura county (6111) at 449,845 dollars and Los Angeles county (6037) at 386,158 dollars
- Homes with 4 bathrooms have a higher tax value average of 685,958 dollars
- Homes with 5 bedrooms have a higher tax value average of 529,151 dollars
4. Multivariate exploration takeaways:
- Age of the home does not really play into the tax value of the home
- The majority of homes are between 40 and 75 years old
- Seems to be a linear corrrelation between tax value and square footage
5. Modeling:
- Both the rfe and kbest both return 'square_feet' as the most significant feature, followed by number bedrooms and bathrooms.
- Baseline model returns 252,577
- The model is better then the baseline.
- The best model on train and validated was the polynomial regression model at train: 222,773 and validate: 221,208
- Tested the data on the polynomial regression model at 221,666
# Tax rate by County
Located in the final project.
- 6037    0.012993
- 6059    0.011846
- 6111    0.011470
# Data Dictionary
| Target                       | Encoded             | Description                                                                                                                              | DataType |
|------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------|
| bathroomcnt                  | renamed             | NA                                                                                                                                       | float64  |
| bedroomcnt                   | renamed             | NA                                                                                                                                       | float64  |
| fips                         | renamed and dropped | NA                                                                                                                                       | float64  |
| yearbuilt                    | dropped             | Year the home was built.                                                                                                                 | float64  |
| taxvaluedollarcnt            | renamed             | NA                                                                                                                                       | float64  |
| taxamount                    | dropped             | Taxes paid on value of home.                                                                                                             | float64  |
| calculatedfinishedsquarefeet | renamed             | NA                                                                                                                                       | float64  |
| NA                           | bathrooms           | Number of bathrooms in the home.                                                                                                         | int64    |
| NA                           | bedrooms            | Number of bedrooms in the home.                                                                                                          | int64    |
| NA                           | county_code         | Similar to a zip this code identifies counties.                                                                                          | int64    |
| NA                           | tax_value           | Value of the home.                                                                                                                       | int64    |
| NA                           | square_feet         | Square footage of the home.                                                                                                              | int64    |
| NA                           | age                 | This is the age of the home. Calculated by subtracting today's date by year built. The calculation can be found in the prepare.py file.  | int64    |
| NA                           | tax_rate            | This is the tax rate by percentage. Calculated by dividing original taxamount by taxvaluedollar and can be found in the prepare.py file. | float64  |
