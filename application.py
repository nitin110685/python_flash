from flask import Flask
from flask import render_template,request,redirect,url_for
from flask import session
import mysql.connector as connector

application=Flask(__name__)
application.secret_key= "abc"

connection= connector.connect(host="localhost",user="root",password="",database="tr_motors")

@application.route('/sign')
def sign():
	return render_template("sign.html")

@application.route('/sign1', methods=['POST'])
def sign1():
	Fname = request.form.get('Fname')
	Lname = request.form.get('Lname')
	Mobile = request.form.get('mobile')
	Email = request.form.get('email')
	Password = request.form.get('password')
	sql= "INSERT INTO sign(Firstname,Lastname,mobile,email,password)values('{}','{}','{}','{}','{}')".format(Fname,Lname,Mobile,Email,Password)
	cursor=connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	return redirect(url_for('login'))



@application.route('/login')
def login():
	return render_template("login.html")

@application.route('/login1', methods=['POST'])
def login1():
	Email = request.form.get('email')
	Password = request.form.get('password')
	sql="SELECT Firstname,Lastname,email,password from sign where Email='{}' and password='{}'".format(Email,Password)
	cursor=connection.cursor()
	cursor.execute(sql)
	result=cursor.fetchone()
	if(result!=None):
		session['response'] = True
		session['fname'] = result[0]
		session['lname'] = result[1]
		return redirect(url_for('Home'))
	else:
		return redirect(url_for('sign'))

@application.route('/enquiry', methods=['POST'])
def enquiry():
	Fname = request.form.get('Fname')
	Lname = request.form.get('Lname')
	mobile = request.form.get('mobile')
	email = request.form.get('email')
	sql= "INSERT INTO enquiry(Fname,Lname,mobile,email)values('{}','{}','{}','{}')".format(Fname,Lname,mobile,email)
	cursor=connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	return render_template('Home.html')

# @app.route('/course')
# def course():
# 	sql="SELECT * from course"
# 	cursor=connection.cursor()
# 	cursor.execute(sql)
# 	result=cursor.fetchall()
# 	print(result)
# 	cursor.close()
# 	return render_template('schedule.html',studlist=result)


@application.route('/Home')
def Home():
	if 'response' in session:
		return render_template("Home.html")
	else:
		return redirect(url_for('login'))

@application.route('/')
def Home():
	if 'response' in session:
		return render_template("Home.html")
	else:
		return redirect(url_for('login'))

# @app.route('/Home')
# def home():
# 	return "You are on User Home Page(Front End)"

# @app.route('/admin/Home')
# def adminhome():
# 	return "You are on Admin Home Page(Back End)"
	

@application.route('/About')
def About():
	if 'response' in session:
		return render_template("About.html")
	else:
		return redirect(url_for('login'))


@application.route('/Courses')
def Courses():
	if 'response' in session:
		return render_template("Courses.html")
	else:
		return redirect(url_for('login'))


@application.route('/Testimonials')
def Testimonials():
	if 'response' in session:
		return render_template("Testimonials.html")
	else:
		return redirect(url_for('login'))

@application.route('/Schedule')
def Schedule():
	if 'response' in session:
		sql="SELECT cid,cname,days,fees,kilometer,gender from course"
		cursor=connection.cursor()
		cursor.execute(sql)
		result=cursor.fetchall()
		print(result)
		cursor.close()
		return render_template("Schedule.html",courselist1=result)
	else:
		return redirect(url_for('login'))
	



@application.route('/Contact')
def Contact():
	if 'response' in session:
		return render_template("Contact.html")
	else:
		return redirect(url_for('login'))


@application.route('/Blog')
def Blog():
	if 'response' in session:
		return render_template("Blog.html")
	else:
		return redirect(url_for('login'))

@application.route('/Services')
def Services():
	if 'response' in session:
		return render_template("Services.html")
	else:
		return redirect(url_for('login'))

@application.route('/Road')
def Road():
	if 'response' in session:
		return render_template("Road.html")
	else:
		return redirect(url_for('login'))

@application.route('/Feedback')
def Feedback():
	if 'response' in session:
		return render_template("Feedback.html")
	else:
		return redirect(url_for('login'))

@application.route('/Term')
def Term():
	if 'response' in session:
		return render_template("Term.html")
	else:
		return redirect(url_for('login'))

@application.route('/userfield', methods=['POST'])
def userfield():
	Courseid = request.form.get('cid')   #pass name
	Coursename = request.form.get('cname')
	Fullname = request.form.get('fullname')
	Mobile = request.form.get('mobile')
	Age = request.form.get('age')
	Email = request.form.get('email')
	Address = request.form.get('add')
	StartDate=request.form.get('startd')
	EndDate = request.form.get('endd')


	sql = "INSERT INTO userdata(cid,cname,fullname,mobile,age,email,address,start_date,end_date)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Courseid,Coursename,Fullname,Mobile,Age,Email,Address,StartDate,EndDate)
	print(sql)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	return redirect(url_for('Schedule'))

@application.route('/Licence')
def Licence():
	if 'response' in session:
		return render_template("Licence.html")
	else:
		return redirect(url_for('login'))

@application.route('/Extra')
def Extra():
	if 'response' in session:
		return render_template("Extra.html")
	else:
		return redirect(url_for('login'))


# Front end end

#Back end Start

@application.route('/admin/login')
def admin_login():
	return render_template("admin_login.html")

@application.route('/adminlogin1', methods=['POST'])
def adminlogin1():
	Email = request.form.get('email')
	Password = request.form.get('password')
	sql="SELECT email,password from adminlogin where email='{}' and password='{}'".format(Email,Password)
	cursor=connection.cursor()
	cursor.execute(sql)
	result=cursor.fetchone()
	if(result!=None):
		session['response'] = True
		return redirect(url_for('index'))
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/404')
def admin_404():
	if 'response' in session:
		return render_template("404.html")
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/blank')
def admin_blank():
	if 'response' in session:
		return render_template("blank.html")
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/index')
def admin_index():
	if 'response' in session:
		return render_template("admin_index.html")
	else:
		return redirect(url_for('admin_login'))

# @app.route('/admin/login')
# def admin_login():
# 	if 'response' in session:
# 		return render_template("admin_login.html")
# 	else:
# 		return redirect(url_for('login'))

@application.route('/admin/register')
def admin_register():
	if 'response' in session:
		return render_template("register.html")
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/forgot')
def admin_forgot():
	if 'response' in session:
		return render_template("forgot.html")
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/student')
def admin_student():
	if 'response' in session:
		sql="SELECT cid,cname,fullname,mobile,age,email,address,start_date,end_date from userdata"
		cursor=connection.cursor()
		cursor.execute(sql)
		result=cursor.fetchall()
		print(result)
		cursor.close()
	if 'response' in session:
		return render_template("student.html" ,studentlist=result)
	else:
		return redirect(url_for('admin_login'))

@application.route('/studentselect', methods=['POST'])
def studentselect():
	if 'response' in session:
		sql="SELECT * from userdata"
		cursor=connection.cursor()
		cursor.execute(sql)
		result=cursor.fetchall()
		cursor.close()
	if 'response' in session:
		return render_template("student.html")
	else:
		return redirect(url_for('admin_login'))

@application.route('/studentupdate', methods=['POST'])
def studentupdate():
	Courseid = request.form.get('cid1')
	Coursename = request.form.get('cname1')
	Fullname = request.form.get('fullname1')
	Mobile = request.form.get('mobile1')
	Age = request.form.get('age1')
	Email = request.form.get('email1')
	Address = request.form.get('add1')
	Startdate = request.form.get('startd1')
	Enddate = request.form.get('endd1')
	
	sql = "UPDATE userdata set cname='{}',fullname='{}',mobile='{}',age='{}',email='{}',address='{}',start_date='{}',end_date='{}' where cid='{}' ".format(Coursename,Fullname,Mobile,Age,Email,Address,Startdate,Enddate,Courseid)
	cursor=connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	return redirect(url_for('admin_student'))

@application.route('/studentdelete', methods=['POST'])
def studentdelete():
	Courseid = request.form.get('cid2')

	sql = "DELETE FROM userdata where cid='{}'".format(Courseid)
	print(sql)
	cursor=connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	return redirect(url_for('admin_student'))

@application.route('/admin/course')
def admin_course():
	if 'response' in session:
		sql="SELECT * from course"
		cursor=connection.cursor()
		cursor.execute(sql)
		result=cursor.fetchall()
		print(result)
		cursor.close()
	if 'response' in session:
		return render_template("course.html" ,courselist=result)

@application.route('/courseupdate', methods=['POST'])
def courseupdate():
	Courseid = request.form.get('cid')
	Coursename = request.form.get('cname')
	Days = request.form.get('days')
	Fees = request.form.get('fees')
	Kilometer = request.form.get('kilometer')
	Gender = request.form.get('gender')
	
	sql = "UPDATE course set cname='{}',days='{}',fees='{}',kilometer='{}',gender='{}' where cid='{}' ".format(Coursename,Days,Fees,Kilometer,Gender,Courseid)
	cursor=connection.cursor()
	cursor.execute(sql)
	connection.commit()

	cursor.close()
	return redirect(url_for('admin_course'))



@application.route('/courseinsert', methods=['POST'])
def courseinsert():
	Courseid = request.form.get('cid') #.get(modal-name)
	Coursename = request.form.get('cname')
	Days = request.form.get('days')
	Fees = request.form.get('fees')
	Kilometer = request.form.get('kilometer')
	Gender = request.form.get('gender')

	sql = "INSERT INTO course(cid,cname,days,fees,kilometer,gender)VALUES('{}','{}','{}','{}','{}','{}');".format(Courseid,Coursename,Days,Fees,Kilometer,Gender)
	print(sql)
	cursor = connection.cursor()
	cursor.execute(sql)
	print(sql)
	connection.commit()
	return redirect(url_for('admin_course'))


@application.route('/coursedelete', methods=['POST'])
def coursedelete():
	Courseid = request.form.get('cid1')

	sql = "DELETE FROM course where cid='{}'".format(Courseid)
	print(sql)
	cursor=connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	return redirect(url_for('admin_course'))





@application.route('/admin/enquiry')
def admin_enquiry():
	if 'response' in session:
		sql="SELECT * from enquiry"
		cursor=connection.cursor()
		cursor.execute(sql)
		result=cursor.fetchall()
		print(result)
		cursor.close()
	if 'response' in session:
		return render_template("enquiry.html" ,enquirylist=result)
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/scheduled')
def admin_scheduled():
	if 'response' in session:
		sql="SELECT fullname,mobile,cname,start_date,end_date from userdata"
		cursor=connection.cursor()
		cursor.execute(sql)
		result=cursor.fetchall()
		print(result)
		cursor.close()
	if 'response' in session:
		return render_template("scheduled.html" ,schedulelist=result)
	else:
		return redirect(url_for('admin_login'))

@application.route('/admin/fees')
def admin_fees():
	if 'response' in session:
		return render_template("fees.html")
	else:
		return redirect(url_for('admin_login'))








if __name__=='__main__':
	application.run(host='0.0.0.0',debug=True)
