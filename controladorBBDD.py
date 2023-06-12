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
    readInstructionFive()