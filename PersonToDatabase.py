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
# conn is connection to SQL
# returns true if could add person
def addPerson(p, conn):
    success = False
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
        success = True
        cursor.close()

    return success

# p is object delete from database
# conn is connection to SQL
def delPerson(p, conn):
    try:
        stmt = "Delete from Persons WHERE first_name = %s AND last_name = %s"

        # get cursor with enable prepared query
        cs = conn.cursor(prepared=True)
        cs.execute(stmt, (p.first_name, p.last_name,))
        #cs.execute(stmt, (p.first_name,))

        conn.commit()
    except mc.Error as e:
        print(e.msg)
    finally:
        cs.close()


# return person from database represented by given person ID
def selectByPersonID(pid, conn):
    # p is person to return
    # return none if person not found
    p = None

    try:
        #Create statement
        stmt = "SELECT * FROM Persons WHERE person_id = %s"
        # get cursor with enable prepared query
        cs = conn.cursor(prepared=True)
        cs.execute(stmt, (pid,))
        #Fetch result
        rs = cs.fetchone()
        
        if rs:
            p = Person.Person("", "")
            p.person_id = rs[0]
            p.first_name = rs[1].decode('utf-8')
            p.last_name = rs[2].decode('utf-8')
            print("Got person\n")
        else:
            print("Person not found \n")

    except mc.Error as e:
        print(e.msg)

    finally:
        cs.close()
    return p


# return list of persons
def selectAllPersons(conn):
    # persons is list to return
    # return none if person not found
    persons = []

    try:
        #Create statement
        stmt = "SELECT * FROM Persons"
        # get cursor with enable prepared query
        cs = conn.cursor(prepared=True)
        cs.execute(stmt)
        #Fetch all results: list matrix[row][column]
        rs = cs.fetchall()
        
        if rs:
            for row in rs:          
                p = Person.Person("", "")
                p.person_id = row[0]
                p.first_name = row[1]
                p.last_name = row[2]
                persons.append(p)
        else:
            print("No record found \n")

    except mc.Error as e:
        print(e.msg)

    finally:
        cs.close()
    return persons   
                       

########### Code to be executed

# person1 = Person.Person("Chiu", "Kok")
# person2 = Person.Person("Harem", "Lord")
# person3 = Person.Person("Goat", "Defiler")

#con = getConnection("root", "password", "localhost", "myFirstDB")
# #delPerson(person1, con)
# #addPerson(person2, con)
# #addPerson(person3, con)


# #personToFind = selectByPersonID("1", con)
# #personToFind.printInfo()

# personList = selectAllPersons(con)

# for p in personList:
#     p.printInfo()

    #print(first_name + " " + last_name + "\n")

    



