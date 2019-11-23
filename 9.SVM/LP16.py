from cvxopt import matrix, solvers

c = matrix([1., -2., -4., 2.])
G = matrix([[1., 0., -2., -1., 0., 0., 0.], [0., 1., 1., 0., -1., 0., 0.], [-2., 0., 8., 0., 0., -1., 0.], [0., -1., 0., 0., 0., 0., -1.]])
h = matrix([4., 8., 12., 0., 0., 0., 0.])

sol = solvers.lp(c, G, h)

print(sol['x'])
print(-sol['primal objective'])