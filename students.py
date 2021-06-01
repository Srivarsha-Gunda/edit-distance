


import sqlite3

db=sqlite3.connect("test.db")
db.execute("drop table if exists results")
try:

   db.execute("create table resultss(name,Class,section,telugu,hindi,english,maths,science,social)")
except:
  print("already ")

db=sqlite3.connect("test.db")
#table created

name="ashu"
Class ="2"
section="a"
telugu="90"
hindi="92"
english="95"
maths="88"
science="89"
social="90"

cmd="insert into resultss(name,Class,section,telugu,hindi,english,maths,science,social)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,Class,section,telugu,hindi,english,maths,science,social)
db.execute(cmd)
db.commit()

name="riya"
Class ="2"
section="a"
telugu="99"
hindi="96"
english="97"
maths="88"
science="89"
social="90"

cmd="insert into resultss(name,Class,section,telugu,hindi,english,maths,science,social)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,Class,section,telugu,hindi,english,maths,science,social)
db.execute(cmd)
db.commit()

name="riyansh"
Class ="2"
section="a"
telugu="92"
hindi="96"
english="97"
maths="88"
science="89"
social="90"

cmd="insert into resultss(name,Class,section,telugu,hindi,english,maths,science,social)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,Class,section,telugu,hindi,english,maths,science,social)
db.execute(cmd)
db.commit()

name="riyanshi"
Class ="2"
section="a"
telugu="82"
hindi="96"
english="97"
maths="98"
science="89"
social="90"



cmd="insert into resultss(name,Class,section,telugu,hindi,english,maths,science,social)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,Class,section,telugu,hindi,english,maths,science,social)
db.execute(cmd)
db.commit()

db=sqlite3.connect("test.db")
rs=db.execute("SELECT * from resultss")
for row in rs:
  print(row)
#output
#('ashu', '2', 'a', '90', '92', '95', '88', '89', '90')
#('riya', '2', 'a', '99', '96', '97', '88', '89', '90')
#('riyansh', '2', 'a', '92', '96', '97', '88', '89', '90')
#('riyanshi', '2', 'a', '82', '96', '97', '98', '89', '90')



mycursor = db.cursor()

sql = "DELETE FROM resultss WHERE name = 'riya'"

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "record(s) deleted")
# row deleted

db=sqlite3.connect("test.db")
rs=db.execute("SELECT * from resultss")
for row in rs:
  print(row)
#output
#('ashu', '2', 'a', '90', '92', '95', '88', '89', '90')
#('riyansh', '2', 'a', '92', '96', '97', '88', '89', '90')
#('riyanshi', '2', 'a', '82', '96', '97', '98', '89', '90')



mycursor = db.cursor()

sql = "UPDATE resultss SET english='99' WHERE name='riyansh'";

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "updated")
#updated

db=sqlite3.connect("test.db")
rs=db.execute("SELECT * from resultss")
for row in rs:
  print(row)

mycursor = db.cursor()

sql = "UPDATE resultss SET name='reeyansh' WHERE name='riyansh'";

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "updated")
