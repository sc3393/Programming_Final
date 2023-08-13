# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template
from app.basecode import format_usd, ev_database

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html", ev_database=ev_database, format_usd=format_usd)

@home_routes.route("/search", methods=["POST"])
def search():
    price_range = request.form["price_range"]
    type = request.form["type"]
    style = request.form["style"]

    min_price, max_price = map(int, price_range.split('-'))

    user_picks = []

    for x in ev_database:
        if (
            min_price <= x["MSRP"] <= max_price
            and x["TYPE"] == type
            and x["STYLE"] == style
        ):
            user_picks.append(x)

    return render_template("home.html", ev_database=ev_database, user_picks=user_picks, format_usd=format_usd)



