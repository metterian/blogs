## Copy list

### Shallow Copy vs. Deep Copy



### 얕은 복사(Shallow Copy)

#### 얕은 복사(Shallow Copy)를 하는 가장 빠른 방법

```python
>>> a = [1,2,3,4,5]
>>> a[:]
[1, 2, 3, 4, 5]

```



주소확인

```python
>>> id(a)
4485492928
>>> id(a[:])
4486010688
```

<br>

#### 빈 리스트를 활용한 방법

```python
>>> a = [1,2,3,4,5]
>>> a + []
[1, 2, 3, 4, 5]
```

<br>



#### `list.copy()` 메소드를 활용한 방법

```python
>>> a = [1,2,3,4,5]
>>> a.copy()
[1, 2, 3, 4, 5]
```

<br>

<br>

### 깊은 복사(Deep Copy)

이중 리스트(nested list) 까지 `copy()` 메소드를 진행 시키고 싶은경우 `deepcopy()` 메소드를 사용한다. 얕은 복사의 경우 한 개의 리스트까지만 복사가 이루어지기 때문에 리스트 안의 리스트까지도 value copy를 하고 싶은경우 깊은 복사를 사용하면 됩니다. 

```python
>>> from copy import deepcopy
>>> l = [[1,2], [3,4]]
>>> l2 = deepcopy(l)
```

#### 깊은 복사 vs. 얕은 복사

얕은 복사의 경우 `a` 리스트 안의 `[2,3,4]` 리스트에 값을 추가 하게 되면 객체가 복사 된 것이기 때문에 `shallow` 변수도 영향을 받습니다.

하지만, `deepcopy()` 메소드를 사용한 경우에는 이중리스트까지 value copy가 일어나면서 독립된 객체를 같게 되어 영향을 받지 않습니다. 

```python
# 얕은 복사
>>> a = [1,[2,3,4]]
>>> shallow = a.copy()


# 깊은 복사
>>> from copy import deepcopy
>>> a[1].append(1000)
>>> shallow
[1, [2, 3, 4, 1000]]
>>> deep
[1, [2, 3, 4]]
```

<br>

## Calcuator

코딩 테스트를 하거나 알고리즘 문제를 풀경우 사칙연산을 코드로 구현해야하 하는 경우가 많이 발생합니다. 이때 다음과 같이 `if` 문을 사용해서 사칙연산을 코드로 구현합니다. 

```python
operators = ['+', '-', '*', '/']
for oper in operators:
    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
... 
```

<br>

하지만, 파이썬의 `operator` 모듈을 사용하면 이를 보다 깔금하게 구현 할 수 있습니다. 

```python
>>> ops = {
...         "+": operator.add,
...         "-": operator.sub,
...         "*": operator.mul,
...         "/": operator.truediv,
...         "**": operator.pow
... }
>>> ops["+"](1,2)
3
```

