# dictionary that maps an action (single, double, triple, homerun, walk)
# and the current base state to the pair of score and the next base state

# base state (left to right are first to thrid base)
# 0: [000], 1: [100], 2: [010], 3: [001], 4: [110], 5: [101], 6: [011], 7: [111]

action_base_score_dict = {
    "single": {
        0: (0, 1),
        1: (0, 4),
        2: (1, 1),
        3: (1, 1),
        4: (1, 4),
        5: (1, 4),
        6: (2, 1),
        7: (2, 4),
    },
    "double": {
        0: (0, 2),
        1: (1, 2),
        2: (1, 2),
        3: (1, 2),
        4: (2, 2),
        5: (2, 2),
        6: (2, 2),
        7: (3, 2),
    },
    "triple": {
        0: (0, 3),
        1: (1, 3),
        2: (1, 3),
        3: (1, 3),
        4: (2, 3),
        5: (2, 3),
        6: (2, 3),
        7: (3, 3),
    },
    "homerun": {
        0: (1, 0),
        1: (2, 0),
        2: (2, 0),
        3: (2, 0),
        4: (3, 0),
        5: (3, 0),
        6: (3, 0),
        7: (4, 0),
    },
    "walk": {
        0: (0, 1),
        1: (0, 4),
        2: (0, 4),
        3: (0, 5),
        4: (0, 7),
        5: (0, 7),
        6: (0, 7),
        7: (1, 7),
    }
}
