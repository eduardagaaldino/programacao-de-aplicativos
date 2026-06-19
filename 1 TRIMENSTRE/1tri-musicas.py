print("---------- Gerenciador de Playlist----------")

playlist = ["ilha", "Meteoro", "morena", "chuva de arroz", "te vivo"]
 
print(f"\nplaylist antiga: {playlist} ")

playlist.remove("morena")
playlist.pop(0)

print(f"playlist atualizada: {playlist} ")
print("\n--------------------------------------------")