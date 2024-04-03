def interface():
    print("Seja bem vindo a Super Calculadora Verdade!\n")
    valP = str(input("Digite o valor de 'p': "))
    valQ = str(input("Digite o valor de 'q': "))
    print("Operadores: and(^),or(v),se então(>), se somente se(#) e not(!)")
    expre = str(input("Digite uma preposição: ")).replace(" ", "")
    print(formatacao(expre,valP,valQ))
    ##resultado = calc(formatacao(expre,valP,valQ))
    

def formatacao(expre,valP,valQ):
    newExpre = ""
    i = 0
    while(i < len(expre)):
        print("Aq")
        if expre[i] == 'q':
            newExpre += valQ

        elif expre[i] == 'p':
            newExpre += valP

        elif expre[i] == '!':
            val = ""
            if expre[i+1] == 'q':
                if valQ == 'V':
                    val = 'F'
                else:
                    val = 'V'
            elif expre[i+1] == 'p':
                if valP == 'V':
                    val = 'F'
                else:
                    val = 'V'
            else:
                val = 'V'
            newExpre += val
            i+=1

        else:
            newExpre += expre[i]
        
        i+=1
    
    return newExpre

def eliminaParenteses(expre):
    newExpre=""
    contParenteses = 0
    ## ((qvp)^p) -> (qvp)^p | (qvp) -> qvp -> F ou V
    i =0
    while(i<len(expre)):
        if expre[i] == '(':
            contParenteses+=1
            while(True):
                i += 1
                if expre[i] == '(':
                    contParenteses += 1

                elif expre[i] == ')':
                    contParenteses -= 1
                if contParenteses <= 0:
                    
                    break

                newExpre += expre[i]
        else:
            newExpre += expre[i]

        i+= 1

    return newExpre



interface()



##((q^p)^((qvp)^p))