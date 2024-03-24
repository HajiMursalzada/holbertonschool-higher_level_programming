#!/usr/bin/python3
""" Lists all states from 
python3the database hbtn_0e_0_usa """

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
    cursor.execute("select * from states order by id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()