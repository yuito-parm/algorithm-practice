def filter_passed(people):
    pass_people = [person for person in people if person["label"] == "Pass"]
    
    return pass_people

with open("scores.csv", "r") as f:
    lines = f.readlines()
    people = []
    for line in lines:
        person = {}
        person["name"], person["score"] = line.strip().split(",")
        person["score"] = int(person["score"])
        if person["score"] >= 70:
            person["label"] = "Pass"
        else:
            person["label"] = "Fail"
        people.append(person)
  
pass_people = filter_passed(people)

print("Passの人だけ表示")
for person in pass_people:
    print(f"{person['name']}: {person['score']} {person['label']}")
    
