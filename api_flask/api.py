from flask import Flask

@app.route("/")
def hello():
    return "Hello World"

if __name__ == 'main':
    app.run(debug=True)
