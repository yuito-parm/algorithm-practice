def filter_passed(people):
    pass_people = []
    for person in people:
        if person["score"] >= 70:
            person["label"] = "Pass"
            pass_people.append(person)
        else:
            person["label"] = "Fail"
    
    return pass_people

with open("scores.csv", "r") as f:
    lines = f.readlines()
    people = []
    for line in lines:
        person = {}
        person["name"], person["score"] = line.strip().split(",")
        person["score"] = int(person["score"])
        print(person)
        people.append(person)
  
pass_people = filter_passed(people)

print("Passの人だけ表示")
for person in pass_people:
    print(f"{person['name']}: {person['score']} {person['label']}")
    
