# Act 5: Dictionaries
students = {
    "Kyla": 85, "Khen": 90, "Tabas": 78, "Steph": 88,
    "Kalex": 92, "Cedrick": 75, "Lei": 80, "James": 89,
    "Maui": 95, "Paydowan": 70, "Jaderie": 84, "Hazel":
    88,"bry": 88,"fhey": 88,"angelo": 88,"mel": 88, "kim": 98
}

while True:
    print("\n1. View all\n2. View grade\n3. Add/Update\n4. Remove\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("Student Grade:", students)
    elif choice == "2":
        name = input("Name: ")
        print(students.get(name, "Not found"))
    elif choice == "3":
        name = input("Name: ")
        grade = int(input("Grade: "))
        students[name] = grade
        print("Saved:", students)
    elif choice == "4":
        name = input("Name: ")
        print("Removed" if students.pop(name, None) else "Not found")
    elif choice == "5":
        break
    else:
        pass
