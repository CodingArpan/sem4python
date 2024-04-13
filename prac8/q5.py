class Lion:
    def roar(self):
        print("Roar")
    
class Cub(Lion):
    def play(self):
        print("Playing")

simba = Cub()
simba.roar()
simba.play()

