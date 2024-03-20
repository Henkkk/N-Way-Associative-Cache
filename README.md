# N-Way-Associative-Cache

The purpose of cache is to speed up memory accesses by storing recently used chunks of memory. Now, main memory (RAM) is nice and cheap. Not as cheap as disk memory, but cheap nevertheless. The disadvantage of this sort of memory is that it is a bit slow. An access from main memory into a register may take 20-50 clock cycles. However, there are other sorts of memory that are very fast, that can be accessed within a single clock cycle. This fast memory is what we call cache.

### Cache replacement policies
Least recently used (LRU):
Discards least recently used items first. This algorithm requires keeping track of what was used and when, which is cumbersome. It requires "age bits" for cache lines, and tracks the least recently used cache line based on them. When a cache line is used, the age of the other cache lines changes.
