from flask_bcrypt import bcrypt
password = u"937fz633fz1473"
hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
print(hashed_password)