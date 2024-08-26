import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for each pair of height and weight.

    Parameters
    ----------
    height : list[int | float]
        A list of heights in meters.
        Values should be positive integers or floats.
    weight : list[int | float]
        A list of weights in kilograms.
        Values should be positive integers or floats.

    Returns
    -------
    list[int | float]
        A list containing the BMI values
        corresponding to each height and weight pair.

    Raises
    ------
    ValueError
        If height and weight lists do not have
        the same length or if any values are non-positive.
    AssertionError
        If height or weight is not a list.
    TypeError
        If any element in height or
        weight is not an integer or float.
    """
    if len(height) != len(weight):
        raise ValueError("Height and Weight should have the same length")
    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("Height and Weight should both be lists")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and Weight can only be integers or floats")
        if h <= 0 or w <= 0:
            raise ValueError("Height and Weight must be positive values")

    height = np.array(height)
    weight = np.array(weight)

    height_sqrd = np.power(height, 2)
    bmi = np.divide(weight, height_sqrd)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to the BMI values and return a list of booleans indicating
    whether each BMI is above the given limit.

    Parameters
    ----------
    bmi : list[int | float]
        A list of BMI values.
    limit : int
        An integer limit above which the BMI should return True.

    Returns
    -------
    list[bool]
        A list of booleans where True indicates that the corresponding BMI
        is above the limit.

    """
    if not isinstance(bmi, list):
        raise TypeError("BMI should be a list")
    if not isinstance(limit, int):
        raise TypeError("Limit should be integer")
    if limit <= 0:
        raise ValueError("Limit should be a positive value")
    return [x > limit for x in bmi]
