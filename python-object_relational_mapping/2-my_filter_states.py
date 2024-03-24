#!/usr/bin/python3
""" bla bla bla bla"""

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

    cursor = connection.cursor()
    cursor.execute("select * from states\
                   where name='{:s}' order by states.id".format(sys.argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cursor.close()
    connection.close()
