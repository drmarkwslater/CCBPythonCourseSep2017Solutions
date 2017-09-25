# generate 3 datasets: exponential, polynomial, gaussian
import random
import math

random.seed(123)
t_noise = 0.5
exp_noise = 5
poly_noise = 5
gauss_noise = 5

# constants for functions
exp_n0 = 500.
exp_lambda = -0.07

poly_a = -5.0
poly_b = 0.78
poly_c = -0.4
poly_d = 0.021
poly_e = -0.017

gauss_n0 = 500.
gauss_mu = 50.
gauss_stddev = 14.0

outf = open('datasets.txt', 'w')

outf.write('# t\t\texp\t\tpoly\t\tgaus\n')

for i in range(1, 100):
    t = i + random.gauss(0, t_noise)
    exp = exp_n0 * math.exp(exp_lambda * t) + random.gauss(0, exp_noise)
    poly = poly_a + t*poly_b + t*t*poly_c + t*t*t*poly_d + t*t*t*poly_e + random.gauss(0, poly_noise)
    gauss = gauss_n0 * math.exp(-1. * (t - gauss_mu) * (t - gauss_mu) / (2 * gauss_stddev * gauss_stddev) ) + random.gauss(0, gauss_noise)
    
    outf.write('%f\t\t%f\t\t%f\t\t%f\n' % (t, exp, poly, gauss))

outf.close()
