with open("scores.csv", "r") as f:
    lines = f.readlines()
    people = []
    for line in lines:
        person = {}
        person["name"], person["score"] = line.strip().split(",")
        person["score"] = int(person["score"])
        people.append(person)

print('得点(高い順)')
score_sorted = sorted(people, key=lambda p: p["score"], reverse=True)
for person in score_sorted:
    print(f'{person["name"]}: {person["score"]}点')

print('名前(昇順)')
name_sorted = sorted(people, key=lambda p: p["name"])
for person in name_sorted:
    print(f'{person["name"]}: {person["score"]}点')
