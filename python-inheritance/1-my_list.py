#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        copy = self[:]
        sorted_l = []
        while len(copy) > 0:
            min = 0
            for i in range(len(copy)):
                if copy[i] <= copy[min]:
                    min = i
            sorted_l.append(copy[min])
            del copy[min]
        print(sorted_l)


