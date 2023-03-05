# Efficient Portfolio

This is a project for dealing with an efficient portfolio by using python.

## 1. Definition of Efficient Portfolio

An efficient portfolio is a portfolio (a combination of various financial assets) that offers the highest expected return for a given level of risk, or the lowest level of risk for a given expected return.

We can express the above sentence as the next mathematical formula

$$
\min_{\mu_{p}=c}\sigma_{p}^{2}\text{ or }\max_{\sigma_{p}^{2}=c}\mu_{p}
$$

## 2. Virtual example of Efficient Portfolio
To understand the above condition formulas vividly, I'm going to set a portfolio comprised of two virtual stocks: $A$ and $B$ 

Let $x_{A}$ and $x_{B}$ as portions of stock A and B each. That is, $x_{A} + x_{B} = 1$. So portfolio $R = x_{A}A + x_{B}B$. 
A mean and variance of $R$ (a.k.a return and volatility) is as follow:
1. $\mu_{R}=x_{A}\mu_{A}+x_{B}\mu_{B}$
2. $Var(R)=x_{A}^{2}\sigma_{A}^{2}+x_{B}^{2}\sigma_{B}^{2}+2x_{A}x_{B}\sigma_{AB}$

We need to assume several information about stock $A$ and $B$. Means and Variances are as follow:

1. $\mu_{A}=10\$,\mu_{B}=5$$
2. $\sigma_{A}=2\$,\sigma_{B}=2\$,\sigma_{AB}=1\$$

If an investor wants to design an efficient portfolio given a return of 6 dollars, below is the condition formula for getting what he wants. 

$$
\min_{10x_{A}+5x_{B}=6}4x_{A}^{2}+4x_{B}^{2}+2x_{A}x_{B}\times1
$$


## 3. Realistic example of Efficient Portfolio

In this project, I will tackle korean five companys: 
1. LG Electronics
2. Naver
3. KEPCO (Korea Electric Power Corporation)
4. Samsung Electronics 
5. Yuhan

I generated 50000 portfolio simulations and plotted them. Also I drew an efficient frontier as below 

![efficient portfolio](https://user-images.githubusercontent.com/90128043/222964721-2f9383e1-a31f-4235-82ef-f788019efe64.jpg)
