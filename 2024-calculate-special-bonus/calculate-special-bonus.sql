select employee_id, 
IF(employee_id % 2 = 1 and name not like 'M%', salary, 0) as bonus 
from employees
order by employee_id;