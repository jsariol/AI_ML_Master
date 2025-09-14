from InquirerPy import inquirer


room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Get list of course codes
course_choices = list(room_numbers.keys())

# Interactive menu to choose a course
course_number = inquirer.select(
    message="Select a course to view details:",
    choices=course_choices,
).execute()

# Display selected course info
print(f"\nCourse: {course_number}")
print(f"Room Number: {room_numbers[course_number]}")
print(f"Instructor: {instructors[course_number]}")
print(f"Meeting Time: {meeting_times[course_number]}")
