#!/usr/bin/env python3
"""
Adds two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays
    """
    summ = []
    if len(arr1) != len(arr2):
        return None
    for i in range(0, len(arr1)):
        summ.append(arr1[i] + arr2[i])
    return summ
