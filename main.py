# from urllib import response
from ensurepip import bootstrap
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import pymongo
from wtforms.validators import InputRequired
import json
import DBHelper

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'files'

# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Upload File")

@app.route('/')  
def message():  
      return render_template("login.html")  
   
@app.route('/signup', methods=["GET"])  
def signup():
    return render_template("signup.html")  

@app.route('/storeinfo', methods=["POST"])  
def storeinfo():
    username= request.form['username']
    password=request.form['password']
    AI =request.form.get('AI Developer')
    Deployer=request.form.get('Deployer')
    Admin=request.form.get('Admin')
    App=request.form.get('App Developer')
    roles_list=[]
    if AI is not None:
        roles_list.append("AI")
    if Deployer is not None:
        roles_list.append("Deployer")
    if Admin is not None:
        roles_list.append("Admin")
    if App is not None:
        roles_list.append("App")
    print(roles_list)
    ret_statement=DBHelper.storeData(username,password,roles_list)
    if(ret_statement=="User Already Exist"):
        return render_template("signup.html")
    return render_template("login.html")  


@app.route('/login', methods=["POST"])  
def login():
    username= request.form['username']
    password=request.form['password']
    role =request.form['role']
    check=DBHelper.checkCredentials(username,password,role)
    if(check=="Invalid Credentials" or check=="Invalid Role"):
        return render_template("login.html")  

    # print(username)
    # print(password)
    if(role=="AI"):
        return redirect("/upload")  
    if(role=="Deployer"):
        return redirect("/deployer") 
    if(role=="Admin"):
        return render_template("admin.html")  
    if(role=="App"):
        return redirect("/upload")  


# @app.route('/upload', methods=['GET',"POST"])
# def upload():




# @app.route('/upload', methods=['GET'])
# def serve_page():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data # First grab the file
#         #create a custom filename
#         cur_index = data_helper.get_last_index()
#         filename = "model_"+str(cur_index)+".zip"
#         print(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER']))
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename)) # Then save the file
    
#         # validation_val=extract_validate.validation()
#         # if(validation_val):
#         #     return "File uploaded and Authenticated successfully" 
#         # return "File is not uploaded and Auth successfully"
#         return render_template('Ai_Dashboard.html', form=form)
    # return render_template('index.html')

# @app.route('/upload', methods=["GET", "POST"])
# def upload():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data # First grab the file
#         #create a custom filename
#         cur_index = data_helper.get_last_index()
#         filename = "application_"+str(cur_index)+".zip"
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename)) # Then save the file
#         director = Director(cur_index)
#         if director.is_valid():
#             director.deploy()
#             return "Created docker file"
#         return "File is not uploaded and Auth successfully"
#     return render_template('index.html', form=form)

# @app.route('/deploy', methods=['GET'])
# def send_page():
#     return render_template("index.html")

# @app.route('/deploy', methods=['POST'])
# def deploy_app():
#     body = request.get_json()
#     print(body["app_id"])
#     print(body["sensors"])

#     # create config file
#     config, idx = "", 1
#     for sensor in body["sensors"]:
#         config += "SENSOR_{}='{}'\n".format(idx, sensor)
#         idx += 1
    
#     # send config and app id ; send this to dispatcher
#     print(config)

#     # call the deployer service(akash)
#     producer = KafkaProducer(bootstrap_servers = ["20.70.192.156:9092"], headers = [('cid','DeployerClient')])
#     producer.send("load_balancer_service_requests", json.dumps(config)) # topicname , data in serilalised mode

#     return "App deployed successfully!!"

if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
    # app.run(debug=True)