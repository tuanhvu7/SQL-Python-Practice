import Person
import mysql.connector as mc


# connect to database using 4 given params
# throws exception if can't connect

# usr = root
# password = password
# host = localhost
# db = myFirstDB    <--- Schema name

def getConnection(usr, pswd, hst, db):
    try:
        cnx = mc.connect(user=usr, password = pswd, host = hst, database = db)
        print("Success")
        return cnx
    except mc.Error as e:
        print(e.msg)
        if cnx is not None:
            cnx.close()
        return None

# p is object inserting to database
#conn is connection to SQL
def addPerson(p, conn):
    try:
        add = """INSERT INTO Persons(      
            first_name,
            last_name)
            
            VALUES(%s, %s);
            """
        cursor = conn.cursor()
        cursor.execute(add,(p.getFirstName(), p.getLastName(),))
        conn.commit()
    except mc.Error as e:
        print(e.msg)
    finally:
        cursor.close()

# p is object delete from database
#conn is connection to SQL
def delPerson(p, conn):
    try:
        stmt = "Delete from Persons WHERE first_name=%s"
        
        cs = conn.cursor(prepared=True)
        #cs.execute(stmt, (p.first_name, p.last_name,))
        cs.execute(stmt, (p.first_name,))

        conn.commit()
    except mc.Error as e:
        print(e.msg)
    finally:
        cs.close()
                       

person1 = Person.Person("Chiu", "Kok")
con = getConnection("root", "password", "localhost", "myFirstDB")
#delPerson(person1, con)
addPerson(person1, con)    
                       
        
