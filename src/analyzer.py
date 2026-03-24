import json

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

# ---------- ANALYZE SKILLS (IMPROVED) ----------
def analyze_skills(resume_text, required_skills):
    found = []
    missing = []

    for skill in required_skills:
        skill_words = skill.lower().split()

        # ✅ Match if ALL words of skill exist
        if all(word in resume_text for word in skill_words):
            found.append(skill)
        else:
            missing.append(skill)

    return found, missing

# ---------- FIND WEAK WORDS ----------
def find_weak_words(resume_text, weak_words):
    found = []
    for word in weak_words:
        if word.lower() in resume_text:
            found.append(word)
    return found

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

    print("\n📌 Available Roles:")
    for role in roles.keys():
        print(f"  - {role.title()}")

    choice = input("\n👉 Choose a role: ").lower().strip()

    if choice not in roles:
        print("❌ Invalid role selected.")
        return

    resume_text = read_resume("sample_resume.txt")

    if not resume_text:
        return

    skills = roles[choice].get("skills", [])
    weak_words = roles[choice].get("weak_words", [])

    found, missing = analyze_skills(resume_text, skills)
    weak_found = find_weak_words(resume_text, weak_words)
    score = calculate_score(found, len(skills))

    # ---------- OUTPUT ----------
    print("\n========= 📊 ANALYSIS REPORT =========")
    print(f"🎯 Role Selected  : {choice.title()}")
    print(f"📈 Resume Score   : {score}%")

    print("\n✔ Skills Found:")
    print("  - " + "\n  - ".join(found) if found else "  - None")

    print("\n❌ Missing Skills:")
    print("  - " + "\n  - ".join(missing) if missing else "  - None")

    print("\n⚠ Weak Words Used:")
    print("  - " + "\n  - ".join(weak_found) if weak_found else "  - None")

    print("\n💡 Suggestions:")
    if score < 50:
        print("  - Resume needs major improvement.")
    elif score < 75:
        print("  - Resume is decent but can be improved.")
    else:
        print("  - Resume is strong for this role.")

    print("=====================================\n")


# ---------- RUN ----------
if __name__ == "__main__":
    main()
