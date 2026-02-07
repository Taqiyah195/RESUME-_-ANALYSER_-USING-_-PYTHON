# Resume Analyzer using Python
# Loops and Conditions Based Mini Project

skills = ["Python", "Java", "C", "C++", "SQL", "HTML", "CSS", "JavaScript", "Machine Learning"]

matched_skills = []   # ✅ defined here

# Read resume file
file = open("resume.py", "r)
resume = file.read().lower()
file.close()

while True:
    print("\n----- Resume Analyzer Menu -----")
    print("1. View Resume")
    print("2. Analyze Skills")
    print("3. Show Match Percentage")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Resume Content ---")
        print(resume)

    elif choice == 2:
        matched_skills.clear()   # now Python knows this variable
        for skill in skills:
            if skill.lower() in resume:
                matched_skills.append(skill)

        print("\nMatched Skills:")
        for s in matched_skills:
            print("-", s)

    elif choice == 3:
        total = len(skills)
        matched = len(matched_skills)

        if total > 0:
            percentage = (matched / total) * 100

        if percentage == 100:
           percentage = 90

        else:
            percentage = 0

        print("Skill Match Percentage:", round(percentage, 2), "%")

    elif choice == 4:
        print("Thank you for using Resume Analyzer")
        break

    else:
        print("Invalid choice. Try again.")
