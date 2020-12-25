class ShogiKoma:
    KOMA_NAMES = ['王','玉','飛','龍','角','馬','金','銀','全','桂','圭','香','杏','歩','と']
    REVERSE_KOMA_NAMES = {'王':'王̟','玉':'玉̟','飛':'飛̟','龍':'龍̟','角':'角̟','馬':'馬̟','金':'金̟','銀':'銀̟','全':'全̟','桂':'桂̟','圭':'圭̟','香':'香̟','杏':'杏̟','歩':'歩̟','と':'と̟'}
    NARI_DICT = {'銀':'全','桂':'圭','香':'杏','歩':'と'}

    def __init__(self, name, x, y, direction):
        if name not in self.KOMA_NAMES: raise ValueError('Invalid KOMA name')
        if (x is not None and (x < 1 or x > 9)) or (y is not None and (y < 1 or y > 9)): raise ValueError('X or Y out of range(1~9)')
        if direction == 0:raise ValueError('direction cannot be 0')
        self.name = name
        self.reverse_name = self.REVERSE_KOMA_NAMES[name]
        self.x = x
        self.y = y
        self.direction = direction

    def can_move(self, x, y):
        if x < 1 or x > 9 or y < 1 or y > 9: return False
        if self.x == x and self.y == y: return False
        if self.name in ['王','玉','龍','馬']:
            if abs(self.x - x) < 2 and abs(self.y - y) < 2: return True
        if self.name in ['飛','龍']:
            if self.x == x or self.y == y:return True
        if self.name in ['角','馬']:
            if abs(self.x - x) == abs(self.y - y):return True
        if self.name in ['金','全','圭','杏','と']:
            if abs(self.x - x) < 2 and abs(self.y - y) < 2 and not (self.x != x and self.y != y and ((y - self.y) > 0) ^ (self.direction > 0)): return True
        if self.name == '銀':
            if abs(self.x - x) < 2 and abs(self.y - y) < 2 and self.y != y and not (self.x == x and (((y - self.y) > 0) ^ (self.direction > 0))): return True
        if self.name == '桂':
            if abs(self.x - x) == 1 and abs(self.y - y) == 2 and not (((y - self.y) > 0) ^ (self.direction > 0)): return True
        if self.name == '香':
            if self.x == x and not (((y - self.y) > 0) ^ (self.direction > 0)): return True
        if self.name == '歩':
            if self.x == x and abs(self.y - y) == 1 and not (((y - self.y) > 0) ^ (self.direction > 0)): return True
        return False

    def movable_points(self):
        points = []
        for x in range(1,10):
            for y in range(1,10):
                if self.can_move(x,y):points.append([x,y])
        return points

    def nari(self):
        if self.name not in self.NARI_DICT.keys(): raise RuntimeError('This KOMA cannot nari')
        self.name = self.NARI_DICT[self.name]

    def move(self, x, y, nari=False):
        if not self.can_move(x, y):raise RuntimeError('cannot move KOMA to {},{}'.format(x,y))
        if nari: self.nari()
        self.x = x
        self.y = y


