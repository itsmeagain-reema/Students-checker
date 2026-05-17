from grading import is_valid_score, classify_score, score_average
from report_writer import create_report, save_report

# program will start from here

students=[]

try:
    print("""This program will calculate the average for each student,
    then show top three!""")
    
    while True:
        student_name = input("Enter student name (or q to quit): ")

        if student_name.lower() == 'q':
            break
         
        if student_name =='':
            print("skipped: student name can't be empty")
            
        math = float(input("-Enter math score: "))
        chemistry = float(input("-Enter chemistry score: "))
        physics = float(input("-Enter physics score: "))


        if not (is_valid_score(math) or is_valid_score(chemistry) or is_valid_score(physics) ):
            print("skipped: score must be between 0 and 100")
            continue

        average = score_average(math, physics, chemistry)
        status = classify_score(average)
        report = create_report(student_name, average, status)
        filename = save_report(student_name, report)

        # add student name + average to the studnets list
        students.append((student_name, average))

        print(f"all done ! here is file name: {filename}")

        # use second element to sort (average score)
        students.sort(key=lambda x : x[1], reverse=True)

    print("\nTop 3 students:")
    for student in students[:3]:
        # student[0]-> student name , student[1]-> student Avg
        print(student[0], "-", round(student[1],2))

except ValueError:
        print("Invalid input. Please enter numbers where required")
        
        