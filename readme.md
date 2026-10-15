Student Performance Analytics System

#Introduction-
This project reads student records from a CSV file, analyses them using Pandas and NumPy, and shows results such as total marks, averages, grades, pass/fail status, subject-wise performance and the top performing students. No machine learning is used.

#Files-
main.py:	Runs the project and prints the final analysis
functions.py:	Reusable functions for calculations and processing
students.csv:	Dataset of 20 students
student_results.csv	:Output file created by the program
readme.md	:project documentation

#Dataset
students.csv has 20 records with these columns: Student_ID, Name, Department, Maths, Physics, Chemistry, English, Computer_Science (each out of 100) and Attendance (%).

#Rules Used
Grade (based on average marks)

Average	Grade
90 and above:A+
80 - 89	:A
70 - 79	:B
60 - 69	:C
50 - 59	:D
40 - 49	:E
Below 40:F(fail)

passing criteria: a student passes only if they score at least 35 in every subject. A student who fails any subject is marked Fail and gets grade F.

#How It Works
-load_data() reads the CSV into a Pandas DataFrame, and the program shows the number of records, columns and missing values.
-add_total_and_average() converts the marks to a NumPy array and uses np.sum and np.mean to get each student's total and average.
-add_grade_and_result() loops through every student and uses get_grade() and get_result() to set the grade and Pass/Fail.
-main.py finds the highest, lowest and class average, and counts passed and failed students.
-subject_summary() loops through each subject and finds its average, highest, lowest, topper and number of fails.
-top_students() sorts by total marks and returns the top 5.
-The final DataFrame is saved to student_results.csv.

#How to Run
pip install pandas numpy
python main.py
Keep students.csv and functions.py in the same folder as main.py.

#Results
Highest average:D - 90.0 (grade A+)
Lowest average:I - 41.8
Class average:70.63
Students passed:18 of 20 (90%)
Students failed:2 (I and Q, both failed in Maths)
Best subject:English (average 74.3)
Weakest subject:Chemistry (average 67.3)
Topppers:D, N, A, H, T

#Conclusion
The project loads raw student data, calculates results with NumPy and Pandas, and presents a clear summary of class, subject and individual performance. It could be extended with charts or multiple semesters of data.
