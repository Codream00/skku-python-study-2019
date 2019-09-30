'''
Using form tag
'''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    '''
    '/'로 접속했을 때의 화면입니다.
    '''
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def index2():
    '''
    /result로 접속했을 때 입니다.
    '''
    if request.method == 'POST':
        result = request.form
        return render_template("index2.html", result=result)

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
