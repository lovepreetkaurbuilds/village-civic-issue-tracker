import pytest

from issue_tracker import (
    add_issue,
    update_issue_status,
    search_issues,
    get_open_issues,
    count_issues_by_priority,
)


def test_add_issue():
    issues = []

    issue = add_issue(
        issues,
        title="Broken streetlight",
        category="Streetlight",
        location="Near school",
        priority="high",
    )

    assert issue["id"] == 1
    assert issue["title"] == "Broken streetlight"
    assert issue["status"] == "open"
    assert issue["priority"] == "high"


def test_update_issue_status():
    issues = []

    add_issue(
        issues,
        title="Garbage pile",
        category="Cleanliness",
        location="Main road",
        priority="medium",
    )

    updated_issue = update_issue_status(issues, 1, "solved")

    assert updated_issue["status"] == "solved"


def test_search_issues():
    issues = []

    add_issue(
        issues,
        title="Water leakage",
        category="Water",
        location="Near panchayat office",
        priority="high",
    )

    results = search_issues(issues, "water")

    assert len(results) == 1
    assert results[0]["title"] == "Water leakage"


def test_get_open_issues():
    issues = []

    add_issue(
        issues,
        title="Pothole",
        category="Road",
        location="Bus stand",
        priority="medium",
    )

    add_issue(
        issues,
        title="Broken drain cover",
        category="Drainage",
        location="Market",
        priority="high",
    )

    update_issue_status(issues, 1, "solved")

    open_issues = get_open_issues(issues)

    assert len(open_issues) == 1
    assert open_issues[0]["title"] == "Broken drain cover"


def test_count_issues_by_priority():
    issues = []

    add_issue(issues, "Issue 1", "Road", "A", "low")
    add_issue(issues, "Issue 2", "Water", "B", "medium")
    add_issue(issues, "Issue 3", "Electricity", "C", "high")
    add_issue(issues, "Issue 4", "Drainage", "D", "high")

    report = count_issues_by_priority(issues)

    assert report["low"] == 1
    assert report["medium"] == 1
    assert report["high"] == 2


def test_invalid_priority():
    issues = []

    with pytest.raises(ValueError):
        add_issue(
            issues,
            title="Invalid issue",
            category="Test",
            location="Test",
            priority="urgent",
        )