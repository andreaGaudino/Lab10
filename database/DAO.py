from database.DB_connect import DBConnect
from model.confini import Confini
from model.stati import Stati


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllBeforYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM contiguity c WHERE c.year <= %s  and c.conttype = 1"
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Confini(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM country c ORDER by c.StateNme"
        cursor.execute(query, ())

        for row in cursor:
            result.append(Stati(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountriesYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary = True)
        query = """SELECT distinct (c2.StateAbb), c2.CCode , c2.StateNme 
                FROM countries.contiguity c, countries.country c2 
                where c.state1no = c2.CCode and c.year <= %s
                order by c2.StateNme """
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Stati(**row))
        cursor.close()
        conn.close()
        return result