from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        def insertion_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            return arr
        seats = [3, 1, 5]
        students = [2, 7, 4]
        
        seats = insertion_sort(seats)
        students = insertion_sort(students)

        print(f'seats: {seats}')
        print(f'students: {students}')

        return sum(abs(seats[i] - students[i]) for i in range(len(seats)))