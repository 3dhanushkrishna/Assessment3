x = int(input("Number of classes held: "))
y = int(input("Number of classes attended: "))
percentage = y/x*100
if percentage >= 75:
    print("The student is allowed to sit in examhall")
else:
    print("The student is not allowed to sit in examhall")