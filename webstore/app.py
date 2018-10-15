from flask import Flask, flash, redirect, render_template, request, session, abort
from webstore.endpoints import home, cart, purchase_history


app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return home.home(req)

@app.route("/cart")
def cart():
    return cart.cart(req)

@app.route("/purchase_history")
def purchase_history():
    return purchase_history.purchase_history(req)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
