from collections import defaultdict
from .base import BaseReport


class PerformanceReport(BaseReport):
    def headers(self):
        return ["position", "avg_performance"]

    def generate(self, rows):
        perf = defaultdict(list)

        for row in rows:
            try:
                pos = row["position"]
                perf_value = float(row["performance"])
                perf[pos].append(perf_value)
            except (KeyError, ValueError):
                continue

        result = [
            [position, round(sum(values) / len(values), 2)]
            for position, values in perf.items()
        ]

        return sorted(result, key=lambda r: r[1], reverse=True)
