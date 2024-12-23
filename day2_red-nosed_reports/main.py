
def get_safe_reports(reports:list[list[int]], dampener=False) -> int:
    """
    Return the number of safe reports.

    A report is safe if it satisfies the folloeing conditions:
        - The levels are all increasing or they are all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    """
    return sum(is_report_safe(report, dampener) for report in reports)

def is_report_safe(report:list[int], dampener=False) -> bool:
    """
    Returns True if report is safe.

    A report is safe if it satisfies the folloeing conditions:
        - The levels(list members) are all increasing
          or they are all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    """
    check = safety_check(report)

    if (not dampener) or check:
        return check
    else:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            dampener_check = safety_check(new_report)
            if dampener_check:
                return True
        return False

def safety_check(report:list[int]) -> bool:
    """
    Safety check.

    A report is safe if it satisfies the folloeing conditions:
        - The levels(list members) are all increasing
          or they are all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    """
    return (
        (is_increasing(report) or is_decreasing(report))
            and
        (between_1_and_3(report))
    )

def is_increasing(report:list[int], dampener=True, idx_=-1):
    """
    Return (True, -1) if the elements of `report` are
    steadily increasing.

    If False, also return the index at which it stopped
    increasing.
    """
    for idx in range(len(report)-1):
        if report[idx] >= report[idx+1]:
            return False
    return True

def is_decreasing(report:list[int]) -> bool:
    """
    Return (True, -1) if the elements of `report` are
    steadily decreasing.

    If False, also return the index at which it stopped
    increasing.
    """
    for idx in range(len(report)-1):
        if report[idx] <= report[idx+1]:
            return False
    return True

def between_1_and_3(report:list[int]) -> bool:
    """
    Return True if the difference between all adjacent elements
    of `report` is between 1 and 3 (inclusive).
    """
    for idx in range(len(report)-1):
        diff = abs(report[idx] - report[idx+1])
        if (diff > 3) or (diff < 1):
            return False
    return True

def render_input() -> list[list[int]]:
    """
    Return a list of lists representing all the reports
    from the Red-Nosed Reactor.
    """
    reports = []
    with open("input.txt") as f:
        for line in f.readlines():
            report_str = line.split(" ")
            report_int = [int(r) for r in report_str]
            reports.append(report_int)
    return reports


if __name__ == "__main__":
    reports = render_input()
    safe_reports_wod = get_safe_reports(reports, dampener=False)
    safe_reports_wd = get_safe_reports(reports, dampener=True)
    print("Safe Reports Without Dampener:", safe_reports_wod)
    print("Safe Reports With Dampener:", safe_reports_wd)
