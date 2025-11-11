def numberOfAlerts(precedingMinutes, alertThreshold, numCalls):
    n = len(numCalls)
    if n < precedingMinutes:
        return 0

    alerts = 0
    window_sum = sum(numCalls[:precedingMinutes])

    for t in range(precedingMinutes, n):
        avg_calls = window_sum / precedingMinutes
        if avg_calls > alertThreshold:
            alerts += 1
        window_sum += numCalls[t] - numCalls[t - precedingMinutes]

    return alerts


if __name__ == "__main__":
    n = int(input().strip())
    precedingMinutes = n
    alertThreshold = int(input().strip())
    numCalls = [int(x) for x in input().split()]
    print(numberOfAlerts(precedingMinutes, alertThreshold, numCalls))
