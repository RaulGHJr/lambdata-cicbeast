import pandas as pd
import numpy as np
from scipy.stats import chisquare

"""
lambdata-cicbeast - Collection of DS Helper Functions
"""
name = 'lambdata_cicbeast'


ZEROS = np.zeros(5)
ONES = np.ones(10)


# Chi Squared test on Contingency Table
def cont_chi2(X, y, ddof=1, dropna=False):

    ctab = pd.crosstab(X, y, dropna=dropna)

    chi2, p = chisquare(
        ctab, ddof=ddof)

    return ctab, chi2


# Date Separater
def date_sep(X, datecol, infer_dtf=True): #where X is the dataframe and datecol is the date column

    X[datecol] = pd.to_datetime(X[datecol], infer_datetime_format=infer_dtf)

    X['year'] = X[datecol].dt.year
    X['month'] = X[datecol].dt.month
    X['day'] = X[datecol].dt.day

    X = X.drop(columns=['date'])

    return X
