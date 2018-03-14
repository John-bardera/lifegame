# coding:utf-8

import os
import time
import numpy as np

# まだ正行列しか対応してない
stage_x = 100
stage_y = 70


class Lifegame:
    def __init__(self):
        #self.game = np.zeros([stage_y + 2, stage_x + 2])

        # 壁ループなし
        game_yet = np.random.randint(0, 2, size=(stage_y + 2, stage_x + 2))

        game_format_x_format =[[0]]
        game_format_x_format.extend([[1]] * stage_y)
        game_format_x_format.append([0])

        game_format_x = np.array(list(map((lambda i: i * (stage_x + 2)), game_format_x_format)))

        game_format_y = [0]
        game_format_y.extend([1] * stage_x)
        game_format_y.append(0)

        game_format = game_format_x * game_format_y
        self.game = game_yet * game_format

        #self.game = np.random.randint(0, 2, size=(stage_y + 2, stage_x + 2))

        # 代入(=)だとarrayのポインタを代入する扱いになるのでnp.arrayでコピーする
        self.next = np.array(self.game)
        while True:
            os.system("clear")
            self.print_game()
            time.sleep(0)
            self.all_do_next()
            self.game = np.array(self.next)

    def pixcel_do(self, x, y):
        x_y_around = np.sum(list(map((lambda i: i[x-1] + i[x] + i[x+1]), (self.game[y-1:y+2]))))
        if not self.game[y][x]:
            if x_y_around == 3:
                self.next[y][x] = 1
        else:
            if x_y_around - 1 <= 1:
                self.next[y][x] = 0
            elif x_y_around - 1 >= 4:
                self.next[y][x] = 0
            else:
                self.next[y][x] = 1

    def all_do_next(self):
        for y in range(1, stage_y + 1):
            for x in range(1, stage_x + 1):
                self.pixcel_do(x, y)

    def print_game(self):
        print("_" * stage_x)
        ans = ""
        for y in range(1, stage_y + 1):
            for x in range(1, stage_x + 1):
                if self.game[y][x]:
                    ans += "人"
                else:
                    ans += "  "
            ans += "\n"
        print(ans)

if __name__ == "__main__":
    Lifegame()
