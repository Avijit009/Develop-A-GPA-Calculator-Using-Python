""" 0-40 = F
41 - 60 = D
61 - 70 = C
71-80 = B
81 - 90 = A
91 - 100 = A+ """

bengali = int(input("Enter Your Bengali Subject Obtain Marks: "))
english = int(input("Enter Your English Subject Obtain Marks: "))
math = int(input("Enter Your Math Subject Obtain Marks: "))
science = int(input("Enter Your Science Subject Obtain Marks: "))

if (bengali > 100 or english > 100 or math > 100 or science > 100):
    print("You can not enter marks greater than 100.")

else: 
    
    totalObtainMasrks = bengali + english + math + science

    averageObtainMarks = round(totalObtainMasrks / 4)

    """ print(totalObtainMasrks)
    print(averageObtainMarks) """

    if (averageObtainMarks <= 40):
        print("Your obtain grade is: F")

    elif (averageObtainMarks > 40 and averageObtainMarks <=0):
        print("Your obtain grade is: D")

    elif (averageObtainMarks > 60 and averageObtainMarks <= 70):
        print("Your obtain grade is: C")
        
    elif (averageObtainMarks >70 and averageObtainMarks <= 80):
        print("Your obtain grade is: B")
        
    elif (averageObtainMarks > 40 and averageObtainMarks <= 90):
        print("Your obtain grade is: A")

    elif (averageObtainMarks > 90 and averageObtainMarks <= 100):
        print("Your obtain grade is: A+")