from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "Hola mundo v.2.0."

if __name__=="__main__":
    application.run()