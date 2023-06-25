import random

print(
    '''
   ++----++----++----++
   Number Baseball Game
   ++----++----++----++\n
   1~9까지의 숫자 중 숫자 3개의 값과 숫자의 위치를 맞추는 게임입니다. \n
   - 포함된 숫자도 맞고 위치도 맞으면 스트라이크(Strike)
   - 포함된 숫자는 맞지만 위치가 맞지 않으면 볼(Ball)
   - 하나도 일치하지 않으면 아웃(out)
   - 숫자는 중복되지 않습니다.
   - 기회는 총 5번입니다.
   '''
)


# 랜덤 숫자 리스트 생성 함수
def r_number():
    random_number = random.sample(range(10), 3)
    return random_number


# 오류 제거 함수
def take_guess():
    i = 0
    n_num = []

    while len(n_num) < 3:

        try:
            game_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        except:
            print("0 ~ 9의 값만 입력할 수 있습니다. 다시 입력하세요.")
            continue

        if game_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue

        elif game_number in n_num:
            print("중복되는 숫자입니다. 다시 입력하세요.")

        else:
            n_num.append(game_number)
            i += 1

    return n_num


# 게임 점수 계산 함수
def game_score(guess, g_num):
    strike_num = 0
    ball_num = 0
    i = 0

    while i < len(guess):

        if guess[i] == g_num[i]:
            strike_num += 1
            i += 1

        elif guess[i] in g_num:
            ball_num += 1
            i += 1

        else:
            i += 1

    return strike_num, ball_num


number_list = r_number()
tries = 0

# 게임 실행문
while 1:

    guess_s = take_guess()
    strike, ball = game_score(guess_s, number_list)

    print(f"-----------------------------\nStrike {strike}개 Ball: {ball}개")
    tries += 1
    print(("\n남은 기회: {}\n-----------------------------".format(5 - tries)))

    if strike == 3:
        print(f"++-------정답입니다-------++\n-----------------------------\n{tries}번 만에 성공하였습니다.\n")
        break

    if tries > 4:
        print("~~~~~~>>> Game Over <<<~~~~~~")
        print(f"정답: {r_number()}")

        while True:
            reset_game = str(input("-----------------------------\n다시 도전하시겠습니까?: [y/n]"))
            if reset_game == "y":
                number_list = r_number()
                tries = 0
                break

            elif reset_game == "n":
                exit()

            else:
                print(" [y] or [n] 만 입력할 수 있습니다. 다시 입력하세요.")
