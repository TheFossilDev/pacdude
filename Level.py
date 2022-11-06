class Level:
  def __init__(self) -> None:
    self.map = []
  
  def generateMapFromFile(self, inFileName) -> None:
    input = open(inFileName, "r")
    for line in input:
      parsedLine = []
      print(len(line))
      for char in line:
        if char == ".":
          parsedLine.append(1)
        elif char == "#":
          parsedLine.append(0)
      self.map.append(parsedLine)

  def printMapToConsole(self):
    for line in self.map:
      for val in line:
        print("." if val else "#", end="")
      print()

  def render(self):
    pass