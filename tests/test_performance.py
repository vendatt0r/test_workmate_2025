from reports.performance import PerformanceReport


def test_performance_report():
    rows = [
        {"position": "Dev", "performance": "4.0"},
        {"position": "Dev", "performance": "6.0"},
        {"position": "QA", "performance": "5.0"},
    ]

    report = PerformanceReport()
    data = report.generate(rows)

    assert ["Dev", 5.0] in data
    assert ["QA", 5.0] in data
    assert len(data) == 2
