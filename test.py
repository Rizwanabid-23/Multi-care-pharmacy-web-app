import imp
import pyodbc
import psycopg2
import pandas as pd


def database():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT PIN FROM Employee", conn)
    conn.commit()
    print(data.iloc[0,0])

def d1():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT PIN FROM Employee", conn)
    conn.commit()
    data_array = data[['ID']].to_numpy()
    name_array=data[['Name']].to_numpy()
    print(data_array,name_array)


def emp_pin():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT PIN FROM Employee", conn)
   # data=data.iloc[0,0]
    conn.commit()
    pin_array=data[['PIN']].to_numpy()
    
    print(pin_array)

emp_pin()
