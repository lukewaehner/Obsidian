
---

## Multi-Stage DDM

More realistic model with different growth rates over time.

Eventually must assume constant growth rate g.

---

## Formula

$$
P_0 = \frac{Div_1}{(1+r)^1} + \frac{Div_2}{(1+r)^2} + ... + \frac{Div_N + P_N}{(1+r)^N}
$$

Where:

$$
P_N = \frac{Div_{N+1}}{r - g}
$$

---

## Example

Walmart: Just paid dividend of $3.23. Dividends grow 8% for 4 years, then 3% forever. Required return 7%.

**Step 1: Calculate dividends**

- $Div_1 = \$3.23 \times 1.08 = \$3.49$
- $Div_2 = \$3.23 \times 1.08^2 = \$3.77$
- $Div_3 = \$3.23 \times 1.08^3 = \$4.07$
- $Div_4 = \$3.23 \times 1.08^4 = \$4.39$

**Step 2: Calculate terminal value**

$$
P_4 = \frac{Div_5}{r-g} = \frac{\$4.39 \times 1.03}{0.07 - 0.03} = \$113.16
$$

**Step 3: Calculate present value**

$$
P_0 = \frac{\$3.49}{1.07} + \frac{\$3.77}{1.07^2} + \frac{\$4.07}{1.07^3} + \frac{\$4.39 + \$113.16}{1.07^4} = \$99.55
$$
