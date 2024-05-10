import sqlite3

try:
  coneccion = sqlite3.connect("db.sqlite3")
  cursor = coneccion
  cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY,nombre VARCHAR(50),categoria VARCHAR(30),descripcion VARCHAR(100),precio INTEGER)")
  cursor.close()
    
except Exception as ex:
  print(ex)
    
def dbagredatos(nom,cat,des,pre):  
  cursor = sqlite3.connect("db.sqlite3")   
  cursor.execute("INSERT INTO productos (nombre,categoria,descripcion,precio) VALUES (?,?,?,?)",(nom,cat,des,pre))
  res = cursor.execute("SELECT * FROM productos")
  for i in res:
    print(i)
  cursor.commit()
  cursor.close()

def dbeditdatos(id,nom,cat,des,pre):
  cursor = sqlite3.connect("db.sqlite3")
  cursor.execute("UPDATE productos SET nombre=? , categoria = ? , descripcion = ? , precio = ? WHERE id = ?", (nom,cat,des,pre,id))
  
  cursor.commit()
  cursor.close()


def Datos():
  conn = sqlite3.connect("db.sqlite3")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM productos")
  
  datos = cursor.fetchall()
  conn.commit()
  conn.close()
  
  return datos
def delete(idd):
  conn = sqlite3.connect("db.sqlite3")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM productos WHERE id = ?",(idd,)) 
  conn.commit() 
  cursor.close()
Datos()
  
    