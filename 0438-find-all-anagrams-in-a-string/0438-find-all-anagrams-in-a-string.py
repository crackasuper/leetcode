class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        length_s, length_p = len(s), len(p)

        window_counter =  Counter(s[:length_p - 1])
        p_pattern = Counter(p)

        result = []


        for  i in range(length_p - 1, length_s):
            window_counter[s[i]] += 1

            if p_pattern == window_counter:
                result.append(i - length_p + 1)

            left_most = s[i - length_p + 1]#removing left most from the string
            window_counter[left_most] -= 1 # remove first value to slide window

            if window_counter[left_most] == 0:
                del window_counter[left_most]

        return result



        