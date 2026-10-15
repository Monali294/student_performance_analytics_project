import numpy as np
from functions import *


def main():
    # load the data
    df=load_data("students.csv")
    print("----- Dataset Information -----")
    print("Records :", df.shape[0])
    print("Columns :", list(df.columns))
    print("Missing values:", df.isnull().sum().sum())
    print()
    print(df.head().to_string(index=False))
    # calculations
    df = add_total_and_average(df)
    df = add_grade_and_result(df)

    print("\nSTUDENT RESULTS")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

    # class performance
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    passed = np.sum(df["Result"] == "Pass")
    failed = np.sum(df["Result"] == "Fail")

    print("\nCLASS PERFORMANCE")
    print("Class average   :", round(np.mean(df["Average"]), 2))
    print("Highest average :", best["Average"], "-", best["Name"])
    print("Lowest average  :", worst["Average"], "-", worst["Name"])
    print("Passed          :", passed)
    print("Failed          :", failed)
    print("Pass percentage :", round(passed / len(df) * 100, 2), "%")

    # grade count
    print("\nGRADE")
    print(df["Grade"].value_counts().sort_index().to_string())

    # subject wise
    summary = subject_summary(df)
    print("\nSUBJECT-WISE RESULT")
    print(summary.to_string(index=False))
    print("Best subject   :", summary.iloc[0]["Subject"])
    print("Weakest subject:", summary.iloc[-1]["Subject"])

    # top performers
    print("\nTOP 5 STUDENTS")
    print(top_students(df).to_string(index=False))

    # failed students
    print("\nFAILED STUDENTS")
    for index, row in df[df["Result"] == "Fail"].iterrows():
        weak_subjects = [s for s in SUBJECTS if row[s]<PASSING_MARKS]
        print(row["Student_ID"], row["Name"], "- failed in", ", ".join(weak_subjects))

    # save everything
    df.to_csv("student_results.csv", index=False)
    print("\nResults saved to student_results.csv")
main()