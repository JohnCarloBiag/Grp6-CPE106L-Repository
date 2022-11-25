#ProgrammingProblem2
#Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and inputs the lines of text into a list. 
#The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. 
#If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.9

filename = input("Enter the file name and format.\n(name.format): ")

file = open(filename, 'r')

linecount = 0
for line in file:
    linecount = linecount + 1
    
print("\n",filename,"has",linecount,"lines")

while True:
    numline = 0
    num = int(input("\nEnter a line number or [0] to quit: "))
    if num >=1 and num <= linecount:
        file = open(filename, 'r')
        for lines in file:
            numline = numline + 1
            if numline == num:
                print(num,":",lines)
    elif num == 0:
        break
    
    else:
        if num!= linecount:
            print("\nline number is not available, please input a number less than",linecount)
