from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'])
def sign_up():
    
    username=request.form['username']
    username_escaped = cgi.escape(username, quote=True)
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']
    username_error=""
    password_error=""
    verify_error=""
    email_error=""
    # If the user's form submission is not valid, you should reject it and 
    # re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:
        # The user leaves any of the following fields empty: 
            # username, password, verify password.
    if username == "" or " " in username or len(username) not in range(3,21):
        username_error='that is not a valid user-name'
    
    if password == "" or " " in password or len(password) not in range(3,21):
        password_error='that is not a valid password'

        # The user's username or password is not valid 
            # -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
        # The user's password and password-confirmation do not match.
    if password != verify:
            verify_error='password does not match verification'
        # The user provides an email, but it's not a valid email. 
            # Note: the email field may be left empty, 
            # but if there is content in it, then it must be validated. 
            # The criteria for a valid email address in this assignment are
                #  that it has a single @, a single ., 
                # contains no spaces, 
                # and is between 3 and 20 characters long.

    if email != "":
        period_count = 0
        amper_count = 0
        for char in email:
            if char == ".":
                period_count = period_count + 1
            if char == "@":
                amper_count = amper_count + 1
        if amper_count != 1 or period_count != 1:
            email_error = "that is not a valid email address"

    # Each feedback message should be next to the field that it refers to.
    if username_error != "" or password_error != "" or verify_error != "" or email_error != "":
        return render_template('index.html', 
            username_error=username_error, 
            password_error=password_error, 
            verify_error=verify_error, 
            email_error=email_error,
            email=email,
            username=username)
    # For the username and email fields, you should preserve what the user typed, 
        # so they don't have to retype it. With the password fields, 
        # you should clear them, for security reasons.

    # If all the input is valid, then you should show the user a welcome page 
        # that uses the username input to display a welcome message of: 
        # "Welcome, [username]!"
    # Use templates (one for the index/home page and one for the welcome page) 
    # to render the HTML for your web app.
    return render_template('welcome.html', username_escaped=username_escaped)
   
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html')

app.run()
