import psycopg2 as db
import sys
import json


url  = "dbname='PlaDat' user='postgres' host='localhost' password='45581222'"

def print_psycopg2_exception(err):
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno
    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

def test(t):
    global url
    print(url)
    url = t
    print(url)
    return (url)

def create_tables():
    #temp_url = "dbname='PlaDat2' user='postgres' host='localhost' password='45581222'"
    with open("PlaDat.sql","r") as sql:
        temp = sql.readlines()
    statement = ""
    for ii in temp:
        statement += ii +" "
    print(statement)
    
    connection = db.connect(url)
    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    connection.close()
    

#city
def insert_city(country,name):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."CITIES"( "COUNTRY", "NAME") VALUES ('{}', '{}') RETURNING "ID";""".format(country.title(),name.title())

    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        connection.commit()
        id = int(id[0])
        flag=True
    except Exception as err:
        # pass exception to function
        #print_psycopg2_exception(err)
        if (err.pgcode == "23505"):
            print("this city already exists")
            id=-1
            flag=False
    
    #print(id)
    finally:
        cursor.close()
        connection.close()
        
    return (flag,id)
def search_city(term):
    '''searches in both the name and the country'''
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT "ID", "COUNTRY", "NAME"
	FROM public."CITIES"
	where "NAME" ilike '%{a}%' or "COUNTRY" ilike '%{a}%';""".format(a=term.lower())
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def get_all_cities():
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT *
	FROM public."CITIES" """
    cursor.execute(statement)
    results = cursor.fetchall()
    return results


#student profile
def student_signup(email,name,password):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."STUDENTS"(
	"EMAIL", "PASSWORD", "NAME")
	VALUES ('{}', '{}', '{}') RETURNING "ID";""".format(email,password,name)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        connection.commit()
        id = int(id[0])
        flag=True
    except Exception as err:
        # pass exception to function
        #print_psycopg2_exception(err)
        if (err.pgcode == "23505"):
            print("this email is already in use")
            id=-1
            flag=False
    #print(id)
    finally:
        cursor.close()
        connection.close()
    return (flag,id)
def student_login(email,pw):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """SELECT "ID" FROM public."STUDENTS" where "EMAIL" = '{}' and "PASSWORD"='{}';""".format(email,pw)

    cursor.execute(statement)
    result = cursor.fetchone()
    if result:
        return (True,int(result[0]))
    
    statement = """SELECT "ID" FROM public."STUDENTS" where "EMAIL" = '{}' ;""".format(email)
    if result:
        print('wrong password')
        return (False,int(result[0]))
    print("user doesn't exist")
    return(False,-1)
def update_student_city(student_id,city_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """UPDATE public."STUDENTS"
	SET "CITY"={}
	WHERE "ID"={} returning "ID";""".format(city_id,student_id)

    try:
        cursor.execute(statement)
        res = cursor.fetchall()
        #print(len(res))
        connection.commit()

        '''
        if len(res) == 0:
            "no student with this id" 
            #return (false,student_id)
            id=student_id
            flag=False'''
        flag = True
        try:

            id = res[0][0]
        except:
            "no student with this id" 
            #return (false,student_id)
            id=student_id
            flag=False

    except Exception as err:
        # pass exception to function
        #print_psycopg2_exception(err)
        if (err.pgcode == "23503"):
            print("no city with this id found")
            id=-1
            flag=False
    
    #print(id)
    finally:
        cursor.close()
        connection.close()
        
    return (flag,id)
def update_student_department(student_id,department_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """UPDATE public."STUDENTS"
	SET "DEPARTMENT"={}
	WHERE "ID"={} returning "ID";""".format(department_id,student_id)

    try:
        cursor.execute(statement)
        res = cursor.fetchall()
        #print(len(res))
        connection.commit()

        '''
        if len(res) == 0:
            "no student with this id" 
            #return (false,student_id)
            id=student_id
            flag=False'''
        
        flag = True
        try:

            id = res[0][0]
        except:
            "no student with this id" 
            #return (false,student_id)
            id=student_id
            flag=False

    except Exception as err:
        # pass exception to function
        print_psycopg2_exception(err)
        if (err.pgcode == "23503"):
            print("no department with this id found")
            id=-1
            flag=False
    
    #print(id)
    finally:
        cursor.close()
        connection.close()
        
    return (flag,id)
def update_student_university(student_id,uni_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """UPDATE public."STUDENTS"
	SET "UNIVERSITY"={}
	WHERE "ID"={} returning "ID";""".format(uni_id,student_id)

    try:
        cursor.execute(statement)
        res = cursor.fetchall()
        #print(len(res))
        connection.commit()

        '''
        if len(res) == 0:
            "no student with this id" 
            #return (false,student_id)
            id=student_id
            flag=False'''
        
        flag = True
        try:

            id = res[0][0]
        except:
            "no student with this id" 
            #return (false,student_id)
            id=student_id
            flag=False

    except Exception as err:
        # pass exception to function
        print_psycopg2_exception(err)
        if (err.pgcode == "23503"):
            print("no uni with this id found")
            id=-1
            flag=False
    
    #print(id)
    finally:
        cursor.close()
        connection.close()
        
    return (flag,id)
def get_student_details(user_id): #fix empty query
    '''spesik öğrencinin 
        (id, name universite bölüm fakülte yaşadığı şehir
        liste halinde skill:açıklama(boş gelebilir) )
        '''

    connection = db.connect(url)
    cursor = connection.cursor()    
    statement ="""select 
    S."ID" as id,
    S."NAME" as name,
    U."NAME" as university,
    D."NAME" as department,
    D."FACULTY" as faculty,
    C."NAME" as student_city,
	ARRAY_AGG( concat(SK."NAME", ':' ,SK."DESCRIPTION")) as skill_list
    from "STUDENTS" S 
    left join "STUDENT_SKILL" SS on S."ID" = SS."STU_ID" 
    left join "SKILLS" SK on SS."SKILL_ID" = SK."ID"
    left join "UNIVERSITIES" U on U."ID"=S."UNIVERSITY"
    left join "DEPARTMENTS" D on D."ID"=S."DEPARTMENT"
    left join "CITIES" C on 	C."ID"=S."CITY"
	where S."ID" = {}
    GROUP BY S."ID",S."NAME",U."NAME",D."NAME",D."FACULTY",C."NAME"
    """.format(user_id)
    cursor.execute(statement)
    result = cursor.fetchone()
    return(result)
def update_student_pref(stu_id,pref):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """UPDATE public."STUDENTS"
	SET "EMP_PREF"= '{}'
	WHERE "ID"={} returning "ID";""".format(pref,stu_id)
    
    cursor.execute(statement)
    res = cursor.fetchall()
    #print(len(res))
    connection.commit()
    try:

        #id = res[0][0]
        flag= True
    except:
        print( "no student with this id" )
        #return (false,student_id)
        #id=stu_id
        flag=False
    cursor.close()
    connection.close()
    return (flag,stu_id)
#departments and universities
def add_department(name,faculty):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."DEPARTMENTS"(
	"FACULTY", "NAME")
	VALUES ( '{}','{}') RETURNING "ID";""".format(faculty.title(),name.title())
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        #print(id)
        id = id[0]
        connection.commit()
        flag=True
    except Exception as err:
        # pass exception to function
        #print_psycopg2_exception(err)
        if (err.pgcode == "23505"):
            print("this department already exists")
            id=-1
            flag=False

    finally:
        cursor.close()
        connection.close()

    return (flag,id)
def get_all_departments():
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT *
	FROM public."DEPARTMENTS" """
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def get_unique_faculties():
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT DISTINCT "FACULTY"
	FROM public."DEPARTMENTS" """
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def get_unique_departments():
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT DISTINCT "NAME"
	FROM public."DEPARTMENTS" """
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def search_department(term):
    '''searches in both the name and the faculty'''
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT "ID", "FACULTY", "NAME"
	FROM public."DEPARTMENTS"
	where "NAME" ilike '%{a}%' or "FACULTY" ilike '%{a}%';""".format(a=term.lower())
    cursor.execute(statement)
    results = cursor.fetchall()
    return results

def add_university(name,city_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."UNIVERSITIES"(
	 "NAME", "CITY")
	VALUES ( '{}',{}) RETURNING "ID";""".format(name.title(),city_id)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        #print(id)
        id = id[0]
        connection.commit()
        flag=True
    except Exception as err:
        # pass exception to function
        #print_psycopg2_exception(err)
        if (err.pgcode == "23505"):
            print("this university already exists")
            id=-1
            flag=False
        elif (err.pgcode == "23503"):
            print("no city with this id found")
            id=-1
            flag=False
        flag=False
    finally:
        cursor.close()
        connection.close()

    return (flag,id)
def search_university(term):
    '''searches in the name '''
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ select "UNIVERSITIES"."ID","UNIVERSITIES"."NAME","CITIES"."COUNTRY","CITIES"."NAME" 
    from "UNIVERSITIES" inner join "CITIES" ON ("UNIVERSITIES"."CITY" = "CITIES"."ID")
	where "UNIVERSITIES"."NAME" ilike '%{a}%';""".format(a=term.lower())
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def all_unis():
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT 
    "UNIVERSITIES"."ID",
    "UNIVERSITIES"."NAME",
    "CITIES"."NAME",
    "CITIES"."COUNTRY"
	FROM public."UNIVERSITIES"
	inner join "CITIES" ON "UNIVERSITIES"."CITY" = "CITIES"."ID" """
    cursor.execute(statement)
    results = cursor.fetchall()
    return results

#skills
def get_all_skills():
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT *
	FROM public."SKILLS" """
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def add_skill(name,desc=None):
    connection = db.connect(url)
    cursor = connection.cursor()
    if desc:
        statement = """INSERT INTO public."SKILLS"(
        "NAME", "DESCRIPTION")
        VALUES ( '{}','{}') RETURNING "ID";""".format(name,desc.title())
    else:
        statement = """INSERT INTO public."SKILLS"(
        "NAME")
        VALUES ( '{}') RETURNING "ID";""".format(name)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        #print(id)
        id = id[0]
        connection.commit()
        flag=True
    except Exception as err:
        # pass exception to function
        print_psycopg2_exception(err)
        
        
        flag=False
    finally:
        cursor.close()
        connection.close()

    return (flag,id)
def search_skill(term):
    '''searches in both the name and the description'''
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """ SELECT "ID", "NAME", "DESCRIPTION"
	FROM public."SKILLS"
	where "NAME" ilike '%{a}%' or "DESCRIPTION" ilike '%{a}%';""".format(a=term.lower())
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
def add_student_skill(student_id,skill_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."STUDENT_SKILL"(
	"STU_ID", "SKILL_ID")
	VALUES ({}, {}) RETURNING "ID";""".format(student_id,skill_id)
    try:
        cursor.execute(statement)
        res = cursor.fetchall()
        #print(len(res))
        connection.commit()
        flag = True
        try:

            id = res[0][0]
        except:
            print("no student with this id" )
            #return (false,student_id)
            id=student_id
            flag=False

    except Exception as err:
        # pass exception to function
        #print_psycopg2_exception(err)
        if (err.pgcode == "23503"):
            print("this skill or student doesnt exist")
            id=-1
            flag=False
        if (err.pgcode == "23505"):
            print("this student already has this skill")
            id=-1
            flag=False
        id=-1
        flag=False
    
    #print(id)
    finally:
        cursor.close()
        connection.close()
        
    return (flag,id)
def remove_student_skill(student_id,skill_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """DELETE FROM public."STUDENT_SKILL"
	WHERE "STU_ID"={} AND "SKILL_ID"={};""".format(student_id,skill_id)
    try:
        cursor.execute(statement)
        connection.commit()
        flag = True
    except Exception as err:
        # pass exception to function
        print_psycopg2_exception(err)
        flag=False
    finally:
        cursor.close()
        connection.close()
        
    return flag

def search_students_by_skill(term):
    '''skilllerde ve açıklamalırında arama yapıp 
        öğrencileri liste halinde
        (id, name universite bölüm fakülte yaşadığı şehir
        liste halinde skill:açıklama(boş gelebilir) )'''

    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """select 
    id,name,university,department,faculty,student_city,
    ARRAY_AGG( concat(skills."NAME", ':' ,skills."DESCRIPTION")) as skill_list
    from (select 
    S."ID" as id,
    S."NAME" as name,
    U."NAME" as university,
    D."NAME" as department,
    D."FACULTY" as faculty,
    C."NAME" as student_city
    from "STUDENTS" S 
    left join "STUDENT_SKILL" SS on S."ID" = SS."STU_ID" 
    left join "SKILLS" SK on SS."SKILL_ID" = SK."ID"
    left join "UNIVERSITIES" U on U."ID"=S."UNIVERSITY"
    left join "DEPARTMENTS" D on D."ID"=S."DEPARTMENT"
    left join "CITIES" C on 	C."ID"=S."CITY"
    where SK."NAME" ilike '%{t}%' or SK."DESCRIPTION" ilike '%{t}%'
    GROUP BY S."ID",S."NAME",U."NAME",D."NAME",D."FACULTY",C."NAME"
    ) as res 
    inner join "STUDENT_SKILL" SS1 on id = SS1."STU_ID"
    inner join "SKILLS" skills on SS1."SKILL_ID" = skills."ID"
    GROUP BY id,name,university,department,faculty,student_city;
    """.format(t=term)
    cursor.execute(statement)
    results = cursor.fetchall()
    return(results)
def search_students_by_skill_ids(ids):
    '''spesifik skillerden birine sahiğ
        öğrencileri liste halinde
        (id, name universite bölüm fakülte yaşadığı şehir
        liste halinde skill:açıklama(boş gelebilir) )'''
    
    key = []
    for ii in ids.split(","):
        key.append(int(ii))
    
    if len(key)==1:
        key = "("+str(key[0]) + ")"
    else:
        key = tuple(key)
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """select 
    id,name,university,department,faculty,student_city,
    ARRAY_AGG( concat(skills."NAME", ':' ,skills."DESCRIPTION")) as skill_list
    from (select 
    S."ID" as id,
    S."NAME" as name,
    U."NAME" as university,
    D."NAME" as department,
    D."FACULTY" as faculty,
    C."NAME" as student_city
    from "STUDENTS" S 
    left join "STUDENT_SKILL" SS on S."ID" = SS."STU_ID" 
    left join "SKILLS" SK on SS."SKILL_ID" = SK."ID"
    left join "UNIVERSITIES" U on U."ID"=S."UNIVERSITY"
    left join "DEPARTMENTS" D on D."ID"=S."DEPARTMENT"
    left join "CITIES" C on 	C."ID"=S."CITY"
    where SK."ID" in {}
    GROUP BY S."ID",S."NAME",U."NAME",D."NAME",D."FACULTY",C."NAME"
    ) as res 
    inner join "STUDENT_SKILL" SS1 on id = SS1."STU_ID"
    inner join "SKILLS" skills on SS1."SKILL_ID" = skills."ID"
    GROUP BY id,name,university,department,faculty,student_city;
    """.format(key)
    cursor.execute(statement)
    results = cursor.fetchall()
    return(results)

#company profile
def company_signup(email,name,password, excname, excdob): #without exc_id 
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """INSERT INTO public."COMPANIES"(
	"EMAIL", "PASSWORD", "NAME", "EXC_NAME", "EXC_DOB")
	VALUES ('{}', '{}', '{}', '{}', '{}') RETURNING "ID" ;""".format(email,password,name, excname, excdob)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        #excid = cursor.fetchone()
        connection.commit()
        id = int(id[0])
        #excid = int(id[0])
        flag=True
    except Exception as err:
        if (err.pgcode == "23505"):
            print("this email is already in use")
            id=-1
            #excid = -1
            flag=False
    finally:
        cursor.close()
        connection.close()
    verification = False
    return (flag,id, verification)
def is_verified_company(v):
    #admin companyyi verified etmeli
    v = True
    return v

def company_login(email,pw, verification ):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """SELECT "ID" FROM public."COMPANIES" where "EMAIL" = '{}' and "PASSWORD"='{}';""".format(email,pw)
    cursor.execute(statement)
    result = cursor.fetchone()
    if is_verified_company(verification) == False :
        print('company not verified')
        return (False,int(result[0]))
    if result:
        return (True,int(result[0]))
    statement = """SELECT "ID" FROM public."COMPANIES" where "EMAIL" = '{}' ;""".format(email)
    if result:
        print('wrong password')
        return (False,int(result[0]))
    print("Company doesn't exist")
    return(False,-1)    
def update_company_city(company_id,city_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """UPDATE public."COMPANIES"
	SET "CITY"={}
	WHERE "ID"={} returning "ID";""".format(city_id,company_id)
    try:
        cursor.execute(statement)
        res = cursor.fetchall()
        connection.commit()
        flag = True
        try:
            id = res[0][0]
        except:
            id=student_id
            flag=False
    except Exception as err:
        if (err.pgcode == "23503"):
            print("No city with this id found")
            id=-1
            flag=False
    finally:
        cursor.close()
        connection.close()
    return (flag,id)

#job listings
def add_job_listing(company_id, description=None):
    connection = db.connect(url)
    cursor = connection.cursor()
    if description:
        statement = """INSERT INTO public."JOB_LISTINGS"("COMPANY","DESCRIPTION")
        VALUES ( '{}','{}') RETURNING "ID";""".format(company_id, description)
    else:
        statement = """INSERT INTO public."JOB_LISTINGS"("COMPANY")
        VALUES ( '{}') RETURNING "ID";""".format(company_id)
    try:
        cursor.execute(statement)
        id = cursor.fetchone()
        id = id[0]
        connection.commit()
        flag=True
    except Exception as err:
        print_psycopg2_exception(err)
        flag=False
    finally:
        cursor.close()
        connection.close()
    return (flag,id)
def update_joblisting_location(joblisting_id,city_id):
    connection = db.connect(url)
    cursor = connection.cursor()
    statement = """UPDATE public."JOB_LISTINGS"
	SET "LOCATION"={}
	WHERE "ID"={} returning "ID";""".format(city_id,joblisting_id)
    try:
        cursor.execute(statement)
        res = cursor.fetchall()
        connection.commit()
        flag = True
        try:
            id = res[0][0]
        except:
            id=student_id
            flag=False
    except Exception as err:
        if (err.pgcode == "23503"):
            print("No city with this id found")
            id=-1
            flag=False
    finally:
        cursor.close()
        connection.close()
    return (flag,id)

#applications
#direction true = job offer by company to student
#direction false = student application to company


if __name__ == "__main__":
    #print(add_university("university of paris",17) )
    #print(student_login("example@mail.com","ataka"))
    #print(update_student_city(1,2))
    #student_signup("example@mail.com","asdas","45581222")
    #print(search_university("ber"))
    #print(update_student_university(4,1))
    #print(remove_student_skill(10,12))
    #add_skill("Excel3")
    #add_student_skill(4,3)
    #print(update_student_pref(10,"fulltime"))
    #company_signup("AWS@mail.com","aws","password","dummy aws", "01/01/99")
    #print(company_login("AWS@mail.com", "password"))
    #print(company_login("yanlis@mail.com", "password"))
    #print(update_company_city(1,3))
    #add_job_listing(1, "a nice company :D")
    #print( update_joblisting_location(1,3 ))
    #print(       search_students_by_skill_ids( 7 )        )
    #print(get_user_details(4))
    create_tables()