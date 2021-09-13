import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_dataframe(df, stratify_by=None, rand=1414, test_size=.2, validate_size=.3):
    """
    Utility function to create train, validate, and test splits.
    Generates train, validate, and test samples from a dataframe.
    Credit to @ryanorsinger
    Parameters
    ----------
    df : DataFrame
        The dataframe to be split
    stratify_by : str
        Name of the target variable. Ensures different results of target variable are spread between the samples. Default is None.
    test_size : float
        Ratio of dataframe (0.0 to 1.0) that should be kept for testing sample. Default is 0.2.
    validate_size: float
        Ratio of train sample (0.0 to 1.0) that should be kept for validate sample. Default is 0.3.
    random_stat : int
        Value provided to create re-produceable results. Default is 1414.
    Returns
    -------
    DataFrame
        Three dataframes representing the training, validate, and test samples
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=test_size, random_state=rand)
        train, validate = train_test_split(train, test_size=validate_size, random_state=rand)
    else:
        train, test = train_test_split(df, test_size=test_size, random_state=rand, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=validate_size, random_state=rand, stratify=train[stratify_by])

    return train, validate, test


    def split_dataframe_continuous_target(dframe, target, bins=5, rand=1414, test_size=.2, validate_size=.3):
    """
    Utility function to create train, validate, and test splits when targeting a continuous variable.
    Generates train, validate, and test samples from a dataframe when targeting a continuous variable.
    Credit to @ryanorsinger
    Parameters
    ----------
    df : DataFrame
        The dataframe to be split
    target : str
        Name of the continuous target variable. Ensures different results of target variable are spread between the samples.
    test_size : float
        Ratio of dataframe (0.0 to 1.0) that should be kept for testing sample. Default is 0.2.
    validate_size: float
        Ratio of train sample (0.0 to 1.0) that should be kept for validate sample. Default is 0.3.
    random_stat : int
        Value provided to create re-produceable results. Default is 1414.
    Returns
    -------
    DataFrame
        Three dataframes representing the training, validate, and test samples
    """
    df = dframe.copy()
    binned_y = pd.cut(df[target], bins=bins, labels=list(range(bins)))
    df["bins"] = binned_y

    train_validate, test = train_test_split(df, stratify=df["bins"], test_size=test_size, random_state=rand)
    train, validate = train_test_split(train_validate, stratify=train_validate["bins"], test_size=validate_size, random_state=rand)

    train = train.drop(columns=["bins"])
    validate = validate.drop(columns=["bins"])
    test = test.drop(columns=["bins"])
    
    return train, validate, test

def scaled_splits(train, validate, test, scaler=MinMaxScaler()):
    """
    Takes in a train, validate, test samples and can specify the type of scaler to use (default=MinMaxScaler). Returns the samples
    after scaling as dataframes.
    """
    scaler.fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns)
    validate_scaled = pd.DataFrame(scaler.transform(validate), columns=validate.columns)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns)

    return train_scaled, validate_scaled, test_scaled