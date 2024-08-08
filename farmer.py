farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

yuck= ["carrots", "celery"]

NE_animals= farms[0]["agriculture"]

for animal in NE_animals:
    print(animal)

for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")


for farm in farms:
    if farm["name"] == choice:
        animals = [item for item in farm["agriculture"] if item not in yuck]
        print(f"The Livestock raised at {choice} are:{animals}")
    break
else:
    print("Farm Not found")
