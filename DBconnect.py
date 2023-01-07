import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="fish",
    password="fhj1371201288",
    database="Justris"
)

mycursor = db.cursor()
# mycursor.execute("show databases")

# CREATE table
'''
mycursor.execute("CREATE TABLE Person\
                (name    VARCHAR(50),\
                age      smallint UNSIGNED,\
                personID int PRIMARY KEY AUTO_INCREMENT,\
                created  datetime,\
                gender   ENUM('M','F','O'))")
'''
# INSERT
mycursor.execute("INSERT INTO Person (name, created, age) VALUES (%s,%s,%s)",("Jus",datetime.now(), 19))
#db.commit()

# DESCRIBE
'''
mycursor.execute("DESCRIBE Person")
for x in mycursor:
    print(x)

print(mycursor.fetchone())
'''
#Selevt
mycursor.execute("SELECT * from Person,\
                WHERE gender = 'M',\
                ORDER BY id DESC,\
                ")
for x in mycursor:
    print(x)

#alter
mycursor.execute("ALTER TABLE Person ADD COLUMN food VARCHAR(50) NOT NULL")
# add drop change
