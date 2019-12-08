import pyodbc
class Database:
    def __init__(self):
         self.conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=HIEP\SQLEXPRESS;DATABASE=desktopapp;UID=sa;PWD=123')
         self.cur = self.conn.cursor()
         self.cur.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='student_info' AND type='U') CREATE TABLE student_info(sid int primary key,name nvarchar(50),sclass text,phone char(10),address text)")
         self.conn.commit()
    def fetch(self):
         self.cur.execute("SELECT * FROM student_info")
         rows = self.cur.fetchall()
         return rows

    def insert(self,sid,name,sclass,phone,address):
        self.cur.execute("INSERT INTO student_info VALUES (?,?,?,?,?)",(sid,name,sclass,phone,address))
        self.conn.commit()
    def remove(self,sid):
        self.cur.execute("DELETE FROM student_info WHERE sid=?",(sid))
        self.conn.commit()
    def update(self,sid,name,sclass,phone,address):
        self.cur.execute("UPDATE student_info SET name=?,sclass=?,phone=?,address=? WHERE sid =?",(name,sclass,phone,address,sid))
        self.conn.commit()
    def __del__(self):
        self.conn.close()

        
