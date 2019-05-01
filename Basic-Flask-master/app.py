from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)
sample = {'name': 'A', 'email': 'aFE@SFD', 'mob-no': 'AWRGW', 'role': 'New Buyer', 'optradio': 'on', 'comment': 'AAGGA'}


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        data = request.form.to_dict()

        conn = sql.connect("data.db")
        c = conn.cursor()
        c.execute("insert into formdata(name, email, mob, role, cmnt) values(?,?,?,?,?)",
                  (data["name"], data["email"], data["mob-no"], data["role"], data["comment"]))
        conn.commit()
        conn.close()
        return render_template("display.html", d=data)
    return render_template("form.html")


if __name__ == '__main__':
    app.run()
