from issue_tracker import add_issue, list_issues, update_issue_status, search_issues
from storage import load_issues, save_issues


def print_issue(issue):
    print(
        f"[{issue['id']}] {issue['title']} | "
        f"Category: {issue['category']} | "
        f"Location: {issue['location']} | "
        f"Priority: {issue['priority']} | "
        f"Status: {issue['status']}"
    )


def show_menu():
    print("\nVillage Civic Issue Tracker")
    print("---------------------------")
    print("1. Add issue")
    print("2. View all issues")
    print("3. Update issue status")
    print("4. Search issues")
    print("5. Exit")


def handle_add_issue(issues):
    title = input("Enter issue title: ")
    category = input("Enter category: ")
    location = input("Enter location: ")
    priority = input("Enter priority (low/medium/high): ").lower()

    try:
        issue = add_issue(issues, title, category, location, priority)
        save_issues(issues)
        print("\nIssue added successfully:")
        print_issue(issue)
    except ValueError as error:
        print(f"Error: {error}")


def handle_view_issues(issues):
    if not issues:
        print("No issues found.")
        return

    for issue in list_issues(issues):
        print_issue(issue)


def handle_update_status(issues):
    try:
        issue_id = int(input("Enter issue ID: "))
    except ValueError:
        print("Issue ID must be a number.")
        return

    new_status = input("Enter new status (open/in_progress/solved): ").lower()

    try:
        issue = update_issue_status(issues, issue_id, new_status)

        if issue is None:
            print("Issue not found.")
            return

        save_issues(issues)
        print("\nIssue updated successfully:")
        print_issue(issue)

    except ValueError as error:
        print(f"Error: {error}")


def handle_search(issues):
    keyword = input("Enter search keyword: ")
    results = search_issues(issues, keyword)

    if not results:
        print("No matching issues found.")
        return

    for issue in results:
        print_issue(issue)


def main():
    issues = load_issues()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_issue(issues)
        elif choice == "2":
            handle_view_issues(issues)
        elif choice == "3":
            handle_update_status(issues)
        elif choice == "4":
            handle_search(issues)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()