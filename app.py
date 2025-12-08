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


@app.route('/instagram-test-instructions')
def instagram_test_instructions():
    return render_template("instagram-test-instructions.html")

@app.route("/facebook-auth-privacy-policy")
def facebook_auth_privacy_policy():
    return render_template("facebook-auth-privacy-policy.html")

@app.route("/facebook-auth-data-deletion")
def facebook_auth_data_deletion():
    return render_template("facebook-auth-data-deletion.html")


if __name__ == "__main__":
    app.run()
