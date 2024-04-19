class Solution:
  def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    ans = []

    for i in reversed(range(len(shifts) - 1)):
      shifts[i] += shifts[i + 1]
      print(shifts[i])

    for c, shift in zip(s, shifts):
       print(c, shift)
       ans.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))

    return ''.join(ans)