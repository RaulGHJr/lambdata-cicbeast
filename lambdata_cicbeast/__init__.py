import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
def date_sep(X, infer_dtf=True):

    X['date'] = pd.to_datetime(X['date'], infer_datetime_format=infer_dtf)

    X['year'] = X['date'].dt.year
    X['month'] = X['date'].dt.month
    X['day'] = X['date'].dt.day

    X = X.drop(columns=['date'])

    return X
