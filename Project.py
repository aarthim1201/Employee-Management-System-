import pymysql.cursors
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='AARTHI1201',
    database='COMPANY'
)
cursor=conn.cursor()
def create_employee(name,department,salary):
    sql="INSERT INTO employee(name,department,salary) values(%s,%s,%s)"
    values=(name,department,salary)
    cursor.execute(sql,values)
    conn.commit()
    print("Employee Add SuccessFully !")
def read_employee():
    cursor.execute("SELECT * FROM employee")
    employee=cursor.fetchall()
    for emp in employee:
        print(emp)
def update_employee(emp_id,name,department,salary):
    sql="UPDATE employee SET name=%s,department=%s,salary=%s WHERE emp_id=%s"
    values=(name,department,salary,emp_id)
    cursor.execute(sql,values)
    conn.commit()
    print("Employee Details Updated SuccessFully !")

def delete_employee(emp_id):
    sql="DELETE FROM employee WHERE emp_id=%s"
    cursor.execute(sql,emp_id)
    conn.commit()
    print("Employee Deleted SuccessFully !")
while True:
    print("\nEmployees Application")
    print("1.Create Employee ID")
    print("2.All Employee's Details")
    print("3.Update Employee Details")
    print("4.Delete employee")
    print("5.EXIT")

    choice=int(input("Enter Choice : "))

    if choice==1:
        name=input("Enter Your Name : ")
        department=input("Enter Your Department : ")
        salary=int(input("Enter Your Salary : "))

        create_employee(name,department,salary)

    elif choice==2:
        read_employee()
elif choice==3:
        emp_id=int(input("Enter Employee ID To Update :"))
        name=input("Enter New Name :")
        department=input("Enter New Department : ")
        salary=int(input("Enter Your New Salary : "))

        update_employee()

    elif choice==4:
        emp_id=int(input("Enter Employee ID To Delete : "))

        delete_employee()

    elif choice==5:
        print("Existing...")

    else:
        print("Invalid Choice ! Try Again.")

cursor.close()
conn.close()