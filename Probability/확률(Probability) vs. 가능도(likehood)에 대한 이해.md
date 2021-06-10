## 확률 (Probability)

간단히 '확률'이란 주어진 확률분포가 있을 때, 관측값 혹은 관측 구간이 분포 안에서 얼마의 확률로 존재하는 가를 나타내는 값이다. 여기서 중요한 것은 **확률 분포(probability distribution)을 고정**(fixed)하고 그 때의 관측 X 에 대한 확률을 구한다는 것! 이를 수식으로 표현하자면 아래와 같이 쓸 수 있겠다.
$$
\text { 확률 }=\mathrm{P}(\text { 관측값 } \mathrm{X} \text { | 확률분포 } \mathrm{D} \text { ) }
$$
이를 그림으로 보아보자. 파란 확률 분포는 귀여운 쥐들의 몸무게 분포로써 평균 32 표준편다 2.5를 갖는 정규분포이다. 이때 해당 분포를 가정하고(고정하고) 쥐의 무게가 32-34 사이로 관측될 확률은 몇일까? 이는 아래 그림의 빨간 영역(red area)와 같을 것이다. 

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99CB8E365B20D66C02)

> 확률은 '**어떤 고정된 분포**'에서 이것이 관측될 확률(Area under distribution)이다. 

<br>

## 가능도(Likelihood)

그렇다면 가능도는 무엇일까? 눈치가 빠른 사람이라면 이번에는 고정되는 요소가 분포가 아니라 관측값들이 고정될 것이라고 예상했을 것이다. 이는 아까 전의 확률의 개념에서 시각만 반대로 한것에 지나지 않는다. '가능도'란 어떤 값이 관측되었을 때, 이것이 어떤 확률 분포에서 왔을 지에 대한 확률이다. 간단히 하면 확률의 확률이라고 할 수 도 있겠다. 이것을 수식으로 표현하자면 아래와 같다.
$$
\text { 가능도 }=\mathrm{L}(\text { 확률분포D } \mid \text { 관측값X })
$$
내가 쥐를 하나 골라서 무게를 달았는데 34g이 딱 나왔다. 이때 이 관측결과가 정규분포(m=32/sd=2.5)에서 나왔을 확률은 0.12(빨간 십자마크)이고 이것이 가능도이다. 관측값이 고정되고, 그것이 주어졌을 때 해당 확률분포에서 나왔을 확률을 구하는 것이다. 그렇다면 두번째 그림에서 평균을 34인 확률분포에서 나왔을 확률은 어떻게 될까? 그림과 같이 그 가능도는 높아진 것을 확인할 수 있다. 

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99B30D365B20D66D04)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F994A81365B20D66C20)



## 요약 Summary

> 확률은 주어진 확률분포에서 해당 관측값이 나올 확률

> 가능도는 주어진 관측값에서 이것이 해당 **확률분포에서 나왔을 확률**. (=연속확률밀도함수pdf의 y값)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99536E365B20D66D36)

