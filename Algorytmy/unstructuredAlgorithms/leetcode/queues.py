from typing import List

# https://leetcode.com/problems/flood-fill/
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    queue = []
    already_done = set()
    in_bounds = lambda r,c: r >= 0 and r < len(image) and c >= 0 and c < len(image[0])

    def append_if_in_bound(r,c):
        if in_bounds(r,c) and image[sr][sc] == image[r][c] and (r,c) not in already_done:
            queue.append((r,c))
            already_done.add((r,c))

    append_if_in_bound(sr,sc)
    while len(queue) != 0:
        r,c = queue.pop(0)
        if not in_bounds(r,c):
            continue

        append_if_in_bound(r, c-1)
        append_if_in_bound(r, c+1)
        append_if_in_bound(r-1, c)
        append_if_in_bound(r+1, c)

    for r,c in already_done:
        image[r][c] = color        

    return image