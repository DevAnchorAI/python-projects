
import utils as ut;
from employee import Employee;

if __name__ == "__main__":
    name="Alice";
    print(ut.greet(name));
    print(ut.farewellMsg(name));
    a, b = 10, 5;
    print(f"Addition: {ut.add(a, b)}");
    print(f"Subtraction: {ut.subtract(a, b)}");
    print(f"Multiplication: {ut.multiply(a, b)}");
    print(f"Division: {ut.divide(a, b)}");
    print(f"Hello Python");
    
    employee = {
    "id": 101,
    "name": "John",
    "salary": 75000
}

print("salary:",employee["salary"])
if employee["salary"]>80000:
   print(f"Good Salary");
elif employee["salary"]>50000:
    print(f"Average salary");  
else:
    print(f"Bad salary");


# for i in range(5):
#     print(i)

employees = ["John", "David", "Robert"]
for employee in employees:
    print(employee)

#Function
def add(a,b):
    return a+b;

result = add(5,6);
print(result)

employee= Employee("SUMAN");
print(employee.name)

