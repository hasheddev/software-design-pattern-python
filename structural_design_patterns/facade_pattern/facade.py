class Buffer:
    def __init__(self, width=30, height=20) -> None:
        self.wisth = width
        self.height = height
        self.buffer = [" "] * (width * height)

    def write(self, text):
        self.buffer += text

    def __getitem__(self, key):
        return self.buffer.__getitem__(key)


class Viewport:
    def __init__(self, buffer=Buffer()) -> None:
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
  def __init__(self):
    b = Buffer()
    self.current_viewport = Viewport(b)
    self.buffers = [b]
    self.viewports = [self.current_viewport]

  # high-level
  def write(self, text):
    self.current_viewport.buffer.write(text)

  # low-level
  def get_char_at(self, index):
    return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
  c = Console()
  c.write('hello')
  ch = c.get_char_at(604)
  print(ch)