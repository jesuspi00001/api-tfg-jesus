from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "Flask application va bien."

if __name__=="__main__":
    application.run()