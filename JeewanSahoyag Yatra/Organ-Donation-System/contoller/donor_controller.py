from app import app
from flask import request
from model.donor_model import donor_model


donor_obj = donor_model()
@app.route('/donor',methods=['POST','GET'])
def addDonor():
  if request.method == 'POST':
    dic_data = request.json
    return donor_obj.addDonor(dic_data)
  else:
    return donor_obj.getDonor()
  
@app.route('/donor/<organ>')
def getDonorsByOrgan(organ):
  return donor_obj.getDonorsByOrgan(organ)

@app.route('/donor/<donorId>', methods = ['DELETE'])
def deleteDonor(donorId):
  return donor_obj.deleteDonor(donorId)




