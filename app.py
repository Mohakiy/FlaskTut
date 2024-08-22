from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {
        "id": "1",
        "title": "Data Analyst",
        "location": "Addis Ababa, Ethiopia",
        "salary": "1,000,000 Br"
    },
    {
        "id": "2",
        "title": "Data Scientist",
        "location": "Jimma, Ethiopia",
        "salary": "1,050,000 Br"
    },
    {
        "id": "3",
        "title": "Frontend Engineer",
        "location": "Jeddah, KSA",
        "salary": "2,000,000 SR"
    },
    {
        "id": "4",
        "title": "Backend Engineer",
        "location": "New York, USA",
        "salary": "500,000 USD"
    },
]

@app.route('/')
def hello():
    return render_template("home.html",
                          jobs = Jobs,
                          company_name = "Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)