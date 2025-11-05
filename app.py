from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("main_page.html")


@app.route('/privacy')
def privacy():
    return render_template("privacy_policy.html")


@app.route('/data-deletion')
def data_deletion():
    return render_template("data_deletion.html")


if __name__ == "__main__":
    app.run()
