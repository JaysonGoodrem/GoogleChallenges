"""
MINION LABOR SHIFTS
Jayson Goodrem 5th March 2020

Inputs
data:   A list of less than 100 integers.
        Each integer is the ID of the Minion working that day.
n:      An integer.
        This is the maximum number of times a Minion can be placed on this job.

Output
data:   A list of less than 100 integers.
        The original input list with the Minions exceeding the maximum number of repeats removed.
"""

def solution(data, n):
    try:
        n = int(n)
    except ValueError:
        print("Fatal error: n must be an integer.")
        return

    # Create a dictionary to record to store where each Minion ID is repeated.
    # Keys: each minion ID.
    # Values: a list of index values where that Minion ID in the data list.
    repeats = {}
    index = 0
    try:
        for assignment in data:
            if assignment in repeats:
                repeats[assignment].append(index)
            else:
                repeats[assignment] = [index]
            index = index+1
    except TypeError:
        print("Fatal error: Minion list is an invalid data type.")
        return

    # Remove any Minion ID repeating more than n times.

    # Find all minions with too many repeats.
    # Then turn their ID to None in the data list.
    for minion in repeats:
        if len(repeats[minion]) > n:    # This minion works this job too much
            for i in repeats[minion]:
                data[i] = None

    # Remove all the Nones from the data list
    while data.count(None):
        data.remove(None)

        
    return data

