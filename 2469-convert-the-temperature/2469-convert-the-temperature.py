class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:

        answer = []

        kelvin = celsius + 273.15
        Fahrenheit = (celsius * 1.80) + 32.00

        answer.append(kelvin)
        answer.append(Fahrenheit)

        return answer
        