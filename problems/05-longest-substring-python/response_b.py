def length_of_longest_substring(s):
    window = set()
    left = 0
    best = 0
    for right in range(len(s)):
        if s[right] in window:
            window.clear()
            left = right
        window.add(s[right])
        best = max(best, right - left + 1)
    return best
