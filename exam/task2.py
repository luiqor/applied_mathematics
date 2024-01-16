import sympy as sp
from sympy import symbols, Function, Eq, Derivative, dsolve, Lambda, solve
from IPython.display import display
from sympy.plotting import plot_parametric

t, C1, C2 = symbols('t C1 C2')
x, y = symbols('x y', cls=Function)

eq1 = Eq(Derivative(x(t), t), x(t) + 4 * y(t))
eq2 = Eq(Derivative(y(t), t), 2 * x(t) + 3 * y(t))
eq = [eq1, eq2]

rez = dsolve(eq)

print("Розв'язки системи:")
for solution in rez:
    display(solution)

eq1_subs = rez[0].rhs.subs(t, 0)
print("\nПерше рівняння для x:")
display(eq1_subs)

eq2_subs = rez[1].rhs.subs(t, 0)
print("\nПерше рівняння для y:")
display(eq2_subs)

x_0 = 1
y_0 = 2
seq = solve([eq1_subs - x_0, eq2_subs - y_0], [C1, C2])
print("Значення довільних сталих")
display(seq)

result_x = rez[0].rhs.subs([(C1, seq[C1]), (C2, seq[C2])])
X = Lambda(t, result_x)
print("частковий розв для x")
display(X(t))

result_y = rez[1].rhs.subs([(C1, seq[C1]), (C2, seq[C2])])
Y = Lambda(t, result_y)
print("частковий розв для y")
display(Y(t))

parametric_plot = plot_parametric((X(t), Y(t)), (t, -10, 10), xlim=(-10, 10), ylim=(-10, 10), show=True)
