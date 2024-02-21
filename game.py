value = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
row = ""
colon =""
token = "x"
number = ""
i = 0
tie = False

def function1():
    print("   |                   |    ")
    print(str(value[0][0]) +  "  |  " +        str(value[0][1]) + "                |  " + str( value[0][2]))
    print("______________________________")
    print("   |                   |    ")
    print(str(value[1][0]) +  "  |  " +        str(value[1][1]) + "                |  " + str( value[1][2]))
    print("______________________________")
    print("   |                   |    ")
    print(str(value[2][0]) +  "  |  " +        str(value[2][1]) + "                |  " + str( value[2][2]))
    print("   |                   |   ")
    
   
def function2():
    if token == "x":
        number = int(input("Enter your number: "))
    if token == "o":
        number = int(input("Enter a number: "))
    if number ==  1:
        row = 0
        colon = 0
    if number == 2:
        row = 0
        colon = 1   
    if number == 3:
        row = 0
        colon = 2
    if number ==  4:
        row = 1
        colon = 0
    if number == 5:
        row = 1
        colon = 1   
    if number == 6:
        row = 1
        colon = 2
    if number ==  7:
        row = 2
        colon = 0
    if number == 8:
        row = 2
        colon = 1   
    if number == 9:
        row = 2
        colon = 2
        
    elif number<1 and number > 9:
        print("Wrong Value!")
    else:
        print("Enter the right number!")  
        
    if token == "x" and value[row][colon] !="x" and value[row][colon] != "o":
        value[row][colon] = "x"
        token = "o"
    elif token =="o" and value[row][colon] !="o" and value[row][colon] !="x":
        value[row][colon] = "o"
        token = "x"
    else:
        print("There is no space!")
        
        print(function2())
        
         
    print(function1()) 
    
def function3():
    for i in range(3):
        if value[i][0] == value[i][1] and value[i][0] == value[i][2] or value[i][0] == value[1][i] and value[i][0] == value[2][0]:
            return True       
        elif value[0][0] == value[1][1] and value[1][1]==value[2][2] or value[0][2] == value[1][1] and value[1][1]== value[2][0]:
            return True
    for i in range(3):
        for j in range(3):
            if value[i][j] !="x" and value[i][j]!="0":
                return False  
    
    
    tie = True
    return False          
                             
                             
print("\t...Welcome to Tic Tac Toe Game...")
name = input("Enter the name of the first player: ")
name2 = input("Enter the name of the second player: ")
print("\n")
print(name + " is the first player!")
print(name2 + " is the name of the second player")

while not function3():
    print(function1())
    print(function2())
    print(function3())

if token == "x" and tie == False:
    print(name + " is the winner")
elif token == "o" and tie == True:
    print(name2 + " is the looser!")
else:
    print("The game is draw!")        
     