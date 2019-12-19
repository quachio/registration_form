from flask import Flask, render_template, redirect, session, request, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = '7VL9f(u]ksirecbW4YMfBmAt37Tb@7MfEk;)i(eeaJMXqi2M2,nD+ya+aD&6gz3P'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)