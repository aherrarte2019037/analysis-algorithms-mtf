from typing import List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class AccessRecord:
    request: int
    position_before: int
    cost: int
    moved_to_front: bool

class MTFNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Optional['MTFNode'] = None
        self.prev: Optional['MTFNode'] = None
        self.access_count: int = 0
        self.last_accessed: int = -1
    
    def __repr__(self) -> str:
        return f"Node({self.value})"

class MTFLinkedList:
    def __init__(self, initial_config: List[int]):
        self.head: Optional[MTFNode] = None
        self.tail: Optional[MTFNode] = None
        self.size: int = 0
        self.total_cost: int = 0
        self.access_history: List[AccessRecord] = []
        self.step_counter: int = 0
        
        for value in initial_config:
            self._append_node(value)
    
    def _append_node(self, value: int) -> MTFNode:
        new_node = MTFNode(value)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        return new_node
    
    def _find_node_and_position(self, value: int) -> Tuple[MTFNode, int]:
        current = self.head
        position = 0
        
        while current:
            if current.value == value:
                return current, position
            current = current.next
            position += 1
        
        raise ValueError(f"Value {value} not found in list")
    
    def _move_to_front(self, node: MTFNode) -> None:
        if node == self.head:
            return
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if node == self.tail:
            self.tail = node.prev
        
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        
        if self.tail is None:
            self.tail = node
    
    def access(self, value: int, move_to_front: bool = True) -> int:
        try:
            node, position = self._find_node_and_position(value)
        except ValueError:
            raise ValueError(f"Cannot access {value}: not in list")
        
        cost = position + 1
        self.total_cost += cost
        
        node.access_count += 1
        node.last_accessed = self.step_counter
        
        will_move = move_to_front and position > 0
        record = AccessRecord(
            request=value,
            position_before=position,
            cost=cost,
            moved_to_front=will_move
        )
        self.access_history.append(record)
        
        if will_move:
            self._move_to_front(node)
        
        self.step_counter += 1
        return cost
    
    def get_configuration(self) -> List[int]:
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def get_analytics(self) -> dict:
        config = self.get_configuration()
        
        node_stats = {}
        current = self.head
        position = 0
        while current:
            node_stats[current.value] = {
                'current_position': position,
                'access_count': current.access_count,
                'last_accessed_step': current.last_accessed
            }
            current = current.next
            position += 1
        
        return {
            'current_configuration': config,
            'total_cost': self.total_cost,
            'total_accesses': len(self.access_history),
            'average_cost': self.total_cost / len(self.access_history) if self.access_history else 0,
            'node_statistics': node_stats
        }

class MTFProcessor:
    @staticmethod
    def execute_mtf(sequence: List[int], initial_config: List[int]) -> Tuple[int, List[str]]:
        mtf_list = MTFLinkedList(initial_config)
        logs = []
        
        for request in sequence:
            config_before = mtf_list.get_configuration()
            cost = mtf_list.access(request, move_to_front=True)
            config_after = mtf_list.get_configuration()
            
            log_line = f"Config before: {config_before} | Request: {request} | Cost: {cost} | Config after: {config_after}"
            logs.append(log_line)
        
        return mtf_list.total_cost, logs
    
    @staticmethod
    def execute_imtf(sequence: List[int], initial_config: List[int]) -> Tuple[int, List[str]]:
        mtf_list = MTFLinkedList(initial_config)
        logs = []
        
        for idx, request in enumerate(sequence):
            config_before = mtf_list.get_configuration()
            
            try:
                _, position = mtf_list._find_node_and_position(request)
            except ValueError:
                raise ValueError(f"Request {request} not found in configuration")
            
            lookahead_window = sequence[idx + 1 : idx + position]
            should_move = request in lookahead_window
            
            cost = mtf_list.access(request, move_to_front=should_move)
            config_after = mtf_list.get_configuration()
            
            log_line = f"Config before: {config_before} | Request: {request} | Cost: {cost} | Config after: {config_after}"
            logs.append(log_line)
        
        return mtf_list.total_cost, logs

def mtf_linked(sequence: List[int], initial_config: List[int]) -> Tuple[int, List[str]]:
    return MTFProcessor.execute_mtf(sequence, initial_config)

def imtf_linked(sequence: List[int], initial_config: List[int]) -> Tuple[int, List[str]]:
    return MTFProcessor.execute_imtf(sequence, initial_config)

if __name__ == "__main__":
    config = [0, 1, 2, 3, 4]
    requests = [2, 1, 3, 2, 0]
    
    print("=== Sophisticated MTF with Linked List ===")
    total_cost, logs = mtf_linked(requests, config)
    
    for log in logs:
        print(log)
    print(f"Total cost: {total_cost}")
    
    mtf_list = MTFLinkedList(config)
    for req in requests:
        mtf_list.access(req)
    
    print("\n=== Analytics ===")
    analytics = mtf_list.get_analytics()
    for key, value in analytics.items():
        print(f"{key}: {value}") 