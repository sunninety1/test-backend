from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'Sunnylego',
        'title':'Blog Post1',
        'content':'First step',
        'date_posted':'15/11/18'
    },{
        'author':'Unknown',
        'title':'Blog Post2',
        'content':'None step',
        'date_posted':'15/11/18'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/yolo")
def yolo():
    return render_template('about.html', title='About YOLO')

if __name__=='__main__':
    app.run(debug=True)