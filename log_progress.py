import json
import os
import datetime
import subprocess

# Config
LOG_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daily_log.json')

def get_input(prompt, required=True):
    while True:
        val = input(prompt).strip()
        if not val and required:
            print("This field is required. Please enter a value.")
            continue
        return val

def main():
    print("=" * 50)
    print("      Data Analyst Learning Tracker & Git Committer")
    print("=" * 50)

    # 1. Gather logs info
    title = get_input("Enter log title (e.g., SQL Window Functions, DAX Basics): ")
    
    print("\nSelect Category:")
    print("1. Skills (Excel, SQL, Power BI concepts)")
    print("2. Projects (Working on dashboards or datasets)")
    print("3. Career (Resume updates, mock interviews, networking)")
    
    cat_choice = get_input("Choose category (1-3) or type custom category: ")
    if cat_choice == "1":
        category = "Skills"
    elif cat_choice == "2":
        category = "Projects"
    elif cat_choice == "3":
        category = "Career"
    else:
        category = cat_choice if cat_choice else "Skills"

    description = get_input("\nEnter description of what you learned/did: ")

    # Generate Date
    today_date = datetime.date.today().strftime("%B %d, %Y")

    new_entry = {
        "date": today_date,
        "title": title,
        "category": category,
        "description": description
    }

    # 2. Update daily_log.json
    try:
        if os.path.exists(LOG_FILE_PATH):
            with open(LOG_FILE_PATH, 'r', encoding='utf-8') as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
        else:
            logs = []
    except Exception as e:
        print(f"Error reading {LOG_FILE_PATH}: {e}")
        logs = []

    # Insert new log at the beginning (newest first)
    logs.insert(0, new_entry)

    try:
        with open(LOG_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
        print(f"\n[Success] Added entry to {LOG_FILE_PATH}!")
    except Exception as e:
        print(f"Error writing to {LOG_FILE_PATH}: {e}")
        return

    # 3. Ask to push to Git
    push_to_git = get_input("\nDo you want to commit and push this update to GitHub? (y/n): ").lower()
    if push_to_git in ['y', 'yes']:
        try:
            print("\nStaging files...")
            subprocess.run(["git", "add", LOG_FILE_PATH], check=True)
            
            commit_message = f"Learn Log: {title} ({today_date})"
            print(f"Committing with message: '{commit_message}'...")
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            
            print("Pushing to remote repository...")
            subprocess.run(["git", "push"], check=True)
            print("\n[Git Success] Contribution graph updated! Green square secured. 🟢")
        except subprocess.CalledProcessError as e:
            print(f"\n[Git Error] Command failed: {e}")
            print("Make sure this directory is a git repository with an active remote backend.")
        except FileNotFoundError:
            print("\n[Git Error] Git is not installed or not in PATH.")
    else:
        print("\nSkipped git commit. You can commit manually later.")

if __name__ == "__main__":
    main()
