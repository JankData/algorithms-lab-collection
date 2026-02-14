def to_onp(wyrazenie):
    wynik = []
    stos = []

    for znak in wyrazenie:
        if znak.isdigit():
            wynik.append(znak)
        elif znak == '(':
            stos.append(znak)
        elif znak == ')':
            #zdejmuje do napotkania (
            while len(stos)>0 and stos[-1] != '(':
                wynik.append(stos.pop())
            if len(stos)>0 and stos[-1] == '(':
                stos.pop()
        elif znak == '+' or znak == '*':
            while len(stos)>0 and stos[-1] != '(':
                #jeśli + zdejmuje wszystko
                #jeśli * zdejmuje *
                if znak == '+' or stos[-1] == '*':
                    wynik.append(stos.pop())
                else:
                    break
            stos.append(znak)

    while len(stos)>0:
        wynik.append(stos.pop())

    return ''.join(wynik)

def eval_onp(onp):
    stos = []
    for znak in onp:
        if znak.isdigit():
            stos.append(int(znak))
        elif znak == '+' or znak == '*':
            b = stos.pop()
            a = stos.pop()
            if znak == '+':
                stos.append((a + b) % 10)
            else:
                stos.append((a * b) % 10)
    return stos[-1]

def eval_m10(infiks):
    return eval_onp(to_onp(infiks))


while True:
    s = input('podaj wyrażenie lub "quit": ').strip()
    if s.lower() == 'quit':
        break
    try:
        print(eval_m10(s))
    except Exception as e:
        print('błąd:', e)