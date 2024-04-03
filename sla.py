import os

def interface():
    os.system('clear')
    print("Seja bem vindo a Super Calculadora Verdade!")
    valP = str(input("Digite o valor de 'p': ")).upper()
    valQ = str(input("Digite o valor de 'q': ")).upper()
    print("Operadores: and(^),or(v),se então(>), se somente se(#) e not(!)")
    print("Exemplo de expressão p^q>p#p^(q#p)")
    expre = str(input("Digite uma proposição: ")).replace(" ", "").replace("Q","q").replace("P","p")
    if calc(expre,valP,valQ) == '1':
        print(expre+" = V")
    else:
        print(expre+" = F")
    ##resultado = calc(formatacao(expre,valP,valQ))  


def calc(expre,valP,valQ):
    print(expre)
    expre = formatar(expre,valP,valQ)
    if eval(expre):
        if isinstance(eval(expre),int):
            if eval(expre) >0:
                return '1'
            else:
                return '0'
    
    else:
        if eval(expre) == False:
            return '0'
        elif eval(expre) == True:
            return '1'


def resolverParenteses(expre,valP,valQ):
    i = 1
    newString = ""
    contParentese = 1
    while True:
        if expre[i] == '(':
            contParentese += 1
        elif expre[i] == ')':
            contParentese -= 1
        if contParentese == 0:
            break
        newString += expre[i]
        i += 1

    lis = [calc(newString, valP, valQ),i]
    return lis

def formatar(expre,valP,valQ):
    if valP == 'V':
        valP = '1'
    elif valP == 'F':
        valP = '0'
    
    if valQ == 'V':
        valQ = '1'
    elif valQ == 'F':
        valQ = '0'

    i = 0
    newExpre = ""
    while i < len(expre):
        if expre[i] == 'q':
            newExpre += valQ
        elif expre[i] == 'p':
            newExpre+= valP
        elif expre[i] == '^':
            newExpre += '*'
        elif expre[i] == 'v':
            newExpre += '+'
        elif expre[i] == '!':
            i += 1
            if expre[i] != '(':
                if expre[i] == 'q':
                    if valQ == '1':
                        newExpre += '0'
                    else:
                        newExpre += '1'
                if expre[i] == 'p':
                    if valP == '1':
                        newExpre += '0'
                    else:
                        newExpre += '1'
            else:
                if resolverParenteses(expre[i:1])[0] == '1':
                    newExpre += '0'
                    i += resolverParenteses(expre[i:1])[1]
                else:
                    newExpre += '1'
                    i += resolverParenteses(expre[i:1])[1]
        elif expre[i] == '(':
            newExpre += resolverParenteses(expre[i::1], valP, valQ)[0]
            i +=  resolverParenteses(expre[i::1], valP, valQ)[1]

        elif expre[i] == '>':
            newExpre += '<='
        
        elif expre[i] == '#':
            newExpre += '=='

        else:
            newExpre += expre[i]
        i += 1

    return newExpre

print(calc("q^p > q",'V','F'))
