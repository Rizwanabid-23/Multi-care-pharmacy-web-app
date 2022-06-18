from cmath import pi
import imp
import pyodbc
import psycopg2
import pandas as pd


def editemployee():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT ID,FirstName,LastName,Username,PIN,CNIC,Address,Phone,Email FROM Employee", conn)
    conn.commit()
    data_array = data[['ID']].to_numpy()
    first_name_array=data[['FirstName']].to_numpy()
    last_name_array=data[['LastName']].to_numpy()
    uname_array=data[['Username']].to_numpy()
    pin_array=data[['PIN']].to_numpy()
    cnic_array=data[['CNIC']].to_numpy()
    address_array=data[['Address']].to_numpy()
    phone_array=data[['Phone']].to_numpy()
    email_array=data[['Email']].to_numpy()
    return data_array,first_name_array,last_name_array,uname_array,pin_array,cnic_array,address_array,phone_array,email_array

def admin_id():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT Username FROM Admin", conn)
    conn.commit()
    return data.iloc[0,0]

def admin_pin():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT PIN FROM Admin", conn)
    conn.commit()
    return data.iloc[0,0]


def emp_id():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT Username FROM Employee", conn)
    conn.commit()
    uname_array=data[['Username']].to_numpy()
    return uname_array

def emp_pin():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT PIN FROM Employee", conn)
    conn.commit()
    pin_array=data[['PIN']].to_numpy()
    return pin_array

def check_emp(id,pin):
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=RIZWAN-LAPTOP;'
                      'Database=MultiCarePharmacy;'
                      'Trusted_Connection=yes;')

    data = pd.read_sql("SELECT Username,ID FROM Employee where Username='"+id+"' and PIN='"+pin+"' ", conn)
    uname_array=data[['Username']].to_numpy()
    id_array=data[['ID']].to_numpy()
    conn.commit()
    return uname_array,id_array

