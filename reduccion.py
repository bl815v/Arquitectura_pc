
from sympy import simplify_logic

def texto_a_expr(expr_str):
    reemplazos = {
        'and': '&',
        'or': '|',
        'not': '~',
    }
    for texto, simbolo in reemplazos.items():
        expr_str = expr_str.replace(texto, simbolo)
    return expr_str

def expr_a_op(expr):
    remplazos = {
        '&': '·',
        '|': '+',
    }
    for texto, simbolo in remplazos.items():
        expr = expr.replace(texto, simbolo)
    return expr

expresion = "not((not(A) or B)) and (not(C) or D)"
resultado = texto_a_expr(expresion)
simplificado = simplify_logic(resultado)

print("convertido:", resultado)
print("Forma simplificada:", simplificado)
print("Forma matematica:", expr_a_op(str(simplificado)))
