total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / total_classes) * 100

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")