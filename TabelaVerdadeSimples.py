def interface():
    print("Seja bem vindo a Super Calculadora Verdade!\n")
    print("ATENÇÃO!!! USE PARENTESES PARA DELIMITAR A ORDEM!")
    valP = str(input("Digite o valor de 'p': ")).upper()
    valQ = str(input("Digite o valor de 'q': ")).upper()
    print("Operadores: and(^),or(v),se então(>), se somente se(#) e not(!)")
    expre = str(input("Digite uma proposição: ")).replace(" ", "").replace("Q","q").replace("P","p")
    print(calc(expre,valP,valQ))
    ##resultado = calc(formatacao(expre,valP,valQ))  


def calc(expre,valP,valQ):
    expre = formatacao(expre,valP,valQ)
    expre = solveParenteses(expre,valP,valQ)
    if len(expre) == 1:
        return expre
    elif len(expre) ==2:
        return expre[0]
    expre = solveOperacao(expre[0],expre[1],expre[2])
    return expre


def  solveOperacao(v1,op,v2):
    match op:
        case '^':
            return ("V" if v1== v2 and v1 == 'V' else 'F')
        case 'v':
            return ("V" if v1== 'V' or v2 == 'V' else 'F')
        case '>':
            return ("F" if v1== 'V' and v2 == 'F' else 'V')
        case '#':
            return ("V" if v1== v2 else 'F')
        

def formatacao(expre,valP,valQ):
    newExpre = ""
    i = 0
    while(i < len(expre)):
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
            elif expre[i+1] == '(':
                resExpre = expre[i+1:len(expre)]
                conteudo = getConteudoParentese(resExpre,valP,valQ)
                if conteudo[0] == 'V':
                    val = 'F'
                elif conteudo[0] == 'F':
                    val = 'V'
                i
            newExpre += val
            i+=1+conteudo[1]

        else:
            
            newExpre += expre[i]
        
        i+=1
    
    return newExpre


def solveParenteses(expre,valP,valQ):
    newExpre=""
    contParenteses = 0
    ## ((qvp)^p) -> (qvp)^p | (qvp) -> qvp -> F ou V
    i =0
    while(i<len(expre)):
        if expre[i] == '(':
            conteudoParentese=""
            contParenteses+=1
            while(True):
                i += 1
                if expre[i] == '(':
                    contParenteses += 1

                elif expre[i] == ')':
                    contParenteses -= 1

                if contParenteses <= 0:
                    break

                conteudoParentese += expre[i]
            newExpre += calc(conteudoParentese,valP,valQ)
        else:
            newExpre += expre[i]

        i+= 1
    return newExpre


##Função que colocar solveParenteses

def criarParenteses(expre):
    pass


def getConteudoParentese(expre,valP,valQ):
    contParenteses = 0
    i =0
    while(i<len(expre)):
        if expre[i] == '(':
            conteudoParentese=""
            contParenteses+=1
            while(True):
                i += 1
                if expre[i] == '(':
                    contParenteses += 1

                elif expre[i] == ')':
                    contParenteses -= 1

                if contParenteses <= 0:
                    break

                conteudoParentese += expre[i]
            return [calc(conteudoParentese,valP,valQ),i]

        i+= 1


interface()

##(FvV)#V)vF
##(!(V)#V)vF
##                         (F#V)vF -> FvF -> F
##FvF
##F