VALID_STATUSES = ["open", "in_progress", "solved"]
VALID_PRIORITIES = ["low", "medium", "high"]


def get_next_issue_id(issues):
    if not issues:
        return 1

    highest_id = max(issue["id"] for issue in issues)
    return highest_id + 1


def add_issue(issues, title, category, location, priority):
    if priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high.")

    issue = {
        "id": get_next_issue_id(issues),
        "title": title,
        "category": category,
        "location": location,
        "priority": priority,
        "status": "open",
    }

    issues.append(issue)
    return issue


def list_issues(issues):
    return issues


def find_issue_by_id(issues, issue_id):
    for issue in issues:
        if issue["id"] == issue_id:
            return issue

    return None


def update_issue_status(issues, issue_id, new_status):
    if new_status not in VALID_STATUSES:
        raise ValueError("Status must be open, in_progress, or solved.")

    issue = find_issue_by_id(issues, issue_id)

    if issue is None:
        return None

    issue["status"] = new_status
    return issue


def search_issues(issues, keyword):
    results = []

    for issue in issues:
        text = (
            issue["title"] + " "
            + issue["category"] + " "
            + issue["location"] + " "
            + issue["priority"] + " "
            + issue["status"]
        )

        if keyword.lower() in text.lower():
            results.append(issue)

    return results