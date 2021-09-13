import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import env
from datetime import date
from sklearn.model_selection import train_test_split

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#zillow db
zillow_sql = "SELECT bathroomcnt, bedroomcnt, fips, yearbuilt, taxvaluedollarcnt, taxamount, calculatedfinishedsquarefeet\
                FROM properties_2017\
                LEFT JOIN predictions_2017 USING(parcelid)\
                JOIN propertylandusetype USING(propertylandusetypeid)\
                WHERE propertylandusetype.propertylandusetypeid LIKE '261' AND predictions_2017.transactiondate BETWEEN '2017-05-01' AND '2017-08-31';"

def get_zillow_data():
    return pd.read_sql(zillow_sql,get_connection('zillow'))


#Distributions. Gets histographs of acquired continuous variables (non-categorical - object)
def get_hist(df):
    ''' Gets histographs of acquired continuous variables'''
    
    plt.figure(figsize=(16, 3))

    # List of columns
    cols = [col for col in df.columns if col not in ['county_code']]

    for i, col in enumerate(cols):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(cols), plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        df[col].hist(bins=5)

        # Hide gridlines.
        plt.grid(False)

        # turn off scientific notation
        plt.ticklabel_format(useOffset=False)

        plt.tight_layout()

    plt.show()

#Gets box plots of acquired continuous variables (non-categorical - object)
def get_box(df):
    ''' Gets boxplots of acquired continuous variables'''
    
    # List of columns
    cols = ['bathrooms', 'bedrooms', 'tax_value', 'tax_rate', 'square_feet', 'age']

    plt.figure(figsize=(16, 3))

    for i, col in enumerate(cols):

        # i starts at 0, but plot should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(cols), plot_number)

        # Title with column name.
        plt.title(col)

        # Display boxplot for column.
        sns.boxplot(data=df[[col]])

        # Hide gridlines.
        plt.grid(False)

        # sets proper spacing between plots
        plt.tight_layout()

    plt.show()   

#removes identified outliers 
def remove_outliers(df, k , col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe. Much like the word “software”, John Tukey is responsible for creating this “rule” called the 
        Inter-Quartile Range rule. In the absence of a domain knowledge reason for removing certain outliers, this is a pretty 
        robust tool for removing the most extreme outliers (with Zillow data, we can feel confident using this, since Zillow markets 
        to the majority of the bell curve and not folks w/ $20mil properties). the value for k is a constant that sets the threshold.
        Usually, you’ll see k start at 1.5, or 3 or less, depending on how many outliers you want to keep. The higher the k, the more 
        outliers you keep. Recommend not going beneath 1.5, but this is worth using, especially with data w/ extreme high/low values.'''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

#Wrangle zillow dataset
def prepare_zillow(df):
    ''' cleans and prepares zillow data'''
#age of home and tax rate calculations. Drop respective columns
    df['age'] = date.today().year - df.yearbuilt
    df['tax_rate'] = (df['taxamount'] / df['taxvaluedollarcnt'])
    df = df.drop(columns=['yearbuilt', 'tax_amount'])
#rename columns
    df = df.rename(columns={"bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms", 
    "calculatedfinishedsquarefeet":"square_feet", "taxvaluedollarcnt":"tax_value", "fips":"county_code"})
#converts to int
    convert_dict = {'county_code': object}
#converted lot_size to object then to int. I tried to convert lot_size from float to obj. When I tried it gave 
#me an error that it could not convert (NA or inf) to int.
    df = df.astype(convert_dict)

#replaces nulls with square_feet mean
    df['square_feet'] = df.square_feet.fillna(value = df['square_feet'].mean())
#replaces nulls with tax_rate mean
    df['tax_rate'] = df.tax_rate.fillna(value = df['tax_rate'].mean())
#replaces nulls with age mean
    df['age'] = df.age.fillna(value = df['age'].mean())
#converts floats to int 
    convert_dict_int = {'bathrooms': int, 'bedrooms': int, 'tax_value':int, 'square_feet':int, 'age':int, 'tax_rate':int}
    df = df.astype(convert_dict_int)
#removes outliers with k values and column features
    df = remove_outliers(df, 1.5, ['bathrooms', 'bedrooms', 'tax_value', 'tax_rate', 'square_feet', 'age'])
#gets graphs
    get_hist(df)
    get_box(df)   
#split data
    train, validate, test = train_validate_test_split(df)
    return df
    
############################### Split Data ##################################

def train_validate_test_split(df):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123, stratify=df['county_code'])
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=123, stratify=train_validate['county_code'])
    return train, validate, test

##########Final wrangle function################
def wrangle_zillow():
    prepared_zillow_data = prepare_zillow(get_zillow_data())

    return prepared_zillow_data
