import numpy as np
import pandas as pd
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]


PASSING_MARKS=35

def load_data(filename):
    return pd.read_csv(filename)

def add_total_and_average(df):
    marks = df[SUBJECTS].to_numpy()
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_grade(average):
    # grade is based on the average marks
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

def get_result(marks):
    # student is marked pass only if marks are passing marks or above
    if np.all(marks >= PASSING_MARKS):
        return "Pass"
    return "Fail"

def add_grade_and_result(df):
    grades = []
    results = []

    for index, row in df.iterrows():
        result = get_result(row[SUBJECTS].to_numpy(dtype=float))
        results.append(result)

        # a failed student always gets F
        if result == "Fail":
            grades.append("F")
        else:
            grades.append(get_grade(row["Average"]))

    df["Result"] = results
    df["Grade"] = grades
    return df

def subject_summary(df):
    rows = []

    for subject in SUBJECTS:
        marks = df[subject].to_numpy()
        topper = df.loc[df[subject].idxmax(), "Name"]

        rows.append({
            "Subject": subject,
            "Average": round(np.mean(marks), 2),
            "Highest": np.max(marks),
            "Lowest": np.min(marks),
            "Topper": topper,
            "Failed": int(np.sum(marks<PASSING_MARKS)),
        })

    summary = pd.DataFrame(rows)
    return summary.sort_values("Average", ascending=False)

def top_students(df,n=5):
    top = df.sort_values("Total", ascending=False).head(n)
    return top[["Student_ID","Name","Department","Total","Average","Grade"]]