from temper_std.json import JsonAdapter, JsonProducer, JsonSyntaxTree, InterchangeContext, JsonString
from datetime import date as date78
from builtins import str as str4, int as int0, bool as bool18, list as list7, len as len10
from temper_core import cast_by_type as cast_by_type57, date_to_string as date_to_string74, date_from_iso_string as date_from_iso_string75, arith_int_mod as arith_int_mod76, int_to_string as int_to_string13, string_get as string_get11, string_next as string_next14, string_count_between as string_count_between77, int_sub as int_sub24
from typing import Sequence as Sequence21
from temper_std.json import JsonAdapter, JsonString
date_to_string_2626 = date_to_string74
date_from_iso_string_2627 = date_from_iso_string75
arith_int_mod_2628 = arith_int_mod76
int_to_string_2629 = int_to_string13
len_2630 = len10
string_get_2631 = string_get11
string_next_2633 = string_next14
string_count_between_2634 = string_count_between77
int_sub_2635 = int_sub24
class DateJsonAdapter_109(JsonAdapter['date78']):
    __slots__ = ()
    def encode_to_json(this_120, x_116: 'date78', p_117: 'JsonProducer') -> 'None':
        encode_to_json_90(x_116, p_117)
    def decode_from_json(this_121, t_118: 'JsonSyntaxTree', ic_119: 'InterchangeContext') -> 'date78':
        return decode_from_json_93(t_118, ic_119)
    def __init__(this_122) -> None:
        pass
# Type `std/temporal/`.Date connected to datetime.date
def encode_to_json_90(this_20: 'date78', p_91: 'JsonProducer') -> 'None':
    t_313: 'str4' = date_to_string_2626(this_20)
    p_91.string_value(t_313)
def decode_from_json_93(t_94: 'JsonSyntaxTree', ic_95: 'InterchangeContext') -> 'date78':
    t_190: 'JsonString'
    t_190 = cast_by_type57(t_94, JsonString)
    return date_from_iso_string_2627(t_190.content)
def json_adapter_124() -> 'JsonAdapter[date78]':
    return DateJsonAdapter_109()
days_in_month_34: 'Sequence21[int0]' = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
def is_leap_year_32(year_41: 'int0') -> 'bool18':
    return_21: 'bool18'
    t_263: 'int0'
    if arith_int_mod_2628(year_41, 4) == 0:
        if arith_int_mod_2628(year_41, 100) != 0:
            return_21 = True
        else:
            t_263 = arith_int_mod_2628(year_41, 400)
            return_21 = t_263 == 0
    else:
        return_21 = False
    return return_21
def pad_to_33(min_width_43: 'int0', num_44: 'int0', sb_45: 'list7[str4]') -> 'None':
    "If the decimal representation of \\|num\\| is longer than [minWidth],\nthen appends that representation.\nOtherwise any sign for [num] followed by enough zeroes to bring the\nwhole length up to [minWidth].\n\n```temper\n// When the width is greater than the decimal's length,\n// we pad to that width.\n\"0123\" == do {\n  let sb = new StringBuilder();\n  padTo(4, 123, sb);\n  sb.toString()\n}\n\n// When the width is the same or lesser, we just use the string form.\n\"123\" == do {\n  let sb = new StringBuilder();\n  padTo(2, 123, sb);\n  sb.toString()\n}\n\n// The sign is always on the left.\n\"-01\" == do {\n  let sb = new StringBuilder();\n  padTo(3, -1, sb);\n  sb.toString()\n}\n```\n\nminWidth__43: Int32\n\nnum__44: Int32\n\nsb__45: builtins.list<String>\n"
    t_346: 'int0'
    t_348: 'int0'
    t_257: 'bool18'
    decimal_47: 'str4' = int_to_string_2629(num_44, 10)
    decimal_index_48: 'int0' = 0
    decimal_end_49: 'int0' = len_2630(decimal_47)
    if decimal_index_48 < decimal_end_49:
        t_346 = string_get_2631(decimal_47, decimal_index_48)
        t_257 = t_346 == 45
    else:
        t_257 = False
    if t_257:
        sb_45.append('-')
        t_348 = string_next_2633(decimal_47, decimal_index_48)
        decimal_index_48 = t_348
    t_349: 'int0' = string_count_between_2634(decimal_47, decimal_index_48, decimal_end_49)
    n_needed_50: 'int0' = int_sub_2635(min_width_43, t_349)
    while n_needed_50 > 0:
        sb_45.append('0')
        n_needed_50 = int_sub_2635(n_needed_50, 1)
    sb_45.append(decimal_47[decimal_index_48 : decimal_end_49])
day_of_week_lookup_table_leapy_35: 'Sequence21[int0]' = (0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6)
day_of_week_lookup_table_not_leapy_36: 'Sequence21[int0]' = (0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)
