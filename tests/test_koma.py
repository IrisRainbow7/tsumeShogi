import unittest
import tsumeShogi

class TestKoma(unittest.TestCase):

    KOMA_NAMES = ['王','玉','飛','龍','角','馬','金','銀','全','桂','圭','香','杏','歩','と']

    def test_ou(self):
        p = tsumeShogi.ShogiKoma('王',5,5,-1)
        points = [[4,4],[5,4],[6,4],[4,5],[6,5],[4,6],[5,6],[6,6]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_gyoku(self):
        p = tsumeShogi.ShogiKoma('玉',5,5,-1)
        points = [[4,4],[5,4],[6,4],[4,5],[6,5],[4,6],[5,6],[6,6]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_hisya(self):
        p = tsumeShogi.ShogiKoma('飛',5,5,-1)
        points = [[1,5],[2,5],[3,5],[4,5],[6,5],[7,5],[8,5],[9,5],[5,1],[5,2],[5,3],[5,4],[5,6],[5,7],[5,8],[5,9]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_ryuu(self):
        p = tsumeShogi.ShogiKoma('龍',5,5,-1)
        points = [[1,5],[2,5],[3,5],[4,5],[6,5],[7,5],[8,5],[9,5],[4,4],[4,6],[6,6],[6,4],[5,1],[5,2],[5,3],[5,4],[5,6],[5,7],[5,8],[5,9]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_kaku(self):
        p = tsumeShogi.ShogiKoma('角',5,5,-1)
        points = [[1,1],[9,1],[2,2],[8,2],[3,3],[7,3],[4,4],[6,4],[6,6],[4,6],[7,7],[3,7],[8,8],[2,8],[9,9],[1,9]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_uma(self):
        p = tsumeShogi.ShogiKoma('馬',5,5,-1)
        points = [[1,1],[9,1],[2,2],[8,2],[3,3],[7,3],[4,4],[6,4],[5,4],[5,6],[4,5],[6,5],[6,6],[4,6],[7,7],[3,7],[8,8],[2,8],[9,9],[1,9]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_kin(self):
        p = tsumeShogi.ShogiKoma('金',5,5,-1)
        points = [[4,4],[5,4],[6,4],[4,5],[6,5],[5,6]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_gin(self):
        p = tsumeShogi.ShogiKoma('銀',5,5,-1)
        points = [[4,4],[5,4],[6,4],[4,6],[6,6]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_kei(self):
        p = tsumeShogi.ShogiKoma('桂',5,5,-1)
        points = [[4,3],[6,3]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_kyou(self):
        p = tsumeShogi.ShogiKoma('香',5,5,-1)
        points = [[5,1],[5,2],[5,3],[5,4]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

    def test_fu(self):
        p = tsumeShogi.ShogiKoma('歩',5,5,-1)
        points = [[5,4]]
        for x in range(1,10):
            for y in range(1,10):
                if x == 5 and y == 5: continue
                self.assertEqual(p.can_move(x,y), [x,y] in points)

