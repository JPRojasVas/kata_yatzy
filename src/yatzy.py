class Yatzy:

    ZERO = 0
    FIFTY = 50
    

    '''
    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total
    '''
    @staticmethod
    def chance(*dice):
        return sum(dice)

    '''
    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    '''
    @staticmethod
    def yatzy(*dice):
        return Yatzy.FIFTY if len(set(dice)) == 1 else Yatzy.ZERO

    '''
    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 1):
            sum += 1
        if (d2 == 1):
            sum += 1
        if (d3 == 1):
            sum += 1
        if (d4 == 1):
            sum += 1
        if (d5 == 1):
            sum += 1

        return sum
    '''

    @staticmethod
    def ones(*dice):
        total = 0
        for n in dice:
            if n == 1:
                total += n
        return total

    '''
    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 2):
            sum += 2
        if (d2 == 2):
            sum += 2
        if (d3 == 2):
            sum += 2
        if (d4 == 2):
            sum += 2
        if (d5 == 2):
            sum += 2
        return sum
    '''

    @staticmethod
    def twos(*dice):
        total = 0
        for n in dice:
            if n == 2:
                total += n
        return total

    '''
    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        s = 0
        if (d1 == 3):
            s += 3
        if (d2 == 3):
            s += 3
        if (d3 == 3):
            s += 3
        if (d4 == 3):
            s += 3
        if (d5 == 3):
            s += 3
        return s
    '''

    @staticmethod
    def threes(*dice):
        total = 0
        for n in dice:
            if n == 3:
                total += n
        return total

    '''
    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    '''

    @staticmethod
    def fours(*dice):
        total = 0
        for n in dice:
            if n == 4:
                total += n
        return total

    @staticmethod
    def fives(*dice):
        total = 0
        for n in dice:
            if n == 5:
                total += n
        return total

    @staticmethod
    def sixes(*dice):
        total = 0
        for n in dice:
            if n == 6:
                total += n
        return total

    '''
    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0
    '''
    @staticmethod
    def pair(*dice):
        numbers = []
        for n in range(1, 7):
            if dice.count(n) == 2:
                numbers.append(n)
        if numbers == []:
            return 0
        return max(numbers) * 2

    '''
    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0
    '''
    @staticmethod
    def two_pair(*dice):
        numbers = []
        for n in range(1, 7):
            if dice.count(n) >= 2:
                numbers.append(n)
        print(numbers)
        if len(numbers) == 2:
            return sum(numbers) * 2
        return 0

    '''
    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0
    '''
    @staticmethod
    def three_of_a_kind(*dice):
        numbers = []
        for n in range(1, 7):
            if dice.count(n) >= 3:
                numbers.append(n)
        if numbers == []:
            return 0
        return max(numbers) * 3

    '''
    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0
    '''
    @staticmethod
    def four_of_a_kind(*dice):
        numbers = []
        for n in range(1, 7):
            if dice.count(n) >= 4:
                numbers.append(n)
        if numbers == []:
            return 0
        return max(numbers) * 4

    '''
    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0
    '''

    @staticmethod
    def small_straight(*dice):
        numbers = sorted(dice)
        if sorted(numbers) == [1, 2, 3, 4, 5]:
            return 15
        return 0
        
    '''
    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0
    '''
    @staticmethod
    def large_straight(*dice):
        numbers = sorted(dice)
        if sorted(numbers) == [2, 3, 4, 5, 6]:
            return 20
        return 0
        
    '''
    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
    '''

    @staticmethod
    def full_house(*dice):
        unique_numbers = set(dice)
        pair = 0
        three_of_a_kind = 0
        for number in unique_numbers:
            count = dice.count(number)
            if count == 2:
                pair = number * 2
            elif count == 3:
                three_of_a_kind = number * 3
        if pair and three_of_a_kind:
            return pair + three_of_a_kind
        else:
            return 0
