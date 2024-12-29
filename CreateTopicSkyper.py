RubricNameSkyper = ""

RubricAdress = input("Topic Adress 1-95: ")
RubricName = input("Topic Name: ")

RubricAdressSkyper = chr(int(RubricAdress) + int(0x1f))

for i in RubricName:
    RubricNameSkyper += chr(ord(i) + 1)

CreateRubricString = f"1{RubricAdressSkyper}*{RubricNameSkyper}"

print(f"Send: {CreateRubricString} to RIC: 4512 with function 3")
