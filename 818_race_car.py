class Solution:
    def racecar(self, target: int) -> int:
        from collections import deque

        queue = deque([(0, 1, 0)])  # (position, speed, steps)
        visited = set((0, 1))

        while queue:
            position, speed, steps = queue.popleft()

            # If we reach the target, return the number of steps
            if position == target:
                return steps

            # Accelerate instruction
            next_position, next_speed = position + speed, speed * 2
            if (
                next_position,
                next_speed,
            ) not in visited and 0 <= next_position < 2 * target:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

            # Reverse instruction
            next_position, next_speed = position, -1 if speed > 0 else 1
            if (next_position, next_speed) not in visited:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

        return -1  # This line should never be reached
