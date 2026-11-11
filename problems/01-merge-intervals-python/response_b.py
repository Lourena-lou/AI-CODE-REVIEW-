def merge_intervals(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()

    result = []
    active = 0
    current_start = None
    for position, delta in events:
        if delta == 1:
            if active == 0:
                current_start = position
            active += 1
        else:
            active -= 1
            if active == 0:
                result.append([current_start, position])
    return result
