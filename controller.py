#Tutorial: https://www.youtube.com/watch?v=uB0928SOTEQ

import sqlite3 as sql

#Crear una función para crear la BBDD
def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

#Crear una tabla para incluir en la BBDD
def createTable():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    cu.execute(
         """ CREATE TABLE streamers(
             name text ,
             followers integer,
             subs integer
             )"""        
     )
    conn.commit()
    conn.close()

#Insertar una fila
def insertRow(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cu.execute(instruccion)
    conn.commit()
    conn.close()

#Leer una columna
def readColumn():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cu.execute(instruccion)
    datos = cu.fetchall()
    conn.commit()
    conn.close()
    print(datos) #Devuelve una lista con Tuplas

#Insertar varias filas en un mismo código
def interRows(streamerList):
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?,?,?)"
    cu.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()
    
#Ordenación de los datos de menor a mayor del campo "subs"
#Para hacerlo de mayor a menos tendremos que poner DESC despues de {field}
def readOrdered(field):
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field}"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    conn.commit()
    conn.close()
    print(datosField) #Devuelve una lista con Tuplas

#Buscar en la BBDD con "="
def searchEqual():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name='Ibai'"
    cu.execute(instruccion)
    datosNameEqual = cu.fetchall()
    conn.commit()
    conn.close()
    print(datosNameEqual) #Devuelve una lista con Tuplas
    
#Buscar en la BBDD con "like" para omitir mayúsculas y minúsculas
def searchLike():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name like 'elxocas'"
    cu.execute(instruccion)
    datosNameLike = cu.fetchall()
    conn.commit()
    conn.close()
    print(datosNameLike) #Devuelve una lista con Tuplas

#Buscar en la BBDD que empiece por "x":
def searchSimilar():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name like 'Cristi%'"
    cu.execute(instruccion)
    datosNameSimilar = cu.fetchall()
    conn.commit()
    conn.close()
    print(datosNameSimilar) #Devuelve una lista con Tuplas

#Buscar en la BBDD los subs mayores de cierto valor:
def searchPromedio():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE subs > 6000"
    cu.execute(instruccion)
    datosNumber = cu.fetchall()
    conn.commit()
    conn.close()
    print(datosNumber) #Devuelve una lista con Tuplas

#Actualizar campos de una fila ya existente
def updateFields():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"UPDATE streamers SET followers= 1200000 WHERE name like 'ibai'"
    cu.execute(instruccion)
    conn.commit()
    conn.close()
    
#Borrar Datos de la BBDD
def deleteRows():
    conn = sql.connect("streamers.db")
    cu = conn.cursor()
    instruccion = f"DELETE FROM streamers WHERE name='Auroplay'"
    cu.execute(instruccion)
    conn.commit()
    conn.close()


#El siguiente IF es solo para la ejecución del archivo controller, en el caso de importar el archivo controller a otro archivo entonces las líneas 5 y 6 no se ejecutarán:

if __name__ == "__main__":
   # createDB() #Se creará un fichero: "streamers.db"
   # createTable()
   # insertRow("Ibai", 12000, 1000)
   # insertRow("Rubius", 130000, 400000)
   #readColumn()
   streamers = [
       ("Elxocas", 20000, 900),
       ("Cristinini", 15000, 500),
       ("Auronplay", 30000, 600)
   ]
   # interRows(streamers)
   # readOrdered("subs")
   # searchEqual()
   # searchLike()
   # searchSimilar()
   # searchPromedio()
   # updateFields()
   deleteRows()