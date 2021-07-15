from flask import Flask
from flask import render_template 
from flask import request, redirect, url_for

users={"mugasa": "qwerty"}
userData=[]
userTasks=[['mugasa','UOC','4b','repairs',2,'done'],['mugasa', 'internet','3a','mtn', 'survey',5,'pending'],['bobby','carpenter','2g','deliver chairs',3,'pending']]
session_var=[]
app = Flask(__name__, template_folder="UI")
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home", methods =["GET", "POST"])
def login():
    if request.method == "POST":
        UserName= request.form["user_name"]
        Password = request.form["pwd"]
        if users[UserName]== Password:
            print ("Welcome" + " " + UserName + "to your bucket list")
            session_var.append(UserName)
            return redirect(url_for('dashboard'))
            #Flask will redirect to the dashborard page where the script will display tasks sorted with the username as a key
        else:
            #Flask will reload the login page
            return redirect(url_for('index'))
    return render_template('home.html')        
    

@app.route("/registration", methods= ["GET","POST"])
def newUser():
    if request.method == "POST":
        mailAddress= request.form["email"]
        Names=request.form["user_name"]
        Password= request.form["pwd"]
        PasswordCheck= request.form["pwdCheck"]
        if Password==PasswordCheck:
            users[Names]=Password
            userData.append([Names,Password,mailAddress])
            #Flask will then redirect to the login page
            return redirect(url_for('login'))
        else:
            return "<p>Please enter matching password</p>"
    return render_template('registration.html')
    



@app.route("/dashboard", methods= ["GET","POST"])
def dashboard():
    if request.method == "GET":
        welcome_statement= str("welcome to your bucketlist"+ " " + session_var[0])
        myTasks=[]
        for i in userTasks:
            if i[0] == session_var[0]:
                myTasks.append(i)
        
                

        
    
    return render_template('dashboard.html', dataToRender= welcome_statement, tasksToRender= myTasks, len = len(myTasks))



@app.route("/newtask", methods=["GET", "POST"])
def newTask():
    if request.method == "POST":
        nameOfTask= request.form["task_name"]
        Ref=request.form["taskRef"]
        description=request.form["descriptions"]
        duration=request.form["eta"]
        status=request.form["taskStatus"]
        userTasks.append([session_var[0],nameOfTask, Ref, description, duration, status])
        return redirect(url_for('dashboard'))

    return render_template('newTask.html')

@app.route("/delete", methods=["GET","POST"])
def deleteTask():
    if request.method == "POST":
        for j in userTasks:
            if j[2]== request.form["ref"]:
                userTasks.remove(j)
        return redirect(url_for('dashboard'))
    return render_template('delete.html')


    
