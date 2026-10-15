from abc import abstractmethod, ABC
from enum import Enum, auto

class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()

class ListStrategy(ABC):

    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    @abstractmethod
    def add_list_item(self, buffer, item):
        pass


class MarkDownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f"* {item}\n")

class HTMLListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"  <li>{item}</li>\n")


class TextPropcessor:
    def __init__(self, list_strategy: ListStrategy=HTMLListStrategy()) -> None:
        self.buffer = []
        self.strategy = list_strategy

    def append_list(self, items):
        ls = self.strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format: OutputFormat):
        if format == OutputFormat.HTML:
            self.strategy = HTMLListStrategy()
        elif format == OutputFormat.MARKDOWN:
            self.strategy = MarkDownListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self) -> str:
        return "".join(self.buffer)


if __name__ == "__main__":
    items = ["foo", "bar", "baz"]
    p = TextPropcessor()
    p.append_list(items)
    print(p)
    p.set_output_format(OutputFormat.MARKDOWN)
    p.clear()
    p.append_list(items)
    print(p)