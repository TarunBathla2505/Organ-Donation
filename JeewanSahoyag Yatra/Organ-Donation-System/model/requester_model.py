from app import app
import sqlite3 as sql
from flask import make_response

class requester_model():
  def __init__(self):
    try:
      self.con = sql.connect("database.db",check_same_thread=False)
      self.con.row_factory = sql.Row 
      self.cur = self.con.cursor()
      app.logger.info("connection established")
    except:
      app.logger.info("some error occured")

  def addRequest(self,dic_data):
    data = {}
    try:
      name = dic_data["name"]
      age = dic_data["age"]
      gender = dic_data["gender"]
      email = dic_data['email']
      bloodGroup = dic_data["bloodGroup"]
      province = dic_data['province']
      city = dic_data['city']
      phone = dic_data['phone']
      country = dic_data['country']
      organ_required = dic_data["organ_required"]
      cause = dic_data["cause"]
      query = "INSERT INTO requesters (name,age,gender,email,bloodGroup,province,city,phone,country,organ_required,cause) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
      self.cur.execute(query,(name,age,gender,email,bloodGroup,province,city,phone,country,organ_required,cause))
      app.logger.info('query executed')
      data['msg'] = "record added successfully"

    except:
      self.con.rollback()
      data['msg'] = "error in insert operation"

    finally:
      self.con.commit()
      return data
    
  def getRequests(self):
    self.cur.execute("SELECT * FROM requesters")
    rows = self.cur.fetchall()
    return self.dict_from_row(rows)
  
  def getPendingRequests(self):
    self.cur.execute("SELECT name,age,gender,email,bloodGroup,province,city,phone,country,organ_required as Organ,cause,id FROM requesters WHERE donorId IS NULL")
    rows = self.cur.fetchall()
    return self.dict_from_row(rows)
  
  def getAcceptedRequests(self):
    self.cur.execute("SELECT donor.age as donor_age,requesters.age as requester_age,donor.name as donor_name,requesters.name as requester_name,donor.organ,donor.bloodGroup,requesters.donorId,requesters.id as requester_id,donor.phone as donor_phone,requesters.phone as requesters_phone FROM requesters CROSS JOIN donor WHERE requesters.donorId = donor.id")
    rows = self.cur.fetchall()
    dictRow = self.dict_from_row(rows)
    return dictRow
  
  def deleteRequest(self,requestId):
    data = {}
    self.cur.execute("delete from requesters where id=?", (requestId,))
    self.con.commit()
    row = self.cur.fetchone()
    data["deleted"] = True
    return data
  
  
  def dict_from_row(self,rows):
    listRow =[]
    for row in rows:
      listRow.append(dict(zip(row.keys(), row)))
    return listRow
  
  def match_and_accept(self, requestId):
    self.cur.execute("SELECT organ_required, bloodGroup, donorId FROM requesters WHERE id=?", (requestId,))
    row = self.cur.fetchone()
    organ_required = row[0]
    blood_group = row[1]
    donor_assigned = row[2]
    if(donor_assigned):
      return make_response({"message":"Donor already assigned"}, 401)
    self.cur.execute("SELECT * FROM donor WHERE organ=? COLLATE NOCASE AND bloodGroup=? COLLATE NOCASE AND hasDonated=?", (organ_required, blood_group,0,))
    record = self.cur.fetchone()
    if(record):
      donorId = record[0]
      self.cur.execute("UPDATE requesters SET donorId=? WHERE id=?", (donorId, requestId,))
      self.cur.execute("UPDATE donor SET hasDonated=1 WHERE id=?", (donorId,))
      self.con.commit()
      return make_response({"message": "Request Accepted"}, 200)
    else:
      return make_response({"message": "Request Rejected"}, 403)