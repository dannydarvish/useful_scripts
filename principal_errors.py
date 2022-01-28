import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

# Rotates the covariance matrix for a set of x data points and y data points
# Returns two matplotlib Line2D object representing the rotated error bars:
#     errorbar_0,errorbar_1 = principal_errors(x,y)
def principal_errors(x, y, x_mean = None, y_mean = None):
    '''Rotates the covariance matrix for a set of x data points and y data points
    Returns two matplotlib Line2D object representing the rotated error bars:
        errorbar_0,errorbar_1 = principal_errors(x,y)'''
    if len(x) != len(y):
        raise RuntimeError('Sample size of variables not equal in construction of covariance matrix')
    if x_mean is None:
        x_mean = np.mean(x)
    if y_mean is None:
        y_mean = np.mean(y)

    cov = np.cov([x,y], ddof=1)
    w,v = np.linalg.eig(cov)
    sigma = np.sqrt(w)

    errorbar_0 = Line2D([x_mean-sigma[0]*v[0,0],x_mean+sigma[0]*v[0,0]],
                        [y_mean-sigma[0]*v[1,0],y_mean+sigma[0]*v[1,0]])
    errorbar_1 = Line2D([x_mean-sigma[1]*v[0,1],x_mean+sigma[1]*v[0,1]],
                        [y_mean-sigma[1]*v[1,1],y_mean+sigma[1]*v[1,1]])
    return errorbar_0,errorbar_1
