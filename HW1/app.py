from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="김지언", student_id="24012016")

if __name__ == "__main__":
    app.run(debug=True)
