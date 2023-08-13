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
    user_price_min = int(request.form["price_min"])
    user_price_max = int(request.form["price_max"])
    user_type = request.form["type"]
    user_style = request.form["style"]

    user_picks = []

    for x in ev_database:
        if (
            user_price_min <= x["MSRP"]
            <= user_price_max
            and x["TYPE"] == user_type
            and x["STYLE"] == user_style
        ):
            user_picks.append(x)

    return render_template("home.html", ev_database=ev_database, user_picks=user_picks, format_usd=format_usd)



