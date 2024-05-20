from fastapi import FastAPI
import mysql.connector
import schemas
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




host_name = "database-parcial.c6fxrh1itneq.us-east-1.rds.amazonaws.com"
port_number = "3306"
user_name = "admin"
password_db = "parcial777"
database_name = "api_publicaciones"

# Get all employees
@app.get("/publicaciones")
def get_publicaciones():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM publicaciones")
    result = cursor.fetchall()
    mydb.close()
    return {"publicaciones": result}

# Get an employee by ID
@app.get("/publicaciones/{id}")
def get_publicacion(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM publicaciones WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"publicacion": result}

# Add a new employee
@app.post("/publicaciones")
def add_publicacion(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    texto = item.texto
    id_usu = item.id_usuario
    titulo= item.titulo
    canti_likes= item.canti_likes
    cursor = mydb.cursor()
    sql = "INSERT INTO publicaciones (texto, titulo, canti_likes, id_usuario) VALUES (%s, %s, %s, %s)"
    val = (texto, titulo, canti_likes, id_usu)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Publicacion agregada correctamente"}

# Modify an employee
@app.put("/publicaciones/{id}")
def update_publicacion(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    texto = item.texto
    id_usu = item.id_usuario
    titulo = item.titulo
    canti_likes = item.canti_likes
    cursor = mydb.cursor()
    sql = "UPDATE publicaciones set texto=%s, titulo=%s, canti_likes=%s,id_usuario=%s where id=%s"
    val = (texto, titulo, canti_likes, id_usu, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Publicacion modificada correctamente"}



# Delete an employee by ID
@app.delete("/publicaciones/{id}")
def delete_publicacion(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM publicaciones WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"miausaje!": "Publicacion borrada correctamente"}

