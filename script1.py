import sqlite3

def create_table():
   conn=sqlite3.connect("lite.db")
   cur=conn.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
   cur.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5) ")
   conn.commit()
   conn.close()

def insert(item, quantity, price):
   conn=sqlite3.connect("lite.db")
   cur=conn.cursor()
   cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
   conn.commit()
   conn.close()


def view():
   conn=sqlite3.connect("lite.db")
   cur=conn.cursor()
   cur.execute("SELECT * FROM store")
   rows=cur.fetchall()
   conn.close()
   return rows

def delete(item):
   conn=sqlite3.connect("lite.db")
   cur=conn.cursor()
   cur.execute("DELETE from store WHERE item=?",(item,))
   rows=cur.fetchall()
   conn.commit()
   conn.close()

def update(quantity, price, item):
   conn=sqlite3.connect("lite.db")
   cur=conn.cursor()
   cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price,item))
   conn.commit()
   conn.close()

# update(11,6,"water glass")
# insert("coffee glass",10,5)
# delete("Wine Glass")
# print(view())
   
