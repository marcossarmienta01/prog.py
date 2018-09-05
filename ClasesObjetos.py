class MixinsData(object):
	def __init__(self, user = "Anonimo", password = "patito", port = "1234", host = "localhost", db = "sqlite3"):
		
		#Atributos
		self._user = user
		self._password = password
		self._port = port
		self._host = host
		self._db = db

	def get_username(self):
		return self._user

	def get_password(self):
		return self._password

	def get_port(self):
		return self._port

	def get_host(self):
		return self._host

	def get_db(self):
		return self._db

usuario = str(input("Nombre de usuario? :"))
password = str(input("Password? :"))

obj = MixinsData(password=password, user=usuario)

print(obj._user)
print(obj._password)

print(obj.get_username())
user = obj.get_username()
print(user * 10)


# JAVA ,C#, C++ y Otros
#MixinsData obj = new MixinsData();
#int x = 0;
#es igual para los siguientes lenguajes 
#Python o Ruby