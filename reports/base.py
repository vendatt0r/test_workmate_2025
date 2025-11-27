from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self, rows):
        pass

    @abstractmethod
    def headers(self):
        pass
