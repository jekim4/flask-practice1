from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="김지언", student_id="24012016")

@app.route("/profile")
def profile():
    hobbies = ["독서", "영화 감상", "코딩"]
    return render_template("profile.html", hobbies=hobbies)

if __name__ == "__main__":
    app.run(debug=True)
