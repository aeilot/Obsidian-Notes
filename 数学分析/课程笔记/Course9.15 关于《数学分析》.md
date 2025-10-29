## Faculty

* 陈贤峰
* chenxf@sjtu.edu.cn
* 13917186452

## 参考书

1. 《数学分析（上册）》（第二版） 陈纪修、於崇华、金路，高等教育出版社
2. 《数学分析试题分析与解答》 上海交通大学数学系，上海交通大学出版社
3. 《数学分析学习指导》 裴兆泰、王承国、章仰文，科学出版社
4. 《数学分析习题集》 吉米多维奇编，李荣 译，高等教育出版社
5. 《数学分析中的典型问题与方法》（第二版） 裴礼文，高等教育出版社
6. 古今数学思想 2

## Grading

* 作业：解题规范（题号、补充题要抄题目），按时交
* 成绩：平时、期中、期末

## 1.1 集合及其运算

### 集合的概念

集合：一定范围内可以相互区别的事物的汇集

元素：集合中的个体称为元素

自然数集 $\mathbb{N}$，有理数 $Q$，整数 $\mathbb{Z}$，实数 $\mathbb{R}$，正实数 $\mathbb{R}_{+}$

> [!important] 自然数
> $0\not\in N$

元素：构成集合的每一个事物

$$
x \in A
$$

$$
x \not\in A
$$

空集 $\phi$ 没有元素的集合

有限集：A = {$a_{1}, a_{2}, a_{3}, \dots a_{n}$}

单点集：B={b}

无限集：不是有限集的集合（空集是有限集）

可列（数）集：A = {$a_{1}, a_{2}, a_{3}, \dots a_{n}$}

不可列集：不是可列集的**无限集**

#### 集合的特性

1. 确定性
2. 互异性

#### 集合的表示

1. 枚举法 $\begin{Bmatrix}a ,b,c, \dots\end{Bmatrix}$
2. 条件法（描述法）

### 集合的相等与包含关系

$\forall x \in A \implies x \in B$ 得到 $A\subset B$

$A\subset B , B\subset A\implies A=B$

真子集 $\subsetneq$ $\supsetneq$

子集 $\subset$ $\supset$

交、并、差、补

差 $A \setminus B$ （集合相减）

补 $C_{X}A$ or $A^C$

### 集族

若集合 A 的元素本身都是集合 X 的子集，则称 A 是集合 X 上的一个集族（集合的集合）

集族的元素可以是**部分的子集**

提出指标集 $\Lambda$ 

$$
C = \begin{Bmatrix}
A_{\lambda} | \lambda\in\Lambda
\end{Bmatrix}
$$

简写为 $\begin{Bmatrix}A_{\Lambda}\end{Bmatrix}_{\lambda\in \Lambda}$，称之为有指标集 $\Lambda$ 确定的 X 上的集族

集族的并与交运算

## 1.2 映射

X, Y 非空集合，从 X 到 Y 的映射

$$
f:X\to Y
$$$$

x\mapsto y

$$
对应关系 $f$
定义域 $D_{f}$
值域 $R_{f}$
$$

f(X) \triangleq \{ f(x) \mid x \in X \}

$$
### 几种映射类型

**满射**或**映上的** $R_{f} = Y$ or $$\forall y\in Y ,\exists x \in X\:\:\:we\;have\:\: y=f(x)$$
**单射**或**1-1映射** $$
\forall x_{1}\neq x_{2},\;f(x_{1}) \neq f(x_{2})
$$

一一对应（双射）：$f$ 既是单射也是满射

常值映射： $$

\exists y_{0}\in Y, \forall x \in X: f(x) = y_{0}

$$
恒等映射：（记作 $I_{X}$）
$$

1)\;Y=X\;\;\;\;2)\;\forall x \in X: f(x) = x

$$
### 逆映射
对于双射 $f:X\to Y$ ，则
$$

\forall y \in Y, \exists \; 唯一的\;x \in X, \;f(x) = y

$$
定义：
$$

f^{-1}: Y\to X 

$$
$$

y\mapsto x=f^{-1}(y)

$$
则 $f^{-1}$ 是 $Y\to X$ 的双射，称之为 $f$ 的逆映射


> [!NOTE] 注
> 对于单射 $f: X\to Y$
> 构造双射：$f': X\to R_{f}$ 有  $f'^{-1}: R_{f}\to X$
### 映射的复合

 设有两个映射 $f: X \to Y$ 和 $g: Y \to Z$，它们的复合记为 $g \circ f: X \to Z$，定义为 $(g \circ f)(x) = g(f(x))$，对所有 $x \in X$ 成立

$$

f^{-1}\circ f = I_{X}

$$
$$

f\circ f^{-1} = I_{Y}

$$
从右向左看，从内到外

## 板书

![[Weixin Image_20250915213524_10.jpg]]

![[Weixin Image_20250915213524_9.jpg]]

![[Weixin Image_20250915213524_6.jpg]]

![[Weixin Image_20250915213524_4.jpg]]

![[Weixin Image_20250915213524_3.jpg]]

![[Weixin Image_20250915213524_2.jpg]]