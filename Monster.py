from probability_of_drops import probability_of_drops_math
from numpy.random import choice
from collections import Counter
import random

class Monster:
    def Zulrah():
        print("Zulrah!!!")
        print("how many times do you want to fight the Zulrah?")
        y = int(input(">"))

        data = []
        answer = Counter(data)
        for n in range(y):
            x = random.randrange(100, 299)
            Zulrah_scales_odds = probability_of_drops_math.drop(1, x, "Zulrah's scales")
            answer.update(Zulrah_scales_odds)
        data = [Zulrah_scales_odds.split("\n")[0] for Zulrah_scales_odds in Zulrah_scales_odds]
        #print(answer)


        drop_tables = "Uniques", "Mutagens", "weapons&armour", "runes", "herbs", "seeds","resources", "other", "rare", "tertiary"
        probability2 = [0.00391, 0.00379, 0.1365728571, 0.1365728571, 0.1365728571, 0.1365728571, 0.1365728571, 0.1365728571,  0.03629, 0.1365728571]
        data = []
        for n in range(y):
            data = choice(drop_tables, p = probability2)
            if data == "Uniques":
                item1 = "Tanzanite fang", "Magic fang", "Serpentine visage", "Uncut onyx", "Nothing"
                probability3 = [0.0009765625, 0.0009765625, 0.0009765625, 0.0009765625, 0.99609375]
                data = choice(item, p = probability3)
                if data == "Tanzanite fang":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Tanzanite fang")
                    answer.update(data)
                elif data == "Magic fang":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Magic fang")
                    answer.update(data)
                elif data == "Serpentine visage":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Serpentine visage")
                    answer.update(data)
                elif data == "Uncut onyx":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Uncut onyx")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "Mutagens":
                item = "Tanzanite mutagen", "Magma mutagen", "Nothing"
                probability3 = [0.000076, 0.000076, 0.999848]
                data = choice(item, p = probability3)
                if data == "Tanzanite mutagen":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Tanzanite mutagen")
                    answer.update(data)
                elif data == "Magma mutagen":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Magma mutagen")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "weapons&armour":
                item = "Battlestaff", "Dragon med helm", "Dragon halberd", "Nothing"
                probability3 = [0.0403, 0.0081, 0.0081, 0.9435]
                data = choice(item, p = probability3)
                if data == "Battlestaff":
                    n = 10
                    data = probability_of_drops_math.drop(1, n, "Battlestaff")
                    answer.update(data)
                elif data == "Dragon med helm":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Dragon med helm")
                    answer.update(data)
                elif data == "Dragon halberd":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Dragon halberd")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "runes":
                item = "Death rune", "Law rune", "Chaos rune", "Nothing"
                probability3 = [0.048, 0.048, 0.048, 0.856]
                data = choice(item, p = probability3)
                if data == "Death rune":
                    n = 300
                    data = probability_of_drops_math.drop(1, n, "Death rune")
                    answer.update(data)
                elif data == "Law rune":
                    n = 200
                    data = probability_of_drops_math.drop(1, n, "Law rune")
                    answer.update(data)
                elif data == "Chaos rune":
                    n = 500
                    data = probability_of_drops_math.drop(1, n, "Chaos rune")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "herbs":
                item = "Snapdragon", "Dwarf weed", "Toadflax", "Torstol", "Nothing"
                probability3 = [0.0081, 0.0081, 0.0081, 0.0081, 0.9676]
                data = choice(item, p = probability3)
                if data == "Snapdragon":
                    n = 10
                    data = probability_of_drops_math.drop(1, n, "Snapdragon")
                    answer.update(data)
                elif data == "Dwarf weed":
                    n = 30
                    data = probability_of_drops_math.drop(1, n, "Dwarf weed")
                    answer.update(data)
                elif data == "Toadflax":
                    n = 25
                    data = probability_of_drops_math.drop(1, n, "Toadflax")
                    answer.update(data)
                elif data == "Torstol":
                    n = 10
                    data = probability_of_drops_math.drop(1, n, "Torstol")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "seeds":
                item = "Palm tree seed", "Papaya tree seed", "Calquat tree seed", "Magic seed", "Toadflax seed", "Snapdragon seed", "Dwarf weed seed", "Torstol seed", "Spirit seed", "Nothing"
                probability3 = [0.0242, 0.0242, 0.0242, 0.016, 0.0081, 0.0081, 0.0081, 0.0081, 0.00403, 0.87497]
                data = choice(item, p = probability3)
                if data == "Palm tree seed":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Palm tree seed")
                    answer.update(data)
                elif data == "Papaya tree seed":
                    n = 3
                    data = probability_of_drops_math.drop(1, n, "Papaya tree seed")
                    answer.update(data)
                elif data == "Calquat tree seed":
                    n = 2
                    data = probability_of_drops_math.drop(1, n, "Calquat tree seed")
                    answer.update(data)
                elif data == "Magic seed":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Magic seed")
                    answer.update(data)
                elif data == "Toadflax seed":
                    n = 2
                    data = probability_of_drops_math.drop(1, n, "Toadflax seed")
                    answer.update(data)
                elif data == "Snapdragon seed":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Snapdragon seed")
                    answer.update(data)
                elif data == "Dwarf weed seed":
                    n = 2
                    data = probability_of_drops_math.drop(1, n, "Dwarf weed seed")
                    answer.update(data)
                elif data == "Torstol seed":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Torstol seed")
                    answer.update(data)
                elif data == "Spirit seed":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Spirit seed")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "resources":
                item = "Snakeskin", "Runite ore", "Pure essence", "Flax", "Yew logs", "Adamantite bar", "Coal", "Dragon bones", "Mahogany logs", "Nothing"
                probability3 = [0.044, 0.044, 0.0403, 0.0403, 0.0403, 0.0323, 0.0323, 0.0323, 0.0323, 0.6619]
                data = choice(item, p = probability3)
                if data == "Snakeskin":
                    n = 35
                    data = probability_of_drops_math.drop(1, n, "Snakeskin")
                    answer.update(data)
                elif data == "Runite ore":
                    n = 2
                    data = probability_of_drops_math.drop(1, n, "Runite ore")
                    answer.update(data)
                elif data == "Pure essence":
                    n = 1500
                    data = probability_of_drops_math.drop(1, n, "Pure essence")
                    answer.update(data)
                elif data == "Flax":
                    n = 1000
                    data = probability_of_drops_math.drop(1, n, "Flax")
                    answer.update(data)
                elif data == "Yew logs":
                    n = 35
                    data = probability_of_drops_math.drop(1, n, "Yew logs")
                    answer.update(data)
                elif data == "Adamantite bar":
                    n = 20
                    data = probability_of_drops_math.drop(1, n, "Adamantite bar")
                    answer.update(data)
                elif data == "Coal":
                    n = 200
                    data = probability_of_drops_math.drop(1, n, "Coal")
                    answer.update(data)
                elif data == "Dragon bones":
                    n = 12
                    data = probability_of_drops_math.drop(1, n, "Dragon bones")
                    answer.update(data)
                elif data == "Mahogany logs":
                    n = 50
                    data = probability_of_drops_math.drop(1, n, "Mahogany logs")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "other":
                item = "Zul-andra teleport", "Manta ray", "Antidote++(4)", "Dragonstone bolt tips", "Grapes", "Coconut", "Swamp tar", "Zulrahs scales", "Nothing"
                probability3 = [0.0605, 0.048, 0.036, 0.0323, 0.0242, 0.0242, 0.0202, 0.0202, 0.7344]
                data = choice(item, p = probability3)
                if data == "Zul-andra teleport":
                    n = 4
                    data = probability_of_drops_math.drop(1, n, "Zul-andra teleport")
                    answer.update(data)
                elif data == "Manta ray":
                    n = 35
                    data = probability_of_drops_math.drop(1, n, "Manta ray")
                    answer.update(data)
                elif data == "Antidote++(4)":
                    n = 10
                    data = probability_of_drops_math.drop(1, n, "Antidote++(4)")
                    answer.update(data)
                elif data == "Dragonstone bolt tips":
                    n = 12
                    data = probability_of_drops_math.drop(1, n, "Dragonstone bolt tips")
                    answer.update(data)
                elif data == "Grapes":
                    n = 250
                    data = probability_of_drops_math.drop(1, n, "Grapes")
                    answer.update(data)
                elif data == "Coconut":
                    n = 20
                    data = probability_of_drops_math.drop(1, n, "Coconut")
                    answer.update(data)
                elif data == "Swamp tar":
                    n = 1000
                    data = probability_of_drops_math.drop(1, n, "Swamp tar")
                    answer.update(data)
                elif data == "Zulrahs scales":
                    n = 500
                    data = probability_of_drops_math.drop(1, n, "Zulrahs scales")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "rare":
                item = "Coins", "Loop half of key", "Tooth half of key", "Uncut sapphire", "Runite bar", "Nature rune", "Rune 2h sword", "Rune battleaxe", "Uncut emerald", "Law rune", "Death rune", "Steel arrow", "Rune arrow", "Adamant javelin", "Rune sq shield", "Dragonstone", "Silver ore", "Uncut ruby", "Rune kiteshield", "Dragon med helm", "Rune spear", "Shield left half", "Nature talisman", "Dragon spear", "Uncut diamond", "Rune javelin", "Nothing"
                probability3 = [0.005952381, 0.0057471264, 0.0057471264, 0.0027932961, 0.0014176354, 0.0008503401, 0.0008503401, 0.0008503401, 0.001396648, 0.0005668934, 0.0005668934, 0.0005668934, 0.0005668934, 0.0005668934, 0.0005668934, 0.0005668934, 0.0005668934, 0.0006978367, 0.0002835271, 0.0002835271, 0.0023148148, 0.0011574074, 0.0002617116, 0.0008680556, 0.0001744592, 0.0000872372, 0.9637310425]
                data = choice(item, p = probability3)
                if data == "Coins":
                    n = 3000
                    data = probability_of_drops_math.drop(1, n, "Coins")
                    answer.update(data)
                elif data == "Loop half of key":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Loop half of key")
                    answer.update(data)
                elif data == "Tooth half of key":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Tooth half of key")
                    answer.update(data)
                elif data == "Uncut sapphire":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Uncut sapphire")
                    answer.update(data)
                elif data == "Runite bar":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Runite bar")
                    answer.update(data)
                elif data == "Nature rune":
                    n = 67
                    data = probability_of_drops_math.drop(1, n, "Nature rune")
                    answer.update(data)
                elif data == "Rune 2h sword":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Rune 2h sword")
                    answer.update(data)
                elif data == "Rune battleaxe":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Rune battleaxe")
                    answer.update(data)
                elif data == "Uncut emerald":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Uncut emerald")
                    answer.update(data)
                elif data == "Law rune":
                    n = 45
                    data = probability_of_drops_math.drop(1, n, "Law rune")
                    answer.update(data)
                elif data == "Death rune":
                    n = 45
                    data = probability_of_drops_math.drop(1, n, "Death rune")
                    answer.update(data)
                elif data == "Steel arrow":
                    n = 150
                    data = probability_of_drops_math.drop(1, n, "Steel arrow")
                    answer.update(data)
                elif data == "Rune arrow":
                    n = 42
                    data = probability_of_drops_math.drop(1, n, "Rune arrow")
                    answer.update(data)
                elif data == "Adamant javelin":
                    n = 20
                    data = probability_of_drops_math.drop(1, n, "Adamant javelin")
                    answer.update(data)
                elif data == "Rune sq shield":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Rune sq shield")
                    answer.update(data)
                elif data == "Dragonstone":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Dragonstone")
                    answer.update(data)
                elif data == "Silver ore":
                    n = 100
                    data = probability_of_drops_math.drop(1, n, "Silver ore")
                    answer.update(data)
                elif data == "Uncut ruby":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Uncut ruby")
                    answer.update(data)
                elif data == "Rune kiteshield":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Rune kiteshield")
                    answer.update(data)
                elif data == "hmm":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Dragon med helm")
                    answer.update(data)
                elif data == "Rune spear":
                    n = 50
                    data = probability_of_drops_math.drop(1, n, "Rune spear")
                    answer.update(data)
                elif data == "Shield left half":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Shield left half")
                    answer.update(data)
                elif data == "Nature talisman":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Nature talisman")
                    answer.update(data)
                elif data == "Dragon spear":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Dragon spear")
                    answer.update(data)
                elif data == "Uncut diamond":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Uncut diamond")
                    answer.update(data)
                elif data == "Rune javelin":
                    n = 5
                    data = probability_of_drops_math.drop(1, n, "Rune javelin")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


            elif data == "Tertiary":
                item = "Brimstone key", "Clue scroll (elite)", "Jar of swamp", "Pet snakeling", "Nothing"
                probability3 = [0.02, 0.0133, 0.00033, 0.00025, 0.96612]
                data = choice(item, p = probability3)
                if data == "Brimstone key":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Brimstone key")
                    answer.update(data)
                elif data == "Clue scroll (elite)":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Clue scroll (elite)")
                    answer.update(data)
                elif data == "Jar of swamp":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Jar of swamp")
                    answer.update(data)
                elif data == "Pet snakeling":
                    n = 1
                    data = probability_of_drops_math.drop(1, n, "Pet snakeling")
                    answer.update(data)
                elif data == "Nothing":
                    data2 = "Nothing"
                    data = data2.split("\n")
                    answer.update(data)


        data = [data.split("\n")[0] for data in data]
        print("Dropped Items Gotten: ", answer)





    def TzTokJad():
        print("TzTokJad!!!")
        print("how many times do you want to fight the TzTok-Jad?")
        y = int(input(">"))

        TzTokJad_pet_odds = probability_of_drops_math.drop(200, y, "Jad Pet")

        print("Dropped Items Gotten: ", TzTokJad_pet_odds)



    def TzKalZuk():
        print("TzKal-Zuk!!!")
        print("how many times do you want to fight the TzKal-Zuk?")
        y = int(input(">"))

        TzKalZuk_pet_odds = probability_of_drops_math.drop(200, y, "Zuk Pet")

        print("Dropped Items Gotten: ", TzKalZuk_pet_odds)


"""
    def KBD():
        print("King Black Dragon!!!")
        print("how many times do you want to fight the King Black Dragon?")
        y = int(input(">"))

        KBD_dbones_odds = probability_of_drops_math.drop(1, y, "Dragon Bones")
        KBD_bdhide_odds = probability_of_drops_math.drop(1, y, "Black Dragon Hide")
        KBD_bdhide_odds = probability_of_drops_math.drop(1, y, "Black Dragon Hide")


        drop_tables = "pre-roll", "weapons&armour", "runes&ammunition", "resources", "other", "rare&gem","Tertiary"
        probability2 = [0.15625, 0.15625, 0.15625, 0.15625, 0.15625, 0.0625, 0.15625]
        data = []
        for n in range(number_of_kills):
            data = choice(drop_tables, p = probability2)
            if data == "pre-roll":
                item1 = "Dragon Pickaxe", "Nothing"
                probability3 = [0.00067, 0.99933]
                data2 = []
                data = choice(item1, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "weapons&armour":
                item = "Rune longsword", "Adamant platebody", "Adamant kiteshield", "Dragon med helm"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "runes&ammunition":
                item = "Fire rune", "Air rune", "Iron arrow", "Runite bolts", "Law rune", "Blood rune"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "resources":
                item = "Yew logs", "Adamantite bar", "Runite bar", "Gold ore"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "other":
                item = "Amulet of power", "Dragon arrowtips", "Dragon dart tip", "Dragon javelin heads", "Runite limbs", "Shark"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "rare&gem":
                item = "Coins", "Loop half of key", "Tooth half of key", "Uncut sapphire", "Runite bar", "Nature rune", "Rune 2h sword", "Rune battleaxe", "Uncut emerald", "Law rune", "Death rune", "Steel arrow", "Rune arrow", "Adamant javelin", "Rune sq shield", "Dragonstone", "Silver ore", "Uncut ruby", "Rune kiteshield", "Dragon med helm", "Rune spear", "Shield left half", "Nature talisman", "Dragon spear", "Uncut diamond", "Rune javelin"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "Tertiary":
                item = "Key (elite)", "Brimstone key", "Kbd heads", "Clue scroll (elite)", "Prince black dragon", "Draconic visage"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)

    def TSD():
        print("Thermonuclear smoke devil!!!")
        print("how many times do you want to fight the Thermonuclear smoke devil?")
        y = int(input(">"))

        ash_odds = probability_of_drops_math.drop(1, y, "Ashes")

        drop_tables = "weapons&armour", "runes&ammunition", "Consumables", "resources", "other", "gem","Tertiary"
        probability2 = [0.1635516667, 0.1635516667, 0.1635516667, 0.1635516667, 0.1635516667, 0.01869, 0.1635516667]
        data = []
        for n in range(number_of_kills):
            data = choice(drop_tables, p = probability2)
            if data == "weapons&armour":
                item1 = "Rune dagger", "Rune chainbody", "Red dhide body", "Rune battleaxe", "Mystic air staff", "Mystic fire staff", "Rune scimitar", "Rune knife(p++)", "Dragon scimita", "Ancient staff", "Occult necklace", "Smoke battlestaff", "Dragon chainbody"
                probability3 = [0.00067, z]
                data2 = []
                data = choice(item1, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "runes&ammunition":
                item = "Smoke rune", "Air rune", "Soul rune", "Rune arrow"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "Consumables":
                item = "Ugthanki kebab", "Tuna potato", "Sanfew serum(4)", "Prayer potion(4)"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "resources":
                item = "Pure essence", "Molten glass", "Mithril bar", "Coal", "Magic logs", "Gold ore", "Diamond"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "other":
                item = "Coins", "Tinderbox", "Fire talisman", "Bullseye lantern", "Desert goat horn", "Grimy toadflax", "Onyx bolt tips", "Snapdragon seed", "Grapes", "Magic seed", "Dragonstone ring", "Crystal key"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "gem":
                item = "Uncut sapphire", "Uncut emerald", "Uncut ruby", "Nature talisman", "Uncut diamond", "Loop half of key", "Tooth half of key", "Rune javelin", "Rune spear", "Shield left half", "Dragon spear"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
            elif data == "Tertiary":
                item = "Brimstone key", "Clue scroll (hard)", "Clue scroll (elite)", "Jar of smoke", "Pet smoke devil"
                probability3 = [0.2,0.3,0.3, z]
                data2 = []
                data = choice(item, p = probability3)
                data2.append(data)
                answer = dict(Counter(data2))
                print(answer)
"""
