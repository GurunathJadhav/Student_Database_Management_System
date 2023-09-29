import mysql.connector
import tkinter.messagebox as msg
import base64
from PIL import Image
import io

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "guru8296jadhav@",
    database = "student_information",
)
cur = mydb.cursor(buffered=True)

def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binary = file.read()
        binpdf = base64.b64encode(binary)
        # print(binpdf)
    return binpdf

def convertbinarytopdf(binarydata,output):
    dec_bin = base64.b64decode(binarydata)
    with open(output, 'wb') as file:
        file.write(dec_bin)
        
def get(usn):
    up = ("SELECT * FROM pdfimg WHERE USN=(%s)")
    val = (usn,)
    cur.execute(up, val)
    result = cur.fetchone()
    return result

def insertimg(filename, usn):
    insert = """ INSERT into student_information.pdfimg (USN,Photo) value (%s,%s)"""
    convert = convertToBinary(filename)
    value = (usn, convert)
    cur.execute(insert, value)
    mydb.commit()

def updateimg(filename, usn):
    update = """UPDATE `student_information`.`pdfimg` SET Photo = %s WHERE USN = %s"""
    convert = convertToBinary(filename)
    value = (convert, usn)
    cur.execute(update, value)
    mydb.commit()
    # print(result)
# get("2MM20EC002")