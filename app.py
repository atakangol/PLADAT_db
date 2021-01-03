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
    res = db_functions.get_student_details(stu_id)
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
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][2],
            "country":res[ii][1],  
        }
        t.append(s)
    ret = {"cities":t }
    return (jsonify(ret))
@app.route('/search_city',methods=["GET"])
def search_city():
    term = request.args.get('term')
    res = db_functions.search_city(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][2],
            "country":res[ii][1],  
        }
        t.append(s)
    ret = {"cities":t }
    return (jsonify(ret))
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

#skills
@app.route('/all_skills',methods=["GET"])
def all_skills():
    res = db_functions.get_all_skills()
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][1],
            "description":res[ii][2],  
        }
        t.append(s)
    ret = {"skills":t }
    return (jsonify(ret))
@app.route('/add_skill',methods=["POST"])
def add_skill():
    name = request.args.get('name')
    desc = request.args.get('desc')
    res = db_functions.add_skill(name,desc)
    ret = {
        "flag":res[0],
        "skill_id":res[1]
    }
    return jsonify(ret)
@app.route('/search_skills',methods=["GET"])
def search_skills():
    term = request.args.get('term')
    res = db_functions.search_skill(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][1],
            "description":res[ii][2],  
        }
        t.append(s)
    ret = {"skills":t }
    return (jsonify(ret))
@app.route("/edit_student_skill",methods=["POST"])
def edit_student_skill():   
    att = request.args.get("type")
    if att == "add":

        stu_id = request.args.get('stu_id')
        skill_id = request.args.get('skill_id')
        res = db_functions.add_student_skill(stu_id,skill_id)
    elif att=="del":
        stu_id = request.args.get('stu_id')
        skill_id = request.args.get('skill_id')
        res = db_functions.remove_student_skill(stu_id,skill_id)
    else:
        return jsonify({"flag":False})
    
    ret = {
        "flag":res
    }
    return jsonify(ret)


@app.route('/search_students_by_skill',methods=["GET"])
def search_students_by_skill():
    term = request.args.get('term')
    res = db_functions.search_students_by_skill(term)
    #print(res)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][1],
            "university":res[ii][2],
            "department":res[ii][3],
            "faculty":res[ii][4],
            "city":res[ii][5],
            "skills":res[ii][6]
        }
        t.append(s)
    ret = {"students":t }
    return jsonify(ret)
@app.route('/search_students_by_skill_ids',methods=["GET"])
def search_students_by_skill_ids():
    '''idler string halinde "1,2,3" '''
    term = request.args.get('term')
    res = db_functions.search_students_by_skill_ids(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][1],
            "university":res[ii][2],
            "department":res[ii][3],
            "faculty":res[ii][4],
            "city":res[ii][5],
            "skills":res[ii][6]
        }
        t.append(s)
    ret = {"students":t }
    return jsonify(ret)

#departments and universities
@app.route("/add_department",methods=["POST"])
def add_department():
    name = request.args.get('name')
    faculty = request.args.get('faculty')
    res = db_functions.add_department(name,faculty)
    ret = {
        "flag":res[0],
        "department_id":res[1]
    }
    return jsonify(ret)
@app.route("/all_dep",methods=["GET"])
def get_all_departments():
    res = db_functions.get_all_departments()
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "faculty": res[ii][1],
            "name":res[ii][2]
        }
        t.append(s)
    ret = {"departments":t }
    return (jsonify(ret))
@app.route("/get_faculties",methods=["GET"])
def get_unique_faculties():
    res = db_functions.get_unique_faculties()
    t = []
    for ii in range(len(res)):
        s = {
            "name": res[ii]
        }
        t.append(s)
    ret = {"faculties":t }
    return (jsonify(ret))
@app.route("/get_departments",methods=["GET"])
def get_unique_departments():
    res = db_functions.get_unique_departments()
    t = []
    for ii in range(len(res)):
        s = {
            "name": res[ii]
        }
        t.append(s)
    ret = {"departments":t }
    return (jsonify(ret))
@app.route("/search_department",methods=["GET"])   
def search_department():
    term = request.args.get('term')
    res = db_functions.search_department(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "faculty": res[ii][1],
            "name":res[ii][2] 
        }
        t.append(s)
    ret = {"departments":t }
    return (jsonify(ret))

@app.route("/all_unis",methods=["GET"])
def all_unis():
    res = db_functions.all_unis()
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][1],
            "city":res[ii][2],  
            "country":res[ii][3]
        }
        t.append(s)
    ret = {"universities":t }
    return (jsonify(ret))
@app.route("/add_uni",methods=["POST"])
def add_university():
    name = request.args.get('name')
    city_id = request.args.get('city_id')
    res = db_functions.add_university(name,city_id)
    ret = {
        "flag":res[0],
        "uni_id":res[1]
    }
    return jsonify(ret)
@app.route("/search_uni",methods=["GET"])
def search_university():
    term = request.args.get('term')
    res = db_functions.search_university(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "name": res[ii][1],
            "city":res[ii][2],  
            "country":res[ii][3]
        }
        t.append(s)
    ret = {"universities":t }
    return (jsonify(ret))





if __name__ == "__main__":
    app.run(debug=True,port=9090)

