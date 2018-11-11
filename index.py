global positions
positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def viewTable():
    print(positions[0] + " | " + positions[1] + " | " + positions[2])
    print("---------")
    print(positions[3] + " | " + positions[4] + " | " + positions[5])
    print("---------")
    print(positions[6] + " | " + positions[7] + " | " + positions[8])

def checkWin(playerNum):
    win = False
    if positions[0] != ' ' and positions[0] == positions[1] and positions[1] == positions[2]:
        win = True
    elif positions[3] != ' ' and positions[3] == positions[4] and positions[4] == positions[5]:
        win = True
    elif positions[6] != ' ' and positions[6] == positions[7] and positions[7] == positions[8]:
        win = True
    elif positions[0] != ' ' and positions[0] == positions[4] and positions[4] == positions[8]:
        win = True
    elif positions[2] != ' ' and positions[2] == positions[4] and positions[4] == positions[6]:
        win = True
    elif positions[0] != ' ' and positions[0] == positions[3] and positions[3] == positions[6]:
        win = True
    elif positions[1] != ' ' and positions[1] == positions[4] and positions[4] == positions[7]:
        win = True
    elif positions[2] != ' ' and positions[2] == positions[5] and positions[5] == positions[8]:
        win = True
    if win == True and playerNum == 1:
        print("Player 1 wins!!!!!!!!!")
    elif win == True and playerNum == 2:
        print("Player 2 wins!!!!!!!!!")
    viewTable()
    if playerNum == 1:
        start2(win)
    if playerNum == 2:
        start1(win)

def markPos(position, marker, playerNum):
    itWorked = True
    if position == "tl" and positions[0] == ' ':
        positions[0] = marker
    elif position == "tc" and positions[1] == ' ':
        positions[1] = marker
    elif position == "tr" and positions[2] == ' ':
        positions[2] = marker
    elif position == "ml" and positions[3] == ' ':
        positions[3] = marker
    elif position == "mc" and positions[4] == ' ':
        positions[4] = marker
    elif position == "mr" and positions[5] == ' ':
        positions[5] = marker
    elif position == "bl" and positions[6] == ' ':
        positions[6] = marker
    elif position == "bc" and positions[7] == ' ':
        positions[7] = marker
    elif position == "br" and positions[8] == ' ':
        positions[8] = marker
    else:
        print("Silly goof, that spot is already taken. Try again")
        itWorked = False
        if playerNum == 1:
            start1(False)
        elif playerNum == 2:
            start2(False)
    if itWorked == True:
        checkWin(playerNum)

def convertPos(position, playerNum):
    marker = ' '
    if playerNum == 1:
        marker = 'X'
    else:
        marker = 'O'
    markPos(position, marker, playerNum)

def askPlayer(playerNum):
    pythonIsAnnoying = ("Player %d pick your position" % playerNum)
    choice = input(pythonIsAnnoying)
    if choice != "tr" and choice != "tc" and choice != "tl" and choice != "ml" and choice != "mc" and choice != "mr" and choice != "bl" and choice != "bc" and choice != "br":
        print("Silly goof, thats an invalid input. Try again")
        if playerNum == 1:
            start1(False)
        elif playerNum == 2:
            start2(False)
    else:
        convertPos(choice, playerNum)

def start1(win):
    if win == False:
        askPlayer(1)

def start2(win):
    if win == False:
        askPlayer(2)

print("Welcome to TicTacToe. When prompted, enter the characters correlating to the position you want to place a marker in. The characters and positions are as follows:")
print("tl | tc | tr")
print("------------")
print("ml | mc | mr")
print("------------")
print("bl | bc | br")

start1(False)
# 64, 58
