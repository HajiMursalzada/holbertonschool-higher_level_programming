#!/usr/bin/python3
""" Displays all values in the states 
table of the database hbtn_0e_0_usa
whose name matches that supplied as argument """

if __name__ == "__main__":
    import sys
    import MySQLdb
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    search = sys.argv[4]
    user_input = search.split(' ')
    if len(user_input) > 1:
        search = user_input[0]

    cursor = connection.cursor()
    cursor.execute("select * from states\
                   where name='{:s}' order by states.id".format(search))

    rows = cursor.fetchall()

    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cursor.close()
    connection.close()
