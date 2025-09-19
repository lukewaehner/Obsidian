$$
\begin{aligned}
\text{Binary Search: } &\quad T(n) = T\!\left(\frac{n}{2}\right) + O(1) \\
\text{Given: } &\quad T(n) = \lg(n) \\[6pt]

\text{Base case: } &\quad T(1) = \lg(1) = 0 = O(1) \\[6pt]

\text{Inductive Hypothesis: } &\quad \forall n \le k,\; T(n) = \lg(n) \\[6pt]

\text{Inductive Step: } &\quad T(k+1) = T\!\left(\frac{k+1}{2}\right) + O(1) \\
&= \lg\!\left(\frac{k+1}{2}\right) + O(1) \\
&= \lg(k+1) - \lg(2) + O(1) \\
&= O(\lg(k+1))
\end{aligned}
$$

$$
\implies \forall n,\; T(n) = O(\lg n)
$$

