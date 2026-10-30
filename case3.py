basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10

gross = basic + hra + da
deduction = gross * 0.05
net = gross - deduction

print("Gross Salary:", gross)
print("Net Salary:", net)