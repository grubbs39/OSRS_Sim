class probability_of_drops_math:

    def drop(x, number_of_kills, name):
        from numpy.random import choice
        from collections import Counter  
        
        item_drops = 1 / x
        z = 1 - item_drops
        item2 = name, "Nothing"
        probability2 = [item_drops, z]
        data = []
        count = Counter(data)
        for n in range(number_of_kills):
            item1 = choice(item2, p = probability2)
            data = item1.split("\n")
            count.update(data)
        return count
