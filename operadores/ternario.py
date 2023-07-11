lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Partir RU'

print(status)

idade = 18
pode_votar = True if idade >= 18 else False

print("Pode votar" if pode_votar else "Não pode votar")
