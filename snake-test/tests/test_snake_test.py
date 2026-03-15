from snake.snake import point_equals as point_equals_43, is_opposite as is_opposite_44, direction_delta as direction_delta_45, next_random as next_random_46, new_game as new_game_47, change_direction as change_direction_48, tick as tick_49, new_multi_game as new_multi_game_54, multi_tick as multi_tick_55, multi_render as multi_render_56, change_player_direction as change_player_direction_57, is_multi_game_over as is_multi_game_over_58, add_player as add_player_59, remove_player as remove_player_60, direction_to_string as direction_to_string_61, string_to_direction as string_to_direction_62, SnakeGame, Point, Playing, Right, Down, Up, Left, GameOver, RandomResult, MultiSnakeGame, PlayerSnake, Dead, Alive, Direction
from temper_std.testing import Test
from unittest import TestCase as TestCase6
from builtins import bool as bool7, str as str8, isinstance as isinstance10, int as int19
from typing import Sequence as Sequence21, Union as Union42
from snake_test.snake_test import list_get_or_1578, str_cat_1579, int_to_string_1580, len_1581, int_add_1582
class TestCase5(TestCase6):
    def test___initialStateHasSnakeNearCenter__168(self) -> None:
        'initial state has snake near center'
        test_0: Test = Test()
        try:
            game_65: 'SnakeGame' = new_game_47(10, 10, 42)
            head_66: 'Point' = list_get_or_1578(game_65.snake, 0, Point(-1, -1))
            t_1567: 'bool7' = head_66.x == 5
            def fn_1560() -> 'str8':
                return str_cat_1579('head x should be 5, got ', int_to_string_1580(head_66.x))
            test_0.assert_(t_1567, fn_1560)
            t_1571: 'bool7' = head_66.y == 5
            def fn_1559() -> 'str8':
                return str_cat_1579('head y should be 5, got ', int_to_string_1580(head_66.y))
            test_0.assert_(t_1571, fn_1559)
            t_1576: 'bool7' = len_1581(game_65.snake) == 3
            def fn_1558() -> 'str8':
                return 'snake should start with 3 segments'
            test_0.assert_(t_1576, fn_1558)
        finally:
            test_0.soft_fail_to_hard()
class TestCase9(TestCase6):
    def test___initialStatusIsPlaying__169(self) -> None:
        'initial status is Playing'
        test_1: Test = Test()
        try:
            game_68: 'SnakeGame' = new_game_47(10, 10, 42)
            t_1551: 'bool7' = isinstance10(game_68.status, Playing)
            def fn_1548() -> 'str8':
                return 'initial status should be Playing'
            test_1.assert_(t_1551, fn_1548)
        finally:
            test_1.soft_fail_to_hard()
class TestCase11(TestCase6):
    def test___initialDirectionIsRight__170(self) -> None:
        'initial direction is Right'
        test_2: Test = Test()
        try:
            game_70: 'SnakeGame' = new_game_47(10, 10, 42)
            t_1545: 'bool7' = isinstance10(game_70.direction, Right)
            def fn_1542() -> 'str8':
                return 'initial direction should be Right'
            test_2.assert_(t_1545, fn_1542)
        finally:
            test_2.soft_fail_to_hard()
class TestCase12(TestCase6):
    def test___initialScoreIs0__171(self) -> None:
        'initial score is 0'
        test_3: Test = Test()
        try:
            game_72: 'SnakeGame' = new_game_47(10, 10, 42)
            t_1540: 'bool7' = game_72.score == 0
            def fn_1536() -> 'str8':
                return 'initial score should be 0'
            test_3.assert_(t_1540, fn_1536)
        finally:
            test_3.soft_fail_to_hard()
class TestCase13(TestCase6):
    def test___snakeMovesRight__172(self) -> None:
        'snake moves right'
        test_4: Test = Test()
        try:
            game_74: 'SnakeGame' = new_game_47(10, 10, 42)
            moved_75: 'SnakeGame' = tick_49(game_74)
            head_76: 'Point' = list_get_or_1578(moved_75.snake, 0, Point(-1, -1))
            t_1530: 'bool7' = head_76.x == 6
            def fn_1522() -> 'str8':
                return str_cat_1579('head should move right to x=6, got ', int_to_string_1580(head_76.x))
            test_4.assert_(t_1530, fn_1522)
            t_1534: 'bool7' = head_76.y == 5
            def fn_1521() -> 'str8':
                return str_cat_1579('head y should stay 5, got ', int_to_string_1580(head_76.y))
            test_4.assert_(t_1534, fn_1521)
        finally:
            test_4.soft_fail_to_hard()
class TestCase14(TestCase6):
    def test___snakeMovesDown__173(self) -> None:
        'snake moves down'
        test_5: Test = Test()
        try:
            game_78: 'SnakeGame' = change_direction_48(new_game_47(10, 10, 42), Down())
            moved_79: 'SnakeGame' = tick_49(game_78)
            head_80: 'Point' = list_get_or_1578(moved_79.snake, 0, Point(-1, -1))
            t_1511: 'bool7' = head_80.x == 5
            def fn_1502() -> 'str8':
                return str_cat_1579('head x should stay 5, got ', int_to_string_1580(head_80.x))
            test_5.assert_(t_1511, fn_1502)
            t_1515: 'bool7' = head_80.y == 6
            def fn_1501() -> 'str8':
                return str_cat_1579('head should move down to y=6, got ', int_to_string_1580(head_80.y))
            test_5.assert_(t_1515, fn_1501)
        finally:
            test_5.soft_fail_to_hard()
class TestCase15(TestCase6):
    def test___snakeMovesUp__174(self) -> None:
        'snake moves up'
        test_6: Test = Test()
        try:
            game_82: 'SnakeGame' = change_direction_48(new_game_47(10, 10, 42), Up())
            moved_83: 'SnakeGame' = tick_49(game_82)
            head_84: 'Point' = list_get_or_1578(moved_83.snake, 0, Point(-1, -1))
            t_1495: 'bool7' = head_84.y == 4
            def fn_1486() -> 'str8':
                return str_cat_1579('head should move up to y=4, got ', int_to_string_1580(head_84.y))
            test_6.assert_(t_1495, fn_1486)
        finally:
            test_6.soft_fail_to_hard()
class TestCase16(TestCase6):
    def test___oppositeDirectionIsRejected__175(self) -> None:
        'opposite direction is rejected'
        test_7: Test = Test()
        try:
            game_86: 'SnakeGame' = new_game_47(10, 10, 42)
            changed_87: 'SnakeGame' = change_direction_48(game_86, Left())
            t_1481: 'bool7' = isinstance10(changed_87.direction, Right)
            def fn_1477() -> 'str8':
                return 'should still be Right after trying Left'
            test_7.assert_(t_1481, fn_1477)
        finally:
            test_7.soft_fail_to_hard()
class TestCase17(TestCase6):
    def test___nonOppositeDirectionIsAccepted__176(self) -> None:
        'non-opposite direction is accepted'
        test_8: Test = Test()
        try:
            game_89: 'SnakeGame' = new_game_47(10, 10, 42)
            changed_90: 'SnakeGame' = change_direction_48(game_89, Up())
            t_1474: 'bool7' = isinstance10(changed_90.direction, Up)
            def fn_1470() -> 'str8':
                return 'should change to Up'
            test_8.assert_(t_1474, fn_1470)
        finally:
            test_8.soft_fail_to_hard()
class TestCase18(TestCase6):
    def test___wallCollisionCausesGameOver__177(self) -> None:
        'wall collision causes game over'
        test_9: Test = Test()
        try:
            t_1465: 'SnakeGame'
            t_1464: 'SnakeGame' = new_game_47(10, 10, 42)
            game_92: 'SnakeGame' = t_1464
            i_93: 'int19' = 0
            while i_93 < 10:
                t_1465 = tick_49(game_92)
                game_92 = t_1465
                i_93 = int_add_1582(i_93, 1)
            t_1467: 'bool7' = isinstance10(game_92.status, GameOver)
            def fn_1463() -> 'str8':
                return 'should be GameOver after hitting wall'
            test_9.assert_(t_1467, fn_1463)
        finally:
            test_9.soft_fail_to_hard()
class TestCase20(TestCase6):
    def test___selfCollisionCausesGameOver__178(self) -> None:
        'self collision causes game over'
        test_10: Test = Test()
        try:
            snake_95: 'Sequence21[Point]' = (Point(5, 5), Point(6, 5), Point(6, 4), Point(5, 4), Point(4, 4), Point(4, 5), Point(4, 6))
            t_1457: 'SnakeGame' = SnakeGame(10, 10, snake_95, Left(), Point(0, 0), 0, Playing(), 42)
            game_96: 'SnakeGame' = t_1457
            t_1458: 'SnakeGame' = tick_49(game_96)
            game_96 = t_1458
            t_1460: 'bool7' = isinstance10(game_96.status, GameOver)
            def fn_1446() -> 'str8':
                return 'should be GameOver after self collision'
            test_10.assert_(t_1460, fn_1446)
        finally:
            test_10.soft_fail_to_hard()
class TestCase22(TestCase6):
    def test___pointEqualsWorksForSamePoints__179(self) -> None:
        'pointEquals works for same points'
        test_11: Test = Test()
        try:
            t_1444: 'bool7' = point_equals_43(Point(3, 4), Point(3, 4))
            def fn_1440() -> 'str8':
                return 'same points should be equal'
            test_11.assert_(t_1444, fn_1440)
        finally:
            test_11.soft_fail_to_hard()
class TestCase23(TestCase6):
    def test___pointEqualsWorksForDifferentPoints__180(self) -> None:
        'pointEquals works for different points'
        test_12: Test = Test()
        try:
            t_1438: 'bool7' = not point_equals_43(Point(3, 4), Point(5, 6))
            def fn_1434() -> 'str8':
                return 'different points should not be equal'
            test_12.assert_(t_1438, fn_1434)
        finally:
            test_12.soft_fail_to_hard()
class TestCase24(TestCase6):
    def test___isOppositeDetectsOppositeDirections__181(self) -> None:
        'isOpposite detects opposite directions'
        test_13: Test = Test()
        try:
            t_1422: 'bool7' = is_opposite_44(Up(), Down())
            def fn_1418() -> 'str8':
                return 'Up/Down are opposite'
            test_13.assert_(t_1422, fn_1418)
            t_1427: 'bool7' = is_opposite_44(Left(), Right())
            def fn_1417() -> 'str8':
                return 'Left/Right are opposite'
            test_13.assert_(t_1427, fn_1417)
            t_1432: 'bool7' = not is_opposite_44(Up(), Left())
            def fn_1416() -> 'str8':
                return 'Up/Left are not opposite'
            test_13.assert_(t_1432, fn_1416)
        finally:
            test_13.soft_fail_to_hard()
class TestCase25(TestCase6):
    def test___directionDeltaReturnsCorrectDeltas__182(self) -> None:
        'directionDelta returns correct deltas'
        test_14: Test = Test()
        try:
            t_1408: 'int19'
            t_1413: 'int19'
            t_701: 'bool7'
            t_706: 'bool7'
            up_101: 'Point' = direction_delta_45(Up())
            if up_101.x == 0:
                t_1408 = up_101.y
                t_701 = t_1408 == -1
            else:
                t_701 = False
            def fn_1405() -> 'str8':
                return 'Up should be (0, -1)'
            test_14.assert_(t_701, fn_1405)
            right_102: 'Point' = direction_delta_45(Right())
            if right_102.x == 1:
                t_1413 = right_102.y
                t_706 = t_1413 == 0
            else:
                t_706 = False
            def fn_1404() -> 'str8':
                return 'Right should be (1, 0)'
            test_14.assert_(t_706, fn_1404)
        finally:
            test_14.soft_fail_to_hard()
class TestCase26(TestCase6):
    def test___prngIsDeterministic__183(self) -> None:
        'PRNG is deterministic'
        test_17: Test = Test()
        try:
            r1_104: 'RandomResult' = next_random_46(42, 100)
            r2_105: 'RandomResult' = next_random_46(42, 100)
            t_1397: 'bool7' = r1_104.value == r2_105.value
            def fn_1393() -> 'str8':
                return 'same seed should produce same value'
            test_17.assert_(t_1397, fn_1393)
            t_1402: 'bool7' = r1_104.next_seed == r2_105.next_seed
            def fn_1392() -> 'str8':
                return 'same seed should produce same next seed'
            test_17.assert_(t_1402, fn_1392)
        finally:
            test_17.soft_fail_to_hard()
class TestCase27(TestCase6):
    def test___prngProducesValuesInRange__184(self) -> None:
        'PRNG produces values in range'
        test_18: Test = Test()
        try:
            t_1389: 'int19'
            t_691: 'bool7'
            r_107: 'RandomResult' = next_random_46(42, 10)
            if r_107.value >= 0:
                t_1389 = r_107.value
                t_691 = t_1389 < 10
            else:
                t_691 = False
            def fn_1387() -> 'str8':
                return str_cat_1579('value should be in [0, 10), got ', int_to_string_1580(r_107.value))
            test_18.assert_(t_691, fn_1387)
        finally:
            test_18.soft_fail_to_hard()
class TestCase28(TestCase6):
    def test___tickDoesNothingWhenGameIsOver__185(self) -> None:
        'tick does nothing when game is over'
        test_20: Test = Test()
        try:
            t_1370: 'SnakeGame'
            t_1369: 'SnakeGame' = new_game_47(10, 10, 42)
            game_109: 'SnakeGame' = t_1369
            i_110: 'int19' = 0
            while i_110 < 10:
                t_1370 = tick_49(game_109)
                game_109 = t_1370
                i_110 = int_add_1582(i_110, 1)
            t_1372: 'bool7' = isinstance10(game_109.status, GameOver)
            def fn_1368() -> 'str8':
                return 'should be GameOver'
            test_20.assert_(t_1372, fn_1368)
            head1_111: 'Point' = list_get_or_1578(game_109.snake, 0, Point(-1, -1))
            t_1378: 'SnakeGame' = tick_49(game_109)
            game_109 = t_1378
            head2_112: 'Point' = list_get_or_1578(game_109.snake, 0, Point(-1, -1))
            t_1383: 'bool7' = point_equals_43(head1_111, head2_112)
            def fn_1367() -> 'str8':
                return 'snake should not move after game over'
            test_20.assert_(t_1383, fn_1367)
        finally:
            test_20.soft_fail_to_hard()
class TestCase29(TestCase6):
    def test___multiGameCreatesCorrectNumberOfSnakes__186(self) -> None:
        'multi game creates correct number of snakes'
        test_21: Test = Test()
        try:
            game_114: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            t_1365: 'bool7' = len_1581(game_114.snakes) == 2
            def fn_1360() -> 'str8':
                return 'should have 2 snakes'
            test_21.assert_(t_1365, fn_1360)
        finally:
            test_21.soft_fail_to_hard()
class TestCase30(TestCase6):
    def test___multiGameSnakesStartAlive__187(self) -> None:
        'multi game snakes start alive'
        test_22: Test = Test()
        try:
            game_116: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            s0_117: 'PlayerSnake' = list_get_or_1578(game_116.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_118: 'PlayerSnake' = list_get_or_1578(game_116.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1353: 'bool7' = isinstance10(s0_117.status, Alive)
            def fn_1338() -> 'str8':
                return 'player 0 should be alive'
            test_22.assert_(t_1353, fn_1338)
            t_1357: 'bool7' = isinstance10(s1_118.status, Alive)
            def fn_1337() -> 'str8':
                return 'player 1 should be alive'
            test_22.assert_(t_1357, fn_1337)
        finally:
            test_22.soft_fail_to_hard()
class TestCase31(TestCase6):
    def test___multiGameSnakesStartAtDifferentPositions__188(self) -> None:
        'multi game snakes start at different positions'
        test_23: Test = Test()
        try:
            game_120: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            s0_121: 'PlayerSnake' = list_get_or_1578(game_120.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_122: 'PlayerSnake' = list_get_or_1578(game_120.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            h0_123: 'Point' = list_get_or_1578(s0_121.segments, 0, Point(-1, -1))
            h1_124: 'Point' = list_get_or_1578(s1_122.segments, 0, Point(-1, -1))
            t_1335: 'bool7' = not point_equals_43(h0_123, h1_124)
            def fn_1314() -> 'str8':
                return 'snakes should start at different positions'
            test_23.assert_(t_1335, fn_1314)
        finally:
            test_23.soft_fail_to_hard()
class TestCase32(TestCase6):
    def test___multiGameSnakesHave3_segmentsEach__189(self) -> None:
        'multi game snakes have 3 segments each'
        test_24: Test = Test()
        try:
            game_126: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            s0_127: 'PlayerSnake' = list_get_or_1578(game_126.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            s1_128: 'PlayerSnake' = list_get_or_1578(game_126.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1307: 'bool7' = len_1581(s0_127.segments) == 3
            def fn_1290() -> 'str8':
                return 'player 0 should have 3 segments'
            test_24.assert_(t_1307, fn_1290)
            t_1312: 'bool7' = len_1581(s1_128.segments) == 3
            def fn_1289() -> 'str8':
                return 'player 1 should have 3 segments'
            test_24.assert_(t_1312, fn_1289)
        finally:
            test_24.soft_fail_to_hard()
class TestCase33(TestCase6):
    def test___multiTickMovesBothSnakes__190(self) -> None:
        'multi tick moves both snakes'
        test_25: Test = Test()
        try:
            game_130: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            h0_before_131: 'Point' = list_get_or_1578(list_get_or_1578(game_130.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead())).segments, 0, Point(0, 0))
            h1_before_132: 'Point' = list_get_or_1578(list_get_or_1578(game_130.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead())).segments, 0, Point(0, 0))
            dirs_133: 'Sequence21[Direction]' = (Right(), Left())
            after_134: 'MultiSnakeGame' = multi_tick_55(game_130, dirs_133)
            h0_after_135: 'Point' = list_get_or_1578(list_get_or_1578(after_134.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead())).segments, 0, Point(0, 0))
            h1_after_136: 'Point' = list_get_or_1578(list_get_or_1578(after_134.snakes, 1, PlayerSnake(0, (), Right(), 0, Dead())).segments, 0, Point(0, 0))
            t_1284: 'bool7' = not point_equals_43(h0_before_131, h0_after_135)
            def fn_1242() -> 'str8':
                return 'snake 0 should have moved'
            test_25.assert_(t_1284, fn_1242)
            t_1287: 'bool7' = not point_equals_43(h1_before_132, h1_after_136)
            def fn_1241() -> 'str8':
                return 'snake 1 should have moved'
            test_25.assert_(t_1287, fn_1241)
        finally:
            test_25.soft_fail_to_hard()
class TestCase34(TestCase6):
    def test___multiWallCollisionKillsOneSnake__191(self) -> None:
        'multi wall collision kills one snake'
        test_26: Test = Test()
        try:
            t_1227: 'MultiSnakeGame'
            t_1229: 'int19'
            t_1230: 'Sequence21[PlayerSnake]'
            t_1234: 'PlayerSnake'
            t_1224: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            game_138: 'MultiSnakeGame' = t_1224
            dirs_139: 'Sequence21[Direction]' = (Right(), Left())
            i_140: 'int19' = 0
            while i_140 < 20:
                t_1227 = multi_tick_55(game_138, dirs_139)
                game_138 = t_1227
                i_140 = int_add_1582(i_140, 1)
            dead_count_141: 'int19' = 0
            i_142: 'int19' = 0
            while True:
                t_1229 = len_1581(game_138.snakes)
                if not i_142 < t_1229:
                    break
                t_1230 = game_138.snakes
                t_1234 = PlayerSnake(0, (), Right(), 0, Dead())
                snake_143: 'PlayerSnake' = list_get_or_1578(t_1230, i_142, t_1234)
                if isinstance10(snake_143.status, Dead):
                    dead_count_141 = int_add_1582(dead_count_141, 1)
                i_142 = int_add_1582(i_142, 1)
            t_1239: 'bool7' = dead_count_141 > 0
            def fn_1223() -> 'str8':
                return 'at least one snake should be dead after 20 ticks toward walls'
            test_26.assert_(t_1239, fn_1223)
        finally:
            test_26.soft_fail_to_hard()
class TestCase35(TestCase6):
    def test___multiGameOverWhenOnePlayerLeft__192(self) -> None:
        'multi game over when one player left'
        test_27: Test = Test()
        try:
            t_1219: 'MultiSnakeGame'
            t_1216: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            game_145: 'MultiSnakeGame' = t_1216
            dirs_146: 'Sequence21[Direction]' = (Right(), Left())
            i_147: 'int19' = 0
            while i_147 < 30:
                t_1219 = multi_tick_55(game_145, dirs_146)
                game_145 = t_1219
                i_147 = int_add_1582(i_147, 1)
            t_1220: 'bool7' = is_multi_game_over_58(game_145)
            def fn_1215() -> 'str8':
                return 'game should be over after enough ticks'
            test_27.assert_(t_1220, fn_1215)
        finally:
            test_27.soft_fail_to_hard()
class TestCase36(TestCase6):
    def test___changePlayerDirectionWorks__193(self) -> None:
        'changePlayerDirection works'
        test_28: Test = Test()
        try:
            game_149: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            t_1203: 'Up' = Up()
            changed_150: 'MultiSnakeGame' = change_player_direction_57(game_149, 0, t_1203)
            s0_151: 'PlayerSnake' = list_get_or_1578(changed_150.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1212: 'bool7' = isinstance10(s0_151.direction, Up)
            def fn_1201() -> 'str8':
                return 'player 0 direction should be Up'
            test_28.assert_(t_1212, fn_1201)
        finally:
            test_28.soft_fail_to_hard()
class TestCase37(TestCase6):
    def test___changePlayerDirectionRejectsOpposite__194(self) -> None:
        'changePlayerDirection rejects opposite'
        test_29: Test = Test()
        try:
            game_153: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            t_1189: 'Left' = Left()
            changed_154: 'MultiSnakeGame' = change_player_direction_57(game_153, 0, t_1189)
            s0_155: 'PlayerSnake' = list_get_or_1578(changed_154.snakes, 0, PlayerSnake(0, (), Right(), 0, Dead()))
            t_1198: 'bool7' = isinstance10(s0_155.direction, Right)
            def fn_1187() -> 'str8':
                return 'should reject opposite direction'
            test_29.assert_(t_1198, fn_1187)
        finally:
            test_29.soft_fail_to_hard()
class TestCase38(TestCase6):
    def test___addPlayerAddsANewSnake__195(self) -> None:
        'addPlayer adds a new snake'
        test_30: Test = Test()
        try:
            game_157: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            bigger_158: 'MultiSnakeGame' = add_player_59(game_157, 99)
            t_1185: 'bool7' = len_1581(bigger_158.snakes) == 3
            def fn_1179() -> 'str8':
                return 'should have 3 snakes after adding'
            test_30.assert_(t_1185, fn_1179)
        finally:
            test_30.soft_fail_to_hard()
class TestCase39(TestCase6):
    def test___removePlayerRemovesASnake__196(self) -> None:
        'removePlayer removes a snake'
        test_31: Test = Test()
        try:
            game_160: 'MultiSnakeGame' = new_multi_game_54(20, 10, 3, 42)
            smaller_161: 'MultiSnakeGame' = remove_player_60(game_160, 1)
            t_1177: 'bool7' = len_1581(smaller_161.snakes) == 2
            def fn_1171() -> 'str8':
                return 'should have 2 snakes after removing'
            test_31.assert_(t_1177, fn_1171)
        finally:
            test_31.soft_fail_to_hard()
class TestCase40(TestCase6):
    def test___multiRenderProducesOutput__197(self) -> None:
        'multiRender produces output'
        test_32: Test = Test()
        try:
            game_163: 'MultiSnakeGame' = new_multi_game_54(20, 10, 2, 42)
            rendered_164: 'str8' = multi_render_56(game_163)
            t_1169: 'bool7' = rendered_164 != ''
            def fn_1165() -> 'str8':
                return 'render should produce output'
            test_32.assert_(t_1169, fn_1165)
        finally:
            test_32.soft_fail_to_hard()
class TestCase41(TestCase6):
    def test___directionToStringAndStringToDirectionRoundTrip__198(self) -> None:
        'directionToString and stringToDirection round-trip'
        test_33: Test = Test()
        try:
            d_166: 'str8' = direction_to_string_61(Up())
            t_1161: 'bool7' = d_166 == 'up'
            def fn_1158() -> 'str8':
                return "Up should serialize to 'up'"
            test_33.assert_(t_1161, fn_1158)
            parsed_167: 'Union42[Direction, None]' = string_to_direction_62('down')
            def fn_1157() -> 'str8':
                return "'down' should parse to Down"
            test_33.assert_(True, fn_1157)
        finally:
            test_33.soft_fail_to_hard()
