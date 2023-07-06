import os
import locale
import decimal

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

    # User reached route via POST
    if request.method == "POST":

        # Validate form input
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username", 400)
        if not password:
            return apology("must provide password", 400)
        if not confirmation:
            return apology("must confirm password", 400)
        if password != confirmation:
            return apology("passwords must match", 400)

        # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if rows:
            return apology("username already exists", 400)

        # Insert new user into database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        # Redirect user to login page
        flash("Registered successfully! Please log in.")
        return redirect("/login")

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get user's stocks and shares
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
                        user_id=session["user_id"])

    # Get user's cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])[0]["cash"]

    # Initialize variables for total values
    total_value = cash
    grand_total = cash

    # Iterate over stocks and add price and total value
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["total_value"] = stock["price"] * stock["total_shares"]
        total_value += stock["total_value"]
        grand_total += stock["total_value"]

    return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Ensure the symbol was submitted
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 400)

        # Ensure the shares were submitted
        shares = request.form.get("shares")
        if not shares.isdigit() or int(shares) < 1:
            return apology("shares must be a positive integer", 400)
        shares = int(shares)

        # Lookup the stock symbol
        stock_info = lookup(symbol)
        if stock_info is None:
            return apology("invalid symbol", 400)

        # Calculate the total purchase cost
        stock_price = stock_info["price"]
        print("Stock Price:", stock_price)
        total_cost = float(shares) * float(stock_price)
        print("Total Cost:", total_cost)

        # Debugging: print total_cost
        print("Total Cost:", total_cost)

        # Check user's cash balance
        user_id = session["user_id"]
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = rows[0]["cash"]
        print("Cash:", cash)

        # Check if the user has enough cash to buy the shares
        if total_cost > cash:
            return apology("not enough cash", 400)

        # Update user's cash
        new_cash = cash - total_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)

        # Insert the transaction into the database
        db.execute(
            """
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (?, ?, ?, ?)
            """,
            user_id,
            symbol,
            shares,
            total_cost,
        )

        # Redirect user to home page
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
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return apology("must provide username", 403)
        if not password:
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
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
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 400)

        quote = lookup(symbol)
        if not quote:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("Shares must be a positive integer", 400)

        if not symbol or shares < 1:
            return apology("Invalid symbol or shares", 400)

        # Query database for user's shares of the stock
        stock = db.execute("""
            SELECT SUM(shares) as total_shares
            FROM transactions
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
        """, session["user_id"], symbol)

        # Ensure user has enough shares to sell
        if not stock or stock[0]["total_shares"] < shares:
            return apology("Not enough shares to sell", 400)

        # Get current price of the stock
        stock_info = lookup(symbol)
        if not stock_info:
            return apology("Invalid symbol", 400)

        # Calculate sell value and update user's cash
        sell_value = stock_info["price"] * shares
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", sell_value, session["user_id"])

        # Insert sell transaction into database
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price, timestamp)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        """, session["user_id"], symbol, -shares, stock_info["price"])

        # Redirect to index page
        return redirect("/")

    else:
        # Query database for user's stocks
        stocks = db.execute("""
            SELECT symbol
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
        """, session["user_id"])

        symbols = [stock["symbol"] for stock in stocks]
        return render_template("sell.html", symbols=symbols)


if __name__ == "__main__":
    app.run(debug=True)
