
from flask import Blueprint, request, render_template
from app.basecode import format_usd, ev_database

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html")

@home_routes.route("/input", methods=["POST"])
def input():
    price_range = request.form["price_range"]
    type = request.form["type"]
    style = request.form["style"]
    
    if price_range == "20000-40000":
        min_price = 20000
        max_price = 40000
    elif price_range == "40001-70000":
        min_price = 40001
        max_price = 70000
    else:
        min_price = 70001
        max_price = float("inf")
    
    user_picks = []

    for x in ev_database:
        if (
            min_price <= x["MSRP"] <= max_price
            and x["TYPE"] == type
            and x["STYLE"] == style
        ):
            user_picks.append(x)

    return render_template("home.html", ev_database=ev_database, user_picks=user_picks, format_usd=format_usd)
    #used OpenAI ChatGPT to resolve error where ev_database, user_picks and format_usd in return


