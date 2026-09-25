import redis
import employee as emp

class EmployeeRepository:

    def __init__(self):
        self.redis = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True,
            protocol=2
        )

    def create(self, employee):
        key = f"employee:{employee.id}"
    
        if self.redis.exists(key):
            raise ValueError(
                f"Employee with ID {employee.id} already exists."
            )
    
        self.redis.hmset(
            key,
            {
                "id": employee.id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "age": employee.age
            }
        )
    
        return employee  

    def get_by_id(self, employee_id):
        key = f"employee:{employee_id}"

        data = self.redis.hgetall(key)

        if not data:
            return None

        return emp.Employee(
            id=str(data["id"]),
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=int(data["age"])
        )

    def update(self, employee):
        key = f"employee:{employee.id}"
    
        if not self.redis.exists(key):
            return False
    
        self.redis.hmset(
            key,
            {
                "id": employee.id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "age": employee.age
            }
        )
    
        return True   

    def delete(self, employee_id):
        key = f"employee:{employee_id}"

        return self.redis.delete(key) > 0