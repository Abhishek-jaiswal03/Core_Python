city_list=["Gorakhpur","Goa","Rampur","Raigarh","Jaunpur","Mirzapur","Delhi","Dautpur","Rishikesh","Kanpur","Kailashpur","Lucknow","Patna","Lotapur"]
d1={}
for city in city_list:
    alphabet=city[0]
    if alphabet in d1:
        d1[alphabet]+=f",{city}"
    else:
        d1[alphabet]=city
for alphabets,city in d1.items():
    print(f"{alphabets}:{city}")