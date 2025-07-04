class Solution:
    def intToRoman(self, num: int) -> str:
        # List of tuples ordered from highest to lowest
        val_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"),
            (1, "I")
        ]

        roman = []

        for val, symbol in val_to_roman:
            # Append as many times as val fits into num
            while num >= val:
                roman.append(symbol)
                num -= val

        return ''.join(roman)