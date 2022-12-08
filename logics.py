import random

class game:
    def start_game(self):
        matrix = [[0 for row in range(4)] for col in range(4)]
        matrix = self.new_2(matrix)
        return matrix

    def availablity(self, matrix):
        for row in range(4):
            for col in range(4):
                if matrix[row][col] == 0:
                    return True
        return False

    def new_2(self, matrix):
        if not(self.availablity(matrix)):
            return matrix
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while matrix[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        matrix[row][col] = 2
        return matrix

    def check(self, matrix):
        won = 1
        lost = 2
        not_over = 0
        for row in range(4):
            for col in range(4):
                if matrix[row][col] == 2048:
                    return won
                
        for row in range(3):
            for col in range(3):
                if matrix[row][col] == 0:
                    return not_over
                if matrix[row][col] == matrix[row][col+1] or matrix[row][col] == matrix[row+1][col]:
                    return not_over
        for row in range(3):
            col = 3
            if matrix[row][col] == 0:
                return not_over
            if matrix[row][col] == matrix[row+1][col]:
                return not_over
        
        for col in range(3):
            row = 3
            if matrix[row][col] == 2048:
                    return won
            if matrix[row][col] == 0:
                return not_over
            if matrix[row][col] == matrix[row][col+1]:
                return not_over

        return lost

    def reverse(self, matrix):
        # print(matrix)
        for row in range(4):
            matrix[row] = matrix[row][::-1]

        # print(matrix)
        return matrix

    def transpose(self, matrix):
        new_matrix = [[0 for j in range(4)] for i in range(4)]
        for row in range(4):
            for col in range(4):
                new_matrix[col][row] = matrix[row][col]
        return new_matrix

    def compress(self, matrix):
        new_matrix = [[0 for j in range(4)] for i in range(4)]
        movement = 0
        for row in range(4):
            pos = 0
            for col in range(4):
                if matrix[row][col] != 0:
                    new_matrix[row][pos] = matrix[row][col]
                    pos += 1
                    if pos != col:
                        movement = 1
                    # matrix[row][col] = 0
        # print(new_matrix)
        return movement, new_matrix

    def merge(self, matrix):
        movement = 0
        for row in range(4):
            for col in range(3):
                if matrix[row][col] == matrix[row][col+1] and matrix[row][col] != 0:
                    matrix[row][col] *= 2
                    matrix[row][col + 1] = 0
                    movement = 1
        # print(matrix)
        return movement, matrix

    def move_left(self, matrix):
        # print("left")
        m, cMatrix = self.compress(matrix)
        m, mMatrix = self.merge(cMatrix)
        m, cMatrix = self.compress(mMatrix)
        check = self.check(cMatrix)
        if not check and m:
            cMatrix = self.new_2(cMatrix)
        return check, cMatrix

    def move_right(self, matrix):
        # print("right")
        rMatrix = self.reverse(matrix)
        m, cMatrix = self.compress(rMatrix)
        m, mMatrix = self.merge(cMatrix)
        m, cMatrix = self.compress(mMatrix)
        rMatrix = self.reverse(cMatrix)
        check = self.check(rMatrix)
        if not check and m:
            rMatrix = self.new_2(rMatrix)
        return check, rMatrix

    def move_down(self, matrix):
        # print("down")
        tMatrix = self.transpose(matrix)
        # print(tMatrix)
        rMatrix = self.reverse(tMatrix)
        m, cMatrix = self.compress(rMatrix)
        m, mMatrix = self.merge(cMatrix)
        m, cMatrix = self.compress(mMatrix)
        rMatrix = self.reverse(cMatrix)
        tMatrix = self.transpose(rMatrix)
        check = self.check(tMatrix)
        if not check and m:
            tMatrix = self.new_2(tMatrix)
        return check, tMatrix

    def move_up(self, matrix):
        # print("up")
        tMatrix = self.transpose(matrix)
        # print(tMatrix)
        m, cMatrix = self.compress(tMatrix)
        # print(cMatrix)
        m, mMatrix = self.merge(cMatrix)
        m, cMatrix = self.compress(mMatrix)
        tMatrix = self.transpose(cMatrix)
        check = self.check(tMatrix)
        if not check and m:
            tMatrix = self.new_2(tMatrix)
        # print(tMatrix)
        return check, tMatrix

g = game()
matrix = g.start_game()
flag = 0
print(matrix)
while (not flag):
    move = random.randint(1,4)
    # print(move)
    if move == 1:
        # print("left")
        flag, matrix = g.move_left(matrix)
    elif move == 2:
        # print("right")
        flag, matrix = g.move_right(matrix)
    elif flag == 3:
        # print("up")
        flag, matrix = g.move_up(matrix)
    else:
        # print("down")
        flag, matrix = g.move_down(matrix)
    if flag == 1:
        print("Yow won")
        break
    if flag == 2:
        print("you lost")
        break
    print(matrix)