import salaryModule as sm

salary = 1000
newSalary = sm.promoteSalary(salary)
newSalary #output: 1200

from salaryModule import demoteSalary
salary = 5000
newSalary = demoteSalary(salary)
newSalary #output: 4000


print(sm.teslaSalaries) #output: [1000, 2000, 3000, 4000]
