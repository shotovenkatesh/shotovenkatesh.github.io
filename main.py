import sys

from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
import logging



app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
PASS = os.environ.get("PASSWORD")



@app.route("/")
def home():
    # if request.method == "POST":
    #     name = request.form["name"]
    #     mail = request.form["email"]
    #     message = request.form["message"]

        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=FROM_EMAIL,
        #                      password=PASS)
        #     connection.sendmail(from_addr=FROM_EMAIL,
        #                         to_addrs=TO_EMAIL,
        #                         msg=f"Subject:A message from your portfolio website \n\n. Hi my name is{name}.{message}. This is my email id: {mail}")
        # return render_template("index.html",sent = True)
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)
