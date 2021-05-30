## 객체의 정의

> 객체는 파이썬이 데이터를 추상화한 것입니다. 파이썬 프로그램의 모든 데이터는 객체나 객체 간의 관계로 표현됩니다. 폰 노이만(Von Neumann)의 “프로그램 내장식 컴퓨터(stored program computer)” 모델을 따르고, 또 그 관점에서 코드 역시 객체로 표현됩니다.

<br>

## 콜러블(Callabe) 객체

우리가 파이썬 함수나 클래스에서 `()` 를 사용하는 의미는 모든 콜러블(Callable) 객체를 의미합니다. 파이썬에서 모든 객체가 `()` 사용할 수 없는 이유가 바로 이것 때문입니다. 콜러블 객체만이 `()` 를 사용할 수 있고, 이는 `__call__` 특수 어트리뷰터(메소드)를 사용하는 것과 의미가 같습니다. 

```python
>>> class c(object):
...     def f(self): pass
>>> '__call__' in dir(c)
False
>>> '__call__' in dir(c().f)
True
```

<br>

기본적으로,`c` 클래스 안에 있는 `f` 라는 메소드는 콜러블 객체이기 때문에 `__call__` 메소드를 포함하고 있는 것입니다. 하지만 `c` 라는 클래스에는 `__call__` 이라는 메소드가 존재하지 않지만 콜러블 객체입니다. 왜냐하면, 클래스 안에 `__call__`  메소드를 선언할 수 있기 때문이죠.

```python
>>> class c(object):
...     def f(self): 
...  				pass
...     def __call__(self):
...         print("callable")
...
>>> '__call__' in dir(c)
True
```

<br>

그럼 Python 인터프리터에서 `c` 을 단독으로 사용할 떄와, `c()` 와 같이 콜러블 객체로 사용하면 어떤점이 다른 걸까요? 그것은 바로 객체의 사용의 유무입니다. `()` 를 사용하지 않고 `c` 를 단독으로 사용하게 된다면 클래스가 저장된 객체 주소를 반환 하게 됩니다. 반면, `c()` 와 같이 콜러블 객체로 사용하게 된다면 클래스의 호출이 일어나고 파이썬은 해당 클래스 객체의 주소를 찾아가 생성과 소멸이 일어나게됩니다. 떄문에, 클래스를 호출 할 때 마다 새로운 주소가 객체로 반환되는 것이죠.

```python
>>> class c(object):
...     def f(self): pass
>>> t = C()
>>> t
<__main__.C object at 0x10c932940> # 주소를 객체로 반환
>>> t = C()
>>> t
<__main__.C object at 0x10ca152e0> # 클래스를 호출 할때마다 새로운 주소를 객체에 반환
>>> C
<class '__main__.C'>
```



<br>

## 클래스에서 `()` 의 의미

클래스를 호출 할 때 일반적으로 `insatnce = C()` 와 같이 `()` 를 사용해서 인스턴스를 할당합니다. 즉, 클래스를 호출 하는 것이지요(=콜러블 객체를 호출). 그렇다면 클래스는 함수인 것일까요? 정확히는 함수는 퍼스트 클래스로 함수가 클래스의 일종입니다. 그렇다면 클래스를 호출의 역할은 무엇일까요?

### 클래스 생성자

**파이썬**에서의 **클래스 생성자**와 **소멸자**에 관해 알아보겠습니다. **생성자**는 이름에서 알 수 있듯이 객체가 만들어질 때 호출되는 함수를 **생성자**라고 이야기 하며, 객체가 사라질 때 호출되는 함수를 소멸자라고 이야기합니다.

우리가 클래스를 사용할 때 흔히 사용하는 `__init__` 이 바로 생성자 였던것이지요. 우리가 클래스를 `()` 를 사용해서 호출하게 되면 파이썬은 자동으로 제일 먼저 `__init__`을 찾아사 이 메소드를 실행시키는 것이지요. 어찌는 보면 함수의 역활과도 비슷합니다. 

### 각 메소드 기능들 살펴 보기

다음과 같이 클래스를 작성하고 각 메소드의 기능들을 살펴 보겠습니다.

```python
>>> class C:
...     def __init__(self): # 생성자
...         print('__init__ method')
...     def __call__(self): # 콜러블 객체 설정
...         print('__call__ method')
...     def special_method(self): # 메소드
...         print('special method')
...     def __del__(self): # 소멸자
...         print('__del__ method')
```

<br>

클래스를 호출하게 되면 가장 먼저 `__init__` 메소드가 가장 먼저 실행되고 이후, 실행된 객체의 주소가 반환 됩니다.

```python
>>> C() # 클래스 호출
__init__ method
<__main__.C object at 0x1062208b0>
```

<br>

`del` 은 인스턴스를 삭제하는 파이썬 내장함수 입니다. 할당된 인스턴스가 존재하지 않으니 오류를 나타내는 것입니다. 여기서 오류 메세지를 살펴 보면 *"cannot delete function call"* 을 확인 할 수 있습니다. 위에서 설명한 클래스의 호출이 함수의 호출과 비슷한 성격이라고 하였던것과 일치하는 부분인것을 확인 할 수 있습니다. 

```python
>>> del C()
  File "<input>", line 1
    del C()
        ^
SyntaxError: cannot delete function call
```

<br>

그렇다면 호출의 호출도 가능 할까요? 위에서 `__call__` 메소드를 사용하여 콜러블 객체를 정의 해줬기 때문에 가능 합니다. 여기서 `__del__` 메소드가 실행된 것은 파이썬에서 객체가 인스턴스에 할당 되지 않았지 때문에 메모리 누수를 방지하고자 자동으로 할당되지 못한 객체를 제거 한것입니다. 

```python
>>> C()()
__init__ method
__call__ method
__del__ method
```

<br>

`t` 변수에 인스턴스를 할당하면 다음과 같습니다. `__call__` 을 사용해서 콜러블 객체로 정의 해줬기 때문에 `t`  인스턴스도 콜러블 인스턴스로 사용하게 된것 입니다. 이후, `del` 내장함수를 사용해서 인스턴스를 제거 할 수 있습니다. 

```python
>>> t = C()
__init__ method
>>> t.special_method()
special method
>>> t() # 콜러블 인스턴스
__call__ method
>>> del t
__del__ method
```

<br>

## 함수의 `()`와 클래스의 `()` 의 비교

그렇다면 메소드(함수)에서의 `()` 사용과 클래스에서의 `()` 사용은 어떠한 차이점이 있을까요?

<br>

### 퍼스트 클래스 함수 (First-class function)

>  퍼스트클래스 함수란 프로그래밍 언어가 함수 (function) 를 **first-class citizen**으로 취급하는 것을 뜻합니다. 쉽게 설명하자면 함수 자체를 인자 (argument) 로써 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴 할수도 있고, 함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있는 함수를 뜻합니다.

위 정의에서 중요하게 살펴봐야할 정보는 **first-class citizen** 라는 것입니다. 퍼스트 클래스 시티즌이라는 것이 무엇을 의미하는 것일까요? 

위에서 파이썬 프로그래밍은 폰 노이만이 설계한 객체의 개념을 사용하여 운영됩니다. 프로그래밍을 할 때 대부분의 기능(함수, 클래스..)들은 객체 단위로 구성되고 실행되어야 한다는 뜻이지요. 하지만 단순한 덧셈 기능을 구현하기 위해서 객체 단위로 프로그래밍을 하면 굉장히 비효율적일 것입니다. 

예를 들어 다음과 같이 덧셈 함수를 정의 한다고 가정해 봅니다. 다음과 같이 단순하게 함수를 선언하여 사용할 수 있습니다.

```python
>>> def add(a,b):
...     return a+b
...
>>> add(2,3)
5
```

<br>

하지만, 객체를 사용해서 이 함수를 정의 한다면 어떻게 해야 할까요? 우리가 위에서 했던 객체를 콜러블 객체로 만들어서 작성해야 합니다.

```python
>>> class C(object):
...     def __call__(self, a, b):
...         return a + b
...
>>> t = C() # 인스턴스 생성
>>> add = C() # 인스턴스 호출
>>> add(2,3)
5
```

<br>

파이썬에서는 이러한 객체 지향적 프로그래밍을 피하고자 함수의 기능(인자, 반환)을 미리 하나의 객체로 설정해 두어 복잡한 프로그래밍을 방지 한것 입니다. 



<br>

## 부록

### 인스턴스 메서드(Instance methods)

인스턴스 메서드는 클래스, 클래스 인스턴스와 모든 콜러블 객체 (보통 사용자 정의 함수)을 결합합니다.  여기서 **인스턴스의 의미**는 객체 지향 프로그래밍(OOP)에서 해당 클래스의 구조로 컴퓨터 저장공간에서 할당된 실체를 의미합니다.

인스턴스 메서드 객체가 호출될 때, 기반을 두는 함수 (`__func__`) 가 호출되는데, 인자 목록의 앞에 클래스 인스턴스 (`__self__`) C.가 삽입됩니다. 예를 들어, `C` 가 함수 `f()` 의 정의를 포함하는 클래스이고, `x` 가 `C` 의 인스턴스일 때, `x.f(1)` 를 호출하는 것은 `C.f(x, 1)` 을 호출하는 것과 같습니다. 

여기서, **self**를 붙인 쪽을 **bound**, 안 붙인 쪽은 unbound 메소드라 합니다.

#### 예제

```python
>>> class C:
...     def method_one():
...         print("method one called")
...     def method_two(self):
...         print("method two called")
...     @staticmethod # 정적 메소드
...     def method_three():
...         print("method three called")
```

위의 코드를 예제 코드로 사용하고자 합니다. `method_three()` 는 데코레이터를 사용하여 정적 메소드로 사용합니다. 이 메소드를 사용하면 `method_three()` 를 bound method로 만들지 말라고 설정 할 수 있습니다. 

`method_one()` 을 실행한 결과는 다음과 같습니다.

```python
>>> C.method_one
<function C.method_one at 0x10ca07b80>  # 단순 객체의 주소 반환
>>> C.method_one()
method one called # C의 인스턴스가 존재하지 않기 때문에 실행 가능
>>> C.method_one(t)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    C.method_one(t)
TypeError: method_one() takes 0 positional arguments but 1 was given
```

<br>

다음으로 

`method_two(self)` 를 실행한 결과는 다음과 같습니다.

```python
>>> C.method_two(t) # t = C(); t.method_two()와 같은 의미
method two called
>>> C.method_two()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    C.method_two()
TypeError: method_two() missing 1 required positional argument: 'self'
```

여기서 눈여겨 봐야할 코드는 `C.method_two(t)` 입니다. 우리는 이전에 클래스의 인스턴스를 할당한 다음 인스턴스의 메소드를 호출 하였습니다. 클래스 내부에서 `self` 라는 인자를 선언 했지만 해당 메소드를 사용할 때, 인자로 값을 넣어주지 않아도 실행이 가는 했습니다. 왜냐하면 파이썬에서는 인스턴스의 메소드가 호출(call)되면 자동으로 인스턴스 객체를 해당 메소드의 인자 즉 `self`로 넘겨주었던 것입니다. 

그러므로 `C.method_two(t)`의 의미는 인스턴스를 변수에 할 당하지 않고, 명시적으로 `self` 라는 변수에 인스턴스로 사용할 변수를 집어 넣어 이를 실행 한 것이지요.

```python
t = C()
t.method_two()
```

