#!/usr/bin/env python3
"""
concatenates two arrays
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates two matrices"""
    return np.concatenate((mat1, mat2), axis)
