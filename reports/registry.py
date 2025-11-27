from .performance import PerformanceReport


REPORTS = {
    "performance": PerformanceReport,
}


def get_report(name):
    if name not in REPORTS:
        raise ValueError(f"Unknown report: {name}")

    return REPORTS[name]()
