num = 0

current = 1 ### 초기값 설정

while current <= 31: ### 현재 값이 31이 될 떄 까지 반복
    
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

    for i in range(num):
        print(f"playerA : {current}")
        if current == 31:
            exit()
        current += 1

    ### 몇 개 까지 작성했는지 알아야 다음 플레이어를 추가 할 수 있으므로 현재 값 추가

    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    ##B 입력 받음

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


    for i in range(num):
        print(f"playerB : {current}")
        if current == 31:
            exit()
        current += 1