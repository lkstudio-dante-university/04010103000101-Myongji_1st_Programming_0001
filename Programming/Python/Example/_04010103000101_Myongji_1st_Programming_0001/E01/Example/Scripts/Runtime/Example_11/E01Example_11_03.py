import os
import sys

# Example 11 - 3
def E01Example_11_03(args):
	i = 0
	print("=====> while 반복문 <=====")
	
	"""
	while 반복문 사용 방법
	- while + 조건 + 반복 할 명령문
	"""
	while i < 10:
		"""
		print 메서드에 end 문자를 명시해주면 자동으로 개행처리되는 것을 방지 할 수 있다. (즉, print 메서드는 항상 주어진 문장을 출력 후
		개행 처리를 하기 때문에 특정 라인에 여러 문장을 출력하고 싶다면 end 문자를 변경해주면 된다.)
		"""
		print("{0}, ".format(i + 1), end="")
		i += 1
	
	print("\n\n=====> for 반복문 <=====")
	
	"""
	for 반복문 사용 방법
	- for + 반복 변수 + 컬렉션 (반복 가능 객체)
	
	for 반복문은 컬렉션 or 반복 가능한 객체를 대상으로 동작한다. (즉, for 반복문은 특정 컬렉션을 순회하는 것이 주된 목적이기 때문에
	순회문이라고도 불린다.)
	
	range 메서드는 입력으로 전달 된 데이터를 기반으로 반복 가능한 객체를 생성하는 역할을 수행한다. (즉, 해당 메서드를 활용하면 특정 횟수만큼
	반복하도록 for 반복문의 조건을 명시하는 것이 가능하다.)
	"""
	for i in range(0, 10):
		print("{0}, ".format(i + 1), end="")
	
	print()
