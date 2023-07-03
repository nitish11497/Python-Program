import pymssql

try:
    conn = pymssql.connect(server="host_or_ip", user="your_username", password="your_password", database="your_db")
    cursor = conn.cursor()
    cursor.execute ("select query")
    row = cursor.fetchone()
    print(f"\n\n server virsion :\n\n{row[0]}")
    cursor.close()
    conn.close()
except Exception:
    print("\nERROR: Unable to connect to the server.")
    exit(-1)
# ------------------------------------------------------------------
import pypyodbc
import pandas as pd

cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=server_name;"
                        "Database=db_name;"
                        "uid=User;pwd=password")
df = pd.read_sql_query('select * from table', cnxn)
# --------------------------------------------------------------------
import pandas as pd
import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server};Server=serverName;UID=UserName;PWD=Password;Database=My_DW;")
df = pd.read_sql_query('select TOP 10 * from dbo.Table WHERE Patient_Key > 1000', cnxn)
df.head()


