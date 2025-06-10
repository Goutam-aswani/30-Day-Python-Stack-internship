import mysql.connector
import mysql

#Establish connection

try:
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "root",
        database = "EMP"
        )
    mycursor = conn.cursor()
except:
    print("connection error")

# Create Database

mycursor.execute("CREATE DATABASE EMP IF NOT exists")
conn.commit()
print("DATABASE CREATED")

# Create Table

mycursor.execute(
    """
    CREATE TABLE emp2(
    emp_id INT PRIMARY key,
    emp_name varchar(50),
    salary int,
    department varchar(20)
    )
    """
)
conn.commit()
print("Table is created")

# Insert data

mycursor.execute(
    """
    INSERT INTO emp2 (emp_id, emp_name, salary, department) VALUES
    (101, 'Goutam Aswani', 60000, 'IT'),
    (102, 'Divya Patel', 58000, 'HR'),
    (103, 'Krish Sharma', 62000, 'Finance'),
    (104, 'Riya Mehta', 55000, 'Marketing'),
    (105, 'Amit Verma', 61000, 'IT')
    """
)
conn.commit()
print("rows are added")

# Update rows

mycursor.execute(
    """
    UPDATE emp2
    set salary = salary *1.10
    WHERE department = "IT"
    """
)
conn.commit()
print("updated succesfully")

# Delete data

mycursor.execute("Delete from emp2 where salary>70000")
conn.commit()

print("Deleted succesfully")

# print table

mycursor.execute("SELECT * from emp2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x) 
