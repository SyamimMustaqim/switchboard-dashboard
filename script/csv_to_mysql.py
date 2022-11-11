import pandas as pd
import mysql.connector as msql

from sqlalchemy import create_engine
from mysql.connector import Error

filename = 'script/Data_Terminals.csv'
data = pd.read_csv(filename)
data.columns = ['switch_lable','terminal_1','terminal_2','terminal_3','terminal_4','terminal_5','unix_timestamp']

try:
    conn = msql.connect(host='localhost', user='root',
                        password='Pernec#123')
    if conn.is_connected():
        cursor = conn.cursor()

        # create sqlalchemy engine
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"  
                      .format(user="root", pw="Pernec#123", host='localhost', db="testDB"))

        # Insert whole DataFrame into MySQL
        data.to_sql('data_terminal', engine, if_exists = 'append', chunksize = 1000,index=False)

except Error as e:
    print("Error while connecting to MySQL", e)