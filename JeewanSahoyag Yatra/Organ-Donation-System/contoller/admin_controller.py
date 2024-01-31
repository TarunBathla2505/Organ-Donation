from app import app
from model.admin_model import admin_model
from flask import request

admin_obj = admin_model()

@app.route("/admin/login",methods=['POST'])
def user_login():
    postedData = request.json

    email = postedData["email"]
    password = postedData["password"]

    return admin_obj.admin_login_model(email, password)
