
# Homework 01 - Intro
**Exercícios 0.1 e 0.2 do livro texto**

## Exercício 0.1

From the textbook, we can apply the following rules to solve the exercices:
> Commonsense rules that help simplify functions by omitting dominated terms:
> 1. Multiplicative constants can be omitted
> 2. $n^a$ dominates $n^b$ if $a>b$
> 3. Any exponential dominates any polynomial: $3^n$ dominates $n^5$ (it even dominates $2^n$ )
> 2. Any polynomial dominates any logarithm: $n$ dominates $(\log n)^3$

$\mathtt{(a)}\;f = \Theta(g)$
$\mathtt{(b)}\;f = O(g)$
$\mathtt{(c)}\;f = \Theta(g)$

$\qquad \begin{aligned}
&f = O(f) = O(100n+\log n) = O(n) \\
&g = O(g) = O(n+{(\log n)}^2) = O(n)  \\
&f = O(g) \space and \space g = O(f)
\end{aligned}$

$\mathtt{(d)}\;f = \Theta(g)$

$\qquad \begin{aligned}
g &= O(g) = O(10n\log 10n) = O(10n\log n + 10n\log 10)\\ 
&= O(n\log n) = O(f)  \\ 
f &= O(f) = O(n\log n) \\
f &= O(g) \space and \space g = O(f)
\end{aligned}$

$\mathtt{(e)}\;f = \Theta(g)$

$\qquad \begin{aligned}
&f = O(\log 2n) = O(\log n) \\ 
&g = O(\log 3n) = O(\log n) 
\end{aligned}$

$\mathtt{(f)}\;f = \Theta(g)$

$\qquad \begin{aligned}
&f = O(10 \log n) = O(\log n) \\ 
&g = O(\log n^2) = O(2 \log n) =  O(\log n)
\end{aligned}$

$\mathtt{(g)}\;f = \Omega(g)$
> Any polynomial dominates any logarithm

$$\lim_{n \to \infty} \frac{f(n)}{g(n)} =  \lim_{n \to \infty} \frac{n^{1.01}}{n\log ^2 n} = \lim_{n \to \infty} \frac{n^{0.01}}{\log ^2 n} = \infty$$
There is no constant $c$ that satisfies $f(n) \leq c * g(n).$

$\mathtt{(h)}\;f = \Omega(g)$
> Any polynomial dominates any logarithm

$$\lim_{n \to \infty} \frac{f(n)}{g(n)} =  \lim_{n \to \infty} \frac{n^2/\log n}{n(\log n)^2} = \lim_{n \to \infty} \frac{n}{(\log n)^3} = \infty$$
There is no constant $c$ that satisfies $f(n) \leq c * g(n).$

$\mathtt{(i)}\;f = \Omega(g)$

> Any polynomial dominates any logarithm

$\mathtt{(j)}\;f = \Omega(g)$

$\quad\lim_{n \to \infty} \frac {(\log n)^{\log n}}{n/ \log n} 
= \lim_{n \to \infty} \frac {(\log n)^{1 + \log n }}{n} \geq
\lim_{n \to \infty} \frac {c^{1 + \log n }}{n} = \infty$ 

$\quad\text{Where c is an arbitrary positive real number}$

$\mathtt{(k)}\;f = \Omega(g)$

> Any polynomial dominates any logarithm

$\mathtt{(l)}\;f = O(g)$

$\mathtt{(m)}\;f = O(g)$

$\mathtt{(n)}\;f = \Theta(g)$

$\quad \frac{2^n}{2^{n+1}} = \frac{1}{2}$

$\mathtt{(o)}\;f = \Omega(g)$

$\mathtt{(p)}\;f = O(g)$

$\mathtt{(q)}\;f = \Theta(g)$


## Exercício 0.2

$g(n) =  \sum_{i=o}^n c^i = 1 + c + c^2 + \cdots + c^n.$

A) Se c < 1, temos:$\quad g(n) =  \sum_{i=o}^n c^i = \frac{1}{1-c} \gt 0.$

$\quad \cdot \space g = O(g) = O(\frac{1}{1-c} \cdot 1) = O(1), \text{onde } \frac{1}{1-c} \text{ é apenas uma constante multiplicativa que pode ser omitida}$

$\quad \cdot \space \text{Do mesmo modo } \frac{1}{\frac{1}{1-c}} \lt 1, \text{ portanto } 1=
O(g).$

$\quad \text{Logo, } g = \Theta(1)$

B) Se c = 1, então:$\quad g(n) =  \sum_{i=o}^n 1^i = \sum_{i=o}^n 1 = n+1$

$\quad \cdot \space g = O(g) = O(n+1) = O(n)$

$\quad \cdot \space \frac{n}{g(n)} = \frac{n}{n+1} \lt 1, \text{ portanto } n=
O(g).$

$\quad \text{Logo, } g = \Theta(n)$

C) se c > 1, então: $\quad g(n) = 1 + c + c^2 + \cdots + c^n$

$\quad \cdot \space g = O(1 + c + c^2 + \cdots + c^n) = O(c^n) \text{, pois } c^n \text{ domina todos os outros exponenciais.}$

$\quad \cdot \space \frac{c^n}{g(n)} = \frac{c^n}{1 + c + c^2 + \cdots + c^n} \lt 1, \text{ portanto } c^n=
O(g).$


$\quad \text{Logo, } g = \Theta(c^n)$
