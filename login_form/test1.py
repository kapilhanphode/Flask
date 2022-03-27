from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['userName']
        passWord=request.form['userPassWord']
        if user=='abc' and passWord=='12345':
            return render_template('loginsuccess.html')
        else:
            return render_template('loginfail.html')
    else:
        user = request.args.get('userName')
        passWord = request.args.get('userPassWord')
        if user == 'abc' and passWord == '12345':
            return render_template('loginsuccess.html')
        else:
            return render_template('loginfail.html')
if (__name__)=='__main__':
    app.run(debug=True)