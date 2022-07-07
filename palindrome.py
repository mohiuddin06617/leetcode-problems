def isPalindrome(x: int):
    extra = ""
    string = str(x)
    len_string = len(string) - 1
    for i in range(len_string, -1, -1):
        extra += str(string[i])

    return True if string == extra else False


def isPalindromeNumber(x: int):
    sr = str(x)
    len_sr = len(sr)
    total = 0
    # print(new_last_position)
    # print(sr)
    # return last_digit
    for i in range(0, len_sr):
        new_last_position = len_sr - 1

        last_digit = int(sr[new_last_position])
        sr = sr[0:new_last_position]
        len_sr -= 1
        print(last_digit)
        print(total)
        total = total + (last_digit * 10)
    # print(total)


if __name__ == "__main__":
    print(isPalindromeNumber(123))
