from Monster import Monster

print("Which Monster do you want to fight?")
print("1) Zulrah")
print("2) TzTok-Jad")
print("3) TzKal-Zuk")
print("4) Thermonuclear smoke devil (work in progress/ commented out)")
print("5) King Black Dragon (work in progress/ commented out)")

answer = input(">")

if answer == "1":
    Monster.Zulrah()
elif answer == "2":
    Monster.TzTokJad()
elif answer == "3":
    Monster.TzKalZuk()
elif answer == "4":
    Monster.TSD()
elif answer == "5":
    Monster.KBD()
