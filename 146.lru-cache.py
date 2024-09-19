#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from typing import *

# @lc code=start
class DoubleLinkedNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __update_rank(self, key: str):
        node = self.__key_to_node.get(key)
        if node == self.__tail:
            if self.__capacity == 2:
                self.__head = node
                self.__tail = node.prev
                node.next = self.__tail
                node.prev = None
                self.__tail.prev = node
                self.__tail.next = None
                return
            elif self.__capacity == 1:
                node.prev = None
                node.next = None
                self.__head = node
                self.__tail = node
                return
                
        prev = node.prev
        next = node.next
        node.prev = None
        node.next = self.__head
        self.__head.prev = node
        prev.next = next

    def __init__(self, capacity: int):
        self.__capacity: int = capacity
        self.__head: Optional[DoubleLinkedNode] = None
        self.__tail: Optional[DoubleLinkedNode] = None
        self.__len: int = 0
        self.__key_to_node: dict[str, DoubleLinkedNode] = {}
        self.__node_to_key: dict[str, DoubleLinkedNode] = {}

    def get(self, key: int) -> int:
        if key in self.__key_to_node:
            self.__update_rank(key)
            return self.__key_to_node[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.__key_to_node:
            self.__update_rank(key)
        else:
            new_node = DoubleLinkedNode(value, None, self.__head)
            self.__key_to_node[key] = new_node
            self.__node_to_key[new_node] = key
            if self.__head is not None:
                self.__head.prev = new_node
            self.__head = new_node
            if self.__tail is None:
                self.__tail = new_node
            
            self.__len += 1
            
            if self.__len == 2:
                self.__tail.prev = new_node
            
            if self.__len == self.__capacity + 1:
                tail_node_key = self.__node_to_key.pop(self.__tail)
                tail = self.__key_to_node.pop(tail_node_key)
                self.__tail = tail.prev
                self.__len -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    lru.get(2)
    lru.put(1, 1)
    lru.put(4, 1)
    lru.get(2)