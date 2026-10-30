marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / n)