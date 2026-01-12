class Solution:
    def canServe(self, arr):
        five_count = 0   # number of 5 coins we have
        ten_count = 0    # number of 10 coins we have

        for paid in arr:
            if paid == 5:
                # No change needed, just collect the 5
                five_count += 1

            elif paid == 10:
                # Need to give back 5
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1

            else:  # paid == 20
                # Need to give back 15
                # Greedy: prefer giving 10+5 if possible
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False

        return True