from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # list dictionary of users 
    users = [
        {"first_name": "Michael", "last_name": "Choi"},
        {"first_name": "John", "last_name": "Supsupin"},
        {"first_name": "Mark", "last_name": "Guillen"},
        {"first_name": "KB", "last_name": "Tonel"},
    ]
    # assigning users to participants to proceed with for-loop and iterate the list length in table
    return render_template("table.html", participants=users)

if __name__ == "__main__":
    app.run(debug=True)
