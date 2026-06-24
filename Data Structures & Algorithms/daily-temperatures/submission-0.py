class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                output.append(0)
                break
            for j in range(i + 1, len(temperatures)):
                if j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                    output.append(0)            
                if temperatures[j] > temperatures[i]:
                    output.append(j - i)
                    break
        return output
