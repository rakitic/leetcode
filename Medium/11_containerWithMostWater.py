def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        res = max(res, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res