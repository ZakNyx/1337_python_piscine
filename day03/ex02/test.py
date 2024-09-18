from DiamondTrap import King
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("Blue")
Joffrey.set_hairs("Light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)