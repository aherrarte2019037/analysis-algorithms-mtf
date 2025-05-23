from typing import List, Tuple

__all__ = ["mtf", "imtf"]

def mtf(sequence: List[int], initial_config: List[int]) -> Tuple[int, List[str]]:
    config = initial_config.copy()
    total_cost = 0
    logs: List[str] = []

    for req in sequence:
        pos = config.index(req)
        cost = pos + 1
        before = config.copy()
        config.pop(pos)
        config.insert(0, req)
        logs.append(
            f"Config before: {before} | Request: {req} | Cost: {cost} | Config after: {config}"
        )
        total_cost += cost

    return total_cost, logs


def imtf(sequence: List[int], initial_config: List[int]) -> Tuple[int, List[str]]:
    config = initial_config.copy()
    total_cost = 0
    logs: List[str] = []

    for idx, req in enumerate(sequence):
        pos = config.index(req)
        cost = pos + 1
        before = config.copy()
        lookahead = sequence[idx + 1 : idx + pos]
        if req in lookahead:
            config.pop(pos)
            config.insert(0, req)
        logs.append(
            f"Config before: {before} | Request: {req} | Cost: {cost} | Config after: {config}"
        )
        total_cost += cost

    return total_cost, logs 