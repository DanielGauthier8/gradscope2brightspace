import csv

# Change the GRADESCOPE_FILENAME to the export filename from gradescope
# Upload the Brightspace_import.csv file created to Brightspace and follow the prompts


gradescope_filename = "scores/Independent_Project_scores.csv"


def create_import_file(gradescope_filename):
    assignment_name = gradescope_filename.replace("_scores.csv", "").replace("_", " ")
    grades = []
    with open(gradescope_filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            grades.append(row)

    with open('brightspace_import.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["OrgDefinedId", assignment_name + "1 Points Grade", "End-of-Line Indicator"])
        for row in grades:
            try:
                writer.writerow([int(row[1]), row[3], "#"])
            except ValueError:
                pass


def main():
    gradescope_filename = "scores/Independent_Project_scores.csv"
    # gradescope_filename = input("What is the filename? ")
    create_import_file(gradescope_filename)


main()
