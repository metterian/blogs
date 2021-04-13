#  🧐대체 시그모이드(Sigmoid) 함수가 뭔데?

> **시그모이드 함수**는 S자형 곡선 또는 **시그모이드 곡선을** 갖는 [수학 함수](https://ko.wikipedia.org/wiki/함수)이다. 시그모이드 함수의 예시로는 첫 번째 그림에 표시된 [로지스틱 함수](https://ko.wikipedia.org/wiki/로지스틱_방정식)가 있으며 다음 수식으로 정의된다.
>
> ![{\displaystyle S(x)={\frac {1}{1+e^{-x}}}={\frac {e^{x}}{e^{x}+1}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9537e778e229470d85a68ee0b099c08298a1a3f6)
>
> 출처: 위키피디아



## 💁🏻‍♀️들어가며

ML/DL을 공부하다 보면 Activation 함수로 시그모이드 함수를 자주 많나게 된다. 혹은 통계학에서도 Logistic 분포, Normal 분포, t-분포에서도 시그모이드 곡선이 자주 등장한다. 어떻게 이런 함수가 등장했는지 왜 사용하는 지 살펴 보고자 글을 작성하게 되었다.



## 🗣분류의 가능성을 확류로 얘기 하기

### 기존 회귀 모형의 문제점들

- Target Label이 1이상 0이하의 수들이 나오는 것을 어떻게 해석 할 것이냐?
- 1 또는 0으로 정확히 표현 가능 한가?
- 변수가 Y에 영향을 주는 정도가 비례하는 가?
- **확률**로 발생할 사건의 가능성을 표현해야 함

## 🏋🏻‍♀️어떤 사건이 일어날 확률

Sigmoid 함수 혹은 Logistic 함수를 **Odds ratio**를 통해 구해지게 된다.

- 일어날 확률 : $ P(X)$ 
- 일어나지 않을 확률 : $1 - P(X)$ 
- $0 ≤ P(X) ≤ 1$ 

위와 같이 $ P(X)$ 를 정의 하자. 그러면 Odds Ratio로 나타 낼 수 있다. 

## Odds Ratio

해당 사건이 일어날 확률과 일어나지 않을 확률의 비율
$$
\frac{P(X)}{1-P(X)}= \frac{일어날 확률}{일어나지 않을 확률}
$$
위 수식을 그래프로 나타내면 다음과 같이 나타난다. 확률이 높으면 높을 수 록 Odds 값이 무한이 증가하는 그래프의 모양이 나타난다.

![image-20210413204647138](/Users/seungjun/Library/Application Support/typora-user-images/image-20210413204647138.png)



우리가 알고 싶은것은 <u>$X$ 값이 주어졌을 때의 확률을 알고 싶다</u>. 때문에 $X$ 값과 $Y$ 값을 바꿔본다. 즉, 역함수를 구해본다. 이때, 이것을 구하기 위해 **Logit 함수**를 이용한다. 

## Logit function

X값이 주어졌을 때 y의 확률을 이용한 Log odds를 구하면 다음과 같다.
$$
\begin{align}
logit(p(y=1|x)) &= log_e(\frac{p}{1-p}) \\
&=log_e(p) - log_e(1-p)\\
&= -log_e(\frac{1}{p} - 1) 
\end{align}
$$
이렇게 얻은 값을 그래프로 표시하면 다음과 같다.

![image-20210413210016068](/Users/seungjun/Library/Application Support/typora-user-images/image-20210413210016068.png)

$ P(X)$확률 일 때의 Logit(P)의 값을 구하는 그래프 이다. 하지만, 우리는 $X$ 값이 주어졌을 때의 확률을 알고 싶기 때문에 역함수를 구해야 한다.



## Sigmoid(=Logistic) 함수

Logit​ 함수의 역함수로 $ z$에 관한 확률로 구하면 다음과 같다.
$$
\begin{align}
f(z) =\, &y = -log_e(\frac{1}{z}-1) \: \text{역함수 변환} \\
&z = -log_e(\frac{1}{y}-1) \: \text{y 에 관한 정리}
\end{align}
$$
여기서 $z$값은 위에서 이야기 했던 $P(X)$ 확률을 의미하는 것이고, 즉 이제 앞으로 구하게 되는 어떤 값으 말한다. 이것을 다시 다음과 같이 변환하면 Logistic 함수를 얻을 수 있다.
$$
\begin{align}
&z = -log_e(\frac{1}{y}-1)\\
&e^{-z} = \frac{1-y}{y}\\
&y*e^{-z} + y = 1\\
&y(e^{-z} + 1) = 1\\
&y = \frac{1}{1+e^{-z}}
\end{align}
$$
이렇게 얻어진 함수를 Logistic 함수라고 하고. 모양이 다음과 같이 S형태로 닮았다고 하여 Sigmoid 함수라고 호칭한다. 이 함수의 가장 중요한 특징은 연속구간에서 미분 가능한 형태를 띈다는 점이다.

![image-20210413212222497](/Users/seungjun/Library/Application Support/typora-user-images/image-20210413212222497.png)

### 선형 함수에서 Sigmoid 함수로 변환

다음과 같이 Logit 함수를 적용해서 기존에 회귀식으로 다룰 수 없었던 확률을 통해 Cost 함수를 얻을 수 있다.  $w_0x_0 + w_1x_1 + ... + w_nx_n$ 값을 구하게 되면 $z$ 값을 알게 되고 $z$을 값을 알게되면 확률 $P$의 값을 얻을 수 있게 된다.
$$
\begin{align}
&p = \sigma(z) = \frac{1}{1+e^{-z}},\: \frac{p}{1-p} = \frac{\frac{1}{1+e^{-z}}}{\frac{e^{-z}}{1+e^{-z}}} = \frac{1}{e^{-z}} = e^{z} \\
&log_e\frac{p}{1-p} = z \\
&log_e\frac{p}{1-o} = z = w_0x_0 + w_1x_1 + ... + w_nx_n
\end{align}
$$
