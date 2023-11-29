# -*- coding:utf-8 -*-
import math
import scipy.special

class EVALChallenge:
    """Expected Number of Restriction Sites"""

    def __init__(self):
        data = []
        with open('rosalind_prob.txt', 'r') as f:
            for line in f:
                data.append(line.strip('\n'))
        self.n = int(data[0])
        self.s = data[1]
        self.As = [float(x) for x in data[2].split()]


    def calc(self):
        self.result = []
        for gcc in self.As:
            self.result.append(self.expected_number(self.n, self.s, gcc))

    def format(self):
        self.output = ' '.join((str(f) for f in self.result))

    def expected_number(self, length, motif, gcc):
        map = {}
        map['G'] = map['C'] = gcc / 2
        map['A'] = map['T'] = (1 - gcc) / 2
        number_of_positions = length - len(motif) + 1
        chance = 1
        for c in motif:
            chance *= map[c]
        return round(number_of_positions * chance, 3)

def main():
    sol = EVALChallenge()
    sol.calc()
    sol.format()
    print(sol.output)


if __name__ == "__main__":
    main()