import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from numbers import Number
from objects.vector import vector


def cos(param):
    """Implements cosine in radians.

    Args:
        param (vector, Number): vector or Number of which to cosine

    Returns:
        cosine of param in radians
    """
    if isinstance(param, vector):
        return vector([np.cos(val) for val in param])
    elif isinstance(param, Number):
        return np.cos(param)
    else:
        raise TypeError('parameter must be a vector or Number')


def cosd(param):
    """Implements cosine in degrees.

    Args:
        param (vector, Number): vector or Number of which to cosine

    Returns:
        cosine of param in degrees
    """
    if isinstance(param, vector):
        return vector([np.cos(np.radians(val)) for val in param])
    elif isinstance(param, Number):
        return np.cos(np.radians(param))
    else:
        raise TypeError('parameter must be a vector or Number')


def sin(param):
    """Implements sine in radians.

    Args:
        param (vector, Number): vector or Number of which to sine

    Returns:
        sine of param in radians
    """
    if isinstance(param, vector):
        return vector([np.sin(val) for val in param])
    elif isinstance(param, Number):
        return np.sin(param)
    else:
        raise TypeError('parameter must be a vector or Number')


def sind(param):
    """Implements sine in degrees.

    Args:
        param (vector, Number): vector or Number of which to sine

    Returns:
        sine of param in degrees
    """
    if isinstance(param, vector):
        return vector([np.sin(np.radians(val)) for val in param])
    elif isinstance(param, Number):
        return np.sin(np.radians(param))
    else:
        raise TypeError('parameter must be a vector or Number')


def tan(param):
    """Implements tangent in radians.

    Args:
        param (vector, Number): vector or Number of which to tangent

    Returns:
        tangent of param in radians
    """
    if isinstance(param, vector):
        return vector([np.tan(val) for val in param])
    elif isinstance(param, Number):
        return np.tan(param)
    else:
        raise TypeError('parameter must be a vector or Number')


def tand(param):
    """Implements tangent in degrees.

    Args:
        param (vector, Number): vector or Number of which to tangent

    Returns:
        tangent of param in degrees
    """
    if isinstance(param, vector):
        return vector([np.tan(np.radians(val)) for val in param])
    elif isinstance(param, Number):
        return np.tan(np.radians(param))
    else:
        raise TypeError('parameter must be a vector or Number')
