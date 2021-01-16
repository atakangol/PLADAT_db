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
def student_update():
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
    elif att=="pref":
        stu_id = request.args.get('stu_id')
        pref = request.args.get('emp')
        res = db_functions.update_student_pref(stu_id,pref)
    elif att=="age":
        stu_id = request.args.get('stu_id')
        age = request.args.get('age')
        res = db_functions.update_student_age(stu_id,age)
    elif att=="grade":
        stu_id = request.args.get('stu_id')
        grade = request.args.get('grade')
        res = db_functions.update_student_grade(stu_id,grade)
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
        "emp_pref":res[6],
        "grade":res[7],
        "age":res[8],
        "skills":res[9]
    }
    return jsonify(ret)

#city 
@app.route('/cities',methods=["GET"])
def cities():
    city_id = request.args.get('id')
    if id == "None":
        res = db_functions.get_city(city_id)
        ret = {"cities": [ {"id":res[0],
                "name": res[2],
                "country":res[1]  } ]}
    else:

        res = db_functions.get_all_cities()
        t = []
        for ii in range(len(res)):

            s = {
                "id":res[ii][0],
                "name": res[ii][2],
                "country":res[ii][1]
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
            "emp_pref":res[ii][6],
            "grade":res[ii][7],
            "age":res[ii][8],
            "skills":res[ii][9]
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
            "emp_pref":res[ii][6],
            "grade":res[ii][7],
            "age":res[ii][8],
            "skills":res[ii][9]
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
            "city":res[ii][3],  
            "country":res[ii][2]
        }
        t.append(s)
    ret = {"universities":t }
    return (jsonify(ret))




#job listings
@app.route("/add_job",methods=["POST"])
def add_job_listing():
    company_id = request.args.get('company')
    desc = request.args.get('desc')
    pref = request.args.get('emp_type')
    city_id = request.args.get('city')
    res = db_functions.add_job_listing(company_id,pref, desc)
    ret = {
        "flag":res[0],
        "job_id":res[1]
    }
    if ret["flag"]:
        db_functions.update_joblisting_location(ret["job_id"],city_id)
    return jsonify(ret)
@app.route("/all_jobs",methods=["GET"])
def all_jobs():
    res = db_functions.get_all_jobs()
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "company_id": res[ii][1],
            "job_desc":res[ii][2],  
            "company_name":res[ii][3],
            "city":res[ii][4],
            "country":res[ii][5],
            "emp_type":res[ii][6],
            "skill_list":db_functions.skill_format(res[ii][7])
        }
        t.append(s)
        
    ret = {"jobs":t }
    return (jsonify(ret))
@app.route("/edit_job_req",methods=["POST"])
def edit_job_req():   
    att = request.args.get("type")
    if att == "add":

        job_id = request.args.get('job_id')
        skill_id = request.args.get('skill_id')
        res = db_functions.add_job_req(job_id,skill_id)
    elif att=="del":
        job_id = request.args.get('job_id')
        skill_id = request.args.get('skill_id')
        res = db_functions.remove_job_req(job_id,skill_id)
    else:
        return jsonify({"flag":False})
    
    ret = {
        "flag":res
    }
    return jsonify(ret)
@app.route("/edit_job",methods=["POST"])
def edit_job():
    job_id = request.args.get('job_id')
   
    city_id = request.args.get('city_id')

    desc = request.args.get('desc')

    pref = request.args.get('emp_type')
    res = db_functions.update_job(job_id,city_id,desc,pref)

    
    ret = {
        "flag":res
    }
    return jsonify(ret)
@app.route("/delete_job",methods=["POST"])
def delete_job():
    job_id = request.args.get('job_id')
    res = db_functions.delete_job(job_id)
    ret = {
        "flag":res
    }
    return jsonify(ret)
@app.route("/job_details",methods=["GET"])
def job_details():
    job_id = request.args.get('job_id')
    res = db_functions.get_job_details(job_id)

    ret = {
        "id":res[0],
        "company_id": res[1],
        "job_desc":res[2],  
        "company_name":res[3],
        "city":res[4],
        "country":res[5],
        "emp_type":res[6],
        "skill_list":db_functions.skill_format(res[7])
    }
    return ret

@app.route('/search_jobs_by_skill',methods=["GET"])
def search_jobs_by_skill():
    term = request.args.get('term')
    res = db_functions.search_jobs_by_skill(term)
    #print(res)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "company_id": res[ii][1],
            "job_desc":res[ii][2],  
            "company_name":res[ii][3],
            "city":res[ii][4],
            "country":res[ii][5],
            "emp_type":res[ii][6],
            "skill_list":db_functions.skill_format(res[ii][7])
        }
        t.append(s)
    ret = {"jobs":t }
    return jsonify(ret)
@app.route('/search_jobs_by_skill_ids',methods=["GET"])
def search_jobss_by_skill_ids():
    '''idler string halinde "1,2,3" '''
    term = request.args.get('term')
    res = db_functions.search_jobs_by_skill_ids(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "company_id": res[ii][1],
            "job_desc":res[ii][2],  
            "company_name":res[ii][3],
            "city":res[ii][4],
            "country":res[ii][5],
            "emp_type":res[ii][6],
            "skill_list":db_functions.skill_format(res[ii][7])
        }
        t.append(s)
    ret = {"jobs":t }
    return jsonify(ret)
@app.route('/search_jobs',methods=["GET"])
def search_jobs():
    term = request.args.get('term')
    res = db_functions.search_jobs(term)
    t = []
    for ii in range(len(res)):

        s = {
            "id":res[ii][0],
            "company_id": res[ii][1],
            "job_desc":res[ii][2],  
            "company_name":res[ii][3],
            "city":res[ii][4],
            "country":res[ii][5],
            "emp_type":res[ii][6],
            "skill_list":db_functions.skill_format(res[ii][7])
        }
        t.append(s)
    ret = {"jobs":t }
    return jsonify(ret)


#applications
#direction true = job offer by company to student
#direction false = student application to company
@app.route("/add_application",methods=["POST"])
def new_application():
    student_id = request.args.get('stu_id')
    job_id = request.args.get('job_id')
    direction = request.args.get('direction')
    flag = db_functions.new_application(student_id,job_id,direction)

    return jsonify({"succes":flag})
@app.route("/delete_application",methods=["POST"])
def delete_application():
    student_id = request.args.get('stu_id')
    job_id = request.args.get('job_id')
    flag = db_functions.delete_application(student_id,job_id)

    return jsonify({"succes":flag})
@app.route("/positive_response",methods=["POST"])
def positive_response():
    student_id = request.args.get('stu_id')
    job_id = request.args.get('job_id')
    flag = db_functions.positive_response(student_id,job_id)

    return jsonify({"succes":flag})
@app.route("/applications_of_company",methods=["GET"])
def applications_of_company():
    company_id = request.args.get('company_id')
    res = db_functions.get_applications_of_company(company_id)

    t = []
    for ii in range(len(res)):

        s = {
            "job_id":res[ii][0],
            "student_id": res[ii][1],
            "direction":res[ii][2],  
            "response":res[ii][3],
            "company_id":res[ii][4],
            "description":res[ii][5],
            "city":res[ii][6]
        }
        t.append(s)
    ret = {"students":t }
    return jsonify(ret)
@app.route("/applications_of_student",methods=["GET"])
def applications_of_student():
    student_id = request.args.get('student_id')
    res = db_functions.get_applications_of_student(student_id)
    t = []
    for ii in range(len(res)):

        s = {
            "job_id":res[ii][0],
            "student_id": res[ii][1],
            "direction":res[ii][2],  
            "response":res[ii][3],
            "company_id":res[ii][4],
            "description":res[ii][5],
            "city":res[ii][6],
            "company_name":res[ii][7]
        }
        t.append(s)
    ret = {"students":t }
    return jsonify(ret)


#company profile
#signup
@app.route('/clogin',methods=['POST'])
def clogin():
    email = request.args.get('email')
    password = request.args.get('password')
    res = db_functions.company_login(email,password)
    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)
@app.route('/csignup',methods=['POST'])
def csignup():
    email = request.args.get('email')
    name = request.args.get('name')
    password = request.args.get('password')
    res = db_functions.company_signup(email,name,password)
    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)
@app.route('/company_update_city',methods=['POST']) #add or update city of the company
def company_update_city():
    company_id = request.args.get('company_id')
    city_id = request.args.get('city_id')
    res = db_functions.update_company_city(company_id,city_id)
    ret = {"flag":res}
    return jsonify(ret)


@app.route('/company_update',methods=['POST'])
def company_update():
    company_id = request.args.get('company_id')
    excid = request.args.get('excid')
    excname = request.args.get('excname')
    excdob = request.args.get('excdob')
    res = db_functions.update_company_profile(company_id, excid, excname, excdob)
    ret = {
        "flag":res[0],
        "company_id":res[1]
    }
    return jsonify(ret)

@app.route('/company_detail',methods=['GET'])
def company_detail():
    company_id = request.args.get('company_id')
    res = db_functions.get_company_details(company_id)
    ret = {
        "id":res[0],
        "email": res[1],
        "name":res[2],
        "city":res[3],
        "excid":res[4],
        "excname":res[5],
        "excdob":res[6],
        "job_lis":res[7]
    }
    return jsonify(ret)



if __name__ == "__main__":
    app.run(debug=True,port=9090)

