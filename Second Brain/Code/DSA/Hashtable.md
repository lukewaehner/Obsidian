
Insert / delete / search

Dictionary = generic way to map keys to values
Hashtable = specific way to map hashes to values

Space requirement is O(k) where k = keys

Introduce a hash function
Key map to a space in the table that whole table
$h(k_0) = \text{data}$

Hashing two different keys can be collisions
We can use chaining
We use linked lists
and our table becomes a bucket of value

Maximizes randomness
Least amount of collisions

- division
- multiplicaiton
- universal hashing
- dunamic perfect hashing

division hash

h(k) = k mod m
m = size of the table


Prehash should not change at all, and have a high change of only giving back unique indexes
