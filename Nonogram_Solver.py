filename = input('Zadejte jmeno souboru se zadáním \n')

x, o, n = '░', '█', '_'
import turtle
Main_turtle = turtle.Turtle()
Main_turtle.up()
Main_turtle.screen.bgcolor('khaki')

file = open(filename, 'r')
cisla = [(x.strip()).split() for x in file.readlines()]
columns, rows, i = [], [], 0
file.close()

maxlen1 = len(cisla[i])
while len(cisla[i]) > 0:
    col = [int(y) for y in cisla[i]]
    columns.append(col)
    maxlen1 = max(len(cisla[i]), maxlen1)
    i += 1
i += 1
maxlen2 = len(cisla[i])
while len(cisla[i]) > 0:
    row = [int(z) for z in cisla[i]]
    rows.append(row)
    maxlen2 = max(len(cisla[i]), maxlen2)
    i += 1
A, B = len(columns), len(rows)

#Data jsou nactena a zacina doplnovani
###

def rozdel_barvy(seznam, colrow):
    A = len(seznam)
    cerna = [0 for _c in range(A)]
    bila = [0 for _b in range(A)]
    for x in range(A):
        if colrow[x] == n:
            if seznam[x] == o:
                cerna[x] = 1
            else:
                bila[x] = 1
    return(cerna, bila, 1)

def policko(colrow, tryout, cisla):
    delka, s = len(colrow), 0
    if cisla == []:
        spor = False
        for index in range(len(tryout), delka):
            tryout.append(x)
            if colrow[index] == o:
                spor = True
        if spor:
            return([0 for _ in range(delka)], [0 for _ in range(delka)], 0)
        else:
            return(rozdel_barvy(tryout, colrow))

    cerne = [0 for _ in range(A)]
    bile = [0 for _ in range(A)]
    scitac = 0
    if len(tryout) > 0:
        s = 1
    for mezera in range(s, delka - sum(cisla) - len(tryout) - len(cisla) + 2):
        zbyla_cisla = cisla[:]
        spor, new_tryout, index = False, tryout[:], -1

        index = len(new_tryout) - 1
        for i_ in range(mezera):
            index += 1
            new_tryout.append(x)
            if colrow[index] != n and colrow[index] != x:
                spor = True

        for j_ in range(zbyla_cisla.pop(0)):
            index += 1
            new_tryout.append(o)
            if colrow[index] != n and colrow[index] != o:
                spor = True
        if spor:
            continue
    
        p = policko(colrow, new_tryout, zbyla_cisla)

        for w in range(delka):
            cerne[w] += p[0][w]
            bile[w] += p[1][w]
        scitac += p[2]

    return(cerne, bile, scitac)
                
def projdi(colrow: list, cisla: list):
    filled = policko(colrow, [], cisla)
    jist_A = []
    jist_B = []
    soucet = filled[2]
    if soucet >= 1:
        for i in range(len(colrow)):
            if filled[0][i] == soucet:
                jist_A.append(i)
            if filled[1][i] == soucet:
                jist_B.append(i)
        return(jist_A, jist_B, soucet)
    else:
        return(False)

#Nakreslí čtverec
def ctverecek(turtle):
    turtle.begin_fill()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.right(90)

grid = [[n for x in range(A)] for y in range(B)]
zmeny_gridu = []
kontrola = [0 for x in range(A+B)]
#pole kontrola je A radku + B sloupcu v tomto poradi

row0, col0 = -(A + maxlen2)/2 + maxlen2, (B + maxlen1)/2 - maxlen1
#jen vzorec aby byl obrázek cca středově zarovnaný (row0, col0 jsou počátky souřadnic)

#Turtle vyznačuje okraje obrázku
Main_turtle.ht()
Main_turtle.color('black')
Main_turtle.goto(row0*10, col0*10)
Main_turtle.down()
Main_turtle.forward(A*10)
Main_turtle.right(90)
Main_turtle.forward(B*10)
Main_turtle.right(90)
Main_turtle.forward(A*10)
Main_turtle.right(90)
Main_turtle.forward(B*10)
Main_turtle.up()
Main_turtle.speed(10.5)

#Nakreslení čísel na okraj:
z = 0
for col in columns:
    z2 = 0
    for number in reversed(col):
        if number > 9:
            z += 0.4
        Main_turtle.goto((row0+z)*10 + 3, (col0+z2)*10)
        z2 += 1
        Main_turtle.write(number)
    z += 1

y = -1
for row in rows:
    y2 = -1
    for number in reversed(row):
        if number > 9:
            y2 -= 0.4
        Main_turtle.goto((row0+y2)*10, (col0+y)*10 - 3)
        
        y2 -= 1
        Main_turtle.write(number)
    y -= 1


#Úvodní kolo procházení
for b in range(B-1, -1, -1):
    v = projdi(grid[b], list(rows[b]))

    for i in v[0]:
        kontrola[A + b] += 1
        kontrola[i] += 1
        grid[b][i] = o
        Main_turtle.color('black', 'black')
        Main_turtle.goto((row0+i)*10, (col0-b-1)*10)
        ctverecek(Main_turtle)
        zmeny_gridu.append(False)
        zmeny_gridu.append(i)
    for i in v[1]:
        kontrola[A + b] += 1
        kontrola[i] += 1
        grid[b][i] = x
        Main_turtle.color('black', 'white')
        Main_turtle.goto((row0+i)*10, (col0-b-1)*10)
        ctverecek(Main_turtle)
        zmeny_gridu.append(False)
        zmeny_gridu.append(i)


for a in range(A-1, -1, -1):
    v = projdi([grid[x][a] for x in range(B)], list(columns[a]))

    for i in v[0]:
        kontrola[a] += 1
        kontrola[A + i] += 1
        grid[i][a] = o
        Main_turtle.color('black')
        Main_turtle.goto((row0+a)*10, (col0-i-1)*10)
        ctverecek(Main_turtle)
        zmeny_gridu.append(True)
        zmeny_gridu.append(i)
    for i in v[1]:
        kontrola[a] += 1
        kontrola[A + i] += 1
        grid[i][a] = x
        Main_turtle.color('white')
        Main_turtle.goto((row0+a)*10, (col0-i-1)*10)
        ctverecek(Main_turtle)
        zmeny_gridu.append(True)
        zmeny_gridu.append(i)

s = 'No error yet'
while len(zmeny_gridu) > 0:
    index = zmeny_gridu.pop()

    if zmeny_gridu.pop() == True:
        if kontrola[A + index] != A:
            # 2.podminka je aby neprocházel už vyplněný colrow
            v = projdi(grid[index], list(rows[index]))
            if v == False:
                zmeny_gridu = []
                s = True
                break

            for i in v[0]:
                kontrola[A + index] += 1
                kontrola[i] += 1
                grid[index][i] = o
                Main_turtle.color('black')
                Main_turtle.goto((row0+i)*10, (col0-index-1)*10)
                ctverecek(Main_turtle)
                zmeny_gridu.append(False)
                zmeny_gridu.append(i)
            for i in v[1]:
                kontrola[A + index] += 1
                kontrola[i] += 1
                grid[index][i] = x
                Main_turtle.color('white')
                Main_turtle.goto((row0+i)*10, (col0-index-1)*10)
                ctverecek(Main_turtle)
                zmeny_gridu.append(False)
                zmeny_gridu.append(i)


    elif kontrola[index] != B:
        v = projdi([grid[x][index] for x in range(B)], list(columns[index]))
        if v == False:
                zmeny_gridu = []
                s = False
                break

        for i in v[0]:
            kontrola[index] += 1
            kontrola[A + i] += 1
            grid[i][index] = o
            Main_turtle.color('black')
            Main_turtle.goto((row0+index)*10, (col0-i-1)*10)
            ctverecek(Main_turtle)
            zmeny_gridu.append(True)
            zmeny_gridu.append(i)
        for i in v[1]:
            kontrola[index] += 1
            kontrola[A + i] += 1
            grid[i][index] = x
            Main_turtle.color('white')
            Main_turtle.goto((row0+index)*10, (col0-i-1)*10)
            ctverecek(Main_turtle)
            zmeny_gridu.append(True)
            zmeny_gridu.append(i)
            


if sum(kontrola) < int(A*B*2):
    if s == True:
        print('Zastaveno na', index, '.', 'řádku z důvodu chyby v zadání.')
    elif s == False:
        print('Zastaveno v', index, '.', 'sloupci z důvodu chyby v zadání.')
    else:
        print('Zastaveno: obrázek není kompletní, nonogram nelze vyřešit.')
print('\n'.join((''.join(str(m) for m in n)) for n in grid))
print('Obrázek hotov')
turtle.done()