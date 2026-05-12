class GameConditions:
    def __init__(self, dice):
        self.dice = dice
    
    def calculate_score(self):
        score = 0
        for i in range(len(self.dice)):
            for j in range(i + 1, len(self.dice)):
                color1, val1 = self.dice[i]
                color2, val2 = self.dice[j]
                if val1 == val2:
                    if color1 == color2:
                        score += val1 * 10
                    else:
                        score += val1 + val2
        return score

    def count_matches(self):
        matches = 0
        for i in range(len(self.dice)):
            for j in range(i + 1, len(self.dice)):
                color1, val1 = self.dice[i]
                color2, val2 = self.dice[j]
                if val1 == val2:
                    matches += 1
        return matches

    def check_even_odd(self):
        even = 0
        odd = 0
        for color, val in self.dice:
            if val % 2 == 0:
                even += 1
            else:
                odd += 1
        return even, odd
        
    
    def check_blister(self):
        values = []
        for color, val in self.dice:
            values.append(val)
        values.sort()
        if values == [1, 2, 3, 4, 5] or values == [2, 3, 4, 5, 6]:
            return True
        return False
    
    def check_all_sixes(self):
        for color, val in self.dice:
            if val != 6:
                return False
        return True
