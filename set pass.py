from flask_bcrypt import bcrypt
password = u"1234"
hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
print(hashed_password)