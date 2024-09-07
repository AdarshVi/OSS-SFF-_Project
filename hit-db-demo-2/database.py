import mysql.connector
import sys 


class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database= "hit-db-demo")

            self.mycurser = self.conn.cursor()
        except:
            print("Error connecting to database")
            sys.exit(0)
        else:
            print("Connecter to Database")
    


    def register(self, name, email, password):
        try:
            self.mycurser.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password))

            self.conn.commit()
        except:
            return -1
        else:
            return 1
        
    def search(self, email, password):

        self.mycurser.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}';
        """.format(email, password))

        data = self.mycurser.fetchall()
        return data

