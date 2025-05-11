from analyze_scores import get_people
from summarize_scores import summarize_scores
import json

with open("scores.csv", "r") as f:
    lines = f.readlines()

people = get_people(lines)
summary = summarize_scores(people)

with open("summary.json", "w") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)