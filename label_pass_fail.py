def label_pass_fail(scores):
    labels = ["Pass" if score >= 70 else "Fail" for score in scores]

    return labels

print(label_pass_fail([80, 65, 90, 70, 55]))
