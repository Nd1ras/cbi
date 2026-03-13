from flask import Flask, redirect, render_template, request

app = Flask(__name__)

appointments = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    service = request.form["service"]
    date = request.form["date"]
    time = request.form["time"]

    appointments.append({"name": name, "service": service, "date": date, "time": time})

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
