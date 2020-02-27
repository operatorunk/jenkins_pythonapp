from flask import Flask
import os


app = Flask(__name__)

def suma(a,b):
    return a+b



@app.route('/')
def showIP():
    res = suma(3,2)
    result = os.popen("curl http://169.254.169.254/latest/meta-data/public-ipv4").read()
    return "Deploy succeed on DEV environment iBOS project! The Host IP is:  %s" % (result)




if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
