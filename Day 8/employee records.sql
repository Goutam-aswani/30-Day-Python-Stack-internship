create DATABASE Emp1;
use Emp1;
create TABLE emp1(
    emp_id INT PRIMARY key,
    emp_name varchar(50),
    salary int,
    department varchar(20)
);

INSERT INTO emp1 (emp_id, emp_name, salary, department) VALUES
(101, 'Goutam Aswani', 60000, 'IT'),
(102, 'Divya Patel', 58000, 'HR'),
(103, 'Krish Sharma', 62000, 'Finance'),
(104, 'Riya Mehta', 55000, 'Marketing'),
(105, 'Amit Verma', 61000, 'IT');

UPDATE emp1
set salary = salary *1.10
WHERE department = "IT"

SELECT * FROM emp1 where (salary >50000 AND salary < 60000);

SELECT * FROM emp1 where (emp_id % 2 = 0);

SELECT * from emp1 ORDER BY emp_name DESC LIMIT 3;

SELECT * FROM emp1 WHERE department = "IT";

SELECT * FROM emp1 ORDER BY salary DESC ;

SELECT * FROM emp1 where emp_name LIKE "K%";

SELECT department, count(*) as empp_numbers
FROM emp1
GROUP BY department
having count(*) <2;

SELECT department, AVG(salary) as avg_salary
from emp1
GROUP BY department;

SELECT * FROM emp1;
