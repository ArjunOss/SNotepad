import cx_Oracle
import traceback

conn = None

try:
    conn = cx_Oracle.connect("mojo/mojo@127.0.0.1/xe")
    print("connection successful")

except cx_Oracle.DatabaseError:
    print("connection failed")

finally:
    if conn is not None:
        conn.close()
        print("disconnect")