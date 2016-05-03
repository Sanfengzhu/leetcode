### 146. LRU Cache ###
class LRUCache(object):

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.pos = self.cnt = 0
        self.record = {}
        self.queue = []

    def _update(self):
        while self.cnt > self.capacity:
            key = self.queue[self.pos]
            if self.record[key][0] > 1:
                self.record[key][0] -= 1
            else:
                del self.record[key]
                self.cnt -= 1
            self.pos += 1

    # @return an integer
    def get(self, key):
        if key in self.record:
            self.queue.append(key)
            self.record[key][0] += 1
            return self.record[key][1]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.record:
            self.queue.append(key)
            self.record[key][0] += 1
            self.record[key][1] = value
        else:
            self.queue.append(key)
            self.record[key] = [1, value]
            self.cnt += 1
        self._update()

### 208. Implement Trie (Prefix Tree) ###
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.chd = [None] * 26
        self.end = False
        self.bj = -1

    # get ordinal number
    def get_ord(self, x):
        return ord(x)-97

class Trie(object):

    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word, mark=-1):
        cur = self.root
        for x in word:
            idx = self.root.get_ord(x)
            if not cur.chd[idx]: cur.chd[idx] = TrieNode()
            cur = cur.chd[idx]
        cur.end = True
        if mark != -1: cur.bj = mark

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for x in word:
            idx = self.root.get_ord(x)
            cur = cur.chd[idx]
            if not cur: return False

        return cur.end

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for x in prefix:
            idx = self.root.get_ord(x)
            cur = cur.chd[idx]
            if not cur: return False

        return True

### 211. Add and Search Word - Data structure design ###
class WordDictionary(object):

    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()

    # get ordinal number
    def get_ord(self, x):
        return ord(x)-97

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur = self.root
        for x in word:
            idx = self.get_ord(x)
            if not cur.chd[idx]: cur.chd[idx] = TrieNode()
            cur = cur.chd[idx]
        cur.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):

        def internal_search(cur, word):
            if not word: return cur.end

            if word[0] == '.':
                for c in cur.chd:
                    if c and internal_search(c, word[1:]):
                        return True
            else:
                idx = ord(word[0])-97
                if cur.chd[idx] and internal_search(cur.chd[idx], word[1:]):
                    return True
            return False

        return internal_search(self.root, word)

### 225. Implement Stack using Queues ###
class Stack(object):

    # initialize your data structure here.
    def __init__(self):
        self.q = []

    # @param {integer} x
    # @return {void}
    def push(self, x):
        self.q.append(x)

    # @return {void}
    def pop(self):
        tq = []
        while len(self.q)>1:
            tq.append(self.q[0])
            del self.q[0]
        del self.q
        self.q = tq

    # @return {integer}
    def top(self):
        if not self.q: return None
        return self.q[-1]

    # @return {boolean}
    def empty(self):
        return False if self.q else True

### 232. Implement Queue using Stacks ###
class Queue(object):

    # initialize your data structure here.
    def __init__(self):
        self.s1, self.s2 = [], []

    # @param {integer} x
    # @return {void}
    def push(self, x):
        self.s1.append(x)

    # @return {void}
    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        if self.s2: self.s2.pop()

    # @return {integer}
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    # @return {boolean}
    def empty(self):
        return not self.s1 and not self.s2

class PeekingIterator(object):

    # Initialize your data structure here.
    # @param {iterator} Iterator
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = None
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()

    # Returns the next element in the iteration without advancing the iterator.
    # @return {integer}
    def peek(self):
        return self.next_val

    # @return {integer}
    def next(self):
        res = self.next_val
        if self.iterator.hasNext(): self.next_val = self.iterator.next()
        else: self.next_val = None

        return res

    # @return {boolean}
    def hasNext(self):
        return self.next_val != None
