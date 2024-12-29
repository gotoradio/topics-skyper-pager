SendToTopicSkyperString = ""
MessageSkyper = ""

RubricID = input("Rubric ID: ")
MessageNumber = input("MessageNumber: ")
Message = input("Message: ")

SendToTopicSkyperString += chr(int(RubricID) + int(0x1f))

SendToTopicSkyperString += chr(int(MessageNumber) + 0x20)

for i in Message:
    MessageSkyper += chr(ord(i) + 1)

SendToTopicSkyperString += MessageSkyper

print(f"Send: {SendToTopicSkyperString} to RIC: 4528 with function 3")
