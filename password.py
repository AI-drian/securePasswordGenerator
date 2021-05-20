import random


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specials = "/&%#!?;:.,-_%{}[]()"

combined = lower_case + upper_case + numbers + specials
length = 15
password = "".join(random.sample(combined, length))
print(password)
    