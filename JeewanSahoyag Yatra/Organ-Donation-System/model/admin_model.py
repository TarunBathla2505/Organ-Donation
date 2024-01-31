from app import app
import bcrypt
import sqlite3 as sql
from flask import make_response

stored_password = "ADMIN!@#".encode()

class admin_model:
            
    def admin_login_model(self, email, password):
        app.logger.info("inside model")
        if email=="admin@gmail.com":
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) 
            is_valid = bcrypt.checkpw(password=stored_password, hashed_password=hashed_password)
            dic = {}
            if(is_valid):
                app.logger.info("user logged in")
                dic['message'] = "User logged in"
                return make_response(dic,200)
            else:
                app.logger.info("Wrong password")
                dic['message']="Wrong password"
                return make_response(dic,401)
        else:
            dic={}
            app.logger.info("ADMIN NOT FOUND")
            dic['message']="ADMIN NOT FOUND"
            return make_response(dic,404)
