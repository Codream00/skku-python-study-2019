'''
Hello wolrd
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    '''
    '/'로 접속했을 때의 화면입니다.
    '''
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
