from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "Hola mundo."

if __name__=="__main__":
    application.run()