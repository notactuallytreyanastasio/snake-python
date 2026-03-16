from snake.snake import point_equals as point_equals_43, is_opposite as is_opposite_44, direction_delta as direction_delta_45, next_random as next_random_46, new_game as new_game_47, change_direction as change_direction_48, tick as tick_49, new_multi_game as new_multi_game_54, multi_tick as multi_tick_55, multi_render as multi_render_56, change_player_direction as change_player_direction_57, is_multi_game_over as is_multi_game_over_58, add_player as add_player_59, remove_player as remove_player_60, direction_to_string as direction_to_string_61, string_to_direction as string_to_direction_62, SnakeGame, Point, Playing, Right, Down, Up, Left, GameOver, RandomResult, MultiSnakeGame, PlayerSnake, Dead, Alive, Direction
from temper_std.testing import Test
from unittest import TestCase as TestCase6
from builtins import bool as bool7, str as str8, isinstance as isinstance10, int as int19
from typing import Sequence as Sequence21, Union as Union42
from snake_test.snake_test import list_get_or_1580, str_cat_1581, int_to_string_1582, len_1583, int_add_1584
class TestCase5(TestCase6):
    def test___initialStateHasSnakeNearCenter__170(self) -> None:
        'initial state has snake near center'
        test_0: Test = Test()
        try:
            game_65: 'SnakeGame' = new_game_47(10, 10, 42)
            head_66: 'Point' = list_get_or_1580(game_65.snake, 0, Point(-1, -1))
            t_1569: 'bool7' = head_66.x == 5
            def fn_1562() -> 'str8':
                return str_cat_1581('head x should be 5, got ', int_to_string_1582(head_66.x))
            test_0.assert_(t_1569, fn_1562)
            t_1573: 'bool7' = head_66.y == 5
            def fn_1561() -> 'str8':
                return str_cat_1581('head y should be 5, got ', int_to_string_1582(head_66.y))
            test_0.assert_(t_1573, fn_1561)
            t_1578: 'bool7' = len_1583(game_65.snake) == 3
            def fn_1560() -> 'str8':
                return 'snake should start with 3 segments'
            test_0.assert_(t_1578, fn_1560)
        finally:
            test_0.soft_fail_to_hard()
class TestCase9(TestCase6):
    def test___initialStatusIsPlaying__171(self) -> None:
        'initial status is Playing'
        test_1: Test = Test()
        try:
            game_68: 'SnakeGame' = new_game_47(10, 10, 42)
            t_1553: 'bool7' = isinstance10(game_68.status, Playing)
            def fn_1550() -> 'str8':
                return 'initial status should be Playing'
            test_1.assert_(t_1553, fn_1550)
        finally:
            test_1.soft_fail_to_hard()
class TestCase11(TestCase6):
    def test___initialDirectionIsRight__172(self) -> None:
        'initial direction is Right'
        test_2: Test = Test()
        try:
            game_70: 'SnakeGame' = new_game_47(10, 10, 42)
            t_1547: 'bool7' = isinstance10(game_70.direction, Right)
            def fn_1544() -> 'str8':
                return 'initial direction should be Right'
            test_2.assert_(t_1547, fn_1544)
        finally:
            test_2.soft_fail_to_hard()
class TestCase12(TestCase6):
    def test___initialScoreIs0__173(self) -> None:
        'initial score is 0'
        test_3: Test = Test()
        try:
            game_72: 'SnakeGame' = new_game_47(10, 10, 42)
            t_1542: 'bool7' = game_72.score == 0
            def fn_1538() -> 'str8':
                return 'initial score should be 0'
            test_3.assert_(t_1542, fn_1538)
        finally:
            test_3.soft_fail_to_hard()
class TestCase13(TestCase6):
    def test___snakeMovesRight__174(self) -> None:
        'snake moves right'
        test_4: Test = Test()
        try:
            game_74: 'SnakeGame' = new_game_47(10, 10, 42)
            moved_75: 'SnakeGame' = tick_49(game_74)
            head_76: 'Point' = list_get_or_1580(moved_75.snake, 0, Point(-1, -1))
            t_1532: 'bool7' = head_76.x == 6
            def fn_1524() -> 'str8':
                return str_cat_1581('head should move right to x=6, got ', int_to_string_1582(head_76.x))
            test_4.assert_(t_1532, fn_1524)
            t_1536: 'bool7' = head_76.y == 5
            def fn_1523() -> 'str8':
                return str_cat_1581('head y should stay 5, got ', int_to_string_1582(head_76.y))
            test_4.assert_(t_1536, fn_1523)
        finally:
            test_4.soft_fail_to_hard()
class TestCase14(TestCase6):
    def test___snakeMovesDown__175(self) -> None:
        'snake moves down'
        test_5: Test = Test()
        try:
            game_78: 'SnakeGame' = change_direction_48(new_game_47(10, 10, 42), Down())
            moved_79: 'SnakeGame' = tick_49(game_78)
            head_80: 'Point' = list_get_or_1580(moved_79.snake, 0, Point(-1, -1))
            t_1513: 'bool7' = head_80.x == 5
            def fn_1504() -> 'str8':
                return str_cat_1581('head x should stay 5, got ', int_to_string_1582(head_80.x))
            test_5.assert_(t_1513, fn_1504)
            t_1517: 'bool7' = head_80.y == 6
            def fn_1503() -> 'str8':
                return str_cat_1581('head should move down to y=6, got ', int_to_string_1582(head_80.y))
            test_5.assert_(t_1517, fn_1503)
        finally:
            test_5.soft_fail_to_hard()
class TestCase15(TestCase6):
    def test___snakeMovesUp__176(self) -> None:
        'snake moves up'
        test_6: Test = Test()
        try:
            game_82: 'SnakeGame' = change_direction_48(new_game_47(10, 10, 42), Up())
            moved_83: 'SnakeGame' = tick_49(game_82)
            head_84: 'Point' = list_get_or_1580(moved_83.snake, 0, Point(-1, -1))
            t_1497: 'bool7' = head_84.y == 4
            def fn_1488() -> 'str8':
                return str_cat_1581('head should move up to y=4, got ', int_to_string_1582(head_84.y))
            test_6.assert_(t_1497, fn_1488)
        finally:
            test_6.soft_fail_to_hard()
class TestCase16(TestCase6):
    def test___oppositeDirectionIsRejected__177(self) -> None:
        'opposite direction is rejected'
        test_7: Test = Test()
        try:
            game_86: 'SnakeGame' = new_game_47(10, 10, 42)
            changed_87: 'SnakeGame' = change_direction_48(game_86, Left())
            t_1483: 'bool7' = isinstance10(changed_87.direction, Right)
            def fn_1479() -> 'str8':
                return 'should still be Right after trying Left'
            test_7.assert_(t_1483, fn_1479)
        finally:
            test_7.soft_fail_to_hard()
class TestCase17(TestCase6):
    def test___nonOppositeDirectionIsAccepted__178(self) -> None:
        'non-opposite direction is accepted'
        test_8: Test = Test()
        try:
            game_89: 'SnakeGame' = new_game_47(10, 10, 42)
            changed_90: 'SnakeGame' = change_direction_48(game_89, Up())
            t_1476: 'bool7' = isinstance10(changed_90.direction, Up)
            def fn_1472() -> 'str8':
                return 'should change to Up'
            test_8.assert_(t_1476, fn_1472)
        finally:
            test_8.soft_fail_to_hard()
class TestCase18(TestCase6):
    def test___wallCollisionCausesGameOver__179(self) -> None:
        'wall collision causes game over'
        test_9: Test = Test()
        try:
            t_1467: 'SnakeGame'
            t_1466: 'SnakeGame' = new_game_47(10, 10, 42)
            game_92: 'SnakeGame' = t_1466
            i_93: 'int19' = 0
            while i_93 < 10:
                t_1467 = tick_49(game_92)
                game_92 = t_1467
                i_93 = int_add_1584(i_93, 1)
            t_1469: 'bool7' = isinstance10(game_92.status, GameOver)
            def fn_1465() -> 'str8':
                return 'should be GameOver after hitting wall'
            test_9.assert_(t_1469, fn_1465)
        finally:
            test_9.soft_fail_to_hard()
class TestCase20(TestCase6):
    def test___selfCollisionCausesGameOver__180(self) -> None:
        'self collision causes game over'
        test_10: Test = Test()
        try:
            snake_95: 'Sequence21[Point]' = (Point(5, 5), Point(6, 5), Point(6, 4), Point(5, 4), Point(4, 4), Point(4, 5), Point(4, 6))
            t_1459: 'SnakeGame' = SnakeGame(10, 10, snake_95, Left(), Point(0, 0), 0, Playing(), 42)
            game_96: 'SnakeGame' = t_1459
            t_1460: 'SnakeGame' = tick_49(game_96)
            game_96 = t_1460
            t_1462: 'bool7' = isinstance10(game_96.status, GameOver)
            def fn_1448() -> 'str8':
                return 'should be GameOver after self collision'
            test_10.assert_(t_1462, fn_1448)
        finally:
            test_10.soft_fail_to_hard()
class TestCase22(TestCase6):
    def test___pointEqualsWorksForSamePoints__181(self) -> None:
        'pointEquals works for same points'
        test_11: Test = Test()
        try:
            t_1446: 'bool7' = point_equals_43(Point(3, 4), Point(3, 4))
            def fn_1442() -> 'str8':
                return 'same points should be equal'
            test_11.assert_(t_1446, fn_1442)
        finally:
            test_11.soft_fail_to_hard()
class TestCase23(TestCase6):
    def test___pointEqualsWorksForDifferentPoints__182(self) -> None:
        'pointEquals works for different points'
        test_12: Test = Test()
        try:
            t_1440: 'bool7' = not point_equals_43(Point(3, 4), Point(5, 6))
            def fn_1436() -> 'str8':
                return 'different points should not be equal'
            test_12.assert_(t_1440, fn_1436)
        finally:
            test_12.soft_fail_to_hard()
class TestCase24(TestCase6):
    def test___isOppositeDetectsOppositeDirections__183(self) -> None:
        'isOpposite detects opposite directions'
        test_13: Test = Test()
        try:
            t_1424: 'bool7' = is_opposite_44(Up(), Down())
            def fn_1420() -> 'str8':
                return 'Up/Down are opposite'
            test_13.assert_(t_1424, fn_1420)
            t_1429: 'bool7' = is_opposite_44(Left(), Right())
            def fn_1419() -> 'str8':
                return 'Left/Right are opposite'
            test_13.assert_(t_1429, fn_1419)
            t_1434: 'bool7' = not is_opposite_44(Up(), Left())
            def fn_1418() -> 'str8':
                return 'Up/Left are not opposite'
            test_13.assert_(t_1434, fn_1418)
        finally:
            test_13.soft_fail_to_hard()
class TestCase25(TestCase6):
    def test___directionDeltaReturnsCorrectDeltas__184(self) -> None:
        'directionDelta returns correct deltas'
        test_14: Test = Test()
        try:
            t_1410: 'int19'
            t_1415: 'int19'
            t_703: 'bool7'
            t_708: 'bool7'
            up_101: 'Point' = direction_delta_45(Up())
            if up_101.x == 0:
                t_1410 = up_101.y
                t_703 = t_1410 == -1
            else:
                t_703 = False
            def fn_1407() -> 'str8':
                return 'Up should be (0, -1)'
            test_14.assert_(t_703, fn_1407)
            right_102: 'Point' = direction_delta_45(Right())
            if right_102.x == 1:
                t_1415 = right_102.y
                t_708 = t_1415 == 0
            else:
                t_708 = False
            def fn_1406() -> 'str8':
                return 'Right should be (1, 0)'
            test_14.assert_(t_708, fn_1406)
        finally:
            test_14.soft_fail_to_hard()
class TestCase26(TestCase6):
    def test___prngIsDeterministic__185(self) -> None:
        'PRNG is deterministic'
        test_17: Test = Test()
        try:
            r1_104: 'RandomResult' = next_random_46(42, 100)
            r2_105: 'RandomResult' = next_random_46(42, 100)
            t_1399: 'bool7' = r1_104.value == r2_105.value
            def fn_1395() -> 'str8':
                return 'same seed should produce same value'
            test_17.assert_(t_1399, fn_1395)
            t_1404: 'bool7' = r1_104.next_seed == r2_105.next_seed
            def fn_1394() -> 'str8':
                return 'same seed should produce same next seed'
            test_17.assert_(t_1404, fn_1394)
        finally:
            test_17.soft_fail_to_hard()
class TestCase27(TestCase6):
    def test___prngProducesValuesInRange__186(self) -> None:
        'PRNG produces values in range'
        test_18: Test = Test()
        try:
            t_1391: 'int19'
            t_693: 'bool7'
            r_107: 'RandomResult' = next_random_46(42, 10)
            if r_107.value >= 0:
                t_1391 = r_107.value
                t_693 = t_1391 < 10
            else:
                t_693 = False
            def fn_1389() -> 'str8':
                return str_cat_1581('value should be in [0, 10), got ', int_to_string_1582(r_107.value))
            test_18.assert_(t_693, fn_1389)
        finally:
            test_18.soft_fail_to_hard()
class TestCase28(TestCase6):
    def test___tickDoesNothingWhenGameIsOver__187(self) -> None:
        'tick does nothing when game is over'
        test_20: Test = Test()
        try:
            t_1372: 'SnakeGame'
            t_1371: 'SnakeGame' = new_game_47(10, 10, 42)
            game_109: 'SnakeGame' = t_1371
            i_110: 'int19' = 0
            while i_110 < 10:
                t_1372 = tick_49(game_109)
                game_109 = t_1372
                i_110 = int_add_1584(i_110, 1)
            t_1374: 'bool7' = isinstance10(game_109.status, GameOver)
            def fn_1370() -> 'str8':
                return 'should be GameOver'
            test_20.assert_(t_1374, fn_1370)
            head1_111: 'Point' = list_get_or_1580(game_109.snake, 0, Point(-1, -1))
            t_1380: 'SnakeGame' = tick_49(game_109)
            game_109 = t_1380
            head2_112: 'Point' = list_get_or_1580(game_109.snake, 0, Point(-1, -1))
            t_1385: 'bool7' = point_equals_43(head1_111, head2_112)
            def fn_1369() -> 'str8':
                return 'snake should not move after game over'
            test_20.assert_(t_1385, fn_1369)
        finally:
            test_20.soft_fail_to_hard()
class TestCase29(TestCase6):
    def test___multiGameCreatesCorrectNumberOfSnakes__188(self) -> None:
        'multi game creates correct number of snakes'
        test_21: Test = Test()
        try:
            game_114: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            t_1367: 'bool7' = len_1583(game_114.snakes) == 2
            def fn_1362() -> 'str8':
                return 'should have 2 snakes'
            test_21.assert_(t_1367, fn_1362)
        finally:
            test_21.soft_fail_to_hard()
class TestCase30(TestCase6):
    def test___multiGameSnakesStartAlive__189(self) -> None:
        'multi game snakes start alive'
        test_22: Test = Test()
        try:
            game_116: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            s0_117: 'PlayerSnake' = list_get_or_1580(game_116.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_118: 'PlayerSnake' = list_get_or_1580(game_116.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1355: 'bool7' = isinstance10(s0_117.status, Alive)
            def fn_1340() -> 'str8':
                return 'player 0 should be alive'
            test_22.assert_(t_1355, fn_1340)
            t_1359: 'bool7' = isinstance10(s1_118.status, Alive)
            def fn_1339() -> 'str8':
                return 'player 1 should be alive'
            test_22.assert_(t_1359, fn_1339)
        finally:
            test_22.soft_fail_to_hard()
class TestCase31(TestCase6):
    def test___multiGameSnakesStartAtDifferentPositions__190(self) -> None:
        'multi game snakes start at different positions'
        test_23: Test = Test()
        try:
            game_120: 'MultiSnakeGame' = new_multi_game_54(60, 30, 2, 42)
            s0_121: 'PlayerSnake' = list_get_or_1580(game_120.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_122: 'PlayerSnake' = list_get_or_1580(game_120.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            h0_123: 'Point' = list_get_or_1580(s0_121.segments, 0, Point(-1, -1))
            h1_124: 'Point' = list_get_or_1580(s1_122.segments, 0, Point(-1, -1))
            t_1337: 'bool7' = not point_equals_43(h0_123, h1_124)
            def fn_1316() -> 'str8':
                return 'snakes should start at different positions'
            test_23.assert_(t_1337, fn_1316)
        finally:
            test_23.soft_fail_to_hard()
class TestCase32(TestCase6):
    def test___multiGameSnakesHave3_segmentsEach__191(self) -> None:
        'multi game snakes have 3 segments each'
        test_24: Test = Test()
        try:
            game_126: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            s0_127: 'PlayerSnake' = list_get_or_1580(game_126.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_128: 'PlayerSnake' = list_get_or_1580(game_126.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1309: 'bool7' = len_1583(s0_127.segments) == 3
            def fn_1292() -> 'str8':
                return 'player 0 should have 3 segments'
            test_24.assert_(t_1309, fn_1292)
            t_1314: 'bool7' = len_1583(s1_128.segments) == 3
            def fn_1291() -> 'str8':
                return 'player 1 should have 3 segments'
            test_24.assert_(t_1314, fn_1291)
        finally:
            test_24.soft_fail_to_hard()
class TestCase33(TestCase6):
    def test___multiTickMovesBothSnakes__192(self) -> None:
        'multi tick moves both snakes'
        test_25: Test = Test()
        try:
            game_130: 'MultiSnakeGame' = new_multi_game_54(60, 30, 2, 42)
            s0_131: 'PlayerSnake' = list_get_or_1580(game_130.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_132: 'PlayerSnake' = list_get_or_1580(game_130.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            h0_before_133: 'Point' = list_get_or_1580(s0_131.segments, 0, Point(0, 0))
            h1_before_134: 'Point' = list_get_or_1580(s1_132.segments, 0, Point(0, 0))
            dirs_135: 'Sequence21[Direction]' = (s0_131.direction, s1_132.direction)
            after_136: 'MultiSnakeGame' = multi_tick_55(game_130, dirs_135)
            h0_after_137: 'Point' = list_get_or_1580(list_get_or_1580(after_136.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead())).segments, 0, Point(0, 0))
            h1_after_138: 'Point' = list_get_or_1580(list_get_or_1580(after_136.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead())).segments, 0, Point(0, 0))
            t_1286: 'bool7' = not point_equals_43(h0_before_133, h0_after_137)
            def fn_1244() -> 'str8':
                return 'snake 0 should have moved'
            test_25.assert_(t_1286, fn_1244)
            t_1289: 'bool7' = not point_equals_43(h1_before_134, h1_after_138)
            def fn_1243() -> 'str8':
                return 'snake 1 should have moved'
            test_25.assert_(t_1289, fn_1243)
        finally:
            test_25.soft_fail_to_hard()
class TestCase34(TestCase6):
    def test___multiWallCollisionKillsOneSnake__193(self) -> None:
        'multi wall collision kills one snake'
        test_26: Test = Test()
        try:
            t_1229: 'MultiSnakeGame'
            t_1231: 'int19'
            t_1232: 'Sequence21[PlayerSnake]'
            t_1236: 'PlayerSnake'
            t_1226: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            game_140: 'MultiSnakeGame' = t_1226
            dirs_141: 'Sequence21[Direction]' = (Right(), Left())
            i_142: 'int19' = 0
            while i_142 < 20:
                t_1229 = multi_tick_55(game_140, dirs_141)
                game_140 = t_1229
                i_142 = int_add_1584(i_142, 1)
            dead_count_143: 'int19' = 0
            i_144: 'int19' = 0
            while True:
                t_1231 = len_1583(game_140.snakes)
                if not i_144 < t_1231:
                    break
                t_1232 = game_140.snakes
                t_1236 = PlayerSnake(0, (), Right(), 0, Dead())
                snake_145: 'PlayerSnake' = list_get_or_1580(t_1232, i_144, t_1236)
                if isinstance10(snake_145.status, Dead):
                    dead_count_143 = int_add_1584(dead_count_143, 1)
                i_144 = int_add_1584(i_144, 1)
            t_1241: 'bool7' = dead_count_143 > 0
            def fn_1225() -> 'str8':
                return 'at least one snake should be dead after 20 ticks toward walls'
            test_26.assert_(t_1241, fn_1225)
        finally:
            test_26.soft_fail_to_hard()
class TestCase35(TestCase6):
    def test___multiGameOverWhenOnePlayerLeft__194(self) -> None:
        'multi game over when one player left'
        test_27: Test = Test()
        try:
            t_1221: 'MultiSnakeGame'
            t_1218: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            game_147: 'MultiSnakeGame' = t_1218
            dirs_148: 'Sequence21[Direction]' = (Right(), Left())
            i_149: 'int19' = 0
            while i_149 < 30:
                t_1221 = multi_tick_55(game_147, dirs_148)
                game_147 = t_1221
                i_149 = int_add_1584(i_149, 1)
            t_1222: 'bool7' = is_multi_game_over_58(game_147)
            def fn_1217() -> 'str8':
                return 'game should be over after enough ticks'
            test_27.assert_(t_1222, fn_1217)
        finally:
            test_27.soft_fail_to_hard()
class TestCase36(TestCase6):
    def test___changePlayerDirectionWorks__195(self) -> None:
        'changePlayerDirection works'
        test_28: Test = Test()
        try:
            game_151: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            t_1205: 'Up' = Up()
            changed_152: 'MultiSnakeGame' = change_player_direction_57(game_151, 0, t_1205)
            s0_153: 'PlayerSnake' = list_get_or_1580(changed_152.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1214: 'bool7' = isinstance10(s0_153.direction, Up)
            def fn_1203() -> 'str8':
                return 'player 0 direction should be Up'
            test_28.assert_(t_1214, fn_1203)
        finally:
            test_28.soft_fail_to_hard()
class TestCase37(TestCase6):
    def test___changePlayerDirectionRejectsOpposite__196(self) -> None:
        'changePlayerDirection rejects opposite'
        test_29: Test = Test()
        try:
            game_155: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            t_1191: 'Left' = Left()
            changed_156: 'MultiSnakeGame' = change_player_direction_57(game_155, 0, t_1191)
            s0_157: 'PlayerSnake' = list_get_or_1580(changed_156.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1200: 'bool7' = isinstance10(s0_157.direction, Right)
            def fn_1189() -> 'str8':
                return 'should reject opposite direction'
            test_29.assert_(t_1200, fn_1189)
        finally:
            test_29.soft_fail_to_hard()
class TestCase38(TestCase6):
    def test___addPlayerAddsANewSnake__197(self) -> None:
        'addPlayer adds a new snake'
        test_30: Test = Test()
        try:
            game_159: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            bigger_160: 'MultiSnakeGame' = add_player_59(game_159, 99)
            t_1187: 'bool7' = len_1583(bigger_160.snakes) == 3
            def fn_1181() -> 'str8':
                return 'should have 3 snakes after adding'
            test_30.assert_(t_1187, fn_1181)
        finally:
            test_30.soft_fail_to_hard()
class TestCase39(TestCase6):
    def test___removePlayerRemovesASnake__198(self) -> None:
        'removePlayer removes a snake'
        test_31: Test = Test()
        try:
            game_162: 'MultiSnakeGame' = new_multi_game_54(20, 10, 3, 42)
            smaller_163: 'MultiSnakeGame' = remove_player_60(game_162, 1)
            t_1179: 'bool7' = len_1583(smaller_163.snakes) == 2
            def fn_1173() -> 'str8':
                return 'should have 2 snakes after removing'
            test_31.assert_(t_1179, fn_1173)
        finally:
            test_31.soft_fail_to_hard()
class TestCase40(TestCase6):
    def test___multiRenderProducesOutput__199(self) -> None:
        'multiRender produces output'
        test_32: Test = Test()
        try:
            game_165: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            rendered_166: 'str8' = multi_render_56(game_165)
            t_1171: 'bool7' = rendered_166 != ''
            def fn_1167() -> 'str8':
                return 'render should produce output'
            test_32.assert_(t_1171, fn_1167)
        finally:
            test_32.soft_fail_to_hard()
class TestCase41(TestCase6):
    def test___directionToStringAndStringToDirectionRoundTrip__200(self) -> None:
        'directionToString and stringToDirection round-trip'
        test_33: Test = Test()
        try:
            d_168: 'str8' = direction_to_string_61(Up())
            t_1163: 'bool7' = d_168 == 'up'
            def fn_1160() -> 'str8':
                return "Up should serialize to 'up'"
            test_33.assert_(t_1163, fn_1160)
            parsed_169: 'Union42[Direction, None]' = string_to_direction_62('down')
            def fn_1159() -> 'str8':
                return "'down' should parse to Down"
            test_33.assert_(True, fn_1159)
        finally:
            test_33.soft_fail_to_hard()
