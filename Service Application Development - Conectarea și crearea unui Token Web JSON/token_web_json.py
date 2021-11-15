import sqlite3
import jwt
from datetime import datetime, timedelta

con = sqlite3.connect("data.db")
cursor = con.cursor()

cursor.execute(
	'''
		CREATE TABLE IF NOT EXISTS Client(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT,
			surname TEXT,
			account_number TEXT,
			password TEXT,
			token TEXT
			)
	'''
)

con.commit()

clients = cursor.execute('SELECT * FROM Client')

if len(clients.fetchall()) == 0:
	client = [
		("Arefte", "Andrei", "1998", "1998", "7212"),
		("Farcaciu", "Darius", "3212", "3212", "1234"),
		("Bulagea", "Alexandru", "2000", "2000", "4321"),
		("Marcu", "Ilie", "1956", "1956", "9876")
		]
	cursor.executemany('''INSERT INTO Client(
		name, surname, account_number, password, token)
	VALUES(?,?,?,?,?)''', client)
	con.commit()

class Bank():

	key = "unknown"
	second = 45

	def __init__(self, account_number="", client_code=""):
		if account_number and client_code:
			self.account_number = account_number
			self.client_code = client_code

	@classmethod
	def input_client(cls):
		cls.account_number = input("Enter account number: ")
		cls.client_code = input("Enter client code: ")
		return cls.account_number, cls.client_code

	def verify(self):
		data = cursor.execute(
			"SELECT * FROM Client WHERE account_number=? AND password=?",
			(self.account_number, self.client_code)
		)
		if len(data.fetchall()) == 0:
			raise TypeError("Wrong client")
		else:
			encoded = jwt.encode({"account_number": (self.account_number, self.client_code), "exp": datetime.utcnow() + timedelta(seconds=45)}, self.key, algorithm="HS256")
			self.insert_token(encoded)

	def insert_token(self, token):
		try:
			cursor.execute(
				"Update Client SET token = ? WHERE account_number=? AND password=? ",
				(token, self.account_number, self.client_code)
			)
			con.commit()
			print(f"Your token is {token}")
		except:
			print("Something wrong")

		


def main():
	client = Bank()
	client.input_client()
	client.verify()

main()
