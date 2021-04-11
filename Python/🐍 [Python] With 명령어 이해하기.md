## 💁🏻‍♂️ 들어가며
`with` 명령어는 Python을 사용할 때 이해하기 어려운 부분 중에 하나입니다. 하지만, 이를 이해하고 나면 Python의 매직같은 기능 중에 하나 인 걸 알게 될겁니다. 게다가, Python 코드가 더 깔끔해지고 읽기 쉬워 집니다.

`with` 명령어의 가장 큰 특징은 재사용되는 부분을 줄여주는 기능입니다. 다음 예제를 보면 이해가 좀 더 쉬울 겁니다.

## <br/>🤔 예제

`with`명령어와  가장 많이 사용되는 예제 중 `open` 함수를 사용한 코드를 쉽게  찾아 불 수 있습니다. 

```python
with open('hello.txt', 'w') as f: 
		f.write('hello, world!')
```

파일을 읽고 쓰는 과정은 PC 입장에서 굉장히 중대한 일 중에 하나입니다. 일반적으로 파일을 읽고 쓸때 파일 디스크립터(File discriptor)란 친구를 불러오고 닫아 줘야 해요. 다음과 같이 말이죠.

```python
f = open('hello.txt', 'w') 
try:
		f.write('hello, world') 
finally:
		f.close()
```

파일에 쓰기 혹은 불러오기에 오류 처리를 해줘야하고 파일을 불러와서 작업이 끝나면 항상 파일 디스크립터를 닫아줘야 해요. 하지만, 이러한 코드는 꽤나 복잡하기에 일반적으로 다음과 같이 작성하기도 해요.

```python
f = open('hello.txt', 'w') 
f.write('hello, world') 
f.close()
```

이제 좀 더 익숙한 파일 읽기 쓰기죠? 하지만 이런 코드는 `f.close()` 이전에 오류가 발생해서 코드가 실행되지 않으면 파일 디스크립터가 메로리에 남게 되는 치명적인 문제가 생길 수 있어요. 그래서 `with` 명령어를 사용해서 이런 반복된 과정을 줄여 줄 수 있어요. `with` 명령어를 사용하므로써, 버그도 줄여주고 효율적인 코드가 되는 것이죠.

## <br/>🤖 클래스 객체와 함께 사용하기

`with`의 다음 기능으로 **context managers** 라는 기능을 살펴 보아요. context manger의 정의는 다음과 같아요.

> What’s a context manager? It’s a simple “**protocol**” (or interface) that your object needs to follow in order to support the with statement.

일반적으로, 클래스를 사용할 때 `__enter__` 혹은 `__exit__`와 같은 메소드와 같은 친구들을 Context manager라고 불러요. 이제 예제를 통해 쉽게 이해 해보아요.

```python
class ManagedFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w') 
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb): 
        if self.file:
            self.file.close()
```

위와 같이 클래스를 선언하고  각 메소드들의 규칙를 따르는 Protocol을 만들 수  있어요. 파일을 읽고 쓸때 이런 프로토콜을 정의 해두면 반복적인 코드와 오류 없이 간단하게 파일을 불러 올 수있어요. 지금 이 역활을 `with` 명령어가 대신 하는 것이예요.

## <br/>요약

- `with` 명령어은 이른바 컨텍스트 관리자(context managers)에서 try/finally 문장의 사용을 캡슐화함으로써 예외 처리를 단순화한다.
- `with` 를 사용하면 리소스 누수를 방지하고 코드를 쉽게 읽을 수 있습니다.