import sqlite3


# backend



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




