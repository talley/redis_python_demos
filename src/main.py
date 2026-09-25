import employee as emp
import employeerepository as repos
import uuid

import redis

    
repository = repos.EmployeeRepository()
    
employee = emp.Employee(
        id=str(uuid.uuid4()),
        first_name="James",
        last_name="Arthur",
        age=40
    )
    
#repository.create(employee)
#print("Employee created.")
con = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True,
            protocol=2
        )

repository = repos.EmployeeRepository()
emp1 = repository.get_by_id(employee_id='c8583d39-029d-4f0c-ac08-8c0ee1b9f66d')
print(emp1)