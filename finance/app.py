import os
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
log.addHandler(file_handler)

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route cia POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password must match", 400)

        # Query databse for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        #Ensure username does not already exist
        if len(rows) != 0:
            return apology("username already exists", 400)

        # Insert new user into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Query database for newly inserted user
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        #Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # user reached route via GET
    else:
        return render_template("register.html")

    # Create the transcation table if it doesn't exist
    db.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            symbol TEXT,
            shares INTEGER,
            price NUMERIC,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user (id)
        )
    """)

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
    total_value = 0

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["total"] = stock["total_shares"] * quote["price"]
        total_value += stock["total"]

    return render_template("index.html", stocks=stocks, total_value=total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Show portfolio of stocks"""

    # User reached route via POST
    if request.method == "POST":

          # Ensure symbol was submitted
          if not request.form.get("symbol"):
              return apology("must provide symbol")

          # Ensure shares was submitted
          elif not request.form.get("shares"):
              return apology("must provide number of shares")

          # Ensure shares is a positive integer
          try:
              shares = int(request.form.get("shares"))
              if shares < 1:
                  return apology("shares must be a positive integer")
          except ValueError:
              return apology("shares must be a positive integer")

          # Query database for user's cash
          rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
          cash = rows[0]["cash"]

          # Lookup stock information
          quote = lookup(request.form.get("symbol"))

          # Ensure symbol is valid
          if quote is None:
              return apology("invalid symbol")

          # Calculate total purchase value
          total_value = shares * quote["price"]

          # Ensure user has enough cash
          if total_value > cash:
              return apology("not enough cash")

          # Update user's cash
          db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_value, session["user_id"])

          # Insert transaction into database
          db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], quote["symbol"], shares, quote["price"])

          # Redirect to home page
          return redirect("/")

    # User reached route via GET
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Query the database for the user's transactions
    transactions = db.execute("SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ?", session["user_id"])

    # Render the template for the history
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

       # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Lookup stock information
        quote = lookup(request.form.get("symbol"))

        # Ensure symbol is valid
        if quote is None:
            return apology("invalid symbol")

        # Display stock information
        return render_template("quoted.html", quote=quote)

    # User reached route via GET
    else:
        return render_template("quote.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST
    if request.method == "POST":

        # Ensure symbol was submitted
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must select a symbol", 400)

        # Ensure shares was submitted
        try:
            shares = int(request.form.get("shares"))
            if shares < 1:
                return apology("shares must be positive integer", 400)
        except ValueError:
            return apology("shares must be a positive integer", 400)

        # Query database for user's shares of the stock
        stock = db.execute("""
            SELECT SUM(shares) as total_shares
            FROM transactions
            WHERE user_id = ? AND symbol = ?
            GROUP by symbol
        """, session["user_id"], symbol)

        # Ensure user has enough shares to sell
        if not stock or stock[0]["total_shares"] < shares:
            return apology("not enough shares", 400)

        # Get current price of the stock
        stock_info = lookup(symbol)
        if not stock_info:
            return apology("invalid symbol", 400)

        # Update user's cash
        db.execute("""
            UPDATE users
            SET cash = cash + ?
            WHERE id = ?
        """, stock_info["price"] * shares, session["user_id"])

        # Insert sell transaction into database
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (?, ?, ?, ?)
        """, session["user_id"], symbol, -shares, stock_info["price"])

        # Redirect to index page
        return redirect("/")

    # User reached route via GET
    else:
        # Query database for user's stocks
       symbols = db.execute("""
            SELECT DISTINCT symbol
            FROM transactions
            WHERE user_id = ?
        """, session["user_id"])

       return render_template("sell.html", symbols=[stock["symbol"] for stock in symbols])

if __name__ == "__main__":
    app.debug = True
    app.run()