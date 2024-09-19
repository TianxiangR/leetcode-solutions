/*
 * @lc app=leetcode id=146 lang=cpp
 *
 * [146] LRU Cache
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
template <typename T>
class DLinkedNode
{
private:
    void clear(DLinkedNode<T> *node)
    {
        if (node == NULL)
        {
            return;
        }

        if (node->next != NULL)
        {
            clear(node->next);
        }

        delete node;

        return;
    }

public:
    T val;
    DLinkedNode<T> *prev, *next;
    DLinkedNode(T _val) : val(_val) {}
    DLinkedNode(T _val, DLinkedNode<T> *_next) : val(_val), next(_next) {}
    DLinkedNode(T _val, DLinkedNode<T> *_next, DLinkedNode<T> *_prev) : val(_val), next(_next), prev(_prev) {}
    ~DLinkedNode()
    {
        clear(this->next);
    }
};

class LRUCache
{
private:
    int capacity, size;
    DLinkedNode<int> *tail, *head;
    unordered_map<int, DLinkedNode<int> *> map;

public:
    LRUCache(int _capacity) : capacity(_capacity), size(0), head(NULL), tail(NULL)
    {
    }

    int get(int key)
    {
        if (map.find(key) != map.end())
        {
            DLinkedNode<int> *node = map[key];
            if (node != head)
            {
                node->prev->next = node->next;
                if (node->next != NULL)
                {
                    node->next->prev = node->prev;
                }
                node->next = head;
                head->prev = node;
                head = node;
            }
            return node->val;
        }

        return -1;
    }

    void put(int key, int value)
    {
        DLinkedNode<int> *node = new DLinkedNode(value);
        map[key] = node;
        if (size < capacity)
        {
            node->next = head;
            if (head != NULL)
            {
                head->prev = node;
            }
            head = node;

            if (size == 0)
            {
                tail = node;
            }
            size++;
        }
        else
        {
            map.erase(tail->val);
            if (capacity == 1)
            {
                delete tail;
                tail = node;
                head = node;
                head->next = tail;
                tail->prev = head;
                return;
            }

            DLinkedNode<int> *new_tail = tail->prev;
            tail->prev->next = NULL;
            delete tail;
            tail = new_tail;

            node->next = head;
            head->prev = node;
            head = node;
        }
    }

    ~LRUCache()
    {
        delete head;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end
int main()
{
    LRUCache *cache = new LRUCache(2);
    cache->put(1, 1);
    cache->put(2, 2);
    cache->get(2);
    cache->put(3, 3);
    cache->get(1);
}