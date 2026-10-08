class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0]* len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                result[st[-1]] = i - st[-1]
                st.pop()

            st.append(i)

        return result