import mysql_database_connection as db
def add_student():
    name = input("Enter a student name: ")
    roll_no = int(input("Enter student roll number: "))
    marks = int(input("Enter student marks: "))
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO info (id, name, marks) VALUES (%s, %s, %s)", (roll_no, name, marks))
    conn.commit()
    conn.close()
    print("Student added successfully")
def view_student():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM info")
    rows = cursor.fetchall()
    conn.close()
    for i in rows:
        print(i)
def update_student():
    sid = int(input("Enter student roll number: "))
    marks = int(input("Enter marks to update: "))
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE info SET marks = %s WHERE id = %s", (marks, sid))
    conn.commit()
    conn.close()
    print("Student updated successfully")
def delete_student():
    sid = int(input("Enter student roll number: "))
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM info WHERE id = %s", (sid,))
    conn.commit()
    conn.close()
    print("Student deleted successfully")

while True:
    print("-"*15 + "MAIN MENU" + "-"*15)
    print("1. Add Student\n2. View Student\n3. Update Student\n4. Delete Student\n5.Exit")
    choice = int(input("Enter the choice from the above menu: "))
    match choice:
        case 1:
            add_student()
        case 2:
            view_student()
        case 3:
            update_student()
        case 4:
            delete_student()
        case 5:
            print("_"*15 + "THANK YOU" + "_"*15)
            break
        case _:
            print("Please choose a valid choice")





