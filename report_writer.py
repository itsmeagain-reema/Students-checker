# create report of performance
def create_report(student_name, score, status):
    report = f""" Student Performance Report!
    ----------------------------------------
    Student : {student_name}
    Average : {score}
    Status : {status}
    """
    return report

# save report with student name
def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ','_')}_report.txt"

    with open(filename,"w", encoding="utf-8") as file:
        file.write(report)

    return filename