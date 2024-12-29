ActivationMagicNumbers = [50, 34, 53, 51, 51, 52, 52, 56]
ActivationString = ""

SkyperRIC = int(input("RIC of Skyper: "))

for i in ActivationMagicNumbers:
	ActivationString += chr((SkyperRIC & 7) + i)

print(f"Send: {ActivationString} to RIC: {SkyperRIC} with fuction 2") 
