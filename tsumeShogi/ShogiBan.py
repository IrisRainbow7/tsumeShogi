import tsumeShogi

class ShogiBan:

    def __init__(self, komas=[]):
        self.ban = [[None] * 9 for i in range(9)]
        for k in komas:
            if self.ban[k.y-1][k.x-1] is not None: raise RuntimeError('invalid komas(same point komas)')
            self.ban[k.y-1][k.x-1] = k
        self.komas = komas[:]
        self.player1_hands = []
        self.player2_hands = []

    def init(self):
        komas = []
        komas.append(tsumeShogi.ShogiKoma('香',1,1,1))
        komas.append(tsumeShogi.ShogiKoma('桂',2,1,1))
        komas.append(tsumeShogi.ShogiKoma('銀',3,1,1))
        komas.append(tsumeShogi.ShogiKoma('金',4,1,1))
        komas.append(tsumeShogi.ShogiKoma('玉',5,1,1))
        komas.append(tsumeShogi.ShogiKoma('金',6,1,1))
        komas.append(tsumeShogi.ShogiKoma('銀',7,1,1))
        komas.append(tsumeShogi.ShogiKoma('桂',8,1,1))
        komas.append(tsumeShogi.ShogiKoma('香',9,1,1))
        komas.append(tsumeShogi.ShogiKoma('飛',8,2,1))
        komas.append(tsumeShogi.ShogiKoma('角',2,2,1))
        for i in range(1,10):
            komas.append(tsumeShogi.ShogiKoma('歩',i,3,1))
        komas.append(tsumeShogi.ShogiKoma('香',1,9,-1))
        komas.append(tsumeShogi.ShogiKoma('桂',2,9,-1))
        komas.append(tsumeShogi.ShogiKoma('銀',3,9,-1))
        komas.append(tsumeShogi.ShogiKoma('金',4,9,-1))
        komas.append(tsumeShogi.ShogiKoma('玉',5,9,-1))
        komas.append(tsumeShogi.ShogiKoma('金',6,9,-1))
        komas.append(tsumeShogi.ShogiKoma('銀',7,9,-1))
        komas.append(tsumeShogi.ShogiKoma('桂',8,9,-1))
        komas.append(tsumeShogi.ShogiKoma('香',9,9,-1))
        komas.append(tsumeShogi.ShogiKoma('飛',2,8,-1))
        komas.append(tsumeShogi.ShogiKoma('角',8,8,-1))
        for i in range(1,10):
            komas.append(tsumeShogi.ShogiKoma('歩',i,7,-1))
        self.komas = komas[:]
        for k in komas:
            self.ban[k.y-1][k.x-1] = k

    def display(self):
        for i in self.ban:
            for j in i[::-1]:
                if j is None:
                    print("口", end="")
                else:
                    if j.direction < 0:
                        print(j.name, end="")
                    else:
                        print(j.reverse_name, end="")
            print("")

    def can_move(self, koma, x, y):
        if not isinstance(koma, tsumeShogi.ShogiKoma): raise RuntimeError('require ShogiKoma object at 1st argument')
        if self.ban[y-1][x-1] is not None and ((koma.direction * self.ban[y-1][x-1]) > 0): return False
        if not koma.can_move(x,y): return False
        if self.name in ['飛','龍']:
            if koma.x == x:
                for i in range(min(koma.y,y)+1,max(koma.y,y)):
                    if self.ban[i][koma.x] is not None: return False
            else:
                for i in range(min(koma.x,x)+1,max(koma.x,x)):
                    if self.ban[koma.y][i] is not None: return False
        if self.name in ['角','馬']:
            for i in range(1,abs(koma.x-x)-1):
                _x = koma.x + i * int(x - koma.x > 0)
                _y = koma.y + i * int(y - koma.y > 0)
                if self.ban[_y-1][_x-1] is not None: return False
        if self.name == '香':
            for i in range(min(koma.y,y)+1,max(koma.y,y)):
                if self.ban[i][koma.x] is not None: return False
        return True


