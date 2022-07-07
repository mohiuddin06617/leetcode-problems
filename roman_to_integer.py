def romanToInt(s: str):
    total = 0
    roman_numeral_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for char in s:
        total += roman_numeral_dict[char]

    if s.count("CM") > 0:
        for i in range(s.count("CM")):
            total -= 100
    if s.count("XC") > 0:
        for i in range(s.count("XC")):
            total -= 10
    if s.count("IV") > 0:
        for i in range(s.count("IV")):
            total -= 5
    return total


if __name__ == '__main__':
    print(romanToInt("MCMXCIV"))
    # print(romanToInt("III"))
