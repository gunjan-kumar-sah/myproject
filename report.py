def grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 40:
        return 'E'
    else:
        return 'F'
    
st = [
    {"name": "Gunjan", "marks":[98,89,90]},
    {"name": "Rohit", "marks":[85,75,65]},
    {"name": "Sita", "marks":[95,85,75]},
    {"name": "Mohan", "marks":[80,70,60]},
    {"name": "Geeta", "marks":[75,65,55]},
    {"name": "Ramesh", "marks":[60,50,40]},
    {"name": "Suresh", "marks":[55,45,35]},
    {"name": "Anita", "marks":[90,80,70]},
    {"name": "Sunil", "marks":[85,75,65]},
    {"name": "Pooja", "marks":[95,85,75]}
    {"name": "Priya", "marks":[80,70,60]},
    {"name": "Piyush", "marks":[75,65,55]},
]

# =========================
# CALCULATE DATA
# =========================
for s in st:
    total = sum(s["marks"])
    percentage = total / len(s["marks"])
    s["total"] = total
    s["percentage"] = percentage
    s["grade"] = grade(percentage)

# =========================
# FUNCTIONS
# =========================
def show_all():
    for s in st:
        print("\nName:", s["name"])
        print("Total:", s["total"])
        print("Percentage:", round(s["percentage"], 2))
        print("Grade:", s["grade"])

def search_student():
    name = input("Enter name: ").lower()

    for s in st:
        if s["name"].lower() == name:
            print("\nFound Student:")
            print(s)
            return

    print("Student not found")

def top_student():
    top = max(st, key=lambda x: x["percentage"])
    print("\nTop Student:", top["name"], top["percentage"])

def average():
    avg = sum(s["percentage"] for s in st) / len(st)
    print("\nClass Average:", round(avg, 2))

# =========================
# MENU SYSTEM
# =========================
while True:

    print("""
========================
 STUDENT MANAGEMENT MENU
========================
1. Show All Students
2. Search Student
3. Top Student
4. Class Average
5. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        show_all()

    elif choice == "2":
        search_student()

    elif choice == "3":
        top_student()

    elif choice == "4":
        average()

    elif choice == "5":
        print("Exiting... Bye 👋")
        break

    else:
        print("Invalid Choice")  