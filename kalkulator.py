print("Prosty Kalkulator")

z = input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:  ")
x = int(input("Podaj składnik 1:  "))
y = int(input("Podaj składnik 2:  "))


operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y}

if z == "1":
    print(operators["+"])
elif z == "2":
    print(operators["-"])
elif z == "3":
    print(operators["*"])
elif z == "4":
    print(operators["/"])
else:
    print("Error: operator not found(make sure you used the designated operators)")