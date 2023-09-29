import mysql.connector
# from studentManagemet import upload
import tkinter.messagebox as msg
import base64
from PIL import Image
import io

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123Sushant3385",
    database="pdf",
)

cur = mydb.cursor(buffered=True)
def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binary = file.read()
        binpdf = base64.b64encode(binary)
    return binpdf

def convertbinarytopdf(binarydata,output):
    dec_bin = base64.b64decode(binarydata)
    with open(output, 'wb') as file:
        file.write(dec_bin)


# create a database
# cur.execute("CREATE DATABASE pdf")

# create a table
# cur.execute("CREATE TABLE pdf(Id INT AUTO_INCREMENT PRIMARY KEY,USN varchar(20),First MEDIUMBLOB,Second MEDIUMBLOB,Third MEDIUMBLOB,Fourth MEDIUMBLOB,Fifth MEDIUMBLOB,Sixth MEDIUMBLOB,Seventh MEDIUMBLOB,Eighth MEDIUMBLOB)")

def insert(filename, sem, usn):
    if sem == "First":
        insert = """ INSERT into pdf (USN,First) value (%s,%s)"""
    elif sem == "Second":
        insert = """ INSERT into pdf (USN,Second) value (%s,%s)"""
    elif sem == "Third":
        insert = """ INSERT into pdf (USN,Third) value (%s,%s)"""
    elif sem == "Fourth":
        insert = """ INSERT into pdf (USN,Fourth) value (%s,%s)"""
    elif sem == "Fifth":
        insert = """ INSERT into pdf (USN,Fifth) value (%s,%s)"""
    elif sem == "Sixth":
        insert = """ INSERT into pdf (USN,Sixth) value (%s,%s)"""
    elif sem == "Seventh":
        insert = """ INSERT into pdf (USN,Seventh) value (%s,%s)"""
    elif sem == "Eighth":
        insert = """ INSERT into pdf (USN,Eighth) value (%s,%s)"""
    else:
        msg.showinfo("Message", "No Data available")

    convert = convertToBinary(filename)
    value = (usn, convert)
    cur.execute(insert, value)
    mydb.commit()

def update(filename, sem, usn):
    if sem == "First":
        update = """UPDATE `pdf`.`pdf` SET First = %s WHERE USN = %s"""
    elif sem == "Second":
        update = """UPDATE `pdf`.`pdf` SET Second = %s WHERE USN = %s"""
    elif sem == "Third":
        update = """UPDATE `pdf`.`pdf` SET Third = %s WHERE USN = %s"""
    elif sem == "Fourth":
        update = """UPDATE `pdf`.`pdf` SET Fourth = %s WHERE USN = %s"""
    elif sem == "Fifth":
        update = """UPDATE `pdf`.`pdf` SET Fifth = %s WHERE USN = %s"""
    elif sem == "Sixth":
        update = """UPDATE `pdf`.`pdf` SET Sixth = %s WHERE USN = %s"""
    elif sem == "Seventh":
        update = """UPDATE `pdf`.`pdf` SET Seventh = %s WHERE USN = %s"""
    elif sem == "Eighth":
        update = """UPDATE `pdf`.`pdf` SET Eighth = %s WHERE USN = %s"""
    else:
        msg.showinfo("Message", "No Data available")
    convert = convertToBinary(filename)
    value = (convert, usn)
    cur.execute(update, value)
    mydb.commit()


def get(usn):
    up = ("SELECT * FROM pdf WHERE USN=(%s)")
    val = (usn,)
    cur.execute(up, val)
    result = cur.fetchone()
    return result
