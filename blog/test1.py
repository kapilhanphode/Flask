from flask import Flask,render_template,url_for
app=Flask(__name__)

post=[
    {
        'author':'abc',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'20 mar 2022'
    },
    {
        'author':'lmn',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'22 mar 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=post,title='home page')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)