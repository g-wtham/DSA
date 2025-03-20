def rotateString(s, goal) -> bool:
        return len(s) == len(goal) and goal in (s + s)