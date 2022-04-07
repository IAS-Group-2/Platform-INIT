# from urllib import response
from ensurepip import bootstrap
from flask import Flask, render_template, request, redirect,session
from werkzeug.utils import secure_filename
import os
from utils.DBHelper import DBHelper
from flask_session import Session
from utils.UploadHelper import get_new_index
import config.config as config

from app_manager.AppDirector import AppDirector
from models.Application import App as application
from storage_manager import config as storage_config

from service_manager.ServiceDirector import Director as ServiceDirector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'files'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = DBHelper()

# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Upload File")

@app.errorhandler(404)
def page_not_found(error):
   return render_template('home/page-404.html', title = '404'), 404
   
@app.errorhandler(400)
def page_not_found(error):
   return render_template('home/page-400.html', title = '400',error=error), 400

@app.errorhandler(500)
def page_not_found(error):
   return render_template('home/page-500.html', title = '500'), 500

@app.route('/')  
def message():  
      return render_template("home/login.html",segment='index')  
   
@app.route('/signup', methods=["GET"])  
def signup():
    return render_template("home/register.html")  

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
    ret_statement=db.storeData(username,password,roles_list)
    if(ret_statement=="User Already Exist"):
        return render_template("signup.html")
    return render_template("home/login.html",segment='login')  



@app.route('/appdev', methods=["GET","POST"])  
def appdev():
    #check for session
    if 'username' in session:
        username=session.get('username')
        #get all the application of the user
        apps=db.getAppByOwner(username)
        return render_template("home/appdev.html",username=username,apps=apps)
    else:
        return render_template("home/login.html",segment='login')



@app.route('/aidev', methods=["GET","POST"])  
def aidev():
    #check for session
    if 'username' in session:
        username=session.get('username')
        return render_template("home/aidev.html",username=username)
    else:
        return render_template("home/login.html",segment='login')

@app.route('/registerApp', methods=["GET","POST"])  
def registerApp():
    #check for session
    if 'username' in session:
        username=session.get('username')
        return render_template("home/register_app.html",username=username)
    else:
        return render_template("home/login.html",segment='login')

@app.route('/registerService', methods=["GET","POST"])  
def registerService():
    #check for session
    if 'username' in session:
        username=session.get('username')
        return render_template("home/register_service.html",username=username)
    else:
        return render_template("home/login.html",segment='login')

@app.route('/uploadApp', methods=["POST"])  
def uploadApp():
    #check for session
    if 'username' in session:
        username=session.get('username')
        if request.method == 'POST':
            app_name=request.form['app_name']
            app_description=request.form['app_discription']
            f = request.files['file']
            cur_index = get_new_index(config.TYPE_SERVICE)
            filename = "application_"+str(cur_index)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)),config.UPLOAD_FOLDER, filename+".zip")
            f.save(path)

            #pushing to db and storage
            app = application(app_name,app_description,'Uploaded',username,cur_index,storage_config.STORAGE_VM_ADDRESS+"/"+filename+".zip")
            app_director = AppDirector(app,path)
            app_director.sync_db()
            app_director.push_app()

        return redirect("/appdev")

    else:
        return redirect("/") 

@app.route('/uploadModel', methods=["POST"])  
def uploadModel():
    #check for session
    if 'username' in session:
        username=session.get('username')
        if request.method == 'POST':
            app_name=request.form['service_name']
            app_description=request.form['service_discription']
            f = request.files['file']
            cur_index = get_new_index(config.TYPE_SERVICE)
            filename = "service_"+str(cur_index)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)),config.UPLOAD_FOLDER, filename+".zip")
            f.save(path)
            
            director = ServiceDirector(cur_index)
            if director.is_valid():
                director.upload()
                
        return redirect("/aidev")

    else:
        return redirect("/") 


#App Deployer
@app.route('/appdeployer', methods=["GET","POST"])  
def appdeployer():
    #check for session
    if 'username' in session:
        username=session.get('username')
        apps=db.getApplications()
        return render_template("home/appdeployer.html",username=username,apps=apps)
    else:
        return render_template("home/login.html",segment='login')
















@app.route('/login', methods=["POST"])  
def login():
    username= request.form['username']
    password=request.form['password']
    role =request.form['role']
    check=db.checkCredentials(username,password,role)
    if(check=="Invalid Credentials" or check=="Invalid Role"):
        return render_template("home/login.html")  
    session['username']=username
    if(role=="AI"):
        return redirect("/aidev")  
    if(role=="Deployer"):
        return redirect("/appdeployer") 
    if(role=="Admin"):
        return render_template("admin.html")  
    if(role=="App"):
        return redirect("/appdev")


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