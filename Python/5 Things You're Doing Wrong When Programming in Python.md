# 5 Things You're Doing Wrong When Programming in Python

<iframe width="auto" height="auto" src="https://www.youtube.com/embed/fMRzuwlqfzs" frameborder="0" allowfullscreen>
</iframe>

> Jack of Some 유투버가 제작한 위 영상을 보고 포스팅한 글입니다. 대학교에서 Python 수강시 다루지 않았던 내용을 다뤄 Python 공부에 도움이 되고자 작성하게 되었습니다. 

## `if _name_ = “__main__”` 사용하지 않는 실수

Git Hub 코드를 보다 보면 코드 마지막 줄에 항항 `if __name__ == "__main__"`으로 시작하는 문장을 본적이 있을 것이다.
```python
if __name__ == '__main__':
    코드
```

이 코드는 현재 스크립트 파일이 실행되는 상태를 파악하기 위새 사용한다. 다음 예시를 보며 살펴보자. 간단하게 For 문을 돌려 String을 출력하는 함수를 만들어 보았다. 
![](https://images.velog.io/images/metterian/post/b3994418-3716-481d-b386-b0ea2f614ec0/image.png)

출력 결과는 다음과 같다.

```python
I swear I'm useful: 0
I swear I'm useful: 1
I swear I'm useful: 2
I swear I'm useful: 3
```

하지만, 파이썬을 모듈화 혹은 라이브러리화 해서 사용하는 경우에는 어떨까? 그럴 경우 위 코드를 다른 곳에서 `import` 하여 사용해야 한다. 간단하게 `ipython`을 실행해서 확인해보자.

```python
>>> from one_main import useful_function
I swear I'm useful: 0
I swear I'm useful: 1
I swear I'm useful: 2
I swear I'm useful: 3
I swear I'm useful: 4
```

나는 모듈을 불러와서 하직 함수를 호출하기도 전 인데 Python은 모든 스크립트를 불러와서 8번 줄의 `useful_function`을 호출해주고 있다. 이것을 해결하기 위해 코드를 다음과 같이 변경해 준다. 

![](https://images.velog.io/images/metterian/post/fde544fe-b9e3-4b0d-a0fc-8252196e4c3d/carbon%20(3).png)

블락되어 있던 Line 11 ~ 12번이 블락 해제 되었다. 코드를 실행 해보면 다음과 같다.
```python
>>> from one_main import useful_function
>>>
```
이전과는 달리 `useful_function`이 호출되지 않은 결과를 볼 수 있고, 다음과 같이 함수를 호출해서 사용할 수 있다.
```python
>>> from one_main import useful_function
>>> useful_function()
I swear I'm useful: 0
I swear I'm useful: 1
I swear I'm useful: 2
I swear I'm useful: 3
I swear I'm useful: 4
```

## `Except`문 제대로 사용하지 않는 실수
Python 코드를 작성할때 디버깅 혹은 테스팅으로 `except`을 사용하는데 다음과 같이 작성하곤 한다. `While` 문 안에 `try`와 `exept`문이 있고, `try`문에 어떠한(모든) 오류가 생격을 경우 `exept`문을 실행 한다는 뜻이다. 

![](https://images.velog.io/images/metterian/post/da1bd7b4-0edc-43aa-ab89-dc137fb1fccb/carbon%20(4).png)


위 코드를 실행시켰을 때 결과는 다음과 같다. 주목할 점은 `While`을 종료하기 위해서 `Ctrl+c`를 계속 눌러 보아도 `execpt`문이 실행 되어 종료 되지 않는 문제이다.

원인은 `Ctrl+c`을 누를 경우 `SIGKILL` Signal 전달되서 Python 실행이 중지 되어야 하나, Python 스크립트에서 이를 무시하고 `execpt`문을 실행 되기 때문이다. 
```python 
Wheeee! You Can't stop me
Wheeee! You Can't stop me
^COww... Whatever imma keep running # Ctrl + C
Wheeee! You Can't stop me
Wheeee! You Can't stop me
^COww... Whatever imma keep running # Ctrl + C
```
이를 결하기 위해서, `except`문에서 `SIGKILL` 신호를 받을 수 있도록 다음과 같이 수정해서 사용해야 한다.

![](https://images.velog.io/images/metterian/post/e317eeb8-2e20-4537-b240-7ae12d679378/carbon%20(5).png)

`execpt`문에 **Execption**이 추가 되었고 이는 `SIGKILL`을 무시 하지 않고 순수 Python code내에서 오류가 발생했을 때만 코드가 실행되도록 도와준다. 