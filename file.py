#Reading files
# r = read information inside file
# w =  you can write information inside the file or changr
# a = append this you can add informatio into the end of file
# r+ = you can read and write

# employee_file = open("doc.txt", "r")
# print(employee_file.readable())  #readable is tell us wethe rthe file is readable or not
#print(employee_file.read()) #read will display all information in the file
#print(employee_file.readline()) #readline will read the first line and second readline will read the second line in the file and same for more
#print(employee_file.readlines()) #readlines will read all the files and put them in an array
#print(employee_file.readlines()[0]) #this will display the first line in the file

# for employee in employee_file.readlines():
#      print(employee)# this will print enery thing in the file
# employee_file.close()

#writing to files
# employee_file = open("doc.txt", "a") #when you use w instead of a, it will overide all the existing doc that is only the pricise name will be viewed
#To create a file
# employee_file = open("doc2.txt", "w") #you can also replcse doc2 with index.html to create its file

# employee_file.write("David - doctor")
# for employee in employee_file.readlines():
#      print(employee)# this will print enery thing in the file
# employee_file.close()


# Modules and pip
# import file2
# print(file2.roll_dice(10))

           