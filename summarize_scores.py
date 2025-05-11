from analyze_scores import get_people, get_average, get_max, passed_filter

with open("scores.csv", "r") as f:
    lines = f.readlines()

def summarize_scores(people):
    average = get_average(people)
    max_score = get_max(people)
    passed_count = len(passed_filter(people))
    passed_percent = passed_count / len(people) * 100

    return {
        "average": average,
        "max_score": max_score,
        "passed_count": passed_count,
        "passed_percent": passed_percent
    }
    

people = get_people(lines)
summary = summarize_scores(people)
print(f"平均点: {summary['average']:.1f}")
print(f"最高点: {summary['max_score']}")
print(f"Pass人数: {summary['passed_count']}")
print(f"Pass率: {summary['passed_percent']:.1f}")