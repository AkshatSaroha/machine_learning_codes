basic_salary = float(input('Enter your salary : '))
TA = 0.1 * basic_salary
DA = 0.05 * basic_salary
gross_salary = basic_salary + TA + DA

print('TA : ', TA)
print('DA : ', DA)
print('Gross salary : ', gross_salary)

tax = gross_salary * 0.1
net_salary = gross_salary - tax
print('Tax : ', tax)
print('Net Salary : ', net_salary)
