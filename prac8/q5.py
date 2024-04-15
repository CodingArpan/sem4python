class Lion:
    legs=4
    _ears=2
    __mane=1
    def roar(self):
        print("Roar")
        print(self.legs, self._ears, self.__mane)
    
class Cub(Lion):
    def play(self):
        print("Playing")

simba = Cub()
simba.roar()
simba.play()
print(simba.legs)
print(simba._ears)
print(simba.__mane)

