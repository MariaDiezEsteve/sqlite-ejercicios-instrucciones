import sqlite3 as sql

def readInstructionOne():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM PRODUCTOS WHERE PRECIO > 500 union SELECT* from PRODUCTOS_NUEVOS WHERE SECCIÓN='ALTA COSTURA'"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas
    
def readInstructionTwo():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM PRODUCTOS UNION ALL SELECT * FROM PRODUCTOS_NUEVOS"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas

#Instrucción incluyendo el nombre directamente de la población
def readInstructionThree():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT CLIENTES.CÓDIGO_CLIENTE, EMPRESA, FORMA_DE_PAGO FROM CLIENTES INNER JOIN PEDIDOS ON CLIENTES.CÓDIGO_CLIENTE=PEDIDOS.CÓDIGO_CLIENTE WHERE POBLACIÓN = 'MADRID'"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas
    
def readInstructionThree(city):
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT CLIENTES.CÓDIGO_CLIENTE, EMPRESA, FORMA_DE_PAGO FROM CLIENTES INNER JOIN PEDIDOS ON CLIENTES.CÓDIGO_CLIENTE=PEDIDOS.CÓDIGO_CLIENTE WHERE POBLACIÓN LIKE'{city}'"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas

def readInstructionFour():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT * FROM CLIENTES INNER JOIN PEDIDOS ON CLIENTES.CÓDIGO_CLIENTE=PEDIDOS.CÓDIGO_CLIENTE WHERE POBLACIÓN='MADRID'"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas

def readInstructionFive():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"DELETE FROM CLIENTES where CÓDIGO_CLIENTE='CT100'"
    cu.execute(instruccion)
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas

def readInstructionSix():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT SUM(precio) AS suma_precio FROM productos"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas


def readInstructionSeven():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT AVG(precio) AS promedio_precios FROM productos"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas    

def readInstructionEigth():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT COUNT(*) AS cantidad_registros FROM productos"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas    

def readInstructionNine():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT MIN(precio) AS valor_minimo FROM productos"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas 

def readInstructionTen():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f"SELECT MAX(precio) AS valor_minimo FROM productos"
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas    

def readInstructionEleven():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f""" SELECT C.EMPRESA, C.POBLACIÓN
        FROM CLIENTES C
        WHERE C."RESPONSABLE" IN (
            SELECT "RESPONSABLE"
            FROM CLIENTES
            WHERE "RESPONSABLE" = 'EGGS POTATO'
        )"""
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas    

def readInstructionTwelve():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f""" SELECT P.SECCIÓN, COUNT(*) AS TOTAL
        FROM PRODUCTOS_NUEVOS P
        WHERE P.PAÍSDEORIGEN = (
            SELECT PAÍSDEORIGEN
            FROM PRODUCTOS_NUEVOS
            WHERE NOMBREARTÍCULO = 'SERRUCHO'
        )
        GROUP BY P.SECCIÓN"""
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas    

def readInstructionThirteen():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f""" SELECT P.SECCIÓN, COUNT(*) AS TOTAL
        FROM PRODUCTOS_NUEVOS P
        WHERE P.PAÍSDEORIGEN = (
            SELECT PAÍSDEORIGEN
            FROM PRODUCTOS_NUEVOS
            WHERE NOMBREARTÍCULO = 'SERRUCHO'
        )
        GROUP BY P.SECCIÓN"""
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas  
    
def readInstructionFourteen():
    conn = sql.connect("data.sqlite")
    cu = conn.cursor()
    instruccion = f""" SELECT P.SECCIÓN, COUNT(*) AS TOTAL
        FROM PRODUCTOS_NUEVOS P
        WHERE P.SECCIÓN IN (
            SELECT SECCIÓN
            FROM PRODUCTOS_NUEVOS
            GROUP BY SECCIÓN
            HAVING COUNT(*) > 5
        )
        GROUP BY P.SECCIÓN"""
    cu.execute(instruccion)
    datosField = cu.fetchall()
    for fila in datosField:
        print(fila) 
    conn.commit()
    conn.close()
    #Devuelve una lista con Tuplas  



if __name__ == "__main__":
    # readInstructionOne()
    # readInstructionTwo()
    # readInstructionThree()
    # readInstructionThree("madrid")
    # readInstructionFour()
    # readInstructionFive()
    # readInstructionSix()
    # readInstructionSeven()
    # readInstructionEigth()
    # readInstructionNine()
    # readInstructionTen()
    # readInstructionEleven()
    # readInstructionThirteen()
    readInstructionFourteen()