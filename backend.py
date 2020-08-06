import sqlite3


# backend
'''def studentData():
    con = sqlite3.connect("studentrecord.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS studentmanagement(id INTEGER PRIMARY KEY,StdID text, Name text, Branch text, Gender text , DoB text, Mobile text,Email text)")
    con.commit()
    con.close()'''


def addStdRec(StdID, Name, Branch, Gender, DoB, Mobile,Email):
    con = sqlite3.connect("studentrecord.db")
    cur = con.cursor()
    cur.execute("INSERT INTO studentmanagement VALUES (NULL,?,?,?,?,?,?,?) ",(StdID, Name, Branch, Gender, DoB, Mobile,Email))
    con.commit()
    con.close()


def deleteRec(id):
    con = sqlite3.connect("studentrecord.db")
    cur = con.cursor()
    cur.execute("DELETE FROM studentmanagement WHERE id=?", (id,))
    con.commit()
    con.close()


'''def dataUpdate(id, StdID="", Name="", Branch="", Gender="", DoB="", Mobile="", Email=""):
    con = sqlite3.connect("studentrecord.db")
    cur = con.cursor()
    cur.execute("UPDATE studentmanagement SET StdID=?,Name=?,Branch=?,Gender=?,Address=?Mobile=?,WHERE id=?",
                (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()'''



