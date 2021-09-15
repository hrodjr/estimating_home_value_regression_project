# Estimating Home Values

1. <a href="https://miro.com/app/board/o9J_lxwpzC0=/">Link</a> to my project planning.



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
