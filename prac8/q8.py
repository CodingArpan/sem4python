from abc import *
class Reptile:
    @abstractmethod
    def crawl(self):
        pass
    @abstractmethod
    def sting(self):
        pass
    
class Snake(Reptile):
    
    def crawl(self):
        print("The snake is crawling.")
    def sting(self):
        print("The snake is stinging.")

class Python(Snake):
    def crawl(self):
        print("The python is crawling.")
    def sting(self):
        print("The python is stinging.")

print(issubclass(Python, Reptile))
print(isinstance(Snake(), Reptile))