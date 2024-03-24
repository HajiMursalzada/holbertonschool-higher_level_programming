#!/usr/bin/python3
""" Lists all cities of that state using the database hbtn_0e_4_usa """

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
    cursor.execute("select cities.name\
                   from cities left join states on cities.state_id\
                   =states.id where states.name = '{:s}'\
                   order by cities.id".format(sys.argv[4]))

    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        print(row[0], end=", " if i < len(rows) - 1 else "")

    print()
    cursor.close()
    connection.close()