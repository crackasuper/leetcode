class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        counter = 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j-1]:
                counter += 1
            else:
                chars[i] = chars[j-1]
                i = i + 1
                if counter > 1:
                    for k in str(counter):
                        chars[i] = k
                        i += 1
                counter = 1
        return i