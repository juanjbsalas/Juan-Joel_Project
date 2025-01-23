import pdfplumber
pdf_path = "/Users/juansalas/Documents/JuanSalasScratchwork/Course Section Enrollment.pdf"
     

##MAIN CODE
with pdfplumber.open(pdf_path) as pdf:
    for x, page in enumerate(pdf.pages):
        text = page.extract_text()


course_list = text.splitlines()

print(course_list)
print(" ")

for index, element in enumerate(course_list):
    if course_list[index][0:3] == "REL":          ##LOOKS FOR RELIGION COURSES
        del course_list[0:index]                  # Now index 0 contains REL
        break


del course_list[len(course_list) - 3:len(course_list)] #Deletes office of info whatever



print(course_list)
print(" ")
print(" ")
print(" ")

print(course_list[1][::-1])

print(" ")
print(" ")
print(" ")

seats = []

for index, course in enumerate(course_list):
    course_reversed = course[::-1]

"""
    for i, ch in enumerate(course_reversed):
        if ch.isnumeric():
            seats.append(int(ch))
        elif ch == "-" and course_reversed[i + 1].isnumeric():
            seats.append(int(course_reversed[i + 1]) * -1)
        else:
            seats.append("X")

"""



## Maybe email Dr. Tobias and see what she thinks? IDKKKKKKKK
print(seats)

















"""

print(course_list[1:])
avail = 0
y = 0

for course in course_list[1:]: #so it starts at an actual course
    if course[0:4] == "2630":
        print("Found course in PDF! Now let's see if there are available seats")
        #Reverse whole course_string, then delete characters until index finds available seat number, then reverse again
        print(course)
        course_seats_only = course[::-1] #reverses course string in the list
        print(" ")
        print(course[::-1])
        print(" ")
        #Find the integer in string and delete name of professor

        for i, ch in enumerate(course_seats_only):
            if ch.isalpha() == True or ch == " ":
                if ch == "-":
                    y = i
                    break 
        
        course_seats_only = course_seats_only[0:y]
        course = course_seats_only[::-1] #reverse again


    else:
        print("CRN entered was not found on course list")

    print(" ")
    print(course)

"""
##NEXT STEPS
"""
1. Remove the names of the professsors from the items of the list so that the ending index of a item is just the seats available
2. check if course available is greater than 0 then print there are seats available

Further steps:
see how i can download the pdf every 5 minutes into a public storage.

"""


