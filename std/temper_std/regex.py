from abc import ABCMeta as ABCMeta5
from builtins import str as str4, bool as bool19, int as int0, list as list8, isinstance as isinstance56, len as len11, tuple as tuple6
from typing import Callable as Callable21, Sequence as Sequence22, Union as Union3, Any as Any58, ClassVar as ClassVar51, MutableSequence as MutableSequence20
from types import MappingProxyType as MappingProxyType54
from temper_core import cast_by_type as cast_by_type57, Label as Label24, Pair as Pair9, map_constructor as map_constructor65, generic_eq as generic_eq71, list_get as list_get18, string_from_code_point as string_from_code_point61, string_get as string_get12, string_next as string_next15, int_add as int_add16, int_to_string as int_to_string14, str_cat as str_cat13
from temper_core.regex import regex_compile_formatted as regex_compile_formatted66, regex_compiled_found as regex_compiled_found67, regex_compiled_find as regex_compiled_find68, regex_compiled_replace as regex_compiled_replace69, regex_compiled_split as regex_compiled_split70, regex_formatter_push_capture_name as regex_formatter_push_capture_name72, regex_formatter_push_code_to as regex_formatter_push_code_to73
pair_2600 = Pair9
map_constructor_2601 = map_constructor65
regex_compile_formatted_2602 = regex_compile_formatted66
regex_compiled_found_2603 = regex_compiled_found67
regex_compiled_find_2604 = regex_compiled_find68
regex_compiled_replace_2605 = regex_compiled_replace69
regex_compiled_split_2606 = regex_compiled_split70
generic_eq_2608 = generic_eq71
regex_formatter_push_capture_name_2610 = regex_formatter_push_capture_name72
list_get_2611 = list_get18
string_from_code_point_2612 = string_from_code_point61
regex_formatter_push_code_to_2613 = regex_formatter_push_code_to73
string_get_2615 = string_get12
string_next_2616 = string_next15
len_2618 = len11
int_add_2619 = int_add16
int_to_string_2620 = int_to_string14
str_cat_2621 = str_cat13
list_2623 = list8
tuple_2625 = tuple6
class RegexNode(metaclass = ABCMeta5):
    def compiled(this_44) -> 'Regex':
        return Regex(this_44)
    def found(this_45, text_172: 'str4') -> 'bool19':
        return this_45.compiled().found(text_172)
    def find(this_46, text_175: 'str4') -> 'Match':
        return this_46.compiled().find(text_175)
    def replace(this_47, text_178: 'str4', format_179: 'Callable21[[Match], str4]') -> 'str4':
        'Replace and split functions are also available. Both apply to all matches in\nthe string, replacing all or splitting at all.\n\nthis__47: RegexNode\n\ntext__178: String\n\nformat__179: fn (Match): String\n'
        return this_47.compiled().replace(text_178, format_179)
    def split(this_48, text_182: 'str4') -> 'Sequence22[str4]':
        return this_48.compiled().split(text_182)
class Capture(RegexNode):
    '`Capture` is a [group](#groups) that remembers the matched text for later\naccess. Temper supports only named matches, with current intended syntax\n`/(?name = ...)/`.'
    name_184: 'str4'
    item_185: 'RegexNode'
    __slots__ = ('name_184', 'item_185')
    def __init__(this_89, name_187: 'str4', item_188: 'RegexNode') -> None:
        this_89.name_184 = name_187
        this_89.item_185 = item_188
    @property
    def name(this_446) -> 'str4':
        return this_446.name_184
    @property
    def item(this_449) -> 'RegexNode':
        return this_449.item_185
class CodePart(RegexNode, metaclass = ABCMeta5):
    pass
class CodePoints(CodePart):
    value_189: 'str4'
    __slots__ = ('value_189',)
    def __init__(this_91, value_191: 'str4') -> None:
        this_91.value_189 = value_191
    @property
    def value(this_452) -> 'str4':
        return this_452.value_189
class Special(RegexNode, metaclass = ABCMeta5):
    pass
class SpecialSet(CodePart, Special, metaclass = ABCMeta5):
    pass
class CodeRange(CodePart):
    min_206: 'int0'
    max_207: 'int0'
    __slots__ = ('min_206', 'max_207')
    def __init__(this_107, min_209: 'int0', max_210: 'int0') -> None:
        this_107.min_206 = min_209
        this_107.max_207 = max_210
    @property
    def min(this_455) -> 'int0':
        return this_455.min_206
    @property
    def max(this_458) -> 'int0':
        return this_458.max_207
class CodeSet(RegexNode):
    items_211: 'Sequence22[CodePart]'
    negated_212: 'bool19'
    __slots__ = ('items_211', 'negated_212')
    def __init__(this_109, items_214: 'Sequence22[CodePart]', negated_544: 'Union3[bool19, None]' = None) -> None:
        _negated_544: 'Union3[bool19, None]' = negated_544
        negated_215: 'bool19'
        if _negated_544 is None:
            negated_215 = False
        else:
            negated_215 = _negated_544
        this_109.items_211 = items_214
        this_109.negated_212 = negated_215
    @property
    def items(this_461) -> 'Sequence22[CodePart]':
        return this_461.items_211
    @property
    def negated(this_464) -> 'bool19':
        return this_464.negated_212
class Or(RegexNode):
    '`Or` matches any one of multiple options, such as `/ab|cd|e*/`.'
    items_216: 'Sequence22[RegexNode]'
    __slots__ = ('items_216',)
    def __init__(this_112, items_218: 'Sequence22[RegexNode]') -> None:
        this_112.items_216 = items_218
    @property
    def items(this_467) -> 'Sequence22[RegexNode]':
        return this_467.items_216
class Repeat(RegexNode):
    item_219: 'RegexNode'
    min_220: 'int0'
    max_221: 'Union3[int0, None]'
    reluctant_222: 'bool19'
    __slots__ = ('item_219', 'min_220', 'max_221', 'reluctant_222')
    def __init__(this_115, item_224: 'RegexNode', min_225: 'int0', max_226: 'Union3[int0, None]', reluctant_546: 'Union3[bool19, None]' = None) -> None:
        _reluctant_546: 'Union3[bool19, None]' = reluctant_546
        reluctant_227: 'bool19'
        if _reluctant_546 is None:
            reluctant_227 = False
        else:
            reluctant_227 = _reluctant_546
        this_115.item_219 = item_224
        this_115.min_220 = min_225
        this_115.max_221 = max_226
        this_115.reluctant_222 = reluctant_227
    @property
    def item(this_470) -> 'RegexNode':
        return this_470.item_219
    @property
    def min(this_473) -> 'int0':
        return this_473.min_220
    @property
    def max(this_476) -> 'Union3[int0, None]':
        return this_476.max_221
    @property
    def reluctant(this_479) -> 'bool19':
        return this_479.reluctant_222
class Sequence(RegexNode):
    '`Sequence` strings along multiple other regexes in order.'
    items_236: 'Sequence22[RegexNode]'
    __slots__ = ('items_236',)
    def __init__(this_121, items_238: 'Sequence22[RegexNode]') -> None:
        this_121.items_236 = items_238
    @property
    def items(this_482) -> 'Sequence22[RegexNode]':
        return this_482.items_236
class Match:
    full_239: 'Group'
    groups_240: 'MappingProxyType54[str4, Group]'
    __slots__ = ('full_239', 'groups_240')
    def __init__(this_124, full_242: 'Group', groups_243: 'MappingProxyType54[str4, Group]') -> None:
        this_124.full_239 = full_242
        this_124.groups_240 = groups_243
    @property
    def full(this_497) -> 'Group':
        return this_497.full_239
    @property
    def groups(this_500) -> 'MappingProxyType54[str4, Group]':
        return this_500.groups_240
class Group:
    name_244: 'str4'
    value_245: 'str4'
    begin_246: 'int0'
    end_247: 'int0'
    __slots__ = ('name_244', 'value_245', 'begin_246', 'end_247')
    def __init__(this_127, name_249: 'str4', value_250: 'str4', begin_251: 'int0', end_252: 'int0') -> None:
        this_127.name_244 = name_249
        this_127.value_245 = value_250
        this_127.begin_246 = begin_251
        this_127.end_247 = end_252
    @property
    def name(this_485) -> 'str4':
        return this_485.name_244
    @property
    def value(this_488) -> 'str4':
        return this_488.value_245
    @property
    def begin(this_491) -> 'int0':
        return this_491.begin_246
    @property
    def end(this_494) -> 'int0':
        return this_494.end_247
class RegexRefs_56:
    code_points_253: 'CodePoints'
    group_254: 'Group'
    match_255: 'Match'
    or_object_256: 'Or'
    __slots__ = ('code_points_253', 'group_254', 'match_255', 'or_object_256')
    def __init__(this_129, code_points_548: 'Union3[CodePoints, None]' = None, group_550: 'Union3[Group, None]' = None, match_552: 'Union3[Match, None]' = None, or_object_554: 'Union3[Or, None]' = None) -> None:
        _code_points_548: 'Union3[CodePoints, None]' = code_points_548
        _group_550: 'Union3[Group, None]' = group_550
        _match_552: 'Union3[Match, None]' = match_552
        _or_object_554: 'Union3[Or, None]' = or_object_554
        t_1292: 'CodePoints'
        t_1293: 'Group'
        t_1295: 'MappingProxyType54[str4, Group]'
        t_1296: 'Match'
        t_1297: 'Or'
        code_points_258: 'CodePoints'
        if _code_points_548 is None:
            t_1292 = CodePoints('')
            code_points_258 = t_1292
        else:
            code_points_258 = _code_points_548
        group_259: 'Group'
        if _group_550 is None:
            t_1293 = Group('', '', 0, 0)
            group_259 = t_1293
        else:
            group_259 = _group_550
        match_260: 'Match'
        if _match_552 is None:
            t_1295 = map_constructor_2601((pair_2600('', group_259),))
            t_1296 = Match(group_259, t_1295)
            match_260 = t_1296
        else:
            match_260 = _match_552
        or_object_261: 'Or'
        if _or_object_554 is None:
            t_1297 = Or(())
            or_object_261 = t_1297
        else:
            or_object_261 = _or_object_554
        this_129.code_points_253 = code_points_258
        this_129.group_254 = group_259
        this_129.match_255 = match_260
        this_129.or_object_256 = or_object_261
    @property
    def code_points(this_503) -> 'CodePoints':
        return this_503.code_points_253
    @property
    def group(this_506) -> 'Group':
        return this_506.group_254
    @property
    def match_(this_509) -> 'Match':
        return this_509.match_255
    @property
    def or_object(this_512) -> 'Or':
        return this_512.or_object_256
class Regex:
    data_262: 'RegexNode'
    compiled_281: 'Any58'
    __slots__ = ('data_262', 'compiled_281')
    def __init__(this_57, data_264: 'RegexNode') -> None:
        t_421: 'RegexNode' = data_264
        this_57.data_262 = t_421
        formatted_266: 'str4' = RegexFormatter_66.regex_format(data_264)
        t_1171: 'Any58' = regex_compile_formatted_2602(data_264, formatted_266)
        this_57.compiled_281 = t_1171
    def found(this_58, text_268: 'str4') -> 'bool19':
        return regex_compiled_found_2603(this_58, this_58.compiled_281, text_268)
    def find(this_59, text_271: 'str4', begin_556: 'Union3[int0, None]' = None) -> 'Match':
        _begin_556: 'Union3[int0, None]' = begin_556
        begin_272: 'int0'
        if _begin_556 is None:
            begin_272 = 0
        else:
            begin_272 = _begin_556
        return regex_compiled_find_2604(this_59, this_59.compiled_281, text_271, begin_272, regex_refs_164)
    def replace(this_60, text_275: 'str4', format_276: 'Callable21[[Match], str4]') -> 'str4':
        return regex_compiled_replace_2605(this_60, this_60.compiled_281, text_275, format_276, regex_refs_164)
    def split(this_61, text_279: 'str4') -> 'Sequence22[str4]':
        return regex_compiled_split_2606(this_61, this_61.compiled_281, text_279, regex_refs_164)
    @property
    def data(this_539) -> 'RegexNode':
        return this_539.data_262
class RegexFormatter_66:
    out_303: 'list8[str4]'
    __slots__ = ('out_303',)
    @staticmethod
    def regex_format(data_309: 'RegexNode') -> 'str4':
        return RegexFormatter_66().format(data_309)
    def format(this_67, regex_312: 'RegexNode') -> 'str4':
        this_67.push_regex_314(regex_312)
        return ''.join(this_67.out_303)
    def push_regex_314(this_68, regex_315: 'RegexNode') -> 'None':
        t_894: 'Capture'
        t_895: 'CodePoints'
        t_896: 'CodeRange'
        t_897: 'CodeSet'
        t_898: 'Or'
        t_899: 'Repeat'
        t_900: 'Sequence'
        if isinstance56(regex_315, Capture):
            t_894 = cast_by_type57(regex_315, Capture)
            this_68.push_capture_317(t_894)
        elif isinstance56(regex_315, CodePoints):
            t_895 = cast_by_type57(regex_315, CodePoints)
            this_68.push_code_points_335(t_895, False)
        elif isinstance56(regex_315, CodeRange):
            t_896 = cast_by_type57(regex_315, CodeRange)
            this_68.push_code_range_341(t_896)
        elif isinstance56(regex_315, CodeSet):
            t_897 = cast_by_type57(regex_315, CodeSet)
            this_68.push_code_set_347(t_897)
        elif isinstance56(regex_315, Or):
            t_898 = cast_by_type57(regex_315, Or)
            this_68.push_or_359(t_898)
        elif isinstance56(regex_315, Repeat):
            t_899 = cast_by_type57(regex_315, Repeat)
            this_68.push_repeat_363(t_899)
        elif isinstance56(regex_315, Sequence):
            t_900 = cast_by_type57(regex_315, Sequence)
            this_68.push_sequence_368(t_900)
        elif generic_eq_2608(regex_315, begin):
            this_68.out_303.append('^')
        elif generic_eq_2608(regex_315, dot):
            this_68.out_303.append('.')
        elif generic_eq_2608(regex_315, end):
            this_68.out_303.append('$')
        elif generic_eq_2608(regex_315, word_boundary):
            this_68.out_303.append('\\b')
        elif generic_eq_2608(regex_315, digit):
            this_68.out_303.append('\\d')
        elif generic_eq_2608(regex_315, space):
            this_68.out_303.append('\\s')
        elif generic_eq_2608(regex_315, word):
            this_68.out_303.append('\\w')
    def push_capture_317(this_69, capture_318: 'Capture') -> 'None':
        this_69.out_303.append('(')
        t_868: 'list8[str4]' = this_69.out_303
        t_1262: 'str4' = capture_318.name
        regex_formatter_push_capture_name_2610(this_69, t_868, t_1262)
        t_1264: 'RegexNode' = capture_318.item
        this_69.push_regex_314(t_1264)
        this_69.out_303.append(')')
    def push_code_324(this_71, code_325: 'int0', inside_code_set_326: 'bool19') -> 'None':
        t_856: 'bool19'
        t_857: 'bool19'
        t_858: 'str4'
        t_860: 'str4'
        t_861: 'bool19'
        t_862: 'bool19'
        t_863: 'bool19'
        t_864: 'bool19'
        t_865: 'str4'
        with Label24() as fn_327:
            special_escape_328: 'str4'
            if code_325 == Codes_83.carriage_return:
                special_escape_328 = 'r'
            elif code_325 == Codes_83.newline:
                special_escape_328 = 'n'
            elif code_325 == Codes_83.tab:
                special_escape_328 = 't'
            else:
                special_escape_328 = ''
            if special_escape_328 != '':
                this_71.out_303.append('\\')
                this_71.out_303.append(special_escape_328)
                fn_327.break_()
            if code_325 <= 127:
                escape_need_329: 'int0' = list_get_2611(escape_needs_165, code_325)
                if generic_eq_2608(escape_need_329, 2):
                    t_857 = True
                else:
                    if inside_code_set_326:
                        t_856 = code_325 == Codes_83.dash
                    else:
                        t_856 = False
                    t_857 = t_856
                if t_857:
                    this_71.out_303.append('\\')
                    t_858 = string_from_code_point_2612(code_325)
                    this_71.out_303.append(t_858)
                    fn_327.break_()
                elif generic_eq_2608(escape_need_329, 0):
                    t_860 = string_from_code_point_2612(code_325)
                    this_71.out_303.append(t_860)
                    fn_327.break_()
            if code_325 >= Codes_83.supplemental_min:
                t_864 = True
            else:
                if code_325 > Codes_83.high_control_max:
                    if Codes_83.surrogate_min <= code_325:
                        t_861 = code_325 <= Codes_83.surrogate_max
                    else:
                        t_861 = False
                    if t_861:
                        t_862 = True
                    else:
                        t_862 = code_325 == Codes_83.uint16_max
                    t_863 = not t_862
                else:
                    t_863 = False
                t_864 = t_863
            if t_864:
                t_865 = string_from_code_point_2612(code_325)
                this_71.out_303.append(t_865)
            else:
                regex_formatter_push_code_to_2613(this_71, this_71.out_303, code_325, inside_code_set_326)
    def push_code_points_335(this_73, code_points_336: 'CodePoints', inside_code_set_337: 'bool19') -> 'None':
        t_1249: 'int0'
        t_1251: 'int0'
        value_339: 'str4' = code_points_336.value
        index_340: 'int0' = 0
        while True:
            if not len11(value_339) > index_340:
                break
            t_1249 = string_get_2615(value_339, index_340)
            this_73.push_code_324(t_1249, inside_code_set_337)
            t_1251 = string_next_2616(value_339, index_340)
            index_340 = t_1251
    def push_code_range_341(this_74, code_range_342: 'CodeRange') -> 'None':
        this_74.out_303.append('[')
        this_74.push_code_range_unwrapped_344(code_range_342)
        this_74.out_303.append(']')
    def push_code_range_unwrapped_344(this_75, code_range_345: 'CodeRange') -> 'None':
        t_1239: 'int0' = code_range_345.min
        this_75.push_code_324(t_1239, True)
        this_75.out_303.append('-')
        t_1242: 'int0' = code_range_345.max
        this_75.push_code_324(t_1242, True)
    def push_code_set_347(this_76, code_set_348: 'CodeSet') -> 'None':
        t_1233: 'int0'
        t_1235: 'CodePart'
        t_841: 'CodeSet'
        adjusted_350: 'RegexNode' = this_76.adjust_code_set_352(code_set_348, regex_refs_164)
        if isinstance56(adjusted_350, CodeSet):
            t_841 = cast_by_type57(adjusted_350, CodeSet)
            if not t_841.items:
                if t_841.negated:
                    this_76.out_303.append('[\\s\\S]')
                else:
                    this_76.out_303.append('(?:$.)')
            else:
                this_76.out_303.append('[')
                if t_841.negated:
                    this_76.out_303.append('^')
                i_351: 'int0' = 0
                while True:
                    t_1233 = len_2618(t_841.items)
                    if not i_351 < t_1233:
                        break
                    t_1235 = list_get_2611(t_841.items, i_351)
                    this_76.push_code_set_item_356(t_1235)
                    i_351 = int_add_2619(i_351, 1)
                this_76.out_303.append(']')
        else:
            this_76.push_regex_314(adjusted_350)
    def adjust_code_set_352(this_77, code_set_353: 'CodeSet', regex_refs_354: 'RegexRefs_56') -> 'RegexNode':
        return code_set_353
    def push_code_set_item_356(this_78, code_part_357: 'CodePart') -> 'None':
        t_826: 'CodePoints'
        t_827: 'CodeRange'
        t_828: 'SpecialSet'
        if isinstance56(code_part_357, CodePoints):
            t_826 = cast_by_type57(code_part_357, CodePoints)
            this_78.push_code_points_335(t_826, True)
        elif isinstance56(code_part_357, CodeRange):
            t_827 = cast_by_type57(code_part_357, CodeRange)
            this_78.push_code_range_unwrapped_344(t_827)
        elif isinstance56(code_part_357, SpecialSet):
            t_828 = cast_by_type57(code_part_357, SpecialSet)
            this_78.push_regex_314(t_828)
    def push_or_359(this_79, or_360: 'Or') -> 'None':
        t_1207: 'RegexNode'
        t_1210: 'int0'
        t_1213: 'RegexNode'
        if not (not or_360.items):
            this_79.out_303.append('(?:')
            t_1207 = list_get_2611(or_360.items, 0)
            this_79.push_regex_314(t_1207)
            i_362: 'int0' = 1
            while True:
                t_1210 = len_2618(or_360.items)
                if not i_362 < t_1210:
                    break
                this_79.out_303.append('|')
                t_1213 = list_get_2611(or_360.items, i_362)
                this_79.push_regex_314(t_1213)
                i_362 = int_add_2619(i_362, 1)
            this_79.out_303.append(')')
    def push_repeat_363(this_80, repeat_364: 'Repeat') -> 'None':
        t_1195: 'str4'
        t_1198: 'str4'
        t_803: 'bool19'
        t_804: 'bool19'
        t_805: 'bool19'
        this_80.out_303.append('(?:')
        t_1187: 'RegexNode' = repeat_364.item
        this_80.push_regex_314(t_1187)
        this_80.out_303.append(')')
        min_366: 'int0' = repeat_364.min
        max_367: 'Union3[int0, None]' = repeat_364.max
        if min_366 == 0:
            t_803 = max_367 == 1
        else:
            t_803 = False
        if t_803:
            this_80.out_303.append('?')
        else:
            if min_366 == 0:
                t_804 = max_367 is None
            else:
                t_804 = False
            if t_804:
                this_80.out_303.append('*')
            else:
                if min_366 == 1:
                    t_805 = max_367 is None
                else:
                    t_805 = False
                if t_805:
                    this_80.out_303.append('+')
                else:
                    t_1195 = int_to_string_2620(min_366)
                    this_80.out_303.append(str_cat_2621('{', t_1195))
                    if min_366 != max_367:
                        this_80.out_303.append(',')
                        if not max_367 is None:
                            t_1198 = int_to_string_2620(max_367)
                            this_80.out_303.append(t_1198)
                    this_80.out_303.append('}')
        if repeat_364.reluctant:
            this_80.out_303.append('?')
    def push_sequence_368(this_81, sequence_369: 'Sequence') -> 'None':
        t_1182: 'int0'
        t_1184: 'RegexNode'
        i_371: 'int0' = 0
        while True:
            t_1182 = len_2618(sequence_369.items)
            if not i_371 < t_1182:
                break
            t_1184 = list_get_2611(sequence_369.items, i_371)
            this_81.push_regex_314(t_1184)
            i_371 = int_add_2619(i_371, 1)
    def max_code(this_82, code_part_373: 'CodePart') -> 'Union3[int0, None]':
        return_159: 'Union3[int0, None]'
        t_1178: 'int0'
        t_791: 'CodePoints'
        if isinstance56(code_part_373, CodePoints):
            t_791 = cast_by_type57(code_part_373, CodePoints)
            value_375: 'str4' = t_791.value
            if not value_375:
                return_159 = None
            else:
                max_376: 'int0' = 0
                index_377: 'int0' = 0
                while True:
                    if not len11(value_375) > index_377:
                        break
                    next_378: 'int0' = string_get_2615(value_375, index_377)
                    if next_378 > max_376:
                        max_376 = next_378
                    t_1178 = string_next_2616(value_375, index_377)
                    index_377 = t_1178
                return_159 = max_376
        elif isinstance56(code_part_373, CodeRange):
            return_159 = cast_by_type57(code_part_373, CodeRange).max
        elif generic_eq_2608(code_part_373, digit):
            return_159 = Codes_83.digit9
        elif generic_eq_2608(code_part_373, space):
            return_159 = Codes_83.space
        elif generic_eq_2608(code_part_373, word):
            return_159 = Codes_83.lower_z
        else:
            return_159 = None
        return return_159
    def __init__(this_140) -> None:
        t_1172: 'list8[str4]' = ['']
        this_140.out_303 = t_1172
class Codes_83:
    ampersand: ClassVar51['int0']
    backslash: ClassVar51['int0']
    caret: ClassVar51['int0']
    carriage_return: ClassVar51['int0']
    curly_left: ClassVar51['int0']
    curly_right: ClassVar51['int0']
    dash: ClassVar51['int0']
    dot: ClassVar51['int0']
    high_control_min: ClassVar51['int0']
    high_control_max: ClassVar51['int0']
    digit0: ClassVar51['int0']
    digit9: ClassVar51['int0']
    lower_a: ClassVar51['int0']
    lower_z: ClassVar51['int0']
    newline: ClassVar51['int0']
    peso: ClassVar51['int0']
    pipe: ClassVar51['int0']
    plus: ClassVar51['int0']
    question: ClassVar51['int0']
    round_left: ClassVar51['int0']
    round_right: ClassVar51['int0']
    slash: ClassVar51['int0']
    square_left: ClassVar51['int0']
    square_right: ClassVar51['int0']
    star: ClassVar51['int0']
    tab: ClassVar51['int0']
    tilde: ClassVar51['int0']
    upper_a: ClassVar51['int0']
    upper_z: ClassVar51['int0']
    space: ClassVar51['int0']
    surrogate_min: ClassVar51['int0']
    surrogate_max: ClassVar51['int0']
    supplemental_min: ClassVar51['int0']
    uint16_max: ClassVar51['int0']
    underscore: ClassVar51['int0']
    __slots__ = ()
    def __init__(this_161) -> None:
        pass
Codes_83.ampersand = 38
Codes_83.backslash = 92
Codes_83.caret = 94
Codes_83.carriage_return = 13
Codes_83.curly_left = 123
Codes_83.curly_right = 125
Codes_83.dash = 45
Codes_83.dot = 46
Codes_83.high_control_min = 127
Codes_83.high_control_max = 159
Codes_83.digit0 = 48
Codes_83.digit9 = 57
Codes_83.lower_a = 97
Codes_83.lower_z = 122
Codes_83.newline = 10
Codes_83.peso = 36
Codes_83.pipe = 124
Codes_83.plus = 43
Codes_83.question = 63
Codes_83.round_left = 40
Codes_83.round_right = 41
Codes_83.slash = 47
Codes_83.square_left = 91
Codes_83.square_right = 93
Codes_83.star = 42
Codes_83.tab = 9
Codes_83.tilde = 42
Codes_83.upper_a = 65
Codes_83.upper_z = 90
Codes_83.space = 32
Codes_83.surrogate_min = 55296
Codes_83.surrogate_max = 57343
Codes_83.supplemental_min = 65536
Codes_83.uint16_max = 65535
Codes_83.underscore = 95
class Begin_49(Special):
    __slots__ = ()
    def __init__(this_93) -> None:
        pass
return_192: 'Special' = Begin_49()
begin: 'Special' = return_192
class Dot_50(Special):
    __slots__ = ()
    def __init__(this_95) -> None:
        pass
return_194: 'Special' = Dot_50()
dot: 'Special' = return_194
class End_51(Special):
    __slots__ = ()
    def __init__(this_97) -> None:
        pass
return_196: 'Special' = End_51()
end: 'Special' = return_196
class WordBoundary_52(Special):
    __slots__ = ()
    def __init__(this_99) -> None:
        pass
return_198: 'Special' = WordBoundary_52()
word_boundary: 'Special' = return_198
class Digit_53(SpecialSet):
    __slots__ = ()
    def __init__(this_101) -> None:
        pass
return_200: 'SpecialSet' = Digit_53()
digit: 'SpecialSet' = return_200
class Space_54(SpecialSet):
    __slots__ = ()
    def __init__(this_103) -> None:
        pass
return_202: 'SpecialSet' = Space_54()
space: 'SpecialSet' = return_202
class Word_55(SpecialSet):
    __slots__ = ()
    def __init__(this_105) -> None:
        pass
return_204: 'SpecialSet' = Word_55()
word: 'SpecialSet' = return_204
def build_escape_needs_163() -> 'Sequence22[int0]':
    t_935: 'bool19'
    t_936: 'bool19'
    t_937: 'bool19'
    t_938: 'bool19'
    t_939: 'bool19'
    t_940: 'bool19'
    t_941: 'bool19'
    t_942: 'bool19'
    t_943: 'bool19'
    t_944: 'bool19'
    t_945: 'bool19'
    t_946: 'bool19'
    t_947: 'bool19'
    t_948: 'bool19'
    t_949: 'bool19'
    t_950: 'bool19'
    t_951: 'bool19'
    t_952: 'bool19'
    t_953: 'bool19'
    t_954: 'bool19'
    t_955: 'bool19'
    t_956: 'bool19'
    t_957: 'bool19'
    t_958: 'bool19'
    t_959: 'int0'
    escape_needs_381: 'MutableSequence20[int0]' = list_2623()
    code_382: 'int0' = 0
    while code_382 <= 127:
        if code_382 == Codes_83.dash:
            t_942 = True
        else:
            if code_382 == Codes_83.space:
                t_941 = True
            else:
                if code_382 == Codes_83.underscore:
                    t_940 = True
                else:
                    if Codes_83.digit0 <= code_382:
                        t_935 = code_382 <= Codes_83.digit9
                    else:
                        t_935 = False
                    if t_935:
                        t_939 = True
                    else:
                        if Codes_83.upper_a <= code_382:
                            t_936 = code_382 <= Codes_83.upper_z
                        else:
                            t_936 = False
                        if t_936:
                            t_938 = True
                        else:
                            if Codes_83.lower_a <= code_382:
                                t_937 = code_382 <= Codes_83.lower_z
                            else:
                                t_937 = False
                            t_938 = t_937
                        t_939 = t_938
                    t_940 = t_939
                t_941 = t_940
            t_942 = t_941
        if t_942:
            t_959 = 0
        else:
            if code_382 == Codes_83.ampersand:
                t_958 = True
            else:
                if code_382 == Codes_83.backslash:
                    t_957 = True
                else:
                    if code_382 == Codes_83.caret:
                        t_956 = True
                    else:
                        if code_382 == Codes_83.curly_left:
                            t_955 = True
                        else:
                            if code_382 == Codes_83.curly_right:
                                t_954 = True
                            else:
                                if code_382 == Codes_83.dot:
                                    t_953 = True
                                else:
                                    if code_382 == Codes_83.peso:
                                        t_952 = True
                                    else:
                                        if code_382 == Codes_83.pipe:
                                            t_951 = True
                                        else:
                                            if code_382 == Codes_83.plus:
                                                t_950 = True
                                            else:
                                                if code_382 == Codes_83.question:
                                                    t_949 = True
                                                else:
                                                    if code_382 == Codes_83.round_left:
                                                        t_948 = True
                                                    else:
                                                        if code_382 == Codes_83.round_right:
                                                            t_947 = True
                                                        else:
                                                            if code_382 == Codes_83.slash:
                                                                t_946 = True
                                                            else:
                                                                if code_382 == Codes_83.square_left:
                                                                    t_945 = True
                                                                else:
                                                                    if code_382 == Codes_83.square_right:
                                                                        t_944 = True
                                                                    else:
                                                                        if code_382 == Codes_83.star:
                                                                            t_943 = True
                                                                        else:
                                                                            t_943 = code_382 == Codes_83.tilde
                                                                        t_944 = t_943
                                                                    t_945 = t_944
                                                                t_946 = t_945
                                                            t_947 = t_946
                                                        t_948 = t_947
                                                    t_949 = t_948
                                                t_950 = t_949
                                            t_951 = t_950
                                        t_952 = t_951
                                    t_953 = t_952
                                t_954 = t_953
                            t_955 = t_954
                        t_956 = t_955
                    t_957 = t_956
                t_958 = t_957
            if t_958:
                t_959 = 2
            else:
                t_959 = 1
        escape_needs_381.append(t_959)
        code_382 = int_add_2619(code_382, 1)
    return tuple_2625(escape_needs_381)
escape_needs_165: 'Sequence22[int0]' = build_escape_needs_163()
regex_refs_164: 'RegexRefs_56' = RegexRefs_56()
def entire(item_228: 'RegexNode') -> 'RegexNode':
    return Sequence((begin, item_228, end))
def one_or_more(item_230: 'RegexNode', reluctant_558: 'Union3[bool19, None]' = None) -> 'Repeat':
    _reluctant_558: 'Union3[bool19, None]' = reluctant_558
    reluctant_231: 'bool19'
    if _reluctant_558 is None:
        reluctant_231 = False
    else:
        reluctant_231 = _reluctant_558
    return Repeat(item_230, 1, None, reluctant_231)
def optional(item_233: 'RegexNode', reluctant_560: 'Union3[bool19, None]' = None) -> 'Repeat':
    _reluctant_560: 'Union3[bool19, None]' = reluctant_560
    reluctant_234: 'bool19'
    if _reluctant_560 is None:
        reluctant_234 = False
    else:
        reluctant_234 = _reluctant_560
    return Repeat(item_233, 0, 1, reluctant_234)
