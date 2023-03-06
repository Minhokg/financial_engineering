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

1. $\mu_{A}=9,\mu_{B}=3$ ($)
2. $\sigma_{A}=2,\sigma_{B}=1,\sigma_{AB}=1$ ($)

If an investor wants to design an efficient portfolio given a return of 6 dollars, below is the condition formula for getting what he wants. 

$$
\min_{9x_{A}+3x_{B}=6}4x_{A}^{2}+x_{B}^{2}+2x_{A}x_{B}\times1
$$

This is a simple optimization problem. 

$$
\begin{align*}
x_{B}=2-3x_{A}\Longrightarrow & 4x_{A}^{2}+(2-3x_{A})^{2}+2x_{A}(2-3x_{A})\\
= & 7x_{A}^{2}-8x_{A}+4
\end{align*}
$$

In summary, what an inverstor has to find is the root of the next formula

$$
\arg\min7x_{A}^{2}-8x_{A}+4, \quad \frac{1}{3}\leq x_{A}\leq\frac{2}{3}
$$

Because $X_{B} = 2 - 3x_{A}$ and $0\leq x_{B} \leq 1$, so the range of $x_{A}$ is like that. Fortunately, the root of the above formula is $\frac{4}{7}$, whici is in the range of $x_{A}$. In conclusion, an efficieint portfolio is comprised of $\frac{4}{7}A$ and $\frac{3}{7}B$

## 3. Generalized Efficient Portfolio

We don't have to confine ourselves to a portfolio comprised of two shares. We can deal with arbitrary numbers of stocks through matrix algebra.

Let's assume that stocks $S_i, i\in I=(1,2,...,k)$ has its own mean and standard deviation ($\mu_i, \sigma_i$). So a mean vector and variance-covariance matrix is as follows.

$$
\mu=\left[\begin{array}{c}
\mu_{1}\\
\mu_{2}\\
\vdots\\
\mu_{k}
\end{array}\right],\sum=\left[\begin{array}{cccc}
\sigma_{1}^{2} & \sigma_{12} & \cdots & \sigma_{1k}\\
\sigma_{21} & \sigma_{2}^{2} & \cdots & \sigma_{2k}\\
\vdots & \vdots & \ddots & \vdots\\
\sigma_{k1} & \sigma_{k2} & \cdots & \sigma_{k}^{2}
\end{array}\right]
$$

And if we set a weight vector as 

$$
\boldsymbol{x}=\left[\begin{array}{c}
x_{1}\\
x_{2}\\
\vdots\\
x_{k}
\end{array}\right],\sum_{i\in I}x_{i}=1
$$

The mean and the variance of portfolio $R$ is in such a way 

$$
\begin{align*}
\mu_{R} & =\boldsymbol{x^{t}}\mu=\sum_{i\in I}x_{i}\mu_{i}\\
\sigma_{R}^{2} & =\boldsymbol{x^{t}}\sum\boldsymbol{x}=\left[\begin{array}{cccc}
x_{1} & x_{2} & \cdots & x_{k}\end{array}\right] \sum\left[\begin{array}{c}
x_{1}\\
x_{2}\\
\vdots\\
x_{k}
\end{array}\right]\\
 & =\sum_{i\in I}x_{i}^{2}\sigma_{i}^{2}+2\sum_{i\neq j}x_{i}x_{j}\sigma_{ij}
\end{align*}
$$

So, to find out the most efficient portfolio, if we fix $\mu_{R} = \mu_0$, the below condition has to be solved.

$$

$$

## 4. Realistic example of Efficient Portfolio

In this project, I will tackle korean five companys: 
1. LG Electronics
2. Naver
3. KEPCO (Korea Electric Power Corporation)
4. Samsung Electronics 
5. Yuhan

I generated 50000 portfolio simulations and plotted them. Also I drew an efficient frontier as below 

![efficient portfolio](https://user-images.githubusercontent.com/90128043/222964721-2f9383e1-a31f-4235-82ef-f788019efe64.jpg)
