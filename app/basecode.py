
def format_usd(my_price):
    return f"${my_price:,.2f}"

ev_database=[
        {"MSRP": 78000, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Rivian", "MODEL":"R1S"},
        {"MSRP": 87100, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"BMW", "MODEL":"iX"},
        {"MSRP": 74400, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"Audi", "MODEL":"Q8 e-tron"},
        {"MSRP": 108700, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"GMC", "MODEL":"Hummer EV"},
        {"MSRP": 42600, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Kia", "MODEL":"EV 6"},
        {"MSRP": 26500, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt"},
        {"MSRP": 28140, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Nissan", "MODEL":"Leaf"},
        {"MSRP": 30900, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"MINI", "MODEL":"Electric Hardtop"},
        {"MSRP": 27800, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt EUV"},
        {"MSRP": 41450, "TYPE":"Compact", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 5"},
        {"MSRP": 88490, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model S"},
        {"MSRP": 40240, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model 3"},
        {"MSRP": 87400, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Lucid", "MODEL":"Air"},
        {"MSRP": 41600, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 6"},
        {"MSRP": 86700, "TYPE":"Sedan", "STYLE":"Conventional", "MAKE":"Porsche", "MODEL":"Taycan"},
        ]

if __name__ =="__main__":
   
    ev_database=[
        {"MSRP": 78000, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Rivian", "MODEL":"R1S"},
        {"MSRP": 87100, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"BMW", "MODEL":"iX"},
        {"MSRP": 74400, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"Audi", "MODEL":"Q8 e-tron"},
        {"MSRP": 108700, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"GMC", "MODEL":"Hummer EV"},
        {"MSRP": 42600, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Kia", "MODEL":"EV 6"},
        {"MSRP": 26500, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt"},
        {"MSRP": 28140, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Nissan", "MODEL":"Leaf"},
        {"MSRP": 30900, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"MINI", "MODEL":"Electric Hardtop"},
        {"MSRP": 27800, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt EUV"},
        {"MSRP": 41450, "TYPE":"Compact", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 5"},
        {"MSRP": 88490, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model S"},
        {"MSRP": 40240, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model 3"},
        {"MSRP": 87400, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Lucid", "MODEL":"Air"},
        {"MSRP": 41600, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 6"},
        {"MSRP": 86700, "TYPE":"Sedan", "STYLE":"Conventional", "MAKE":"Porsche", "MODEL":"Taycan"},
        ]
    
    user_price_min=int(input("Price Min"))
    user_price_max=int(input("Price Max"))
    user_type=input("Type")
    user_style=input("Style")
    
    user_picks=[]
    
    for x in ev_database:
        if user_price_min <= x["MSRP"] <= user_price_max and (x["TYPE"]== user_type) and (x["STYLE"]== user_style):
            user_picks.append(x)
    
    if user_picks:
        print("selection")
        for x in user_picks:
            print(f"MSRP: {format_usd(x['MSRP'])} | Type: {x['TYPE']} | Style: {x['STYLE']} | Make: {x['MAKE']} | Model: {x['MODEL']}")
    else:
        print("none")
    