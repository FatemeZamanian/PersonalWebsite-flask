from flask_bcrypt import bcrypt
password = u"your pass"
hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
print(hashed_password)