from conexion import db

db.empleados.insert_many([
    {"nombre": "Jose Effio", "cargo": "Administrador", "salario": 2200},
    {"nombre": "Roldan Arancibia", "cargo": "Vendedor", "salario": 1500},
    {"nombre": "Cayan Roldan", "cargo": "Cajero", "salario": 1400},
    {"nombre": "Luis Perez", "cargo": "Almacén", "salario": 1300},
    {"nombre": "Ana Torres", "cargo": "Vendedora", "salario": 1500},
    {"nombre": "Maria Soto", "cargo": "Marketing", "salario": 1800},
    {"nombre": "Juan Diaz", "cargo": "Soporte", "salario": 1600},
    {"nombre": "Lucia Ramos", "cargo": "Vendedora", "salario": 1500},
    {"nombre": "Carlos Vega", "cargo": "Cajero", "salario": 1400},
    {"nombre": "Paola Mendez", "cargo": "Ventas", "salario": 1550}
])

db.productos.insert_many([
    {"nombre": "Atarashii Gakko - Vinyl", "genero": "J-Pop", "precio": 150},
    {"nombre": "Laufey - Bewitched", "genero": "Jazz Pop", "precio": 170},
    {"nombre": "Corazon Serrano - Grandes Exitos", "genero": "Cumbia", "precio": 120},
    {"nombre": "Blackpink - Born Pink", "genero": "K-Pop", "precio": 180},
    {"nombre": "BTS - Proof", "genero": "K-Pop", "precio": 190},
    {"nombre": "Miles Davis - Kind of Blue", "genero": "Jazz", "precio": 200},
    {"nombre": "Taylor Swift - 1989", "genero": "Pop", "precio": 160},
    {"nombre": "Bad Bunny - Un Verano Sin Ti", "genero": "Pop Latino", "precio": 155},
    {"nombre": "Daft Punk - Random Access Memories", "genero": "Electronic", "precio": 175},
    {"nombre": "Adele - 30", "genero": "Pop", "precio": 165}
])

db.clientes.insert_many([
    {"nombre": "Jose Effio", "correo": "jose@mail.com", "edad": 30},
    {"nombre": "Roldan Arancibia", "correo": "roldan@mail.com", "edad": 28},
    {"nombre": "Cayan Roldan", "correo": "cayan@mail.com", "edad": 25},
    {"nombre": "Ana Torres", "correo": "ana@mail.com", "edad": 27},
    {"nombre": "Luis Perez", "correo": "luis@mail.com", "edad": 35},
    {"nombre": "Maria Soto", "correo": "maria@mail.com", "edad": 29},
    {"nombre": "Juan Diaz", "correo": "juan@mail.com", "edad": 33},
    {"nombre": "Lucia Ramos", "correo": "lucia@mail.com", "edad": 24},
    {"nombre": "Carlos Vega", "correo": "carlos@mail.com", "edad": 31},
    {"nombre": "Paola Mendez", "correo": "paola@mail.com", "edad": 26}
])

db.ventas.insert_many([
    {"cliente": "Jose Effio", "producto": "Laufey - Bewitched", "total": 170},
    {"cliente": "Roldan Arancibia", "producto": "Atarashii Gakko - Vinyl", "total": 150},
    {"cliente": "Cayan Roldan", "producto": "Blackpink - Born Pink", "total": 180},
    {"cliente": "Ana Torres", "producto": "Corazon Serrano - Grandes Exitos", "total": 120},
    {"cliente": "Luis Perez", "producto": "Miles Davis - Kind of Blue", "total": 200},
    {"cliente": "Maria Soto", "producto": "Taylor Swift - 1989", "total": 160},
    {"cliente": "Juan Diaz", "producto": "Daft Punk - RAM", "total": 175},
    {"cliente": "Lucia Ramos", "producto": "Adele - 30", "total": 165},
    {"cliente": "Carlos Vega", "producto": "BTS - Proof", "total": 190},
    {"cliente": "Paola Mendez", "producto": "Bad Bunny - UVST", "total": 155}
])
