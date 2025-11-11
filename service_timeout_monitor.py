def findTimedOutServices(timestamp, serviceId, threshold):
    from collections import defaultdict

    service_map = defaultdict(list)
    for t, sid in zip(timestamp, serviceId):
        service_map[sid].append(t)

    timed_out = []
    for sid, times in service_map.items():
        times.sort()
        for i in range(1, len(times)):
            if times[i] - times[i - 1] > threshold:
                timed_out.append(sid)
                break

    return sorted(timed_out)


if __name__ == "__main__":
    n = int(input().strip())
    timestamps = [int(input().strip()) for _ in range(n)]
    _ = int(input().strip())  # ignore duplicate count
    serviceIds = [input().strip() for _ in range(n)]
    threshold = int(input().strip())

    result = findTimedOutServices(timestamps, serviceIds, threshold)
    for svc in result:
        print(svc)
