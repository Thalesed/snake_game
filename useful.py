import random
def title(word):
    print('\033[33m-\033[m'*(len(word)+12))
    print('    ',word)
    print('\033[33m-\033[m' * (len(word) + 12))
def menu(lis):
    for c in range(len(lis)):
        print(lis[c])
def line(n):
    print('\033[33m-\033[m' *n)
def sort():
    r = random.randint(10, 570)
    b = r - (r % 10)
    return b
def comun(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])
def exist(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def makefile(file):
    try:
        a = open(file, 'wt+')
    except:
        print('Erro ao criar o arquivo')
    else:
        print(f'{file} criado com sucesso')
def readfile(file):
    try:
        a = open(file, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        title('Pessoas cadastradas')
        print(a.read())
    finally:
        a.close()

def cadastrar(file, name='desconhecido', age= 0):
    try:
        a = open(file, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{name} {age}')
        except:
            print('erro')

def letras():
    l = random.randint(0, 36)
    if l == 0:
        return 'a'
    if l == 1:
        return 'b'
    if l == 2:
        return 'c'
    if l == 3:
        return 'd'
    if l == 4:
        return 'e'
    if l == 5:
        return 'f'
    if l == 6:
        return 'g'
    if l == 7:
        return 'h'
    if l == 8:
        return 'i'
    if l == 9:
        return 'j'
    if l == 10:
        return 'k'
    if l == 11:
        return 'l'
    if l == 12:
        return 'm'
    if l == 13:
        return 'n'
    if l == 14:
        return 'o'
    if l == 15:
        return 'p'
    if l == 16:
        return 'q'
    if l == 17:
        return 'r'
    if l == 18:
        return 's'
    if l == 19:
        return 't'
    if l == 20:
        return 'u'
    if l == 21:
        return 'v'
    if l == 22:
        return 'w'
    if l == 23:
        return 'x'
    if l == 24:
        return 'y'
    if l == 25:
        return 'z'
    if l == 26:
        return '1'
    if l == 27:
        return '2'
    if l == 28:
        return '3'
    if l == 29:
        return '4'
    if l == 30:
        return '5'
    if l == 31:
        return '6'
    if l == 32:
        return '7'
    if l == 33:
        return '8'
    if l == 34:
        return '9'
    if l == 35:
        return '0'
    if l == 36:
        return 'ç'

def loru(str):
    num = random.randint(0, 1)
    if num == 0:
        return str.lower()
    else:
        return str.upper()

def gerate():
    len = random.randint(6, 15)
    word = ''
    for c in range(len):
        wordin = letras()
        wordint = loru(wordin)
        word += wordint
    return word
def selectword():
    final = ''
    words = ['serjo burro', 'neymar',' de',' para',' por', ' que', ' bot',' ante',' a',' apos',' perante',' mussolini', ' xuxa', ' esquizofrênico',' hitler', ' boot', ' robo', ' aleatorio', ' trabalho', ' história', ' geografia', ' matématica', ' loucura', ' português', ' facismo', ' nazismo', ' racismo', ' bolsonaro', ' sérgio', ' maluco', ' deus', ' jesus', ' maome',' judeu', ' adulto ney', ' ney cresceu', 'menino ney cresceu']
    quant = random.randint(3, 12)
    for c in range(0, quant):
        word = random.randint(0, len(words) - 1)
        final += words[word]
    return final
def selectext():
    final = ''
    words = [' ney adulto', ' de', ' para', ' por', ' que', ' bot', ' ante',' neymaradulto', ' a', ' apos', ' perante', ' mussolini', ' xuxa',
             ' esquizofrênico', ' hitler', ' boot', ' robo', ' aleatorio', ' trabalho', ' história', ' geografia', ' grande ney'
             ' matématica', ' loucura', ' português', ' facismo', ' nazismo', ' racismo', ' bolsonaro', ' sérgio',
             ' maluco', ' deus', ' jesus', ' maome', ' judeu',' neycresceu', ' serjo folgado', ' grandeney', ' fabiana', ' cão', ' hoje', ' comunismo',                      ' socialismo', ' capitalismo', 'bomba', 'giromangoba',' Chechenia', 'brasil', 'goiaba', 'bot', 'robooot', 'text', 'automatico', ' neyadulto',                 ' neymar', ' bot', ' hacker', ' neymar', ' serjo burro', ' socialismo é uma merda', ' adulto ney', ' fuguete', ' grande ney', ' menino ney cresceu']
    quant = random.randint(39, len(words))
    for c in range(1, quant):
        word = random.randint(0, len(words)-1)
        final += words[word]
    return final
