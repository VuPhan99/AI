from cvxopt import matrix, solvers

c = matrix([-5., -3.])
G = matrix([[1., 2., 1., -1., 0.], [1., 1., 4., 0., -1.]])
h = matrix([10., 16., 32., 0., 0.])

sol = solvers.lp(c, G, h)
print(sol['x'])
print(-sol['primal objective'])