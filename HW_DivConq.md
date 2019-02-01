# Exercícios Divide and Conquer

## Ex. 2.3
### (A) $T(n) = 3T(n/2) + O(n)$
$$\begin{aligned}
T(n) &\le 3T(n/2) + cn \\
&\le 3[3T(n/4) + cn/2] + cn = 9T(n/4) + cn \cdot (1 + 3/2)\\
&\le 9[3T(n/8) + cn/4] + cn \cdot (5/2) = 27 T(n/8) + cn \cdot (1 + 3/2 + 9/4)\\
&\le 27[3T(n/16) + cn/8] + cn \cdot (19/4) = 81 T(n/16) + cn \cdot (1 + 3/2 + 9/4 + 27/8)\\
& \;\text{ }\vdots \\
\end{aligned}
$$
General term is
$$ T(n) \le 3^kT(n/2^k) + cn \sum_{i=0}^{k-1} (3/2)^k $$
Taking $k = log_2(n)$, we get
$$\begin{aligned}
T(n) &\le 3^{\log_2(n)}T(1) + cn \left(\frac{1 - (3/2)^{\log_2(n)}}{1 - (3/2)}\right)\\
&\le 3^{\log_23 \cdot \log_3(n)}T(1) + 2cn \left((3/2)^{\log_23 \cdot \log_3(n)} - 1\right) \\
&\le n^{\log_23}T(1) + 2cn \left(\frac{n^{\log_23}}{n} - 1\right) \\
&\le n^{\log_23}T(1) + 2cn^{\log_23} - 2cn = O(n^{\log_23})\\
\end{aligned}$$

### (B) $T(n) = T(n-1) + O(1)$
$$\begin{aligned}
T(n) &\le T(n-1) + c \\
&\le [T(n-2) + c] + c = T(n-2) + 2c\\
&\le [T(n-3) + c] + 2c = T(n-3) + 3c\\
& \;\text{ }\vdots \\
\end{aligned}
$$
General term is
$$ T(n) \le T(n-k) + kc $$
Taking $k = n-1$, we get $T(n) \le T(1) + (n-1)c = O(n)$

## Ex. 2.4
>**Master Theorem** If $T(n) = aT(n/b) + O(n^d )$ for some constants a > 0, b > 1, and d ≥ 0, then
> $$T(n) \begin{cases} O(n^d) &\text{if $d \gt \log_ba$}\\
> O(n^d \log n) &\text{if $d = \log_ba$}\\
> O(n^{\log_ba}) &\text{if $d \lt \log_ba$} \end{cases}$$

From the result of **Master Theorem**, we can find out divide-and-conquer algorithms' complexity. 

**Algorithm A** has recurrence $T(n) = 5T(n/2)+O(n)$, where $a=5,  b=2, d=1$, which implies complexity $O(n^{\log_25})$.

**Algorithm B** has recurrence $T(n) = 2T(n-1)+O(1)$. We can't use the *Master Theorem* in this case. However, we know that the general term is $$T(n) = 2^kT(n-k) + O(1) \sum_{i=0}^{k-1} 2^k$$ Taking $k = n-1$, we get $T(n) = 2^{n-1}T(1) + O(1)(2^{n-1}-1) \implies O(2^n)$, exponential complexity.

**Algorithm C** has recurrence $T(n) = 9T(n/3)+O(n^2)$, where $a=9,  b=3, d=2$, which implies complexity $O(n^2 \log n)$.

I would choose **Algorithm C** which has the smallest complexity.

## Ex. 2.12
We can state the Function **f(n)** recurrence as $f(n) = 2f(n/2) + O(1)$, where for each call of the function, it compares the argument value and, if True, it calls itself twice with half of it's argument's value and prints a sentence, which is a constant time operation.

The big-$O$ notation represents the algorithm complexity, but also, in this case, the upper bound of print calls.

From the **Master Theorem**, we know that this algorith complexity is $O(n)$, so that fuction **f** will call print no more then $c\cdot n$ times, where $c$ is a constant.

On the other hand, we get the general term as 
$$f(n) = 2^k f(n/2^k) + O(1) \cdot \sum_{i=0}^{k-1} 2^k$$
Taking $k = \log_2n$, we get $f(n) = n*f(1) + O(1) \cdot (n-1)$, where $f(1)$ does not call print and $n-1$ constant operations, which are compare the argument's value and print the sentece. So the funtion **f** calls print at least $c' \cdot n$ times, where $c'$ is a constant.

In other words, the number of  **f** calls print


## Ex. 2.14
Just do a slightly change in the Mergesort algorithm. 

In the merge function, add the equal comparison between elements of the two lists been merged and drop any item in one of the lists that is duplicated when merging back. 

The Mergesort algorithm has complexity $O(n \log n)$, so does the resulting Remove Duplicates algorithm, since the additional operation has a constant complexity (it's just a comparision between elements).
