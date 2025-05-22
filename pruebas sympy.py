
from sympy.logic import SOPform, simplify_logic
from sympy.logic.boolalg import Or, And
from sympy import symbols

a, b, c, d = symbols('a b c d')
minterms = [[0, 0, 0, 1], [0, 0, 1, 1],
            [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]

dontcares = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]]
sop = SOPform([a, b, c, d], minterms, dontcares)

# simplificado = simplify_logic((a | b) & (a | ~a))
simplificado = simplify_logic(And((Or(a,b)),(Or(a, ~a))))
print("suma de productos: " + str(sop))
print("forma simplificada: " + str(simplificado))
