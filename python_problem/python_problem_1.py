def brGame(player, current):
    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
    while True:
        if not num.isdigit():
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
        print(f"{player} : {current}")
        if current == 31:
            if player == "playerA":
                print("playerB win!")
            else:
                print("playerA win!")
            exit()
        current += 1

    return current



current = 1
while True:
    current = brGame("playerA", current)
    current = brGame("playerB", current)