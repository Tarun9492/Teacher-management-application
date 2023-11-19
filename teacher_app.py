import os
import json

# File to store teacher records
TEACHERS_FILE = "teachers.json"

# Function to load teacher records from file
def load():
    if os.path.exists(TEACHERS_FILE):
        with open(TEACHERS_FILE, "r") as file:
            teachers = json.load(file)
        return teachers
    else:
        return []

# Function to save teacher records to file
def save(teachers):
    with open(TEACHERS_FILE, "w") as file:
        json.dump(teachers, file, indent=2)

# Function to display the landing page
def display():
    print("\nTeacher Management Application")
    print("1. Show all teachers")
    print("2. Add a teacher")
    print("3. Filter teachers based on criteria")
    print("4. Search for a teacher")
    print("5. Update a teacher's record")
    print("6. Delete a teacher")
    print("0. Exit")

# Function to show all teachers
def show(teachers):
    print("\nAll Teachers:")
    for teacher in teachers:
        print(teacher)
        

# Function to add a new teacher
def add(teachers):
    print("\nEnter teacher details:")
    name = input("Full Name: ")
    age = int(input("Age: "))
    dob = input("Date of Birth (YYYY-MM-DD): ")
    num_classes = int(input("Number of Classes: "))

    new_teacher = {
        "Full Name": name,
        "Age": age,
        "Date of Birth": dob,
        "Number of Classes": num_classes
    }

    teachers.append(new_teacher)
    save(teachers)
    print("Teacher added successfully!")

# Function to filter teachers based on criteria
def filter(teachers):
    print("\nFilter Teachers:")
    print("1. Filter by Age")
    print("2. Filter by Number of Classes")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        age_filter = int(input("Enter age for filtering: "))
        filtered_teachers = [teacher for teacher in teachers if teacher["Age"] == age_filter]
        show(filtered_teachers)
    elif choice == 2:
        class_filter = int(input("Enter number of classes for filtering: "))
        filtered_teachers = [teacher for teacher in teachers if teacher["Number of Classes"] == class_filter]
        show(filtered_teachers)
    else:
        print("Invalid choice")

# Function to search for a teacher
def search(teachers):
    print("\nSearch for a Teacher:")
    search_term = input("Enter full name to search: ")
    found_teachers = [teacher for teacher in teachers if search_term.lower() in teacher["Full Name"].lower()]
    show(found_teachers)

# Function to update a teacher's record
def update(teachers):
    print("\nUpdate Teacher's Record:")
    search_term = input("Enter full name of the teacher to update: ")
    for teacher in teachers:
        if search_term.lower() in teacher["Full Name"].lower():
            print("Current Details:")
            print(teacher)
            teacher["Full Name"] = input("New Full Name: ")
            teacher["Age"] = int(input("New Age: "))
            teacher["Date of Birth"] = input("New Date of Birth (YYYY-MM-DD): ")
            teacher["Number of Classes"] = int(input("New Number of Classes: "))
            save(teachers)
            print("Teacher's record updated successfully!")
            return
    print("Teacher not found")

# Function to delete a teacher
def delete(teachers):
    print("\nDelete a Teacher:")
    search_term = input("Enter full name of the teacher to delete: ")
    for teacher in teachers:
        if search_term.lower() in teacher["Full Name"].lower():
            teachers.remove(teacher)
            save(teachers)
            print("Teacher deleted successfully!")
            return
    print("Teacher not found")

# Main function
def main():
    teachers = load()

    while True:
        display()
        choice = input("Enter your choice (0-6): ")

        if choice == "1":
            show(teachers)
        elif choice == "2":
            add(teachers)
        elif choice == "3":
            filter(teachers)
        elif choice == "4":
            search(teachers)
        elif choice == "5":
            update(teachers)
        elif choice == "6":
            delete(teachers)
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
