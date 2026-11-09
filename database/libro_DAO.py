from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_libri(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = "SELECT * FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libro = Libro(*row)
                result.append(libro)
            cursor.close()
            cnx.close()
            return result

    def read_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = "SELECT genere FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                if row[0] not in result:
                    result.append(row[0])
            cursor.close()
            cnx.close()
            return result
