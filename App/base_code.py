
def format_usd(my_price):
    return f"${my_price:,.2f}"

if __name__ =="__main__":

    ev_database=[
        {"MSRP": 60, "TYPE":"compact", "STYLE":"innovative", "MAKE":"Hyundai", "MODEL":"Lyric"},
        {"MSRP": 90, "TYPE":"SUV", "STYLE":"conventional","MAKE":"Ford","MODEL":"F150"},
        {"MSRP": 120, "TYPE":"sedan", "STYLE":"innovative","MAKE":"Porsche","MODEL":"Taycan"}
                 ]
    
    user_price_min=int(input("Price Min"))
    user_price_max=int(input("Price Max"))
    user_type=input("Type")
    user_style=input("Style")
    
    user_picks=[]
    
    print(format_usd(60))
    
    for x in ev_database:
        if user_price_min <= x["MSRP"] <= user_price_max and (x["TYPE"]== user_type) and (x["STYLE"]== user_style):
            user_picks.append(x)
    
    if user_picks:
        print("selection")
        for x in user_picks:
            print(f"MSRP: {format_usd(x['MSRP'])} | Type: {x['TYPE']} | Style: {x['STYLE']} | Make: {x['MAKE']} | Model: {x['MODEL']}")
    else:
        print("none")
    