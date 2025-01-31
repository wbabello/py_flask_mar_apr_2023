from flask import render_template, request, redirect, session
from flask_app import app

@app.route("/")
def login_page(): # View the login page
    return render_template("login.html")

@app.route("/companies/new")
def new_company_page(): # showing the new company page
    # Question from Wednesday - how can we check to see
    # whether a user actually filled out the form to log in?
    if "name" not in session: # If user is not logged in, send back to login
        print("Not logged in - going back to root route")
        return redirect("/")
    return render_template("add_company.html")

@app.route("/companies")
def all_companies_page(): # all companies page
    if "name" not in session: # If user is not logged in, send back to login
        print("Not logged in - going back to root route")
        return redirect("/")
    # TEMPORARY: If we're starting from the beginning, create an empty list that will 
    # hold the companies added.  We will use the database instead of session soon to do this.
    if "added_companies" not in session:
        session["added_companies"] = []
    print(session)
    print("Now in companies route")
    # print(request.form) # Form data is now gone from logging in!
    return render_template("all_companies.html")

@app.route("/login", methods=["POST"])
def login_user(): # Logging in a user
    print(session) # Show empty session
    # print(request.form)
    session["name"] = request.form["your_name"] # Save user in session (temporary log-in)
    print(session)
    return redirect("/companies")

@app.route("/logout")
def logout_user(): # Logging out a user
    session.pop("name") # Remove only the name (user) from session
    # session.clear() # Remove all key-value pairs from session
    return redirect("/") # Send back to login route

@app.route("/companies/add", methods=["POST"])
def add_company(): # Adding a company
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    # TEMPORARY: Save user data into a dictionary to simulate what it'll look like from database
    form_results = {
        "name": request.form["name"],
        "slogan": request.form["slogan"],
        "location": request.form["location"],
        "over_one_billion": request.form["over_one_billion"],
    }
    session.modified = True # To allow the list to change
    session["added_companies"].append(form_results) # Add dictionary to list
    return redirect("/companies")
