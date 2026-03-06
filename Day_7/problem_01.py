# Hospital Bed Allocation Optimization

class Solution:

    def solution(self, intervals):
        n = len(intervals)

        arrival = []
        discharge = []

        for i in intervals:
            arrival.append(i[0])
            discharge.append(i[1])

        arrival.sort()
        discharge.sort()

        beds = 1
        max_beds = 1

        i = 1
        j = 0

        while i < n and j < n:
            if arrival[i] < discharge[j]:
                beds += 1
                max_beds = max(max_beds, beds)
                i += 1

            else:
                beds -= 1
                j += 1

        return max_beds        
                   