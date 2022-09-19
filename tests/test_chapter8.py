from src.chapter8 import (greedy_pick, greedy_pick_price_per_mass, set_covering,
                       travelling_salesperson)

items: list[dict[str,str|int]] = [
{"name":"stereo", "price": 3000, "mass" : 32},
{"name":"laptop", "price": 2000, "mass" : 19},
{"name":"guitar", "price": 1500, "mass" : 15},
]

knapsack_capacity: int = 35

def test_greedy_pick():
    assert(greedy_pick(items, knapsack_capacity) == 3000)

def test_greedy_pick_price_per_mass():
    assert(greedy_pick_price_per_mass(items, knapsack_capacity) == 3500)

states_to_cover = set(("mt", "wa", "or", "id", "nv", "ut", "ca", "az"))
stations: dict[str,set[str]] = {}
stations["kone"] = set(("id", "nv", "ut"))
stations["ktwo"] = set(("wa", "id", "mt"))
stations["kthree"] = set(("or", "nv", "ca"))
stations["kfour"] = set(("nv", "ut"))
stations["kfive"] = set(("ca", "az"))

def test_set_covering():
   assert(set_covering(stations, states_to_cover) == {'ktwo','kfive','kfour','kthree'})

nodes = [
    (208, 664),
    (203, 885),
    (408, 182),
    (511, 111),
    (491, 807),
    (303, 384),
    (701, 140),
    (941, 364),
    (489, 420),
    (403, 59),
    (778, 364),
    (343, 778),
    (590, 672),
    (643, 489),
    (642, 743),
    (726, 799),
    (666, 511),
    (641, 122),
    (690, 867),
    (494, 428),
    (511, 50),
    (714, 985),
    (422, 640),
    (239, 375),
    (428, 762),
    (365, 127),
    (94, 713),
    (90, 899),
    (412, 324),
    (812, 225),
    (20, 850),
    (80, 368),
    (325, 189),
    (110, 745),
    (101, 924),
    (999, 792),
    (355, 528),
    (355, 70),
    (252, 184),
    (940, 874),
    (841, 155),
    (506, 423),
    (678, 365),
    (954, 696),
    (54, 701),
    (680, 151),
    (474, 463),
    (259, 547),
    (670, 430),
    (736, 42),
    (345, 852),
    (873, 778),
    (620, 902),
    (866, 895),
    (411, 711),
    (638, 158),
    (891, 638),
    (393, 959),
    (216, 422),
    (895, 845),
    (309, 540),
    (49, 917),
    (187, 311),
    (101, 664),
    (791, 306),
    (970, 302),
    (693, 111),
    (526, 375),
    (33, 670),
    (771, 574),
    (253, 664),
    (994, 270),
    (99, 834),
    (238, 227),
    (12, 604),
    (570, 922),
    (743, 808),
    (569, 177),
    (898, 900),
    (346, 773),
    (625, 700),
    (509, 367),
    (487, 570),
    (124, 960),
    (401, 254),
    (27, 940),
    (724, 843),
    (636, 31),
    (58, 495),
    (892, 617),
    (985, 329),
    (657, 742),
    (52, 87),
    (792, 760),
    (363, 439),
    (993, 564),
    (866, 994),
    (315, 236),
    (603, 898),
    (276, 88),
]

def test_travelling_salesperson():
    assert(travelling_salesperson(nodes) == ([
        18, 86, 76, 15, 93, 51, 59, 39, 78, 53, 96, 21, 52, 98, 75, 4, 24, 54, 22, 82, 46, 19, 8, 41, 67, 81, 28, 84, 2, 25, 37, 9,
         20, 3, 77, 55, 17, 45, 6, 66, 49, 87, 40, 29, 64, 10, 42, 48, 13, 16, 69, 89, 56, 43, 35, 95, 7, 90, 65, 71, 80, 12, 14, 91, 79,
          11, 50, 57, 1, 83, 34, 27, 61, 85, 30, 72, 33, 26, 44, 68, 63, 0, 70, 47, 60, 36, 94, 5, 23, 58, 62, 73, 38, 32, 97, 99,
           92, 31, 88, 74],
    8474.663240497215))