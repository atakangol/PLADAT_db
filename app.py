from flask import Flask,request,jsonify
import db_functions

app = Flask(__name__)



#student profile
@app.route('/slogin',methods=['POST'])
def slogin():
    email = request.args.get('email')
    
    password = request.args.get('pw')
    res = db_functions.student_login(email,password)
    #print(res)
    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)
@app.route('/ssignup',methods=['POST'])
def ssignup():
    email = request.args.get('email')
    name = request.args.get('name')
    pw = request.args.get('pw')

    res = db_functions.student_signup(email,name,pw)

    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)
@app.route('/student_update',methods=['POST'])
def studentupdate():
    att = request.args.get("type")
    if att == "city":

        stu_id = request.args.get('stu_id')
        city_id = request.args.get('city_id')
        res = db_functions.update_student_city(stu_id,city_id)
    elif att=="dep":
        stu_id = request.args.get('stu_id')
        dep_id = request.args.get('dep_id')
        res = db_functions.update_student_department(stu_id,dep_id)
    elif att=="uni":
        stu_id = request.args.get('stu_id')
        uni_id = request.args.get('uni_id')
        res = db_functions.update_student_university(stu_id,uni_id)
    else:
        return jsonify({"flag":False})
    ret = {
        "flag":res[0],
        "student_id":res[1]
    }
    return jsonify(ret)
@app.route('/stu_detail',methods=['GET'])
def stu_detail():
    stu_id = request.args.get('stu_id')
    res = db_functions.get_user_details(stu_id)
    ret = {
        "id":res[0],
        "name": res[1],
        "university":res[2],
        "department":res[3],
        "faculty":res[4],
        "city":res[5],
        "skills":res[6]
    }
    return jsonify(ret)

#city
@app.route('/all_cities',methods=["GET"])
def cities():
    res = db_functions.get_all_cities()
    return (jsonify(res))
@app.route('/search_city',methods=["GET"])
def search_city():
    key = request.args.get('key')
    res = db_functions.search_city(key)
    return (jsonify(res))
@app.route('/add_city',methods=["POST"])
def add_city():
    name = request.args.get('name')
    country = request.args.get('country')
    res = db_functions.insert_city(country,name)
    ret = {
        "flag":res[0],
        "city_id":res[1]
    }
    return jsonify(ret)







if __name__ == "__main__":
    app.run(debug=True,port=9090)

