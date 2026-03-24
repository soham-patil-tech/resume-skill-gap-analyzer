import json
import os

# ---------- LOAD JOB ROLE DATA ----------
def load_roles():
    try:
        with open("data/roles.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ roles.json file not found. Check path: data/roles.json")
        return {}

# ---------- READ RESUME ----------
def read_resume(path):
    try:
        with open(path, "r") as file:
            return file.read().lower()
    except FileNotFoundError:
        print("❌ Resume file not found.")
        return ""

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
    return [word for word in weak_words if word.lower() in resume_text]

# ---------- CALCULATE SCORE ----------
def calculate_score(found, total):
    if total == 0:
        return 0
    return round((len(found) / total) * 100, 2)

# ---------- MAIN ----------
def main():
    roles = load_roles()

    if not roles:
        return

    print("\nAvailable Roles:")
    for role in roles.keys():   # ✅ FIXED
        print(f"- {role.title()}")

    choice = input("\nChoose a role: ").lower()

    if choice not in roles:
        print("❌ Invalid role selected.")
        return

    resume_text = read_resume("sample_resume.txt")

    if not resume_text:
        return

    skills = roles[choice].get("skills", [])          # ✅ SAFE ACCESS
    weak_words = roles[choice].get("weak_words", [])  # ✅ SAFE ACCESS

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
    if weak_found:
        for w in weak_found:
            print(f"  - {w}")
    else:
        print("  - None")

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
