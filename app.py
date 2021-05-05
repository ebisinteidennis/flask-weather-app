from flask import Flask, render_template, request
import req
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html",code = 0, weather = "Type city name and press search", country = "")

@app.route("/", methods=["POST"])
def search():
    City = request.form.get("city")
    code,weather,country = req.weather(City)
    print(weather)
    return render_template("index.html", code = code, weather = weather, country = country)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

