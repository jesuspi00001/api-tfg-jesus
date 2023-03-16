from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "<h1>Hola mundo </h1> v.2.0."

if __name__=="__main__":
    application.run()