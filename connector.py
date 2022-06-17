import mysql.connector
import pandas as pd

class Connector:
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address
        self.con = mysql.connector.connect(host = self.address,
                                           user = self.username,
                                           password = self.password)
        self.cur = self.con.cursor()

    


