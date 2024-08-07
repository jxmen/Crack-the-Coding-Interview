class Solution:
    numDict = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }

    # 자리를 나눠서 재귀함수로 구현?
    # 23 -> Twenty Three
    # 123 -> 1/23으로 쪼개기
    # 뒤에서부터 쪼개고 뒤집기?
    # ["Twenty Three", "One Hundred"]
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        if num < 100:
            if num <= 20:
                return self.numDict[num]

            string = ''
            string += self.numDict[int(str(num)[0] + '0')]

            num = int(str(num)[1])
            if num != 0:
                string += ' '
                string += self.numDict[num]
            
            return string

        if num < 1000:
            # 앞에 숫자 + Hundred와 뒤에 잘라낸 숫자 2개를 붙인다.
            string = ''
            string += self.numDict[int(str(num)[0])]
            string += ' Hundred '

            # 뒤에 붙는 0은 Zero를 붙이지 않는다. ex) 100
            back_num = int(str(num)[1:])
            if back_num != 0:
                string += self.numberToWords(back_num)
            return string.strip()

        # num string을 3개 단위로 쪼갠다.
        # 123000 -> 123 / 000
        # 123 -> 1 / 23

        string = ''
        units = ["", "Thousand", "Million", "Billion"]
        split_number_strings = self.split_number_by_threes(num)
        for i in range(len(split_number_strings)):
            i_num = int(split_number_strings[i])
            # 뒤에 붙는 0은 Zero를 붙이지 않는다. ex) 123000
            if i_num == 0: 
                continue
            words = self.numberToWords(i_num)
            string += words + ' ' + units[len(split_number_strings) - i - 1] + ' '

        return string.strip()

    def split_number_by_threes(self, num: int) -> list:
        num_str = str(num)
        parts = []
        while num_str:
            parts.insert(0, num_str[-3:])
            num_str = num_str[:-3]
        return parts
