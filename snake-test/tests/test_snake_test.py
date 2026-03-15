from snake.snake import point_equals as point_equals_29, is_opposite as is_opposite_30, direction_delta as direction_delta_31, next_random as next_random_32, new_game as new_game_33, change_direction as change_direction_34, tick as tick_35, SnakeGame, Point, Playing, Right, Down, Up, Left, GameOver, RandomResult
from temper_std.testing import Test
from unittest import TestCase as TestCase6
from builtins import bool as bool7, str as str8, isinstance as isinstance10, int as int19
from typing import Sequence as Sequence21
from snake_test.snake_test import list_get_or_777, str_cat_778, int_to_string_779, len_780, int_add_781
class TestCase5(TestCase6):
    def test___initialStateHasSnakeNearCenter__86(self) -> None:
        'initial state has snake near center'
        test_0: Test = Test()
        try:
            game_38: 'SnakeGame' = new_game_33(10, 10, 42)
            head_39: 'Point' = list_get_or_777(game_38.snake, 0, Point(-1, -1))
            t_766: 'bool7' = head_39.x == 5
            def fn_759() -> 'str8':
                return str_cat_778('head x should be 5, got ', int_to_string_779(head_39.x))
            test_0.assert_(t_766, fn_759)
            t_770: 'bool7' = head_39.y == 5
            def fn_758() -> 'str8':
                return str_cat_778('head y should be 5, got ', int_to_string_779(head_39.y))
            test_0.assert_(t_770, fn_758)
            t_775: 'bool7' = len_780(game_38.snake) == 3
            def fn_757() -> 'str8':
                return 'snake should start with 3 segments'
            test_0.assert_(t_775, fn_757)
        finally:
            test_0.soft_fail_to_hard()
class TestCase9(TestCase6):
    def test___initialStatusIsPlaying__87(self) -> None:
        'initial status is Playing'
        test_1: Test = Test()
        try:
            game_41: 'SnakeGame' = new_game_33(10, 10, 42)
            t_750: 'bool7' = isinstance10(game_41.status, Playing)
            def fn_747() -> 'str8':
                return 'initial status should be Playing'
            test_1.assert_(t_750, fn_747)
        finally:
            test_1.soft_fail_to_hard()
class TestCase11(TestCase6):
    def test___initialDirectionIsRight__88(self) -> None:
        'initial direction is Right'
        test_2: Test = Test()
        try:
            game_43: 'SnakeGame' = new_game_33(10, 10, 42)
            t_744: 'bool7' = isinstance10(game_43.direction, Right)
            def fn_741() -> 'str8':
                return 'initial direction should be Right'
            test_2.assert_(t_744, fn_741)
        finally:
            test_2.soft_fail_to_hard()
class TestCase12(TestCase6):
    def test___initialScoreIs0__89(self) -> None:
        'initial score is 0'
        test_3: Test = Test()
        try:
            game_45: 'SnakeGame' = new_game_33(10, 10, 42)
            t_739: 'bool7' = game_45.score == 0
            def fn_735() -> 'str8':
                return 'initial score should be 0'
            test_3.assert_(t_739, fn_735)
        finally:
            test_3.soft_fail_to_hard()
class TestCase13(TestCase6):
    def test___snakeMovesRight__90(self) -> None:
        'snake moves right'
        test_4: Test = Test()
        try:
            game_47: 'SnakeGame' = new_game_33(10, 10, 42)
            moved_48: 'SnakeGame' = tick_35(game_47)
            head_49: 'Point' = list_get_or_777(moved_48.snake, 0, Point(-1, -1))
            t_729: 'bool7' = head_49.x == 6
            def fn_721() -> 'str8':
                return str_cat_778('head should move right to x=6, got ', int_to_string_779(head_49.x))
            test_4.assert_(t_729, fn_721)
            t_733: 'bool7' = head_49.y == 5
            def fn_720() -> 'str8':
                return str_cat_778('head y should stay 5, got ', int_to_string_779(head_49.y))
            test_4.assert_(t_733, fn_720)
        finally:
            test_4.soft_fail_to_hard()
class TestCase14(TestCase6):
    def test___snakeMovesDown__91(self) -> None:
        'snake moves down'
        test_5: Test = Test()
        try:
            game_51: 'SnakeGame' = change_direction_34(new_game_33(10, 10, 42), Down())
            moved_52: 'SnakeGame' = tick_35(game_51)
            head_53: 'Point' = list_get_or_777(moved_52.snake, 0, Point(-1, -1))
            t_710: 'bool7' = head_53.x == 5
            def fn_701() -> 'str8':
                return str_cat_778('head x should stay 5, got ', int_to_string_779(head_53.x))
            test_5.assert_(t_710, fn_701)
            t_714: 'bool7' = head_53.y == 6
            def fn_700() -> 'str8':
                return str_cat_778('head should move down to y=6, got ', int_to_string_779(head_53.y))
            test_5.assert_(t_714, fn_700)
        finally:
            test_5.soft_fail_to_hard()
class TestCase15(TestCase6):
    def test___snakeMovesUp__92(self) -> None:
        'snake moves up'
        test_6: Test = Test()
        try:
            game_55: 'SnakeGame' = change_direction_34(new_game_33(10, 10, 42), Up())
            moved_56: 'SnakeGame' = tick_35(game_55)
            head_57: 'Point' = list_get_or_777(moved_56.snake, 0, Point(-1, -1))
            t_694: 'bool7' = head_57.y == 4
            def fn_685() -> 'str8':
                return str_cat_778('head should move up to y=4, got ', int_to_string_779(head_57.y))
            test_6.assert_(t_694, fn_685)
        finally:
            test_6.soft_fail_to_hard()
class TestCase16(TestCase6):
    def test___oppositeDirectionIsRejected__93(self) -> None:
        'opposite direction is rejected'
        test_7: Test = Test()
        try:
            game_59: 'SnakeGame' = new_game_33(10, 10, 42)
            changed_60: 'SnakeGame' = change_direction_34(game_59, Left())
            t_680: 'bool7' = isinstance10(changed_60.direction, Right)
            def fn_676() -> 'str8':
                return 'should still be Right after trying Left'
            test_7.assert_(t_680, fn_676)
        finally:
            test_7.soft_fail_to_hard()
class TestCase17(TestCase6):
    def test___nonOppositeDirectionIsAccepted__94(self) -> None:
        'non-opposite direction is accepted'
        test_8: Test = Test()
        try:
            game_62: 'SnakeGame' = new_game_33(10, 10, 42)
            changed_63: 'SnakeGame' = change_direction_34(game_62, Up())
            t_673: 'bool7' = isinstance10(changed_63.direction, Up)
            def fn_669() -> 'str8':
                return 'should change to Up'
            test_8.assert_(t_673, fn_669)
        finally:
            test_8.soft_fail_to_hard()
class TestCase18(TestCase6):
    def test___wallCollisionCausesGameOver__95(self) -> None:
        'wall collision causes game over'
        test_9: Test = Test()
        try:
            t_664: 'SnakeGame'
            t_663: 'SnakeGame' = new_game_33(10, 10, 42)
            game_65: 'SnakeGame' = t_663
            i_66: 'int19' = 0
            while i_66 < 10:
                t_664 = tick_35(game_65)
                game_65 = t_664
                i_66 = int_add_781(i_66, 1)
            t_666: 'bool7' = isinstance10(game_65.status, GameOver)
            def fn_662() -> 'str8':
                return 'should be GameOver after hitting wall'
            test_9.assert_(t_666, fn_662)
        finally:
            test_9.soft_fail_to_hard()
class TestCase20(TestCase6):
    def test___selfCollisionCausesGameOver__96(self) -> None:
        'self collision causes game over'
        test_10: Test = Test()
        try:
            snake_68: 'Sequence21[Point]' = (Point(5, 5), Point(6, 5), Point(6, 4), Point(5, 4), Point(4, 4), Point(4, 5), Point(4, 6))
            t_656: 'SnakeGame' = SnakeGame(10, 10, snake_68, Left(), Point(0, 0), 0, Playing(), 42)
            game_69: 'SnakeGame' = t_656
            t_657: 'SnakeGame' = tick_35(game_69)
            game_69 = t_657
            t_659: 'bool7' = isinstance10(game_69.status, GameOver)
            def fn_645() -> 'str8':
                return 'should be GameOver after self collision'
            test_10.assert_(t_659, fn_645)
        finally:
            test_10.soft_fail_to_hard()
class TestCase22(TestCase6):
    def test___pointEqualsWorksForSamePoints__97(self) -> None:
        'pointEquals works for same points'
        test_11: Test = Test()
        try:
            t_643: 'bool7' = point_equals_29(Point(3, 4), Point(3, 4))
            def fn_639() -> 'str8':
                return 'same points should be equal'
            test_11.assert_(t_643, fn_639)
        finally:
            test_11.soft_fail_to_hard()
class TestCase23(TestCase6):
    def test___pointEqualsWorksForDifferentPoints__98(self) -> None:
        'pointEquals works for different points'
        test_12: Test = Test()
        try:
            t_637: 'bool7' = not point_equals_29(Point(3, 4), Point(5, 6))
            def fn_633() -> 'str8':
                return 'different points should not be equal'
            test_12.assert_(t_637, fn_633)
        finally:
            test_12.soft_fail_to_hard()
class TestCase24(TestCase6):
    def test___isOppositeDetectsOppositeDirections__99(self) -> None:
        'isOpposite detects opposite directions'
        test_13: Test = Test()
        try:
            t_621: 'bool7' = is_opposite_30(Up(), Down())
            def fn_617() -> 'str8':
                return 'Up/Down are opposite'
            test_13.assert_(t_621, fn_617)
            t_626: 'bool7' = is_opposite_30(Left(), Right())
            def fn_616() -> 'str8':
                return 'Left/Right are opposite'
            test_13.assert_(t_626, fn_616)
            t_631: 'bool7' = not is_opposite_30(Up(), Left())
            def fn_615() -> 'str8':
                return 'Up/Left are not opposite'
            test_13.assert_(t_631, fn_615)
        finally:
            test_13.soft_fail_to_hard()
class TestCase25(TestCase6):
    def test___directionDeltaReturnsCorrectDeltas__100(self) -> None:
        'directionDelta returns correct deltas'
        test_14: Test = Test()
        try:
            t_607: 'int19'
            t_612: 'int19'
            t_279: 'bool7'
            t_284: 'bool7'
            up_74: 'Point' = direction_delta_31(Up())
            if up_74.x == 0:
                t_607 = up_74.y
                t_279 = t_607 == -1
            else:
                t_279 = False
            def fn_604() -> 'str8':
                return 'Up should be (0, -1)'
            test_14.assert_(t_279, fn_604)
            right_75: 'Point' = direction_delta_31(Right())
            if right_75.x == 1:
                t_612 = right_75.y
                t_284 = t_612 == 0
            else:
                t_284 = False
            def fn_603() -> 'str8':
                return 'Right should be (1, 0)'
            test_14.assert_(t_284, fn_603)
        finally:
            test_14.soft_fail_to_hard()
class TestCase26(TestCase6):
    def test___prngIsDeterministic__101(self) -> None:
        'PRNG is deterministic'
        test_17: Test = Test()
        try:
            r1_77: 'RandomResult' = next_random_32(42, 100)
            r2_78: 'RandomResult' = next_random_32(42, 100)
            t_596: 'bool7' = r1_77.value == r2_78.value
            def fn_592() -> 'str8':
                return 'same seed should produce same value'
            test_17.assert_(t_596, fn_592)
            t_601: 'bool7' = r1_77.next_seed == r2_78.next_seed
            def fn_591() -> 'str8':
                return 'same seed should produce same next seed'
            test_17.assert_(t_601, fn_591)
        finally:
            test_17.soft_fail_to_hard()
class TestCase27(TestCase6):
    def test___prngProducesValuesInRange__102(self) -> None:
        'PRNG produces values in range'
        test_18: Test = Test()
        try:
            t_588: 'int19'
            t_269: 'bool7'
            r_80: 'RandomResult' = next_random_32(42, 10)
            if r_80.value >= 0:
                t_588 = r_80.value
                t_269 = t_588 < 10
            else:
                t_269 = False
            def fn_586() -> 'str8':
                return str_cat_778('value should be in [0, 10), got ', int_to_string_779(r_80.value))
            test_18.assert_(t_269, fn_586)
        finally:
            test_18.soft_fail_to_hard()
class TestCase28(TestCase6):
    def test___tickDoesNothingWhenGameIsOver__103(self) -> None:
        'tick does nothing when game is over'
        test_20: Test = Test()
        try:
            t_569: 'SnakeGame'
            t_568: 'SnakeGame' = new_game_33(10, 10, 42)
            game_82: 'SnakeGame' = t_568
            i_83: 'int19' = 0
            while i_83 < 10:
                t_569 = tick_35(game_82)
                game_82 = t_569
                i_83 = int_add_781(i_83, 1)
            t_571: 'bool7' = isinstance10(game_82.status, GameOver)
            def fn_567() -> 'str8':
                return 'should be GameOver'
            test_20.assert_(t_571, fn_567)
            head1_84: 'Point' = list_get_or_777(game_82.snake, 0, Point(-1, -1))
            t_577: 'SnakeGame' = tick_35(game_82)
            game_82 = t_577
            head2_85: 'Point' = list_get_or_777(game_82.snake, 0, Point(-1, -1))
            t_582: 'bool7' = point_equals_29(head1_84, head2_85)
            def fn_566() -> 'str8':
                return 'snake should not move after game over'
            test_20.assert_(t_582, fn_566)
        finally:
            test_20.soft_fail_to_hard()
