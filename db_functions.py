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
        print(len(res))
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

if __name__ == "__main__":
    #kk = get_all_cities()
    #print(student_login("example@mail.com","ataka"))
    #print(update_student_city(1,2))
    #student_signup("example@mail.com","asdas","45581222")
    #print(search_university("ber"))
    print(update_student_university(4,1))


