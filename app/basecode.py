
def format_usd(my_price):
    return f"${my_price:,.2f}"

ev_database=[
        {"MSRP": 78000, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Rivian", "MODEL":"R1S", "IMG_URL":"static/images/Rivian.jpeg"},
        {"MSRP": 87100, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"BMW", "MODEL":"iX", "IMG_URL":"static/images/1-BMW-iX_0.jpg"},
        {"MSRP": 74400, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"Audi", "MODEL":"Q8 e-tron", "IMG_URL":"static/images/2024-audi-q8-sportback-front-three-quarter.jpg"},
        {"MSRP": 108700, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"GMC", "MODEL":"Hummer EV", "IMG_URL":"static/images/2024-gmc-hummer-ev-suv-302-6419ae6383a10.jpg"},
        {"MSRP": 42600, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Kia", "MODEL":"EV 6", "IMG_URL":"static/images/2023-kia-ev6-gt-002-1669747412.jpg"},
        {"MSRP": 26500, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt", "IMG_URL":"static/images/2022-chevrolet-bolt-ev-101-1613168160.jpg"},
        {"MSRP": 28140, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Nissan", "MODEL":"Leaf", "IMG_URL":"static/images/2023-nissan-leaf-13-1200x800-1649784914.jpg"},
        {"MSRP": 30900, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"MINI", "MODEL":"Electric Hardtop", "IMG_URL":"static/images/2024-mini-cooper-electric-101-63ff8395c399b.jpg"},
        {"MSRP": 27800, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt EUV", "IMG_URL":"static/images/2023_chevrolet_bolt-euv_4dr-hatchback_premier_fq_oem_1_1600.jpg"},
        {"MSRP": 41450, "TYPE":"Compact", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 5", "IMG_URL":"static/images/2022-hyundai-ioniq-5-103-1650640843.jpg"},
        {"MSRP": 88490, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model S", "IMG_URL":"static/images/Tesla S.jpeg"},
        {"MSRP": 40240, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model 3", "IMG_URL":"static/images/2023-tesla-model-3-101-1671468297.jpeg"},
        {"MSRP": 87400, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Lucid", "MODEL":"Air", "IMG_URL":"static/images/2023-lucid-air-touring-9444-1675346750.jpg"},
        {"MSRP": 41600, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 6", "IMG_URL":"static/images/large-52940-2023ioniq6-1669059842.jpg"},
        {"MSRP": 86700, "TYPE":"Sedan", "STYLE":"Conventional", "MAKE":"Porsche", "MODEL":"Taycan", "IMG_URL":"static/images/2022-porsche-taycan-sport-turismo-gts-19-1638148404.jpg"},
        ]

if __name__ =="__main__":
   
    ev_database=[
        {"MSRP": 78000, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Rivian", "MODEL":"R1S", "IMG_URL":"static/images/Rivian .jpeg"},
        {"MSRP": 87100, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"BMW", "MODEL":"iX", "IMG_URL":"static/images/1-BMW-iX_0.jpg"},
        {"MSRP": 74400, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"Audi", "MODEL":"Q8 e-tron", "IMG_URL":"static/images/2024-audi-q8-sportback-front-three-quarter.jpg"},
        {"MSRP": 108700, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"GMC", "MODEL":"Hummer EV", "IMG_URL":"static/images/2024-gmc-hummer-ev-suv-302-6419ae6383a10.jpg"},
        {"MSRP": 42600, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Kia", "MODEL":"EV 6", "IMG_URL":"static/images/2023-kia-ev6-gt-002-1669747412.jpg"},
        {"MSRP": 26500, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt", "IMG_URL":"static/images/2022-chevrolet-bolt-ev-101-1613168160.jpg"},
        {"MSRP": 28140, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Nissan", "MODEL":"Leaf", "IMG_URL":"static/images/2023-nissan-leaf-13-1200x800-1649784914.jpg"},
        {"MSRP": 30900, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"MINI", "MODEL":"Electric Hardtop", "IMG_URL":"static/images/2024-mini-cooper-electric-101-63ff8395c399b.jpg"},
        {"MSRP": 27800, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt EUV", "IMG_URL":"static/images/2023_chevrolet_bolt-euv_4dr-hatchback_premier_fq_oem_1_1600.jpg"},
        {"MSRP": 41450, "TYPE":"Compact", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 5", "IMG_URL":"static/images/2022-hyundai-ioniq-5-103-1650640843.jpg"},
        {"MSRP": 88490, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model S", "IMG_URL":"static/images/Tesla S.jpeg"},
        {"MSRP": 40240, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model 3", "IMG_URL":"static/images/2023-tesla-model-3-101-1671468297.jpeg"},
        {"MSRP": 87400, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Lucid", "MODEL":"Air", "IMG_URL":"static/images/2023-lucid-air-touring-9444-1675346750.jpg"},
        {"MSRP": 41600, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 6", "IMG_URL":"static/images/large-52940-2023ioniq6-1669059842.jpg"},
        {"MSRP": 86700, "TYPE":"Sedan", "STYLE":"Conventional", "MAKE":"Porsche", "MODEL":"Taycan", "IMG_URL":"static/images/2022-porsche-taycan-sport-turismo-gts-19-1638148404.jpg"},
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
            print(f"Image URL: {x['IMG_URL']}")
    else:
        print("none")
    