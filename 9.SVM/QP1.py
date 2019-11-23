from cvxopt import matrix, solvers

P = matrix([[1., 0.], [0., 1.]])
q = matrix([-0.14285, -0.42857])
G = matrix([[-1., 0., 1.], [0., -1., 1.]])
h = matrix([0., 0., 1.])

#solvers.options['show_progress'] = False
sol = solvers.qp(P, q, G, h)

print(sol['x'])
print(-sol['primal objective'])