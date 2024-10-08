import os
import sys

from .E01Example_10_01 import E01Example_10_01
from .E01Example_10_02 import E01Example_10_02
from .E01Example_10_03 import E01Example_10_03

"""
Python 변수 종류
- 지역 변수
- 전역 변수

지역 변수 vs 전역 변수
- 지역 변수는 특정 영역에 속해있는 변수를 의미하며 해당 변수가 선언 된 지역 내부에서만 사용 할 수 있다는 특징이 존재한다. 반면, 전역 변수는
특정 영역에 속해 읺지 않은 변수를 의미하며 프로그램 전체에서 사용 가능하다는 차이점이 존재한다. (즉, 지역 변수는 해당 변수가 선언 된 영역을
벗어나면 사라지는 특징이 있다는 것을 알 수 있다.)

Python 에서 특정 지역 (영역) 은 : (콜론) 기호로 시작한다. (즉, 해당 기호 하위에 선언 된 변수 또는 매개 변수는 지역 변수라는 것을 의미한다.)

Python 변수 선언 방법
- 변수 이름 + 자료형 (옵션) + 초기화 데이터

Ex)
nVal = 0
nVal: int = 0

Python 은 강력 형식 언어 (Strong Type Language) 가 아니기 때문에 자료형을 명시하지 않고 변수를 선언하는 것이 가능하다.
(즉, Python 은 변수가 관리하는 데이터의 자료형을 제한하지 않는다는 것을 알 수 있다.)

단, Python 은 변수에 자료형을 명시하는 기능을 제공하며 해당 기능을 활용하면 에디터의 인텔리센스 기능의 도움을 받는 것이 가능하다.
(즉, 지역 변수나 매개 변수는 초기화 데이터를 통해 에디터가 해당 변수의 자료형을 유추하는 것이 가능하지만 매개 변수는 초기화 데이터가 존재하지
않기 때문에 자료형을 명시하지 않으면 에디터의 인텔리센스 기능이 동작하지 않는다.)

Python 은 변수 이름을 비롯한 특정 대상의 이름을 작성 할 때에는 알파벳 대/소문자, _ (언더 스코어), 숫자만 사용하는 것을 추천한다. (즉, 일부
특수 문자를 제외한 여러 문자를 통해 이름을 작성하는 것이 가능하지만 대부분의 언어가 알파벳만을 지원하기 때문에 이를 따르는 것이 좋은 선택이라는
것을 알 수 있다.)

또한, 이름의 첫 문자는 숫자가 될 수 없다는 특징이 존재한다.

Ex)
nValA = 0
01nVal = 0

위의 경우 nValA 이름은 사용하는 것이 가능하지만 01nVal 은 첫 문자로 숫자로 시작하기 때문에 사용하는 것이 불가능하다.

연산자란?
- 프로그램이 동작하는데 특별한 역할을 수행하는 기호 (심볼) 을 의미한다. (즉, 연산자를 활용하면 특정 데이터를 프로그램의 목적에 맞게 처리하는
것이 가능하다는 것을 알 수 있다.)

Python 은 피연산자를 1 개 요구하는 단항 연산자와 피연산자를 2 개 요구하는 이항 연산자를 지원한다. 또한, 연산자는 한 라인에 중첩으로 작성하는
것이 가능하며 한 라인에 중첩으로 작성 된 연산자는 우선 순위에 따라 처리 순서가 결정된다.

Ex)
2 + 2 * 2		<- 6
(2 + 2) * 2		<- 8

* (곱하기 연산자) 는 + (더하기 연산자) 보다 우선 순위가 높기 때문에 먼저 처리 된다는 것을 알 수 있다. 이때, 연산자의 처리 순서를 변경하고
싶다면 ( ) (우선 순위 연산자) 를 명시해주면 된다.

Python 연산자 종류
- 산술 연산자 (+, -, *, /, %, **, //)
- 관계 연산자 (<, >, <=, >=, ==, !=)
- 할당 연산자 (=, +=, -=, *=, /=, 등등...)
- 논리 연산자 (and, or, not)
- 비트 연산자 (&, |, ^, <<, >>, ~)
- 기타 연산자 (우선 순위 연산자, 함수 호출 연산자 등등...)

관계 연산자란?
- 데이터의 대/소 여부를 판단하기 위한 연산자를 의미한다. (즉, 해당 연산자의 결과는 참 or 또는 거짓을 나타내는 bool 형 데이터가
반환된다는 것을 알 수 있다.)

할당 연산자란?
- 우항에 명시 된 데이터를 좌항에 명시 된 변수에 저장하는 연산자를 의미한다. (즉, 특정 변수에 데이터를 저장하기 위해서는 할당 연산자를
활용하면 된다는 것을 알 수 있다.)

비트 연산자란?
- 프로그래밍 언어의 기본 단위는 바이트이기 때문에 대부분의 연산자는 바이트 단위로 동작하는 특징이 존재한다. 반면, 비트 연산자는 비트 단위로
데이터를 제어하는 것이 가능하다. (즉, 비트 단위로 데이터를 제어함으로서 프로그램이 사용하는 메모리를 최소화 시키는 것이 가능하다.)
"""

# Example 10
def E01Example_10(args):
	# E01Example_10_01(args)
	# E01Example_10_02(args)
	E01Example_10_03(args)
