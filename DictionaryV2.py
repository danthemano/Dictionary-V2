import mysql.connector

#establish a connection, credentials of the DB will be in the parentheses
con = mysql.connector.connect(
user = "ardit700_student", #username of the DB
password = "ardit700_student",
host = "108.167.140.122", #this is the ip of the server that has the DB
database = "ardit700_pm1database"
)

#cursor object used to navigate through the DB
cursor = con.cursor()

word = input("Enter a word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE expression = '%s'" % word)

#returns a list with all of the results from the query above, each element of the list
#is a list of 2 elements, an expression and a definition
results = cursor.fetchall()

#checks if the list is not empty, and if it isn't, then print each definition of that list
if results:
    for result in results:
        print(result[1]) #result[0] is the expression, result[1] is the definition
else:
    print("Word not found")
