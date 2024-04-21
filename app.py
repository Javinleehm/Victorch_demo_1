from flask import Flask, render_template, request, jsonify #import only the necessary parts 
import random
import string
app = Flask(__name__) #get a flask object called "app". This will be backend server

@app.route("/", methods=["GET", "POST"]) #The function below this line is executed every time someone visit "/" and the methods must be either a GET request and a POST request.
def index():
    if request.method == "POST": # If the request is POST, it must be the user submitting a form. In which case, read the data in the form and process them.
        # Process Form 1
        if "text1_1" in request.form:
            # request.form is a dictionary, which is sent through the Internet as a json format.
            print("Form 1 Data:")
            print("Text 1:", request.form["text1_1"])
            print("Text 2:", request.form["text1_2"])
            print("File 1:", request.files["file1"])
            print("Radio 1:", request.form["radio1"])
            print("Radio 2:", request.form["radio2"])

        # Process Form 2
        if "text2_1" in request.form:
            print("Form 2 Data:")
            print("Text 1:", request.form["text2_1"])
            print("Text 2:", request.form["text2_2"])
            print("File 2:", request.files["file2"])
            print("Radio 3:", request.form["radio3"])
            print("Radio 4:", request.form["radio4"])

    return render_template("index.html") #If the request is a GET request, someone is trying to visit the page. Therefore, return the index.html.


@app.route("/request_text", methods=["POST"]) # Here is another route to demonstrate how a client communcates with the server. When a client sends a POST request to /request_text, it does the following
def getText():
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) # For now, I just generate a random string
    print(random_str)
    return jsonify({"showText": random_str}) # Send the string as a json format

if __name__ == "__main__": #If the file is directly executed (In production servers, it will not be directly executed but instead hosted by a WSGI web server)
    app.run(debug=True, # Debug mode is activated so each time an edit of this file is detected, flask experimental server will restart and update
            host="127.0.0.1", # The URL is set to 127.0.0.1 right now, which is localhost
            port=5000) # Port 5000 is currently selected. Change it to whatever you want.
    