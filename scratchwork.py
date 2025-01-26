import pdfplumber
pdf_path = "/Users/juansalas/Documents/JuanSalasScratchwork/Course Section Enrollment.pdf"
     

##MAIN CODE

######## This is assuming PDF only has one page#######

with pdfplumber.open(pdf_path) as pdf: 
    for x, page in enumerate(pdf.pages):
        text = page.extract_text()

######### Makes a list, each item is a different course

course_list = text.splitlines()

print(course_list)
print(" ")

######## Updates course_list to ONLY be filtered with religion courses

for index, element in enumerate(course_list):
    if course_list[index][0:3] == "REL":          ##LOOKS FOR RELIGION COURSES
        del course_list[0:index]                  # Now index 0 contains REL
        break


#in this case, the few last items in course_list were irrelevant information so I deleted it.

del course_list[len(course_list) - 3:len(course_list)] #Deletes office of info whatever


print(course_list)
print(" ")
print(" ")


print(course_list[1][::-1])

print(" ")
print(" ")
print(" ")

seats = []

course_list_copy = []
course_list_copy.append(course_list[0]) ##Appends which type of course is in the filtered list (For example 'REL)

for item, value in enumerate(course_list[1:]):
    course_list_copy.append(value[::-1])


print("This is the course list with reversed strings!!")
print(course_list_copy)
print("")
print("Now let's remove the name of the professors to get the seats!")


desired_CRN = '2630'
desired_CRN_index = 0



#NEXT STEP WOULD BE TO FIND WHAT INDEX IS THE desiredCRN in the regular course_list

for index, course in enumerate(course_list):
    if course[:4] == desired_CRN:
        desired_CRN_index = index
        break

#When you find the index, plug it to the of the course_list_reversed; then removethe professors name and geet number of seats

seat = 0
x = course_list_copy[desired_CRN_index]

for index, ch in enumerate(x):
    if ch.isnumeric() == True and x[index - 1].isalpha() ==  True:
        seat = int(ch)
        break
    elif ch == "-":
        seat = x[index + 1]
        seat = int(seat) * -1
        break

#If number of seats is greater than 0 then send message to user.

if seat == 1:
    print(f"There is {seat} seat available in Course with CRN {desired_CRN}. Register now!!")
elif seat > 0:
    print(f"There are {seat} seats available in Course with CRN {desired_CRN}. Register now!!")
else:
    print(f"There are no seats available at the moment.")



