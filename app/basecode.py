
def format_usd(my_price):
    return f"${my_price:,.2f}"

ev_database=[
        {"MSRP": 78000, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Rivian", "MODEL":"R1S", "IMG_URL":"https://cars.usnews.com/static/images/Auto/custom/15225/2023_Rivian_R1S_17.jpg"},
        {"MSRP": 87100, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"BMW", "MODEL":"iX", "IMG_URL":"https://www.topgear.com/sites/default/files/2022/01/1-BMW-iX_0.jpg"},
        {"MSRP": 74400, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"Audi", "MODEL":"Q8 e-tron", "IMG_URL":"https://www.motortrend.com/uploads/2022/11/2024-audi-q8-etron-sq8-passenger-side.jpg?fit=around%7C875:492.1875"},
        {"MSRP": 108700, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"GMC", "MODEL":"Hummer EV", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2024-gmc-hummer-ev-suv-302-6419ae6383a10.jpg"},
        {"MSRP": 42600, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Kia", "MODEL":"EV 6", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2023-kia-ev6-gt-002-1669747412.jpg?crop=0.574xw:0.430xh;0.284xw,0.404xh&resize=1200:*"},
        {"MSRP": 26500, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2022-chevrolet-bolt-ev-101-1613168160.jpg?crop=0.819xw:0.922xh;0.0489xw,0.0122xh&resize=640:*"},
        {"MSRP": 28140, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Nissan", "MODEL":"Leaf", "IMG_URL":"https://electrek.co/wp-content/uploads/sites/3/2019/12/2019-Nissan-LEAF-6-source-2000.jpg?quality=82&strip=all&w=1600"},
        {"MSRP": 30900, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"MINI", "MODEL":"Electric Hardtop", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2024-mini-cooper-electric-101-63ff8395c399b.jpg?crop=0.779xw:0.584xh;0.168xw,0.342xh&resize=1200:*"},
        {"MSRP": 27800, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt EUV", "IMG_URL":"https://media.ed.edmunds-media.com/chevrolet/bolt-euv/2023/oem/2023_chevrolet_bolt-euv_4dr-hatchback_premier_fq_oem_1_1600.jpg"},
        {"MSRP": 41450, "TYPE":"Compact", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 5", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2022-hyundai-ioniq-5-103-1650640843.jpg?crop=0.666xw:0.751xh;0.231xw,0.249xh&resize=640:*"},
        {"MSRP": 88490, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model S", "IMG_URL":"https://www.topgear.com/sites/default/files/cars-car/image/2018/09/ab3t4352.jpg"},
        {"MSRP": 40240, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model 3", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2019-tesla-model3-lt-airporthero-low-101-1587061146.jpg?crop=0.8888888888888888xw:1xh;center,top&resize=1200:*"},
        {"MSRP": 87400, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Lucid", "MODEL":"Air", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2023-lucid-air-touring-9444-1675346750.jpg?crop=0.631xw:0.709xh;0.155xw,0.248xh&resize=640:*"},
        {"MSRP": 41600, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 6", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/large-52940-2023ioniq6-1669059842.jpg"},
        {"MSRP": 86700, "TYPE":"Sedan", "STYLE":"Conventional", "MAKE":"Porsche", "MODEL":"Taycan", "IMG_URL":"https://i0.wp.com/electrek.co/wp-content/uploads/sites/3/2022/07/2023-Porsche-Taycan.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1"},
        ]

if __name__ =="__main__":
   
    ev_database=[
        {"MSRP": 78000, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Rivian", "MODEL":"R1S", "IMG_URL":"https://cars.usnews.com/static/images/Auto/custom/15225/2023_Rivian_R1S_17.jpg"},
        {"MSRP": 87100, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"BMW", "MODEL":"iX", "IMG_URL":"https://www.topgear.com/sites/default/files/2022/01/1-BMW-iX_0.jpg"},
        {"MSRP": 74400, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"Audi", "MODEL":"Q8 e-tron", "IMG_URL":"https://www.motortrend.com/uploads/2022/11/2024-audi-q8-etron-sq8-passenger-side.jpg?fit=around%7C875:492.1875"},
        {"MSRP": 108700, "TYPE":"SUV", "STYLE":"Conventional", "MAKE":"GMC", "MODEL":"Hummer EV", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2024-gmc-hummer-ev-suv-302-6419ae6383a10.jpg"},
        {"MSRP": 42600, "TYPE":"SUV", "STYLE":"Innovative", "MAKE":"Kia", "MODEL":"EV 6", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2023-kia-ev6-gt-002-1669747412.jpg?crop=0.574xw:0.430xh;0.284xw,0.404xh&resize=1200:*"},
        {"MSRP": 26500, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2022-chevrolet-bolt-ev-101-1613168160.jpg?crop=0.819xw:0.922xh;0.0489xw,0.0122xh&resize=640:*"},
        {"MSRP": 28140, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Nissan", "MODEL":"Leaf", "IMG_URL":"https://electrek.co/wp-content/uploads/sites/3/2019/12/2019-Nissan-LEAF-6-source-2000.jpg?quality=82&strip=all&w=1600"},
        {"MSRP": 30900, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"MINI", "MODEL":"Electric Hardtop", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2024-mini-cooper-electric-101-63ff8395c399b.jpg?crop=0.779xw:0.584xh;0.168xw,0.342xh&resize=1200:*"},
        {"MSRP": 27800, "TYPE":"Compact", "STYLE":"Conventional", "MAKE":"Chevrolet", "MODEL":"Bolt EUV", "IMG_URL":"https://media.ed.edmunds-media.com/chevrolet/bolt-euv/2023/oem/2023_chevrolet_bolt-euv_4dr-hatchback_premier_fq_oem_1_1600.jpg"},
        {"MSRP": 41450, "TYPE":"Compact", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 5", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2022-hyundai-ioniq-5-103-1650640843.jpg?crop=0.666xw:0.751xh;0.231xw,0.249xh&resize=640:*"},
        {"MSRP": 88490, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model S", "IMG_URL":"https://www.topgear.com/sites/default/files/cars-car/image/2018/09/ab3t4352.jpg"},
        {"MSRP": 40240, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Tesla", "MODEL":"Model 3", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2019-tesla-model3-lt-airporthero-low-101-1587061146.jpg?crop=0.8888888888888888xw:1xh;center,top&resize=1200:*"},
        {"MSRP": 87400, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Lucid", "MODEL":"Air", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/2023-lucid-air-touring-9444-1675346750.jpg?crop=0.631xw:0.709xh;0.155xw,0.248xh&resize=640:*"},
        {"MSRP": 41600, "TYPE":"Sedan", "STYLE":"Innovative", "MAKE":"Hyundai", "MODEL":"Ioniq 6", "IMG_URL":"https://hips.hearstapps.com/hmg-prod/images/large-52940-2023ioniq6-1669059842.jpg"},
        {"MSRP": 86700, "TYPE":"Sedan", "STYLE":"Conventional", "MAKE":"Porsche", "MODEL":"Taycan", "IMG_URL":"https://i0.wp.com/electrek.co/wp-content/uploads/sites/3/2022/07/2023-Porsche-Taycan.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1"},
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
    