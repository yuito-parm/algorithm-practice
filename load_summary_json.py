import json

with open("summary.json", "r") as f:
    summary = json.load(f)

print(f"平均点: {summary['average']:.1f}点")
print(f"最高点: {summary['max_score']}点")
print(f"Pass人数: {summary['passed_count']}人")
print(f"Pass率: {summary['passed_percent']:.1f}%")