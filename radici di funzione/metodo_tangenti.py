from scipy.misc import derivative

def metodo_tangenti(x0, fun, tol, kmax):
	stop = False
	k = 0

	while not(stop) and k < kmax:
		y0 = fun(x0)
		d0 = derivative(fun, x0)

		x1 = x0 - (y0/d0)

		stop = abs(fun(x1)) + ( abs(x1-x0)/(1+abs(x1)) ) < tol/5
		x0 = x1
		k +=1

	return x1
