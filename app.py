
from flask import *
import sqlite3

app = Flask(__name__, static_folder='static')



@app.route('/')
def home():
  return render_template("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/faq')
def faq():
  return render_template("faq.html")

@app.route('/gallery')
def gallery():
  return render_template("gallery.html")


@app.route('/prices')
def pricing():
  return render_template("prices.html")


@app.route('/projects-1')
def projectsOne():
  return render_template("projects-1.html")


@app.route('/projects-2')
def projectsTwo():
  return render_template("projects-2.html")


@app.route('/projects-3')
def projectsThree():
  return render_template("projects-3.html")


@app.route('/service-1')
def serviceOne():
  return render_template("/service-1.html")


@app.route('/service-2')
def serviceTwo():
  return render_template("/service-2.html")


@app.route('/service-3')
def serviceThree():
  return render_template("/service-3.html")


@app.route('/team')
def team():
  return render_template("/team.html")


#form handling code
@app.route('/contacts-1', methods=["POST", "GET"])
def contactOne():
    msg = ""
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            with sqlite3.connect("dreamjourney.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Dreamjourney (name, email, address) VALUES (?, ?, ?)", (name, email, address))
                con.commit()
                msg = "Employee successfully Added"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error: " + str(e)
        finally:
            return render_template("contacts-1.html", msg=msg)

    return render_template("contacts-1.html", msg=msg)



  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)