from label_pass_fail import label_pass_fail

with open("scores.csv", "r") as f:
    lines = f.readlines()
    names = []
    scores = []
    for line in lines:
        name, score = line.strip().split(",")
        names.append(name)
        scores.append(int(score))
    
labels = label_pass_fail(scores)

for name, label in zip(names, labels):
    print(f"{name}:{label}")


with open("scores.csv", "r") as f:
    lines = f.readlines()
    people = []
    for line in lines:
        person = {}
        person["name"], person["score"] = line.strip().split(",")
        person["score"] = int(person["score"])
        people.append(person)
    
    for person in people:
        if person["score"] >= 70:
            person["label"] = "Pass"
        else:
            person["label"] = "Fail"
    
    for person in people:
        print(f"{person['name']}: {person['score']}点, {person['label']}")