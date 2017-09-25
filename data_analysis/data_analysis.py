# import what's needed
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# create the models for the data
def exp_model(x, n0, l):
    return n0 * np.exp(l * x)

def poly_model(x, a, b, c, d, e):
    return a + x*b + x*x*c + x*x*x*d + x*x*x*x*e

def gauss_model(x, n0, mu, sd):
    return n0 * np.exp(-1. * (x - mu) * (x - mu) / (2 * sd * sd) )

# initialise the required lists
t_list = []
exp_list = []
poly_list = []
gauss_list = []

# open up the file and read each line in turn
for ln in open('datasets.txt').readlines():

    # ignore comments
    if ln.strip()[0] == '#':
        continue

    #get the tokens
    toks = ln.split()
    t_list.append( float(toks[0]) )
    exp_list.append( float(toks[1]) )
    poly_list.append( float(toks[2]) )
    gauss_list.append( float(toks[3]) )

# plot each list on the same axes
plt.plot(t_list, exp_list, 'ro', label = 'exp data')
plt.plot(t_list, poly_list, 'bo', label = 'poly data')
plt.plot(t_list, gauss_list, 'go', label = 'gauss data')

# do the fits
exp_opt, exp_cov = curve_fit(exp_model, t_list, exp_list, bounds=([400, -1.0], [600, 0]))
poly_opt, poly_cov = curve_fit(poly_model, t_list, poly_list)
gauss_opt, gauss_cov = curve_fit(gauss_model, t_list, gauss_list)

# generate the fitted data
exp_fit = []
poly_fit = []
gauss_fit = []

for t in t_list:
    exp_fit.append( exp_model(t, *exp_opt) )
    poly_fit.append( poly_model(t, *poly_opt) )
    gauss_fit.append( gauss_model(t, *gauss_opt) )

# plot the fits
plt.plot(t_list, exp_fit, 'r-', label='exp fit')
plt.plot(t_list, poly_fit, 'b-', label='poly fit')
plt.plot(t_list, gauss_fit, 'g-', label='gauss fit')

plt.xlabel('t')
plt.legend()
plt.show()
