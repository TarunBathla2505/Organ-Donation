from app import app
from flask import request,session,jsonify
from flask_mail import Mail, Message
import random
from flask_cors import cross_origin


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tarunbathla721@gmail.com'
app.config['MAIL_PASSWORD'] = 'fdwc zydq jwwj jenb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

otps=[238632,743723,832743,938212,379932,320840,392932]
@app.route('/send/<email>',methods=['POST'])
def send(email):

  recipient =[]
  recipient.append(email)
  message = Message(
    subject = 'OTP',
    recipients = recipient,
    sender = 'tarunbathla721@gmail.com'
  )
  otp = random.choice(otps)
  message.body = "hey this is your otp for verification "+str(otp)
  app.logger.info(message.body)
  mail.send(message)
  app.logger.info("Session after sending OTP: {}".format(session))
  return jsonify({"message": otp})

@app.route('/verify/<otpInput>',methods=['POST'])
@cross_origin(supports_credentials=True)
def verify(otpInput):
  app.logger.info("otp is"+otpInput)
  data = False
  app.logger.info("Session after sending OTP: {}".format(session))
  if int(otpInput) in otps:
    data = True
  return jsonify({"message": data})

@app.route('/rejectMail/<email>')
def reject(email):
  recipient =[]
  recipient.append(email)
  message = Message(
    subject = 'Organ Request Rejected',
    recipients = recipient,
    sender = 'tarunbathla721@gmail.com'
  )
  message.body = "Your request for the organ has been rejected."
  app.logger.info(message.body)
  mail.send(message)
  data ={}
  data["email"]="sent"
  return data


@app.route('/acceptMail/<email>')
def accept(email):
  recipient =[]
  recipient.append(email)
  message = Message(
    subject = 'Organ Request Accepted',
    recipients = recipient,
    sender = 'tarunbathla721@gmail.com'
  )
  message.body = "Your request for the organ has been accepted."
  app.logger.info(message.body)
  mail.send(message)
  data ={}
  data["email"]="sent"
  return data