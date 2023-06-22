import os

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
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username")
        elif not request.form.get("password"):
            return apology("must provide password")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password must match")

        hash = generate_password_hash(request.form.get("password"))
        new_user_id = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)

        if not new_user_id:
            return apology("username already exists")

        session["user_id"] = new_user_id
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute
    ("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
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
          db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], quote["symbol"], shares, quote["price"])

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
    # ... your existing quote function code here ...


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""


if __name__ == "__main__":
    app.run(debug=True)


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

        # Lookup stock information
        quote = lookup(request.form.get("symbol"))

        # Ensure symbol is valid
        if quote is None:
            return apology("invalid symbol")

        # Query database for user's shares of the stock
        user_shares = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ?",
                                 session["user_id"], quote["symbol"])

        # Ensure user has enough shares to sell
        if not user_shares or user_shares[0]["total_shares"] < shares:
            return apology("not enough shares")

        # Update user's cash
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", shares * quote["price"], session["user_id"])

        # Insert sell transaction into database (negative shares)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], quote["symbol"], -shares, quote["price"])

        # Redirect to home page
        return redirect("/")

    # User reached route via GET
    else:
        # Query database for user's stocks
        stocks = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = ?", session["user_id"])

        return render_template("sell.html", stocks=stocks)