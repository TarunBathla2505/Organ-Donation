from app import app
import sqlite3 as sql

class donor_model():
  def __init__(self):
    try:
      self.con = sql.connect("database.db",check_same_thread=False)
      self.con.row_factory = sql.Row 
      self.cur = self.con.cursor()
      app.logger.info("connection established")
    except:
      app.logger.info("some error occured")

  def addDonor(self,dic_data):
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
      organ = dic_data["organ"]
      cause = dic_data["cause"]
      query = "INSERT INTO donor (name,age,gender,email,bloodGroup,province,city,phone,country,organ,cause) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
      self.cur.execute(query,(name,age,gender,email,bloodGroup,province,city,phone,country,organ,cause))
      app.logger.info('query executed')
      data['msg'] = "record added successfully"

    except:
      app.logger.info('an exception has been ocurred')
      self.con.rollback()
      data['msg'] = "error in insert operation"

    finally:
      self.con.commit()
      return data
    
  # def getDonor(self):
  #   self.cur.execute("SELECT name,age,gender,email,bloodGroup,province,city,phone,country,organ as Organ_Required,cause FROM donor where hasDonated =0")
  #   rows = self.cur.fetchall()
  #   return self.dict_from_row(rows)
    
  def getDonor(self):
    self.cur.execute("SELECT age as Age, bloodGroup as BloodGroup, cause as Cause, city as City, organ as Organ_Required, country as Country, email as Email, gender as Gender, name as Name, phone as Phone, province as Province FROM donor where hasDonated = 0")
    rows = self.cur.fetchall()
    return self.dict_from_row(rows)
  
  def getDonorsByOrgan(self,organ):
    self.cur.execute("SELECT * FROM donor WHERE organ = ? COLLATE NOCASE",(organ,))
    rows = self.cur.fetchall()
    return self.dict_from_row(rows)
  
  def deleteDonor(self,donorId):
    data = {}
    self.cur.execute("delete from donor where id=?", (donorId,))
    self.con.commit()
    row = self.cur.fetchone()
    data["deleted"] = True
    return data
  
  
  def dict_from_row(self,rows):
    listRow =[]
    for row in rows:
      listRow.append(dict(zip(row.keys(), row)))
    return listRow
  