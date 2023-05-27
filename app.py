from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")

def homeInfo():
    details = readDetails('static/Summarytitle.txt')
    name = "Victor Contreras"
    return render_template("base.html", name=name, aboutMe=details)


#function to read detail in a page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route("/Wordle")
def project0():
    return render_template("wordle.html")

@app.route("/DiscordMessageBot")
def project1():
    return render_template("MessageBot.html")

@app.route("/CPPMusicPlaylist")
def project2():
    return render_template("CPPMusic.html")
    

## When running this file directly...
if __name__ == "__main__":
    app.run(debug=True)