from Level import *
def main():
  testLevel = Level()
  testLevel.generateMapFromFile("pacmapdemo.txt")
  testLevel.printMapToConsole()

main()