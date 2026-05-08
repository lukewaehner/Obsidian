Assumptions:
1. Investor Behavior:
	- Investors are rational, mean-variance optimizers.
	- Their common planning horizon is a single period.
	- Investors all use identical input lists, this is known as homogeneous expectations, aligns with the assumption all relevant information is publicly available
2. Market structure
	- All assets are publicly held and trade on public exchanges
	- Investors can borrow or lend at a common risk-free rate, and they can take short positions on traded securities
	- No taxes
	- No transaction costs

## Market Portfolio
All investors choose to hold (the same) market portfolio
Its on the efficient frontier, and is an optimal risky portfolio
Risk premium on market portfolio is proportional to variance (risk) of market portfolio and investor's risk aversion
$$E(R_M) = E(r_m) - r_f = \bar{A}\sigma_M^2$$
**Market Price of Risk:** 
Quantified the excess return demanded by investors to bear 1 unit of market risk
$$\frac{\text{Market risk premium}}{\text{Market variance}} = \frac{E(R_M)}{\sigma_M^2}$$
**The idea:**
A carton of eggs should be proportional to the number of eggs, and rely on the price of every one egg
Similarly, a stock should be priced with the expected annual rate of return equal to every 1 point of systemic risk that underlies the stock 

**Market Beta:**
The rate at which a business comoves with the market.
Correlation and volatility are used in this computation.
A stock can move with and more extremely than the market

**CAPM Formula:**
For any asset $i$, in a well-organized and active market:
$$\frac{E(r_i)-R_f}{\beta_i}=E(r_m)-R_f $$
Which we can isolate to:
$$ E(r_i)=R_f+[E(r_m) - R_f]\times\beta_i$$

**SML:**
In a well-organized and active market every asset should be on the SML
Its a graphical representation between Systemic Risk and Expected Return in financial markets

For a market portfolio, the slope of the SML line is:
$$\frac{E(R_M)-R_F}{\beta_M}= \frac{E(R_M)-R_F}{1}=E(R_M)-R_F$$

CAPM shows that expected returns on an asset $E(R_i)$ relies on,
- Time value of money, $R_F$
- Reward for bearing systemic risk, $E(R_M)-R_F$
- The amount of systemic risk, $\beta_M$

![[IMG-20251223193053131.png]]

```folder-overview
id: cc820ede-9747-44e6-9cb5-b8ab8416be56
folderPath: Finance/Investments/Capital Asset Pricing Model
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="cc820ede-9747-44e6-9cb5-b8ab8416be56"></span>
<span class="fv-link-list-end" id="cc820ede-9747-44e6-9cb5-b8ab8416be56"></span>
