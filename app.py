from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/user/<name>")
def greet(name):
    return f"<p> Hello, { name }! </p>"


@app.route("/")

def homeInfo():
    title = "My Personal Site"
    details = readDetails('static/Summarytitle.txt')
    name = "Victor Contreras"
    ## aboutMe = ["Hi, my name is Victor and I'm a Computer Science student at UTRGV.", "I'm passionate about Coding and learning about Technology, whether it's Frontend, Backend, or Full Stack."]
    return render_template("base.html", name=name, aboutMe=details)


#function to read detail in a page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route("/Goals")
def goals():
    my_goals = ['Learn more languages like Rust, mySQL, Java and Frameworks like Node.js', 'Try to obtain an internship', 'Practice Coding', 'Network with professors and classmates']
    return render_template('Goals.html', Goals=my_goals)

@app.route("/Projects")
def projects():
    return "<h1> None Yet! Maybe this one could be the first... </h1>"

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        if request.form['name']:
           name = request.form['name']
        #if request.form['message']:
            #writeToFile('/static/comments.txt', request.form['message'])
    return render_template('form.html', name=name)




## When running this file directly...
if __name__ == "__main__":
    app.run(debug=True)