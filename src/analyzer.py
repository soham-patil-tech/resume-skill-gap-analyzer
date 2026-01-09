import json

# ---------- LOAD JOB ROLE DATA ----------
def load_roles():
    with open("data/roles.json", "r") as file:
        return json.load(file)


# ---------- READ RESUME ----------
def read_resume(path):
    with open(path, "r") as file:
        return file.read().lower()


# ---------- ANALYZE SKILLS ----------
def analyze_skills(resume_text, required_skills):
    found = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_text:
            found.append(skill)
        else:
            missing.append(skill)

    return found, missing


# ---------- FIND WEAK WORDS ----------
def find_weak_words(resume_text, weak_words):
    return [word for word in weak_words if word in resume_text]


# ---------- CALCULATE SCORE ----------
def calculate_score(found, total):
    return round((len(found) / total) * 100, 2)


# ---------- MAIN ----------
def main():
    roles = load_roles()

    print("\nAvailable Roles:")
    for role in roles:
        print(f"- {role.title()}")

    choice = input("\nChoose a role: ").lower()

    if choice not in roles:
        print("❌ Invalid role selected.")
        return

    resume_text = read_resume("sample_resume.txt")

    skills = roles[choice]["skills"]
    weak_words = roles[choice]["weak_words"]

    found, missing = analyze_skills(resume_text, skills)
    weak_found = find_weak_words(resume_text, weak_words)
    score = calculate_score(found, len(skills))

    print("\n========= ANALYSIS REPORT =========")
    print(f"Role Selected     : {choice.title()}")
    print(f"Resume Score      : {score}%")

    print("\n✔ Skills Found:")
    for s in found:
        print(f"  - {s}")

    print("\n❌ Missing Skills:")
    for s in missing:
        print(f"  - {s}")

    print("\n⚠ Weak Words Used:")
    for w in weak_found:
        print(f"  - {w}")

    print("\n💡 Suggestions:")
    if score < 50:
        print("- Resume needs major improvement.")
    elif score < 75:
        print("- Resume is decent but can be improved.")
    else:
        print("- Resume is strong for this role.")

    print("=================================\n")


if __name__ == "__main__":
    main()
