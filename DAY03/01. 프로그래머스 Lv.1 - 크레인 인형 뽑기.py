# 게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이다.
# 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있다.
# 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸이다.
# 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있다.
# 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있다. 
# 집어 올린 인형은 바구니에 쌓이게 되는데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 된다. 
# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 된다.
# 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않는다.
# 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다. 
# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어진다.
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성하라.

import numpy as np

def solution(board, moves):
    answer = 0
    n = len(board)
    doll = 0
    basket = []
    board1 = np.transpose(board)

    for move in moves:
        doll = 0
        for i, doll in enumerate(board1[move-1]):
            
            # 인형이 있는 경우
            if doll != 0:
                board1[move-1][i] = 0
                # 바구니가 비어 있을 경우
                if len(basket) == 0:
                    basket.append(doll)
                # 이전 인형과 같지 않을 경우
                elif doll != basket[len(basket)-1]:
                    basket.append(doll)
                # 이전 인형과 같은 경우
                else:
                    basket.pop()
                    answer += 2
                break
            else:
                continue

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
