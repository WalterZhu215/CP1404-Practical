"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Main function: Load data and display formatted subject information"""
    data = load_data()
    display_subject_details(data)


def load_data(filename=FILENAME):
    """Read data from the file and return a processed list.
    Each element in the list is [subject_code, lecturer, number_of_students]."""
    input_file = open(filename)
    data = []
    for line in input_file:
        line = line.strip()  # Remove newline characters and leading/trailing spaces
        parts = line.split(',')  # Split data by commas
        # Clean up extra spaces in each part and convert student count to integer
        parts = [part.strip() for part in parts]
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details in a formatted way"""
    for subject in data:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()