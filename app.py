from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# Database model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    service = db.Column(db.String(50))
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():

    name = request.form["name"]
    phone = request.form["phone"]
    service = request.form["service"]
    date = request.form["date"]
    time = request.form["time"]

    new_appointment = Appointment(
        name=name, phone=phone, service=service, date=date, time=time
    )

    db.session.add(new_appointment)
    db.session.commit()

    return redirect("/")


@app.route("/dashboard")
def dashboard():

    appointments = Appointment.query.all()

    return render_template("dboard.html", appointments=appointments)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
