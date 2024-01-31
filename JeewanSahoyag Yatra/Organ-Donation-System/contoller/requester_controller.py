from app import app
from flask import request
from model.requester_model import requester_model


requester_obj = requester_model()
@app.route('/request',methods=['POST','GET'])
def addRequest():
  if request.method == 'POST':
    dic_data = request.json
    return requester_obj.addRequest(dic_data)
  else:
    return requester_obj.getRequests()
  
@app.route('/pending-requests', methods=['GET'])
def getPendingRequests():
    return requester_obj.getPendingRequests()

@app.route('/accepted-requests', methods=['GET'])
def getAcceptedRequests():
    return requester_obj.getAcceptedRequests()

@app.route('/request/<requestId>', methods = ['DELETE'])
def deleteRequest(requestId):
  return requester_obj.deleteRequest(requestId)

@app.route('/request/match/<requestId>', methods=['PUT'])
def match_and_accept(requestId):
    return requester_obj.match_and_accept(requestId)
