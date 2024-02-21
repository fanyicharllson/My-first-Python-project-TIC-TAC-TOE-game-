value = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
row = ""
colon = ""
token = "x"
number = ""
i = 0
tie = False

def function1():
    print("   |   |   ")
    print(" " + str(value[0][0]) + " | " + str(value[0][1]) + " | " + str(value[0][2]))
    print("-----------")
    print(" " + str(value[1][0]) + " | " + str(value[1][1]) + " | " + str(value[1][2]))
    print("-----------")
    print(" " + str(value[2][0]) + " | " + str(value[2][1]) + " | " + str(value[2][2]))
    print("   |   |   ")

def function2():
    global token
    global row
    global colon
    number = int(input("Enter your number: "))
    if number == 1:
        row = 0
        colon = 0
    elif number == 2:
        row = 0
        colon = 1
    elif number == 3:
        row = 0
        colon = 2
    elif number == 4:
        row = 1
        colon = 0
    elif number == 5:
        row = 1
        colon = 1
    elif number == 6:
        row = 1
        colon = 2
    elif number == 7:
        row = 2
        colon = 0
    elif number == 8:
        row = 2
        colon = 1
    elif number == 9:
        row = 2
        colon = 2
    else:
        print("Enter the right number!")
        return function2()
    if value[row][colon] != "x" and value[row][colon] != "o":
        value[row][colon] = token
        if token == "x":
            token = "o"
        else:
            token = "x"
    else:
        print("There is no space!")
        return function2()
    function1()

def function3():
    global tie
    for i in range(3):
        if value[i][0] == value[i][1] == value[i][2] or value[0][i] == value[1][i] == value[2][i]:
            return value[i][0]
        elif value[0][0] == value[1][1] == value[2][2] or value[0][2] == value[1][1] == value[2][0]:
            return value[1][1]
    for i in range(3):
        for j in range(3):
            if value[i][j] != "x" and value[i][j] != "o":
                return False
    tie = True
    return False

print("\t...Welcome to Tic Tac Toe Game...")
name = input("Enter the name of the first player (x): ")
name2 = input("Enter the name of the second player (o): ")
print("\n")
print(name + " is the player for 'x'")
print(name2 + " is the player for 'o'")

function1()
winner = function3()
while not winner:
    print(f"{name}'s turn:")
    function2()
    winner = function3()
    if winner:
        break
    print(f"{name2}'s turn:")
    function2()

if winner == "x":
    print(f"{name} is the winner!")
elif winner == "o":
    print(f"{name2} is the winner!")
else:
    print("The game is a draw!")
