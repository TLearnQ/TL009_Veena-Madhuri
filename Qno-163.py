days = [
    {"sales": 1000, "cost": 1200},
    {"sales": 2000, "cost": 1500},
    {"sales": 5000, "cost": 2000},
]
for d in days:
    profit = d["sales"] - d["cost"]
    if profit < 0:      
        tag = "Loss"
    elif profit < 500:  
        tag = "Low Margin"
    elif profit < 3000: 
        tag = "Healthy"
    else:               
        tag = "Peak"
    print(d, "->", tag)

    
        
        