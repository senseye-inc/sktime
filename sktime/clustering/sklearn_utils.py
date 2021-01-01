# -*- coding: utf-8 -*-
from typing import List, Callable
import numpy as np
import pandas as pd

Data_Frame = pd.DataFrame
Series = pd.Series
Numpy_Array = np.ndarray
SkLearn_Data = List[List[float]]


def convert_df_to_sklearn_format(df: Data_Frame) -> SkLearn_Data:
    """
    Method that is used to convert the sktime dataframe into a format that
    can be passed into sklearn algorithms

    Parameters
    ----------
    df: sktime dataframe
        Sktime dataframe to be converted into sklearn format

    Returns
    -------
    sklearn_format: 2D numpy array
        Numpy array ready to be passed into sklearn algorithms
    """
    find_longest_series: Callable[[Series], int] = lambda series: len(series)

    for col in df:
        max_length_series: int = df[col].map(find_longest_series).max()
        __check_shape(df[col], max_length_series)

    sklearn_format = np.concatenate(df.fillna("").values.tolist())
    return sklearn_format


def __check_shape(series: Series, max_length: int) -> Numpy_Array:
    """
    Method that is used to check the shape of the data frame to ensure
    no uneven length or missing values. Desirable to flag this to the
    user as early as possible

    TODO: Add more rigerous testing of series length and throw more
    informative excpetions

    Parameters
    ----------
    arr: numpy array
        Numpy array which is a given dimension sub series
    max_length: int
        Integer that is the intended max length of each array. Needed
        so that the array can be padded to the correct legnth
    """
    for sub in series:
        sub_series_len: int = len(sub)
        if sub_series_len != max_length:
            raise Exception(
                "Cannot convert df as not all \
                            series are equal length"
            )
