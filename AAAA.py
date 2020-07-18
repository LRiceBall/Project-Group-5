query = int(input("Pick a Number 1-10"))

if (query < 1 or query > 10):
    query = int(input("Pick a number that's allowed"))

answer = ""

if (query == 1):
    answer = "aon"
elif (query == 2):
    answer = "dó"
elif (query == 3):
    answer = "trí"
elif (query == 4):
    answer = "ceathair"
elif (query == 5):
    answer = "cúig"
elif (query == 6):
    answer = "sé"
elif (query == 7):
    answer = "seacht"
elif (query == 8):
    answer = "ocht"
elif (query == 9):
    answer = "naoi"
elif (query == 10):
    answer = "deach"


print(f"Your number was: {answer}, comhghairdeas")