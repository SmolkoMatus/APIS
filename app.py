from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL


app = Flask(__name__)
CORS(app)


Employee = ["Peter"]

@app.route("/GetEmployee", methods=["GET"])
def employee():
    with open ("DB/get/get_employee.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    mydb.close()
    return jsonify(result),200

@app.route("/GetWorposition", methods=["GET"])
def workposition():
    with open ("DB/get/get_worposition.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    mydb.close()
    return jsonify(result),200

@app.route("/GetEmployment", methods=["GET"])
def employment():
    with open ("DB/get/get_employment.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    mydb.close()
    return jsonify(result),200

@app.route("/GetPayment", methods=["GET"])
def main():
    with open ("DB/get/get_salary.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return jsonify(result),200

@app.route("/CreateEmployee", methods=["POST"])
def create():
    data = request.get_json(force=True)
    employee_dict = dict(data)
    with open ("DB/create/create_employee.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    databaza = databaza.replace("ID", employee_dict["ID"])
    databaza = databaza.replace("Name", employee_dict["Name"])
    databaza = databaza.replace("Hours", employee_dict["Hours"])
    databaza = databaza.replace("WorPositionID", employee_dict["WorPositionID"])
    databaza = databaza.replace("EmploymentID", employee_dict["EmploymentID"])
    cursor.execute(databaza)
    mydb.commit()
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return jsonify("created"),201

@app.route("/CreateEmployment", methods=["POST"])
def createE():
    data = request.get_json(force=True)
    employment_dict = dict(data)
    with open ("DB/create/create_employment.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    databaza = databaza.replace("ID", employment_dict["ID"])
    databaza = databaza.replace("AddressEmployment", employment_dict["AddressEmployment"])
    databaza = databaza.replace("EmailEmployment", employment_dict["EmailEmployment"])
    cursor.execute(databaza)
    mydb.commit()
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return jsonify("created"),201

@app.route("/CreateWorposition", methods=["POST"])
def createW():
    data = request.get_json(force=True)
    workposition_dict = dict(data)
    with open ("DB/create/create_worposition.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    databaza = databaza.replace("ID", workposition_dict["ID"])
    databaza = databaza.replace("WorkPositionName", workposition_dict["WorkPositionName"])
    databaza = databaza.replace("ActivityCosts", workposition_dict["ActivityCosts"])
    cursor.execute(databaza)
    mydb.commit()
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return jsonify(databaza),201

@app.route("/UpdateEmployee/<id>", methods=["PUT"])
def update(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    with open ("DB/update/update_employee.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    mydb.commit()
    cursor.close()
    mydb.close()
    return jsonify("updated"),201

@app.route("/UpdateEmployment/<id>", methods=["PUT"])
def updateE(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    with open ("DB/update/update_employment.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    mydb.commit()
    cursor.close()
    mydb.close()
    return jsonify("updated"),201

@app.route("/UpdateWorkposition/<id>", methods=["PUT"])
def updateW(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    with open ("DB/update/update_workposition.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    mydb.commit()
    cursor.close()
    mydb.close()
    return jsonify("updated"),201

@app.route("/DeleteEmployee/<id>", methods=["DELETE"])
def delete(id):
    with open ("DB/delete/delete_employee.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    mydb.commit()
    cursor.close()
    mydb.close()
    return jsonify("deleted"),204

@app.route("/DeleteEmployment/<id>", methods=["DELETE"])
def deleteE(id):
    with open ("DB/delete/delete_employment.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    mydb.commit()
    cursor.close()
    mydb.close()
    return jsonify("deleted"),204

@app.route("/DeleteWorkPosition/<id>", methods=["DELETE"])
def deleteW(id):
    with open ("DB/delete/delete_workposition.ddl") as ddl_file:
        databaza = ddl_file.read()
    mydb = MYSQL.connect(host="147.232.40.14", user="sl267qr", passwd="boiLo6ah", database="sl267qr")
    cursor = mydb.cursor()
    cursor.execute(databaza)
    mydb.commit()
    cursor.close()
    mydb.close()
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
