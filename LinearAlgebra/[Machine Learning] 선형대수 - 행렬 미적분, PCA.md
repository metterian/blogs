## 들어가며
### 선형대수를 왜 알아야 하는가?

DL(Deep Learning)을 이해하기 위해서는 선형대수 + 행렬미분 + 확률의 기초지식이 필요합니다. 최근에 사용되는 Transformer의 경우 attention matrix를 사용하는데

$$
\operatorname{Att}_{\leftrightarrow}(Q, K, V)=D^{-1} A V, A=\exp \left(Q K^{T} / \sqrt{d}\right), D=\operatorname{diag}\left(A 1_{L}\right)
$$

이러한 경우 행렬에 대한 이해가 필요합니다. 이번 포스팅의 목표는 선형대수와 행렬 미분의 기초를 배우고 간단히 머신러닝 알고리즘(PCA)를 유도 해보고자 합니다.

## 기본 표기법 (Basic Notation)

- $A\in \mathbb{R}^{m\times n}$는 $m$개의 행과 $n$개의 열을 가진 행렬을 의미한다.
- $x \in \mathbb{R}^n$는 $n$개의 원소를 가진 벡터를 의미한다. $n$차원 벡터는 $n$개의 행과 1개의 열을 가진 행렬로 생각할 수도 있다. 이것을 열벡터(column vector)로 부르기도 한다. 만약, 명시적으로 행벡터(row vector)를 표현하고자 한다면, $x^T$($T$는 transpose를 의미)로 쓴다.
- 벡터 $x$의 $i$번째 원소는 $x_i$로 표시한다.


$$
x=\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right]
$$


- $a_{ij}$(또는 $A_{ij}, A_{i,j}$)는 행렬 $A$의 $i$번째 행, $j$번째 열에 있는 원소를 표시한다.

$$
A=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]
$$

- $A$의 $j$번째 열을 $a_j$ 혹은 $A_{:,j}$로 표시한다.

$$
A=\left[\begin{array}{cccc}
\mid & \mid & & \mid \\
a_{1} & a_{2} & \cdots & a_{n} \\
\mid & \mid & & \mid
\end{array}\right]
$$

- $A$의 $i$번째 행을 $a_i^T$ 혹은 $A_{i,:}$로 표시한다.

$$
A=\left[\begin{array}{ccc}
- & a_{1}^{T} & - \\
- & a_{2}^{T} & - \\
& \vdots & \\
- & a_{m}^{T} & -
\end{array}\right]
$$


### Python에서 벡터, 행렬의 표현 방법

```python
x = np.array([10.5, 5.2, 3.25])
```


```python
x.shape
# (3,)
```

위의 결과 같이 (3,)으로 표시가 된다. 이는 1차원 배열을 나타낸다



#### `numpy.expand_dims(a, axis)`
- Expand the shape of an array.

`np.expand_dims` 메소드를 사용해서 차원의 크기를 임의로 크게해 수 있습니다. 이는 우리가 이전의 포스팅에서 `x[:, np.newaxis]`으로 차원의 크기를 늘려주었던 방법과 동일한 방법입니다. 또한, `axis` 인자를 통해 열의 방향으로 확장할 것인지, 행의 방향으로 확장할 것인지를 지정 할 수있습니다


```python
np.expand_dims(x, axis=1) # column 방향으로 확장
"""
array([[10.5 ],
       [ 5.2 ],
       [ 3.25]])
"""
```


```python
np.expand_dims(x, axis=1).shape
# (3, 1)
```

```python
numpy.expand_dims(x, axis=0) # row 방향으로 확장,  x[np.newaxis, :] or x[np.newaxis]와 동일한 방법

"""
array([[10.5 ,  5.2 ,  3.25]])
"""
```


```python
np.expand_dims(x, axis=0).shape
#(1, 3)
```


```python
A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```


```python
A.shape
# (2, 3)
```


```python
A[0,2] # equivalent A[0][2]
# 30
```


```python
# Column vector
A[:, 1]
# array([20, 50])
```



위 벡터는 column 벡터를 추출하였지만, row 벡터 인 것처럼 보입니다. 이는 단순히 표기를 1차원 배열로 한 것일 뿐입니다.


```python
# Row vector
A[1, :]
```


    array([40, 50, 60])





## 행렬의 곱셈(Matrix Muliplication)

두 개의 행렬 $A\in \mathbb{R}^{m\times n}$, $B\in \mathbb{R}^{n\times p}$의 곱 $C = AB \in \mathbb{R}^{m\times p}$는 다음과 같이 정의된다.

$$C_{ij} = \sum_{k=1}^n A_{ik}B_{kj}$$

행렬의 곱셈을 이해하는 몇 가지 방식들이 존재 합니다.
- 벡터 $\times$ 벡터
- 행렬 $\times$ 벡터
- 행렬 $\times$ 행렬

### 벡터 $\times$ 벡터 (Vector-Vector Products)

두 개의 벡터 $x, y\in \mathbb{R}^n$이 주어졌을 때 **내적**(inner product 또는 dot product) $x^Ty$는 다음과 같이 정의된다.

$$
x^{T} y \in \mathbb{R}=\left[\begin{array}{llll}
x_{1} & x_{2} & \cdots & x_{n}
\end{array}\right]\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right]=\sum_{i=1}^{n} x_{i} y_{i}
$$

$$
x^{T} y=y^{T} x
$$


```python
x = np.array([1,2,3])
y = np.array([4,5,6])
x.dot(y)
```


    32



#### 외적
외적을 구할 때는 두 벡터의 차원이 다른 경우입니다. 내적의 경우에는 두 벡터의 차원이 같은 경우입니다.
두 개의 벡터 $x\in \mathbb{R}^m, y\in \mathbb{R}^n$이 주어졌을 때 외적(outer product) $xy^T\in \mathbb{R}^{m\times n}$는 다음과 같이 정의된다.

여기서 기억해야 할 점은 내적을 구했을 때는 스칼라값을 얻을 수 있었지만, 외적을 구했을 떄는 행령을 얻을 수 있습니다.

$$
\left.x y^{T_{*}} \in \mathbb{R}^{m \times n}=\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{m}
\end{array}\right]\left[\begin{array}{lll}
y_{1} & y_{2} & \cdots
\end{array}\right]_{n}\right]=\left[\begin{array}{cccc}
x_{1} y_{1} & x_{1} y_{2} & \cdots & x_{1} y_{n} \\
x_{2} y_{1} & x_{2} y_{2} & \cdots & x_{2} y_{n} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m} y_{1} & x_{m} y_{2} & \cdots & x_{m} y_{n}
\end{array}\right]
$$


```python
x = np.array([1,2,3])
y = np.array([4,5,6])
```


```python
x = np.expand_dims(x, axis=1) # column 방향으로 추가
y = np.expand_dims(y, axis=0) # row 방향으로 추가
x.shape, y.shape # x: column vector, y: row vector
```


    ((3, 1), (1, 3))




```python
x
```


    array([[1],
           [2],
           [3]])




```python
y
```


    array([[4, 5, 6]])




```python
np.matmul(x,y)
```


    array([[ 4,  5,  6],
           [ 8, 10, 12],
           [12, 15, 18]])





#### 외적이 유용한 경우
외적이 유용한 경우는 다음과 같습니다. 행렬 $A$는 모든 colummn이 동일한 벡터 $x$를 가지고 있다고 가정해 봅시다. 외적을 이용하면 간편하게 $x \mathbf{1}^{T}$로 나타낼 수 있습니다. ($1 \in \mathbb{R}^{n}$은 모든 원소가 1인 $n$-차원 벡터)

$$
A=\left[\begin{array}{llll}
\mid & \mid & & \mid \\
x & x & \cdots & x \\
\mid & \mid & & \mid
\end{array}\right]=\left[\begin{array}{cccc}
x_{1} & x_{1} & \cdots & x_{1} \\
x_{2} & x_{2} & \cdots & x_{2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m} & x_{m} & \cdots & x_{m}
\end{array}\right]=\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{m}
\end{array}\right]\left[\begin{array}{llll}
1 & 1 & \cdots & 1
\end{array}\right]=x \mathbf{1}^{T}
$$


```python
# column 벡터
x = np.expand_dims(np.array([1,2,3]), axis=1)
x
```


    array([[1],
           [2],
           [3]])




```python
ones = np.ones([1,4])
A = np.matmul(x, ones)
A
```


    array([[1., 1., 1., 1.],
           [2., 2., 2., 2.],
           [3., 3., 3., 3.]])





### 행렬 $\times$ 벡터 (Matrix-Vector Products)

행렬 $A\in \mathbb{R}^{m\times n}$와 벡터 $x\in \mathbb{R}^n$의 곱은 벡터 $y = Ax \in \mathbb{R}^m$이다. 이 곱을 몇 가지 측면에서 바라볼 수 있다.

#### 열벡터를 오른쪽에 곱하고($Ax$), $A$가 행의 형태로 표현되었을 때

$$
y=A x=\left[\begin{array}{ccc}
- & a_{1}^{T} & - \\
- & a_{2}^{T} & - \\
& \vdots & \\
- & a_{m}^{T} & -
\end{array}\right] x=\left[\begin{array}{c}
a_{1}^{T} x \\
a_{2}^{T} x \\
\vdots \\
a_{m}^{T} x
\end{array}\right]
$$


```python
A = np.array([
    [1,2,3],
    [4,5,6]
])
```


```python
ones = np.ones([3,1])
ones
```


    array([[1.],
           [1.],
           [1.]])




```python
np.matmul(A, ones)
```


    array([[ 6.],
           [15.]])



#### column 벡터를 오른쪽에 곱하고, $A$가 Column의 형태로 표현 되었을 때

$$
y=A x=\left[\begin{array}{cccc}
\mid & \mid & & 1 \\
a_{1} & a_{2} & \cdots & a_{n} \\
\mid & \mid & & \mid
\end{array}\right]\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right]=\left[\begin{array}{c}
1 \\
a_{1} \\
1
\end{array}\right] x_{1}+\left[\begin{array}{c}
1 \\
a_{2} \\
1
\end{array}\right] x_{2}+\cdots+\left[\begin{array}{c}
1 \\
a_{n} \\
1
\end{array}\right] x_{n}
$$


```python
A = np.array([
    [1,0,1],
    [0,1,1]
])

x = np.array([
    [1],
    [2],
    [3]
])
np.matmul(A, x)
```


    array([[4],
           [5]])




```python
for i in range(A.shape[1]):
    print('a_'+str(i)+':', A[:,i], '\tx_'+str(i)+':', x[i], '\ta_'+str(i)+'*x_'+str(i)+':', A[:,i]*x[i])
```

    a_0: [1 0] 	x_0: [1] 	a_0*x_0: [1 0]
    a_1: [0 1] 	x_1: [2] 	a_1*x_1: [0 2]
    a_2: [1 1] 	x_2: [3] 	a_2*x_2: [3 3]




## 행렬 $\times$ 행렬(Matrix-Matrix Product)

행렬 $\times$ 행렬 연산도 몇 가지 관점으로 접근할 수있다.

### 일련의 벡터 $\times$ 벡터 연산으로 표현 경우

$A$와 $B$가 행 또는 열로 표현되었는가에 따라 두가지롤 나눌 수 있다.

#### $A$가 행(row)으로 $B$가 열(column)로 표현되었을 때

$$
C=A B=\left[\begin{array}{ccc}
- & a_{1}^{T} & - \\
- & a_{2}^{T} & - \\
\vdots & \\
- & a_{m}^{T} & -
\end{array}\right]\left[\begin{array}{cccc}
\mid & \mid & & \mid \\
b_{1} & b_{2} & \cdots & b_{p} \\
\mid & \mid & & \mid
\end{array}\right]=\left[\begin{array}{cccc}
a_{1}^{T} b_{1} & a_{1}^{T} b_{2} & \cdots & a_{1}^{T} b_{p} \\
a_{2}^{T} b_{1} & a_{2}^{T} b_{2} & \cdots & a_{2}^{T} b_{p} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m}^{T} b_{1} & a_{m}^{T} b_{2} & \cdots & a_{m}^{T} b_{p}
\end{array}\right]
$$

$A \in \mathbb{R}^{m \times n}, B \in \mathbb{R}^{n \times p}, a_{i} \in \mathbb{R}^{n}, b_{j} \in \mathbb{R}^{n}$ 이기 때문에 내적값들이 자연스럽게 정의된다.

#### $A$가 열(column)으로 $B$가 행(row)로 표현되었을 때


$$
C=A B=\left[\begin{array}{cccc}
\mid & \mid & & 1 \\
a_{1} & a_{2} & \cdots & a_{n} \\
\mid & \mid & & \mid
\end{array}\right]\left[\begin{array}{ccc}
- & b_{1}^{T} & - \\
- & b_{2}^{T} & - \\
\vdots & \\
- & b_{n}^{T} & -
\end{array}\right]=\sum_{i=1}^{n} a_{i} b_{i}^{T}
$$

$AB$는 모든 $i$에 대해서 $a_{i} \in \mathbb{R}^{m}$ 와 $b_{i} \in \mathbb{R}^{p}$ 의 외적의 합니다. $a_{i} b_{i}^{T}$의 차원은 $m \times p$이다. $C$의 차원과 동일)

내적이 아니라 외적이기 때문에 결과 값이 스칼라 값이 아니라, 행렬의 값을 출력하게 된다.

### 일련의 행렬 \times 벡터 연산으로 표현하는 경우

#### $B$가 열(column)으로 표현 되었을 때

$C = AB$ 일때 $C$의 열들을 A와 B의 열들의 곱으로 나타낼 수 있다

$$
C=A B=A\left[\begin{array}{cccc}
\mid & \mid & & \mid \\
b_{1} & b_{2} & \cdots & b_{p} \\
\mid & \mid & & \mid
\end{array}\right]=\left[\begin{array}{cccc}
\mid & \mid & & \mid \\
A b_{1} & A b_{2} & \cdots & A b_{p} \\
\mid & \mid & & \mid
\end{array}\right]
$$

각각의 $c_{i}=A b_{i}$는 앞에서 설펴본 행렬 $\times$ 벡터의 두가지 관점에서 해석 할 수 있다.


#### $A$가 행(row)로 표현 되었을 때

$$
C=A B=\left[\begin{array}{ccc}
- & a_{1}^{T} & - \\
- & a_{2}^{T} & - \\
& \vdots & \\
- & a_{m}^{T} & -
\end{array}\right] B=\left[\begin{array}{ccc}
- & a_{1}^{T} R & - \\
- & a_{2}^{T} B & - \\
& \vdots & \\
- & a_{m}^{T} B & -
\end{array}\right]
$$



### 정방(Square), 삼각(triangular), 대각(diagonal), 단위(identity) 행렬들

정방행렬(square matrix): 행과 열의 개수가 동일
$$
\begin{bmatrix}
  4 & 9 & 2 \\
  3 & 5 & 7 \\
  8 & 1 & 6
\end{bmatrix}
$$

**상삼각행렬**(upper triangluar matrix): 정방 행렬 이면서, 주대각선 아래 원소들이 모두 0

$$
\left[\begin{array}{lll}
4 & 9 & 2 \\
0 & 5 & 7 \\
0 & 0 & 6
\end{array}\right]
$$

**하삼각행렬**(lower triangluar matrix): 정방 행렬 이면서, 주대각선 위 원소들이 모두 0

$$
\left[\begin{array}{lll}
4 & 0 & 0 \\
3 & 5 & 0 \\
8 & 1 & 6
\end{array}\right]
$$


**대각행렬**(digonal matrix): 정방행렬이면서, 주대각 원소들을 제외한 나머지 원소가 0

$$
\left[\begin{array}{lll}
4 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 6
\end{array}\right]
$$

`numpy.diag()` 메소드를 사용해서 대각행렬을 생성 할 수있습니다.


```python
np.diag([4,5,6]) # 주대각선의 원소만 입력
```


    array([[4, 0, 0],
           [0, 5, 0],
           [0, 0, 6]])



**단위행렬**(identity matrix) : 대각행렬이면서, 주대각 원소들이 모두 1인 행렬

$$
\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$

`numpy.eye` 함수를 이용해 단위 행렬 생성이 가능


```python
np.eye(3)
```


    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])



### 전치 (Transpose)

행렬을 전치하는 것은 그 행렬을 뒤집는 것으로 생각할 수 있다. 행렬 $A\in \mathbb{R}^{m\times n}$이 주어졌을 때 그것의 전치행렬은 $A^T \in \mathbb{R}^{n\times m}$으로 표시하고 각 원소는 다음과 같이 주어진다.

$$
\left( A^T \right)_{ij} = A_{ji}
$$

다음의 성질들이 성립한다.

- $(A^T)^T = A$
- $\left(AB\right)^T = B^TA^T$
- $(A + B)^T = A^T + B^T$

$$
A^T =
\begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6
\end{bmatrix}^T =
\begin{bmatrix}
  1 & 4 \\
  2 & 5 \\
  3 & 6
\end{bmatrix}
$$

Numpy의 `T` 속성(attribute)을 사용해서 전치행렬을 구할 수 있다.



###  대칭행렬 (Symmetic Matrices)

정방행렬 $A$가 $A^T$와 동일할 때 대칭행렬이라고 부른다. $A = -A^T$일 때는 반대칭(anti-symmetric)행렬이라고 부른다.


주대각선을 원소를 기반으로 위쪽 원소와 아래족 원소가 같다면 대칭행렬이라고 할 수 있다.

다음의 경우, 대칭행렬이라고 할 수 있다.

$$
\left[\begin{array}{ll}
1 & 3 \\
3 & 2
\end{array}\right]=\left[\begin{array}{ll}
1 & 3 \\
3 & 2
\end{array}\right]
$$


하지만, 다음의 경우는 대칭행렬이라고 할 수 없다

$$
\left[\begin{array}{ll}
1 & 3 \\
4 & 2
\end{array}\right] \neq\left[\begin{array}{ll}
1 & 4 \\
3 & 2
\end{array}\right]
$$

$AA^T$는 항상 대칭행렬이다.

$A + A^T$는 대칭, $A - A^T$는 반대칭이다.


$$A = \frac{1}{2}(A+A^T)+\frac{1}{2}(A-A^T)$$



### 대각합 (Trace)

정방행렬 $A\in \mathbb{R}^{n\times n}$의 대각합은 $\mathrm{tr}(A)$로 표시(또는 $\mathrm{tr}A$)하고 그 값은 $\sum_{i=1}^n A_{ii}$이다. 대각합은 다음과 같은 성질을 가진다.

- For $A\in \mathbb{R}^{n\times n}$, $\mathrm{tr}A = \mathrm{tr}A^T$

    대각합과 전치행렬의 대각합은 같다.
- For $A,B\in \mathbb{R}^{n\times n}$, $\mathrm{tr}(A+B) = \mathrm{tr}A + \mathrm{tr}B$
    행렬의 합을 구하고 대각합을 구하나, 대각합을 구하고 행렬의 합을 구한 것은 서로 같다.
- For $A\in \mathbb{R}^{n\times n}, t\in\mathbb{R}$, $\mathrm{tr}(tA) = t\,\mathrm{tr}A$
    대각합의 실수배는 값다.
- For $A, B$ such that $AB$ is square, $\mathrm{tr}AB = \mathrm{tr}BA$
    $AB$ 가 정방행렬일때, $\mathrm{tr}AB = \mathrm{tr}BA$
- For $A, B, C$ such that $ABC$ is square, $\mathrm{tr}ABC = \mathrm{tr}BCA = \mathrm{tr}CAB$, and so on for the product of more matrices
    여러개의 행렬이 주어졌을때, 일련의 사이클을 따라서(A,B,C 순) 대각합을 구하면 같은 값을 같게 된다


```python
A = np.array([
    [100,200,300],
    [10, 20, 30],
    [1,2,3,]
])
np.trace(A)
```




    123



### Norms

벡터의 norm은 벡터의 길이로 이해할 수 있다. $l_2$ norm (Euclidean norm)은 다음과 같이 정의된다.

$$\left \Vert x \right \|_2 = \sqrt{\sum_{i=1}^n{x_i}^2}$$

$\left \Vert x \right \|_2^2 = x^Tx$임을 기억하라.

$l_p$ norm

$$\left \Vert x \right \|_p = \left(\sum_{i=1}^n|{x_i}|^p\right)^{1/p}$$

Frobenius norm (행렬에 대해서)

$$\left \Vert A \right \|_F = \sqrt{\sum_{i=1}^m\sum_{j=1}^n A_{ij}^2} = \sqrt{\mathrm{tr}(A^TA)}$$


```python
A = np.array([
    [100,200,300],
    [10, 20, 30],
    [1,2,3,]
])

print(np.linalg.norm(A))
print(np.trace(A @ A.T)**0.5)
```

    376.0505285197722
    376.0505285197722




## 선형독립과 랭크(Rank)

벡터들의 집합 $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\} \subset \mathbb{R}^{m}$에 속하는 어떤 벡터도 나머지 벡터들의 선형 조합으로 나타 낼 수 없을 때 이를 선형독립(linear independent)라고 하고, 역으로 어떤 벡터가 나머지 벡터들을 선형 조합으로 나타내질 수 있을 때 이를 선형 종속이라고 부른다


```python
A = np.array([
    [1,4,2],
    [2,1,-3],
    [3,5,-1]
])
```

위의 행렬은 Column에 대해서 종속(dependent)되어 있습니다. 왜냐하면 한 열을 통해 다른 열을 표현 할 수 있기 때문입니다.



```python
A[:, 2] == -2*A[:, 0] + A[:, 1]
```


    array([ True,  True,  True])



Column rank: 행렬 $A\in \mathbb{R}^{m\times n}$의 열들의 부분집합 중에서 가장 큰 선형독립인 집합의 크기

Row rank: 행렬 $A\in \mathbb{R}^{m\times n}$의 행들의 부분집합 중에서 가장 큰 선형독립인 집합의 크기

모든 행렬의 column rank와 row rank는 동일하다. 따라서 단순히 $\mathrm{rank}(A)$로 표시한다. 다음의 성질들이 성립한다.

- For $A\in \mathbb{R}^{m\times n}$, $\mathrm{rank}(A) \leq \min(m, n)$. If $\mathrm{rank}(A) = \min(m, n)$, then $A$ is said to be ***full rank***.
- For $A\in \mathbb{R}^{m\times n}$, $\mathrm{rank}(A) = \mathrm{rank}(A^T)$.
- For $A\in \mathbb{R}^{m\times n}, B\in \mathbb{R}^{n\times p}$, $\mathrm{rank}(A+B) \leq \min(\mathrm{rank}(A), \mathrm{rank}(B))$.
- For $A, B\in \mathbb{R}^{m\times n}$, $\mathrm{rank}(A+B) \leq \mathrm{rank}(A) + \mathrm{rank}(B)$.


```python
np.linalg.matrix_rank(A)
```


    2



### 역행렬 (The Inverse)

정방행렬 $A\in \mathbb{R}^{n\times n}$의 역행렬 $A^{-1}$은 다음을 만족하는 정방행렬($\in \mathbb{R}^{n\times n}$)이다.

$$A^{-1}A = I = AA^{-1}$$

$A$의 역행렬이 존재할 때, $A$를 ***invertible*** 또는 ***non-singular***하다고 말한다.

- $A$의 역행렬이 존재하기 위해선 $A$는 full rank여야 한다.
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^{-1})^T = (A^T)^{-1}$


```python
A = np.array([
        [1, 2],
        [3, 4],
    ])
np.linalg.inv(A)
```


    array([[-2. ,  1. ],
           [ 1.5, -0.5]])



### 직교 행렬 (Orthogonal Matrices)

$x^Ty=0$가 성립하는 두 벡터 $x, y \in \mathbb{R}^n$를 직교(orthogonal)라고 부른다. $\|x\|_2 = 1$인 벡터 $x\in \mathbb{R}^n$를 정규화(normalized)된 벡터라고 부른다.

모든 열들이 서로 직교이고 정규화된 정방행렬 $U\in \mathbb{R}^{n\times n}$를 직교행렬이라고 부른다. 따라서 다음이 성립한다.

- $U^TU = I$
- $UU^T = I$ 이건 밑에서 증명
- $U^{-1} = U^T$
- $\|Ux\|_2 = \|x\|_2$ for any $x\in \mathbb{R}^{n}$
    $\|U x\|_{2}=\sqrt{(U x)^{\top}(U x)}=\sqrt{x^{\top} U^{\top} v x}=\sqrt{x^{\top} x}=\|x\|_{2}$

직교 행렬의 이러한 성질 때문에 직교 행렬을 이용하면 선형시스템의 해를 구하기 쉽습니다. 왜냐하면 직교행렬의 역행렬을 구하기 위해서 단순히 직교행렬의 전치행렬만 구하면 되기 때문이죠


$$
U=\left[\begin{array}{l}
\mid \\
u_{1} \ldots \\
\mid
\end{array}\right] \quad U^{\top}=\left[\begin{array}{c}
-u_{1}^{\top}- \\
\vdots
\end{array}\right]
$$

$$
U^T U = \left[\begin{array}{c}
-u_{1}^{\top}- \\
\vdots
\end{array}\right]
\left[\begin{array}{i}
\mid \\
j \ldots \\
\mid
\end{array}\right]
$$

$$
\left(U^{\top} u\right)_{i j}=u_{\vec{u}}^{\top} u_{j}\left\{\begin{array}{ll}
0 & i \neq j \\
1 & i = j
\end{array}\right.
$$


### 치역(Range), 영공간(Nullspace)

#### 벡터의 집합($\{x_1,x_2,\ldots,x_n\}$)에 대한 생성(span)
주어진 행렬을 선형결합을 통해 만들 수 있는 차원을 생성(span)한다고 표현한다.

$$\mathrm{span}(\{x_1,x_2,\ldots,x_n\}) = \left\{ v : v = \sum_{i=1}^n\alpha_i x_i, \alpha_i \in \mathbb{R} \right\}$$



#### 행렬의 치역 (range)

행렬 $A\in \mathbb{R}^{m\times n}$의 치역 $\mathcal{R}(A)$는 A의 **모든 열들에 대한 생성**(span)이다.

즉, 주어진 행렬을 사용하여 만들 수 있는 행렬변환 혹은 차원을 치역이라고 한다. 여기서 조심해야 할 부분은 치역의 차원이 $n$ 차원이라는 점이다. 즉, column의 수만큼 치역의 차원이 만들어 진다는 것이다.

$$\mathcal{R}(A) = \{ v\in \mathbb{R}^m : v = Ax, x\in \mathbb{R}^n\}$$



#### 영공간 (nullspace)

행렬 $A\in \mathbb{R}^{m\times n}$의 영공간(nullspace) $\mathcal{N}(A)$는 $A$와 곱해졌을 때 0이 되는 모든 벡터들의 집합이다. 여기서도 주의 해야할 점은 영공간의 차원은 주어진 행렬의 row의 갯수와 같다는 점이다. 즉, row의 차원 수만큼 영공간의 차원이 결정 된다.
$$\mathcal{N}(A) = \{x\in \mathbb{R}^n : Ax = 0\}$$


치역의 차원과 영공간의 차원을 살펴보면 다음과 같다. 치역의 경우 column 수가 치역의 차원 수를 결정하고, 영공간의 경우 row의 수가 영공간의 차원을 결정한다. 그러므로 주어진 행렬의 전치행렬(transpose)의 치역을 구하면 영공간의 차원과 동일게 된다.

이말을 해석하면, 치역은 A행렬의 column을 기준으로 차원을 구성하고, 영공간은 row 벡터들을 기준으로 차원을 생성한다고 이해하면 쉽다.

**중요한 성질**:

위의 성질 통해 다음과 같은 성질이 유도 될 수 있다. 임의의 $n$차원 실수 공간 $\mathbb{R}^n$에서 임의의 원소 $w$를 뽑았다고 가정해보자. 이때 이 원소 $w$는 $\mathcal{R}(A^T)$에 속한 원소 $u$와 $\mathcal{N}(A)$에 속한 원소 $v$로 분해(decompose)될 수 있다.

이는 $\mathcal{N}(A)$ 과 $\mathcal{R}(A^T)$를 합하면 실수 전체의 원소 집합 $\mathbb{R}^n$이 만들어 진다는 의미이도 하다.

$$
\{w : w = u + v, u\in \mathcal{R}(A^T), v \in \mathcal{N}(A)\} = \mathbb{R}^n ~\mathrm{and}~ \mathcal{R}(A^T) \cap \mathcal{N}(A) = \{0\}
$$
$\mathcal{R}(A^T)$와 $\mathcal{N}(A)$를 직교여공간(orthogonal complements)라고 부르고 $\mathcal{R}(A^T) = \mathcal{N}(A)^\perp$라고 표시한다.



#### 투영 (projection)

$\mathcal{R}(A)$위로 벡터 $y\in \mathbb{R}^m$의 투영(projection)은 다음과 같이 나타낼 수 있습니다.

투영의 의미는 단순히 선을 임의의 공간에 투영시켰다 라는 의미 보다는 임의의 좌표 혹은 원소를 주어진 행렬(A)의 차원에서 가장 가까운 점을 구하는 의미 입니다. (직각으로 내릴 꼿았기 때문에 가장 가까운 위치)

$$\mathrm{Proj}(y;A) = \mathop{\mathrm{argmin}}_{v\in \mathcal{R}(A)} \| v - y \|_2 = A(A^TA)^{-1}A^Ty$$


$U^TU = I$인 정방행렬 $U$는 $UU^T = I$임을 보이기
- $U$의 치역은 전체공간이므로 임의의 $y$에 대해 $\mathrm{Proj}(y;U) = y$이어야 한다.
- 모든 $y$에 대해 $U(U^TU)^{-1}Uy = y$이어야 하므로 $U(U^TU)^{-1}U^T= I$이다.
- 따라서 $UU^T = I$이다.

### 행렬식 (Determinant)

정방행렬 $A\in \mathbb{R}^{n\times n}$의 행렬식(determinant) $|A|$ (또는 $\det A$)는 다음과 같이 계산할 수 있다.

$$
|A| = A_{1,1}\times|A^{(1,1)}| - A_{1,2}\times|A^{(1,2)}| + A_{1,3}\times|A^{(1,3)}| - A_{1,4}\times|A^{(1,4)}| + \cdots ± A_{1,n}\times|A^{(1,n)}|
$$
where $A^{(i,j)}$ is the matrix $A$ without row $i$ and column $j$.

$$
A = \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 0
\end{bmatrix}
$$

위의 식을 사용하면 아래와 같이 전개된다.

$$
\begin{aligned}
|A| = 1 \times \left | \begin{bmatrix} 5 & 6 \\ 8 & 0 \end{bmatrix} \right |
     - 2 \times \left | \begin{bmatrix} 4 & 6 \\ 7 & 0 \end{bmatrix} \right |
     + 3 \times \left | \begin{bmatrix} 4 & 5 \\ 7 & 8 \end{bmatrix} \right |
\end{aligned}
$$

이제 위의 $2 \times 2$ 행렬들의 행렬식을 계산하면 된다.

$\left | \begin{bmatrix} 5 & 6 \\ 8 & 0 \end{bmatrix} \right | = 5 \times 0 - 6 \times 8 = -48$

$\left | \begin{bmatrix} 4 & 6 \\ 7 & 0 \end{bmatrix} \right | = 4 \times 0 - 6 \times 7 = -42$

$\left | \begin{bmatrix} 4 & 5 \\ 7 & 8 \end{bmatrix} \right | = 4 \times 8 - 5 \times 7 = -3$

최종결과는 다음과 같다.

$$
|A| = 1 \times (-48) - 2 \times (-42) + 3 \times (-3) = 27
$$


```python
A = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])
np.linalg.det(A)
#     27.0
```




### 행렬식의 기하학적 해석
다음과 같이 행렬이 주어 졌다고 가정 해 봅시다.

$$
\left[\begin{array}{ccc}
- & a_{1}^{T} & - \\
- & a_{2}^{T} & - \\
& \vdots & \\
- & a_{n}^{T} & -
\end{array}\right]
$$

이렇게 주어 졌을 때, 벡터들의 선형조합(단, 이 조합에서 쓰이는 계수들은 0에서 1사이)이 나타내는 $\mathbb{R}^{n}$ 공간 상의 모든 점들의 집합 $S$를 생각해보자. 즉, 행렬식이라는 것도 원소와 벡터를 결합한 일종의 선형결합이다. 단, 여기서 벡터들과 곱해지는 $\alpha$의 값은 0에서 1사이의 값을 갖는다고 해봅시다. 이를 식으로 표현하면 다음과 같습니다.

$$
S=\left\{v \in \mathbb{R}^{n}: v=\sum_{i=1}^{n} \alpha_{i} a_{i} \text { where } 0 \leq \alpha_{i} \leq 1, i=1, \ldots, n\right\}
$$

위 식을 기하학적으로 해석하면, **행렬식의 절대값은 $S$의 부피(volume)과 일치합니다**


예를 들어 행렬 $A$가 다음과 같이 주어졌다고 가정해 봅시다.

$$
A=\left[\begin{array}{ll}
1 & 3 \\
3 & 2
\end{array}\right]
$$

위 행렬의 열벡터(column vector)들은 다음과 같습니다.

$$
a_{1}=\left[\begin{array}{l}
1 \\
3
\end{array}\right] a_{2}=\left[\begin{array}{l}
3 \\
2
\end{array}\right]
$$

위 열벡터들에 $\alpha$를 곱하여 표현된 선형결합의 점들을 그림으로 표현하면 다음과 같습니다.

<img src="https://github.com/learn-programmers/programmers_kdt_II/raw/d6f59b80fb967241f3a4b1ce8d610ee5b1b69ecd/images/fig_det.png" style="zoom:33%;" />


위 그림의 평행사변형 넓이는 7인데, $A$의 행렬식인 $|A|=-7$과 같음을 확일 할 수 있습니다.
뒤에서 언급하겠지만, 확률변수에서 연속확률함수에서 확률을 구할 때 자코비안 행렬식을 사용하여 확률 값을 구했습니다. 이는 행렬식이 넓이 값과 같다는 의미과 연관이 있어서 행렬식을 통해서 확률값을 구했던 것입니다.



### 행렬식의 중요한 성질들

- $|I|=1$
- $A$의 한 개의 row(행)에 $\in \mathbb{R}$를 스칼라배 하면, 행렬식은 $t|A|$이 됩니다.

기하학적으로 생각해 보았을 때, 하나의 벡터에 스칼라배를 한다면 벡터의 길이가 스칼래배 만큼 들어나게 되고 그 만큼 면적의 크기도 늘어 나게 됩니다.

$$
\left|\left[\begin{array}{ccc}
- & t a_{1}^{T} & - \\
- & a_{2}^{T} & - \\
& \vdots & \\
- & a_{n}^{T} & -
\end{array}\right]\right|=t|A|
$$

- $A$의 두 row(행)을 교환하면 행렬식은 $-|A|$이 됩니다.

$$
\left|\left[\begin{array}{ccc}
- & a_{2}^{T} & - \\
- & a_{1}^{T} & - \\
& \vdots & \\
- & a_{n}^{T} & -
\end{array}\right]\right|=-|A|
$$

- For $A\in \mathbb{R}^{n\times n}$, $|A| = |A^T|$.
- For $A, B\in \mathbb{R}^{n\times n}$, $|AB| = |A| |B|$.
- For $A\in \mathbb{R}^{n\times n}$, $|A|=0$, if and only if A is singular (non-invertible). $A$가 singular이면 행들이 linearly dependent할 것인데, 이 경우 $S$의 형태는 부피가 0인 납작한 판의 형태가 될 것이다.
- For $A\in \mathbb{R}^{n\times n}$ and $A$ non-singular, $|A^{-1}| = 1/|A|$.





## 이차형식 (Quadratic Forms)

2차인 항으로만 구성된 다항식을 이차형식 (quadratic form)이라 한다. $n$개 변수의 이차형식은 $n \times n$ 대칭행렬 $A$를 이용하여 $x^{\top} A x$의 형태로 표현 할 수 있다

예를 들면, $4 x_{1}^{2}+5 x_{2}^{2}$, 혹은 $3 x_{1}^{2}-6 x_{1} x_{2}+7 x_{2}^{2}$과 같은 식이 이차 형식이다.

이차형식 $a_{1} x_{1}^{2}+a_{2} x_{2}^{2}+a_{3} x_{3}^{2}+a_{4} x_{1} x_{2}+a_{5} x_{2} x_{3}+a_{6} x_{1} x_{3}$은 대칭행렬 $A$를 사용하여 $x^{\top} A x$로 표현 할 수 있다.

$$
\begin{aligned}
a_{1} x_{1}^{2}+a_{2} x_{2}^{2}+a_{3} x_{3}^{2}+a_{4} x_{1} x_{2}+a_{5} x_{2} x_{3}+a_{6} x_{1} x_{3} &=\left[x_{1} x_{2} x_{3}\right]\left[\begin{array}{ccc}
a_{1} & a_{4} / 2 & a_{6} / 2 \\
a_{4} / 2 & a_{2} & a_{5} / 2 \\
a_{6} / 2 & a_{5} / 2 & a_{3}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right] \\
&=x^{\top} A x
\end{aligned}
$$


단, 이차형식은 $3 x^{2}+4 x y+y^{2}$과 같이 모든 항의 차수가 2인 것을 말하고, 이차식(quadratic expreesion)은 $3 x^{2}+2 x y+5 x-6 y+3$ 과 같이 최고차항만 차수가 2인 식을 이차식이라고 한다.

$x_{i}^{2}$ 의 계수를 $a_{i i}$ 에, $x_{i} x_{j}$ 의 계수의 $1 / 2$ 을 $a_{i j}$ 와 $a_{j i}$ 에 넣는다.

다음이 성립함을 알 수 있다.

$$
x^TAx = (x^TAx)^T = x^TA^Tx = x^T\left(\frac{1}{2}A + \frac{1}{2}A^T\right)x
$$
즉, 위 식과 같이 행렬 $A$는 대칭행렬로 표현된다.

따라서 이차형식에 나타나는 행렬을 대칭행렬로 가정하는 경우가 많다.

- 대칭행렬 $A\in \mathbb{S}^n$이 0이 아닌 모든 벡터 $x\in \mathbb{R}^n$에 대해서 $x^TAx \gt 0$을 만족할 때, 양의 정부호(positive definite)라고 부르고 $A\succ 0$(또는 단순히 $A \gt 0$)로 표시한다. 모든 양의 정부호 행렬들의 집합을 $\mathbb{S}_{++}^n$으로 표시한다.
- 대칭행렬 $A\in \mathbb{S}^n$이 0이 아닌 모든 벡터 $x\in \mathbb{R}^n$에 대해서 $x^TAx \ge 0$을 만족할 때, 양의 준정부호(positive semi-definite)라고 부르고 $A\succeq 0$(또는 단순히 $A \ge 0$)로 표시한다. 모든 양의 준정부호 행렬들의 집합을 $\mathbb{S}_{+}^n$으로 표시한다.
- 대칭행렬 $A\in \mathbb{S}^n$이 0이 아닌 모든 벡터 $x\in \mathbb{R}^n$에 대해서 $x^TAx \lt 0$을 만족할 때, 음의 정부호(negative definite)라고 부르고 $A\prec 0$(또는 단순히 $A \lt 0$)로 표시한다.
- 대칭행렬 $A\in \mathbb{S}^n$이 0이 아닌 모든 벡터 $x\in \mathbb{R}^n$에 대해서 $x^TAx \leq 0$을 만족할 때, 음의 준정부호(negative semi-definite)라고 부르고 $A\preceq 0$(또는 단순히 $A \leq 0$)로 표시한다.
- 대칭행렬 $A\in \mathbb{S}^n$가 양의 준정부호 또는 음의 준정부호도 아닌 경우, 부정부호(indefinite)라고 부른다. 이것은 $x_1^TAx_1 > 0, x_2^TAx_2 < 0$을 만족하는 $x_1, x_2\in \mathbb{R}^n$이 존재한다는 것을 의미한다.

Positive definite 그리고 negative definite 행렬은 full rank이며 따라서 invertible이다.

#### Gram matrix
임의의 행렬 $A\in \mathbb{R}^{m\times n}$이 주어졌을 때 행렬 $G = A^TA$를 Gram matrix라고 부르고 항상 positive semi-definite이다. 만약 $m\ge n$이고 $A$가 full rank이면, $G$는 positive definite이다.


### 고유값 (Eigenvalues), 고유벡터 (Eigenvectors)

정방행렬 $A\in \mathbb{R}^{n\times n}$이 주어졌을 때,
$$Ax = \lambda x, x\neq 0$$
을 만족하는 $\lambda \in \mathbb{C}$를 $A$의 고유값(eigenvalue) 그리고 $x\in \mathbb{C}^n$을 연관된 고유벡터(eigenvector)라고 부른다.


고옷값과 고유벡터는 **정방행렬**에 의한 선형변환에 대해 정의되는 개념이다. 행렬을 시용하 여 선형변환할 때, 크기 비율만 바뀔 뿐 방향은 바뀌지 않는 벡터를 **고유벡터**라 하고, 이때 크기 변화 비율을 **고옷값**이라 한댜 따라서 고옷값과 고유벡터는 기본적으로 선형변환의 사상 과정에서 만들어지는 왜곡 distortion에 대한 정보를 제공한다.

#### 고유값과 고유벡터의 계산

고윳값과 고유벡터를 계산하기 위해서는 특정방정식(characteristic equation)을 이용하면 된다. 즉, $\operatorname{det}(\lambda I-A)=0$의 특성 방정식을 풀면 고윳값과 고유벡터를 찾을 수 있다.

그 이유는 다음과 같다. 예를 들어 7이 고윳값이라고 가정한다면 행렬 $A$와 고유벡터 $x$는 다음 관계를 만족한다.

$$
\begin{aligned}
A x=7 x & & \Rightarrow & 7 x-A x=0 \\
& & \Rightarrow &(7 I-A) x=0
\end{aligned}
$$

위의 행렬방정식 $(7 I-A) x=0$의 해를 구해보자. 영벡터는 고유벡터가 될 수 없기 때문에(실수로만 존재) trivial solution인 $x=0$아닌 해를 찾아야 한다. 즉, 고유벡터 $x$를 찾기 위해서는 $(7 I-A)$가 invertible해야 고유벡터를 구할 수 있다 떄문에 위와 같은 특정방정식을 통해 고윳값과 고유벡터를 구할 수 있다.




`numpy.linalg` 모듈의 `eig` 함수를 사용하여 고유값과 고유벡터를 구할 수 있다.


```python
A = np.array([
    [2,1],
    [4,3]
])
eigen_values, eigen_vectors = np.linalg.eig(A)
print(eigen_values)
print(eigen_vectors)
```

    [0.43844719 4.56155281]
    [[-0.5392856  -0.36365914]
     [ 0.84212294 -0.93153209]]


#### 고유값, 고유벡터의 성질들

- $\mathrm{tr}A = \sum_{i=1}^n \lambda_i$
    대각합은 고유값들을 합한 값고 같습니다.

- $|A| = \prod_{i=1}^n \lambda_i$
    행렬식은 고유값을 곱한 값과 같습니다.
- $\mathrm{rank}(A)$는 0이 아닌 $A$의 고유값의 개수와 같다.
- $A$가 non-singular(invertibele, linearly independent)일 때, $1/\lambda_i$는 $A^{-1}$의 고유값이다(고유벡터 $x_i$와 연관된). 즉, $A^{-1}x_i = (1/\lambda_i)x_i$이다.

이는 다음과 같이 쉽게 증명이 가능 하다. $A$가 가역 행렬리아면, $A x=\lambda x$의 관계로 부터 다음 방정식을 유도 할 수 있다.

$$
\begin{aligned}
A x=\lambda x & \Rightarrow \quad x=\lambda A^{-1} x \\
& \Rightarrow \quad A^{-1} x=\frac{1}{\lambda} x
\end{aligned}
$$




- 대각행렬 $D = \mathrm{diag}(d_1,\ldots,d_n)$의 고유값들은 $d_1,\ldots,d_n$이다.


```python
A = np.array([
        [1, 2, 3],
        [4, 5, 9],
        [7, 8, 15]
    ])

eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvalues.round(3), eigenvectors
"""
(array([21.282, -0.282,  0.   ]),
array([[ 0.17485683,  0.85386809, -0.57735027],
    [ 0.50887555,  0.18337571, -0.57735027],
    [ 0.84289427, -0.48711666,  0.57735027]]))

"""

```

```python
np.linalg.matrix_rank(A)
#  2
```




모든 고유값과 고유벡터들을 다음과 같이 하나의 식으로 나타낼 수 있다.

$$
AX = X\Lambda
$$

$$
X\in \mathbb{R}^{n\times n} =
\begin{bmatrix}
    \vert & \vert & & \vert\\
    x_1 & x_2 & \cdots & x_n\\
    \vert & \vert & & \vert
\end{bmatrix},~
\Lambda = \mathrm{diag}(\lambda_1,\ldots,\lambda_n)
$$

## 대칭 행렬일 떄의 고유값과 고유벡터

행렬 $A$가 대칭행렬일 때, $A \in \mathbb{S}^{n}$ 다음과 같은 성질을 지닙니다.

- $A$의 모든 고유값들은 실수값(real number)이다.

원래, 주어진 행렬이 대칭행렬이 아니라면 고유값은 complex number 였습니다. 하지만, 대칭행렬일 경우 고유값은 실수값을 갖게 됩니다.

- $A$의 고유벡터들은 orthonormal(정규 직교)성을 갖습니다.

따라서, 임의이 대칭행렬 $A$를 $A=U \Lambda U^{T}$ ($U$는 위의 $X$처럼 $A$의 고유벡터들로 이루어진 행렬)로 나타낼 수 있습니다.

$A=U \Lambda U^{T}$로 표현되는 이유는 다음과 같습니다.

$$
AU = U\Lambda^T\\
U^{-1} = U^T\\
A=U \Lambda U^{T}
$$

$A \in \mathbb{S}^{n}=U \Lambda U^{T}$이라고 해봅시다. 그러면 이차형식(quadratic form)을 다음과 같이 표현 할 수 있습니다.

$$
x^{T} A x=x^{T} U \Lambda U^{T} x=y^{T} \Lambda y=\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}
$$

where $y=U^Tx$

$y_i^2$가 양수이므로 위 식의 부호는 $\lambda_i$ 값들에 의해서 결정된다. 만약 모든 $\lambda_i > 0$이면, $A$는 positive definite이고 모든 $\lambda_i \ge 0$이면, $A$는 positive seimi-definite이다.





## 행렬미분(Matrix Calculus)

$f\left(x_{1}, x_{2}\right)=x_{1}^{2}+2 x_{2}^{2}-x_{1} x_{2}$ 와 같이 두 개 이상의 변수를 포함 하는 함수를 **다변수 함수**(mlutivariate function)이라고 한다.

### 다변수 함수의 벡터 미분과 그래디언트

다변수 함수 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$의 벡터 $x=\left[\begin{array}{c}x_{1} \\ x_{2} \\ \vdots \\ x_{n}\end{array}\right]$에 대한 미분 $\frac{\partial f}{\partial x}$은 다음과 같이 각 변수에 대한 $f$의 편미분을 성분으로 같는 벡터이다.

$$
\frac{\partial f}{\partial x}=\left[\begin{array}{c}
\frac{\partial f}{\partial x_{1}} \\
\frac{\partial f}{\partial x_{2}} \\
\vdots \\
\frac{\partial f}{\partial x_{n}}
\end{array}\right]
$$

$\frac{\partial f}{\partial x}$을 $f$의 **그래디언트**(gradient)라고 하며 $\nabla f$라고 표기한다.

그래디언트 $\nabla f$ 는 주어진 위치 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 에서 함수 $f$ 의 값이 가장 커지는 인접
한 위치 방향으로의 벡터에 해당한다.

항수의 최솟값 위치를 찾는 최적화 문제에 사용하는 경사하강법(gradient descent method)에서는 그래디언트의 반대 방향으로 위치를 조금씩 움직이면서 최솟값의 위치를 찾는다. 경사하강법은 머신러닝의 다양한 학습 알고리즘에서 널리 제공공된다.



### 벡터 함수의 스칼라 미분

실수값을 반환하는 벡터함수 $F\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\left[\begin{array}{c}f_{1}\left(x_{1}, x_{2}, \cdots, x_{n}\right) \\ f_{2}\left(x_{1}, x_{2}, \cdots, x_{n}\right) \\ \vdots \\ f_{n}\left(x_{1}, x_{2}, \cdots, x_{n}\right)\end{array}\right]$가 주어졌을 때, 이 벡터함수의 변수 $x_{i}$에 대한 미분 $\frac{\partial F}{\partial x_{i}}$은 다음과 같이 $F$의 각 성분의 $x_i$에 대한 편미분을 성분으로 같는 벡터이다.

$$
\frac{\partial F}{\partial x_{i}}=\left[\begin{array}{llll}
\frac{\partial f_{1}}{\partial x_{i}} & \frac{\partial f_{2}}{\partial x_{i}} & \cdots & \frac{\partial f_{n}}{\partial x_{i}}
\end{array}\right]
$$

### 백터함수의 벡터 미분과 야코비안 행렬

실수값을 반환하는 벡터함수 $F\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\left[\begin{array}{c}f_{1}\left(x_{1}, x_{2}, \cdots, x_{n}\right) \\ f_{2}\left(x_{1}, x_{2}, \cdots, x_{n}\right) \\ \vdots \\ f_{n}\left(x_{1}, x_{2}, \cdots, x_{n}\right)\end{array}\right]$가 주어졌을 때, 이 벡터함수의 변수 $x=\left[\begin{array}{c}x_{1} \\ x_{2} \\ \vdots \\ x_{n}\end{array}\right]$에 대한 미분 $\frac{\partial F}{\partial x}$은 다음과 같이 벡터함수의 각 성분의 편미분을 성분으로 갖는 행렬이다.


$$
\frac{\partial F}{\partial x}=\left[\begin{array}{cccc}
\frac{\partial f_{1}}{\partial x_{1}} & \frac{\partial f_{2}}{\partial x_{1}} & \cdots & \frac{\partial f_{n}}{\partial x_{1}} \\
\frac{\partial f_{1}}{\partial x_{2}} & \frac{\partial f_{2}}{\partial x_{2}} & \cdots & \frac{\partial f_{n}}{\partial x_{2}} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial f_{1}}{\partial x_{n}} & \frac{\partial f_{2}}{\partial x_{n}} & \cdots & \frac{\partial f_{n}}{\partial x_{n}}
\end{array}\right]
$$

$\frac{\partial F}{\partial x}$를 야코비안 행렬(Jacobian matrix)또는 자코비안 행렬이라고 하며 $J_{F}$로 나타내기도 한다.


자코비안 행렬은 다변수 벡터함수의 미분에 해당하므로, 벡터함수의 지역적 변화가 가장 큰 방향의 변화율을 나타낸다고 볼 수 있다.



### 헤시안(Hessian) 행렬, 다변수 함수의 2차 함수 미분

다변수 함수 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$의 벡터 $\boldsymbol{x}=\left[\begin{array}{c}x_{1} \\ x_{2} \\ \vdots \\ x_{n}\end{array}\right]$에 대한 2차 미분 $\frac{\partial^{2} f}{\partial x^{2}}$은 다음과 같이 각 성분이 $f$의 2차 편미분으로 구성되는 행렬이다.

$$
\frac{\partial^{2} f}{\partial x^{2}}=\left[\begin{array}{cccc}
\frac{\partial^{2} f}{\partial x_{1}^{2}} & \frac{\partial^{2} f}{\partial x_{1} \partial x_{2}} & \cdots & \frac{\partial^{2} f}{\partial x_{1} \partial x_{n}} \\
\frac{\partial^{2} f}{\partial x_{2} \partial x_{1}} & \frac{\partial^{2} f}{\partial x_{2}^{2}} & \cdots & \frac{\partial^{2} f}{\partial x_{2} \partial x_{n}} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial^{2} f}{\partial x_{n} \partial x_{1}} & \frac{\partial^{2} f}{\partial x_{n} \partial x_{2}} & \cdots & \frac{\partial^{2} f}{\partial x_{n}^{2}}
\end{array}\right]
$$

$\frac{\partial^{2} f}{\partial x^{2}}$을 헤시안 행렬(Hessian Matrix)이라고 하며 $H(f)$로 나타낼 수 있다.

#### 중요한 공식들

A는 대칭 해렬일 때, 다음 조건을 만족한다.

$x, b\in \mathbb{R}^n$, $A\in \mathbb{S}^n$일 때 다음이 성립한다.
- $\nabla_x b^Tx = b$
- $\nabla_x x^TAx = 2Ax$
- $\nabla_x^2 x^TAx = 2A$
- $\nabla_A \log |A| = A^{-1}$ ($A\in\mathbb{S}_{++}^n$인 경우)

## 최소제곱법(Least Squares)
$Ax = b$ 라는 선형 시스템이 주어졌다고 가정해보자. 행렬 $A \in \mathbb{R}^{m \times n}$ ($A$는 여기서 full rank)와 벡터 $b \in \mathbb{R}^{n}$가 주어졌고, $b \notin \mathcal{R}(A)$ 즉, $A$라는 선형 조합으로 벡터 $b$를 표현 할 수 없을때, $Ax = b$ 를 만족하는 벡터 $x \in \mathbb{R}^{n}$를 찾을 수 없습니다.

이때, 선형 조합 $Ax$가 $b$와 가장 가까워지는 즉,

$$
\|A x-b\|_{2}^{2}
$$

을 최소화 시키는 $x$를 찾는 문제를 고려 할 수 있습니다. $\|x\|_{2}^{2}=x^{T} x$ 이므로,

$$
\begin{aligned}
\|A x-b\|_{2}^{2}=&(A x-b)^{T}(A x-b) \\
=& x^{T} A^{T} A x-2 b^{T} A x+b^{T} b \\
\nabla_{x}\left(x^{T} A^{T} A x-2 b^{T} A x+b^{T} b\right) &=\nabla_{x} x^{T} A^{T} A x-\nabla_{x} 2 b^{T} A x+\nabla_{x} b^{T} b \\
&=2 A^{T} A x-2 A^{T} b
\end{aligned}
$$

위 식의 해를 0으로 놓고 $x$에 관하여 풀면 다음과 같은 식을 얻을 수 있고, 이를 Normal Equation이라고 합니다.

$$
x=\left(A^{T} A\right)^{-1} A^{T} b
$$



### 고유값과 최적화문제 (Eigenvalues as Optimization)

다음 형태의 최적화문제를 행렬미분을 사용해 풀면 고유값이 최적해가 되는 것을 보일 수 있다.

$$
\max_{x\in \mathbb{R}^n} x^TAx \\
\mathrm{~~~~subject~to~} \|x\|_2^2=1
$$

제약조건이 있는 최소화문제는 Lagrangian을 사용해서 해결

$$\mathcal{L}(x, \lambda) = x^TAx - \lambda x^Tx$$

다음을 만족해야 함.

$$\nabla_x \mathcal{L}(x, \lambda) = \nabla_x ( x^TAx - \lambda x^Tx) = 2A^Tx - 2\lambda x = 0$$

따라서 최적해 $x$는 $Ax = \lambda x$를 만족해야 하므로 $A$의 고유벡터만이 최적해가 될 수 있다. 고유벡터 $u_i$는

$$u_i^TAu_i = \sum_{j=1}^n \lambda_j y_j^2 = \lambda_i$$
을 만족하므로($y=U^Tu_i$), 최적해는 가장 큰 고유값에 해당하는 고유벡터이다. 즉 이말을 다시 하면 이차형식에서 가장 최대화 되는 지점은 고유값이 나타나는 지점이라는 것 입니다.

## AutoEncoder와 PCA

### 오토인코더(AutoEncoder)란?

오터인코더를 설명하기에 앞서, 인코딩(encoding)의 의미는 아래 그림과 같이 높은 차원의 데이터를 낮은 차원(code 부분)으로 낮추는 것을 인코딩이라고 합니다. 역으로, 다시 원래의 높은 차원으로 복구시키는 과정은 Decoding이라고 합니다.

이럴 과정이 왜 필요할 까요? 주어진 데이터가 고차원이거나 너무 커서 저장하기 어렵다면, 공간 효율성 측면에서 이를 축소해 저장해 놓고 이를 필요할 때마다 다시 고차원으로 복원하여 사용하는 것이 효율적일 것입니다. 이러한 바탕에서 나온 개념이 바로 오토 인코더 입니다. 참고로 이러한 차원 축소(dimension reduction)이라고 합니다.

![](https://github.com/learn-programmers/programmers_kdt_II/raw/d6f59b80fb967241f3a4b1ce8d610ee5b1b69ecd/images/autoencoder.png)


### AutoEncoder의 적용사례

- 차원축소(Dimensionality Reduction)
- Image Compression
- Image Denoising(이미지 노이즈 줄이기)
- Feature Extraction
- Image generation
- Sequence to Sequence prediction
- 추천시스템


### PCA(Principal Component Analysis)

우리가 이전에 배운 PCA를 가장 간단한 형태의 autoencoder라고 생각할 수 있습니다. 이러한 관점에서 PCA를 유도할 것인데, 위에서 설명한 내용으로도 충분히 설명 합니다.

$m$개의 점들 $\left\{x_{1}, \ldots, x_{m}\right\}, x_{i} \in \mathbb{R}^{n}$ 이 주저쳤다고 가정해봅시다. 각각의 점들을 $l$차원 공간으로 투영시키는 함수 $f(x)=c \in \mathbb{R}^{l}$와 이것을 다시 $n$차원 공간으로 회복하는 함수 $g(c)$를 생각해봅시다. 이를 정리하면,$f$를 인코딩 함수 $g$를 디코딩 함수라고 하고,


$$
x \approx g(f(x))
$$

와 같이 인코딩과 디코딩을 거친 후의 값의 원래의 값과 가장 근사하기를 원합니다. 즉, 중요한 함수를 최대한 저장하면서 차원을 축소한 형태를 저장하기를 원하는 것입니다.


### 디코딩 함수

함수 $g$는 간단한 선형함수로 정의하기로 한다.

$$
g(c)=D c, \quad D \in \mathbb{R}^{n \times l}
$$

여기서 $D$열들이 정규화 되어 있고, 서로 직교한는 경우로 한정한다.


### 인코딩 함수

디코딩 함수가 위와 같이 주어졌을 때, 어떤 함수가 최적의 인코딩 함수 일까요?

$$
f(x)^{*}=\underset{f(x)}{\operatorname{argmin}} \int\|x-g(f(x))\|_{2}^{2} d x
$$


즉, 인코더를 통하고 다시 디코더를 통한 값이 원래의 입력값 $x$와 차이를 최소화 하는 최적화 문제로 생각 할 수 있습니다. 위의 최적화 식을 푸는 방법은 오일러-라그랑주 변분법(Euler-Lagrange calculus of variantions)의 방법을 풀 수 있습니다. 다음과 같이 방정식

$$
\nabla_{f}\|x-g(f(x))\|_{2}^{2}=0
$$

위의 방정식을 $f$에 관하여 풀면 됩니다. (함수의 변화에 대한 학문: 변분법) $f(x)=c$를 두고 풀면

$$
\begin{aligned}
\|x-g(c)\|_{2}^{2} &=(x-g(c))^{T}(x-g(c)) \\
&=x^{T} x-x^{T} g(c)-g(c)^{T} x+g(c)^{T} g(c) \\
&=x^{T} x-2 x^{T} g(c)+g(c)^{T} g(c) \\
&=x^{T} x-2 x^{T} D c+c^{T} D^{T} D c \\
&=x^{T} x-2 x^{T} D c+c^{T} I_{l} c \\
&=x^{T} x-2 x^{T} D c+c^{T} c
\end{aligned}
$$

이렇게 정리한 식을 $c = f(x)$로 미분을 해줍니다.

$$
\begin{array}{c}
\nabla_{c}\left(x^{T} x-2 x^{T} D c+c^{T} c\right)=0 \\
-2 D^{T} x+2 c=0 \\
c=D^{T} x
\end{array}
$$

따라서 위식을 통해 얻은 최적의 인코더 함수는 다음과 같습니다.

$$
f(x)=D^{T} x
$$



### 최적의 $D$ 찾기

디코딩 함수 $g(c)=DC$는 정의 하였지만, 여기서 쓰이는 변환함수 $D$는 정의하지 않았습니다. 때문에 $D$를 찾기 위햇, 입력값 $x$와 출력값 $g(f(x))$의 사이의 거리가 최소화되는 $D$를 다음과 같이 찾을 수 있습니다.

모든 $x$를 다음과 같이 블록행렬의 개념으로 생각할 수 있습니다. 대문자 $X$를 사용해서 $m$개의 입력벡터들을 다음과 같이 행렬로 표현 할 수 있습니다.(단, $x_i$는 행(row)벡터) 행렬 $R$은 입력벡터가 인코더와 디코더를 통해 변환된 값이라고 생각 할 수 있습니다.

$$
X=\left[\begin{array}{ccc}
- & x_{1}^{T} & - \\
& \vdots & \\
- & x_{m}^{T} & -
\end{array}\right], \quad R=\left[\begin{array}{ccc}
- & g\left(f\left(x_{1}\right)\right)^{T} & - \\
\vdots & \\
- & g\left(f\left(x_{m}\right)\right)^{T} & -
\end{array}\right]
$$

이렇게 주어진 행렬의 차를 오류행렬 $E$라고 다음과 같이 정의 할 수 있습니다.

$$
E=X-R
$$

이렇게 주어진 조건을 통해서 우리가 찾는 최적의 $D$는 다음과 같이 목적함수를 세울 수 있습니다.

$$
D^{*}=\underset{D}{\operatorname{argmin}}\|E\|_{F}^{2} \\
\text { subject to } D^{T} D=I_{l}
$$



$$
\begin{aligned}
R &=\left[\begin{array}{ccc}
- & g\left(f\left(x_{1}\right)\right)^{T} & - \\
& \vdots \\
- & g\left(f\left(x_{m}\right)\right)^{T} & -
\end{array}\right] \\
&=\left[\begin{array}{ccc}
- & \left(D D^{T} x_{1}\right)^{T} & - \\
& \vdots \\
- & \left(D D^{T} x_{m}\right)^{T} & -
\end{array}\right] \\
&=\left[\begin{array}{ccc}
- & x_{1}^{T} D D^{T} & - \\
& \vdots & \\
- & x_{m}^{T} D D^{T} & -
\end{array}\right] \\
&=X D D^{T}
\end{aligned}
$$

$$
\begin{aligned}
\mathop{\mathrm{argmin}}_{D} \|E\|_F^2 &= \mathop{\mathrm{argmin}}_{D} \| X - XDD^T\|_F^2\\
&= \mathop{\mathrm{argmin}}_{D} \mathrm{tr}\left( \left(X - XDD^T\right)^T\left(X - XDD^T\right) \right)\\
&= \mathop{\mathrm{argmin}}_{D} \mathrm{tr} \left( X^TX - X^TXDD^T - DD^TX^TX + DD^TX^TXDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} \mathrm{tr} \left( X^TX \right) - \mathrm{tr} \left( X^TXDD^T \right) - \mathrm{tr} \left( DD^TX^TX \right) + \mathrm{tr} \left( DD^TX^TXDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} - \mathrm{tr} \left( X^TXDD^T \right) - \mathrm{tr} \left( DD^TX^TX \right) + \mathrm{tr} \left( DD^TX^TXDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} - 2\mathrm{tr} \left( X^TXDD^T \right) + \mathrm{tr} \left( DD^TX^TXDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} - 2\mathrm{tr} \left( X^TXDD^T \right) + \mathrm{tr} \left( X^TXDD^TDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} - 2\mathrm{tr} \left( X^TXDD^T \right) + \mathrm{tr} \left( X^TXDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} - \mathrm{tr} \left( X^TXDD^T \right)\\
&= \mathop{\mathrm{argmin}}_{D} - \mathrm{tr} \left( D^TX^TXD \right)\\
&= \mathop{\mathrm{argmax}}_{D} \mathrm{tr} \left( D^TX^TXD\right)\\
&= \mathop{\mathrm{argmax}}_{d_1,\ldots,d_l} \sum_{i=1}^l d_i^TX^TXd_i
\end{aligned}
$$

$d_i^Td_i = 1$이므로 벡터들 $d_1,\ldots,d_l$이 $X^TX$의 가장 큰 $l$개의 고유값에 해당하는 고유벡터들일 때 $\sum_{i=1}^l d_i^TX^TXd_i$이 최대화된다.

$$
\begin{aligned}
\left( D^{\top} X^{\top} X D\right)_{i i}&=\left(\left[\begin{array}{c}
-d_{1}^{T}- \\
\vdots \\
\vdots
\end{array}\right] X^{T} X\left[\begin{array}{l}
\mid \\
d_{1} & \ldots \\
\mid
\end{array}\right]\right) \\
&=\left(\left[\begin{array}{c}
-d_{1}^{T}X^TX- \\
\vdots \\
\vdots
\end{array}\right] \left[\begin{array}{l}
\mid \\
d_{1} & \ldots \\
\mid
\end{array}\right]\right) \\
&=d_i^TX^TX
\end{aligned}
$$
