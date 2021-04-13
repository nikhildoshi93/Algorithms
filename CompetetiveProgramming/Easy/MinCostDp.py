# In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

# Train tickets are sold in 3 different ways:

# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

# Return the minimum number of dollars you need to travel every day in the given list of days.

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        def recursive_dp(i, matrix):
            if len(days) <= i:
                return 0
            
            if matrix[i] != -1:
                return matrix[i]
            
            allowance = [0,6,29]
            allowance_dict = {
                0: costs[0],
                6: costs[1],
                29: costs[2]
            }
            indexes = []
            scores = []
            for a in allowance:
                start_day = days[i]
                j = i + 1
                while (j < len(days) and days[j] - start_day <= a):
                    j += 1
                indexes.append(j-1)
                score = recursive_dp(j, matrix) + allowance_dict[a]
                scores.append(score)
            
            min_score = min(scores)
            matrix[i] = min_score
            return min_score
        
        matrix = [-1]*len(days)
        return recursive_dp(0, matrix)
