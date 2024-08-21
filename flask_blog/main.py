from flask import Flask, render_template, url_for

app = Flask(__name__) # __name__ is a special variable name of the module

posts = [
    {
        'title': 'Post 1',
        'content': 'This is the first post',
        'author': 'John Doe',
        'date_posted': 'April 1, 2016',
    },
    {
        'title': 'Post 2',
        'content': 'This is the second post',
        'author': 'jackson Doe',
        'date_posted': 'April 1, 2016',
    },
        
]


@app.route("/") # decorators add extra functionality to an existing function
@app.route("/home")
def home_page():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About Us')


# run directy from the file 
if __name__ == '__main__':
    app.run(debug=True)