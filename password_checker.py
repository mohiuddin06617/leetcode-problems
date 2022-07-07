class Solution:
    def __init__(self):
        super(Solution, self).__init__()
        self.min_len = 6
        self.max_len = 20

    def password_length_checker(self, pass_len):
        if self.min_len <= pass_len <= self.max_len:
            return True, 0
        elif pass_len < self.min_len:
            return False, self.min_len - pass_len
        elif pass_len > self.max_len:
            return False, self.max_len - pass_len

    def lower_upper_case_digit_checker(self, password):
        lower_status = False
        upper_status = False
        digit_status = False

        for index, alphabet in enumerate(password):
            if alphabet.islower():
                lower_status = True
            elif alphabet.isupper():
                upper_status = True
            elif alphabet.isdigit():
                digit_status = True

        return lower_status and upper_status and digit_status

    def consecutive_char_check(self, pass_len, password):
        consecutive_status = False
        for index, char in enumerate(password):
            start_index = index
            end_index = index + 3

            if end_index > pass_len:
                end_index = pass_len

            if end_index <= pass_len:
                sliced_string = password[start_index:end_index]
                if sliced_string.isalpha():
                    consecutive_status = len(set(sliced_string)) <= 1

            if consecutive_status:
                return consecutive_status

        return consecutive_status

    def strongPasswordChecker(self, password: str) -> int:
        pass_len = len(password)
        pass_check_stat, checked_pass_len = self.password_length_checker(pass_len)

        if not checked_pass_len.__eq__(0):
            return checked_pass_len

        case_checker = self.lower_upper_case_digit_checker(password)
        consecutive_char_check = self.consecutive_char_check(pass_len, password)

        # Case Check Condition Fulfilled and Consecutive Character Doesn't Exist
        if case_checker and not consecutive_char_check:
            return 0
        else:
            # Return Total Number of Improvement Steps For Strong Password
            # True+False+True = 2
            # True+True+True = 3
            return pass_check_stat.__add__(case_checker).__add__(consecutive_char_check)


if __name__ == '__main__':
    solution = Solution()
    password = input("Enter your password: ")
    print(password)
    # print(solution.consecutive_char_check(len(password), password))

    print(solution.strongPasswordChecker(password))
