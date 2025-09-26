# Polynomial Time - O(n^d)

Time taken is $\leq c \cdot n^d$ for some fixed constant $d$.

Superset of everything we've seen until now:
- Constant is $d = 0$
- Linear is $d = 1$ 
- Quadratic is $d = 2$
- Cubic is $d = 3$
- Drone Drop Durability with 2 drones is $d = \frac{1}{2}$

Considered practical and efficient in the algorithms world. Generally true, but any $d > 3$ starts to become bad in practice.

Usually when polynomial time algorithms are found, $d$ is subsequently improved.

**Notable Example:** Checking if a number is prime
- AKS polynomial time primality checking algorithm history:
  - 2002: $d = 12$
  - 2004: brought down to $10.5$, then $7.5$
  - 2005: brought down to $6$
