def interface():
    print("Seja bem vindo a Super Calculadora Verdade!\n")
    print("ATENÇÃO!!! USE PARENTESES PARA DELIMITAR A ORDEM!")
    valP = str(input("Digite o valor de 'p': ")).upper()
    valQ = str(input("Digite o valor de 'q': ")).upper()
    print("Operadores: and(^),or(v),se então(>), se somente se(#) e not(!)")
    expre = str(input("Digite uma proposição: ")).replace(" ", "").replace("Q","q").replace("P","p")
    if calc(expre,valP,valQ) == '1':
        print("V")
    else:
        print("F")
    ##resultado = calc(formatacao(expre,valP,valQ))  


def calc(expre,valP,valQ):
    expre = formatar(expre,valP,valQ)
    if eval(expre) > 0:
        return '1' 
    else: 
        return '0'

def resolverSeESomente(expre):
    i =0 
    newExpre = ""
    while(i < len(expre)):
        if expre[i] == '>':
            newExpre += '<='
        
        elif expre[i] == '#':
            newExpre += '='
        
        else:
            newExpre += expre[i]

    return newExpre

def resolverParenteses(expre,valP,valQ):
    i =0
    newString = ""
    contParentese = 0
    while(i < len(expre)):
        if expre[i] == '(':
            contParentese += 1
        elif expre[i] == ')':
            contParentese -= 1
        if contParentese == 0:
            break
        i+=1
        newString += expre[i]
    
    return calc(newString,valP,valQ)

def extrairParenteses(expre,valP,valQ):
    i =0
    newString = ""
    contParentese = 0
    while(True):
        newString += expre[i]
        if expre[i] =='(':
            contParentese += 1
        elif expre[i] == ')':
            contParentese -= 1

        if contParentese == 0:
            break

        i+=1
    
    return newString

def formatar(expre,valP,valQ):
    if valP == 'V':
        valP = '1'
    else:
        valP = '0'
    
    if valQ == 'V':
        valQ = '1'
    else:
        valP = '0'

    i =0
    newExpre = ""
    while(i < len(expre)):
        if expre[i] == 'q':
            newExpre += valQ

        elif expre[i] == 'p':
            newExpre+= valP
        
        elif expre[i] == '^':
            newExpre += '*'

        elif expre[i] == 'v':
            newExpre += '+'

        elif expre[i] == '!':
            i+=1
            if expre[i] != '(':
                if expre[i] == 'q':
                    if(valQ == '1'):
                        newExpre += '0'
                    else:
                        newExpre += '1'
                
                if expre[i] == 'p':
                    if(valP == '1'):
                        newExpre += '0'
                    else:
                        newExpre += '1'
            else:
                pass
        i+=1

    return newExpre


print(calc("q^p > q",'V','F'))