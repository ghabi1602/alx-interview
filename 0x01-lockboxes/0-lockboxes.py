#!/usr/bin/env python3
"""a module that checks if all boxes can be opened"""
from collections import deque


def canUnlockAll(boxes):
    """function definition to check if all boxes can be opened"""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    q = deque([0])
    while q:
        current_box = q.popleft()

        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                q.append(key)

    return all(opened)
