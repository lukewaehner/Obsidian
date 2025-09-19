## Arithmetic Averages vs. Geometric Averages
- Arithmetic average return answers the question: "What was your return in an average year over a particular period"
- Geometric average return answers the question: "What was your average compound return per year over a particular period?"
- When do we use each?
	- 
## Historical Average Returns
- A useful number to help summarize historical financial data is the simple, or arithmetic average
- If you add up the returns for large-company stocks from 1926 through 2015, you get about 1,067 percent.
- Because there are 90 returns, the average return is about 11.9%. How do we get this?
- If you make a guess about the size of the return for a year selected at random, the best guess is 11.9%
- The formula for average return is:
$$
	\text{Historical Average Return} = \frac{\sum_{i=1}^n \text{Yearly Return}}{n}
$$
## Arithmetic Averages vs. Geometric Averages
- Arithmetic average tells you what you earned in one typical year
- Geometric average tells you what you actually earned per year on average, compounded annually, if you buy-and-hold
- When we talk about average returns, we generally are talking about arithmetic average returns
- For forecasting future returns:
	- Arithmetic is probably too high for long forecasts
	- Geometric is probably too low for short forecasts

### Example Calculating a Geometric Average return
- Using the supplied stock data

| Year | % Return |
| ---- | -------- |
| 2009 | 26.46    |
| 2010 | 15.06    |
| 2011 | 2.11     |
| 2012 | 16.00    |
Calculate:
$$
$1 
\cdot (1.2646) 
\cdot (1.1506)
\cdot (1.0211)
\cdot (1.1600)
$$
This implies that the above calculation would be the same as:
$$
(1+\text{Geometric Return})^4
$$
But, we need to solve for the geometric return, which we can do with:
$$
\text{Geometric Return} = 
($1 
\cdot (1 + \text{Ret 2009}) 
\cdot (1 + \text{Ret 2010}) 
\cdot (1 + \text{Ret 2011}) 
\cdot (1 + \text{Ret 2012}) 
)^{\frac{1}{4}}-1
$$

> The generalized formula then becomes
$$
1+\text{Geometric average return}^n 
= 
(1+\text{return}_1) \times
(1+\text{return}_2) \times
\ ... \ \times
(1+\text{return}_n)
$$

---
