num = 0

num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
### 정수 타입으로만 받으면 그 이외의 상황에 에러가 나므로 2단계에 대해서 수정함

while True:
    if not num.isdigit(): ###정수 확인 메서드 사용
        print("정수를 입력하세요")
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        continue

    num = int(num)

    if num not in [1, 2, 3]:
        print("1, 2, 3 중 하나를 입력하세요")
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        continue

    break

for i in range(1, num + 1):
    print(f"playerA : {i}")