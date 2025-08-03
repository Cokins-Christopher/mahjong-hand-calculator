"""
American Mahjong Rules Specification
Comprehensive rules and pattern definitions for 2024 American Mahjong
"""

from typing import Dict, List, Any

class MahjongRules:
    """Comprehensive 2024 American Mahjong rules specification"""
    
    def __init__(self):
        # Tile Definitions
        self.tile_definitions = {
            'numbered_tiles': {
                'bams': [f"{i}B" for i in range(1, 10)],      # 1B-9B (Bamboo)
                'cracks': [f"{i}C" for i in range(1, 10)],     # 1C-9C (Characters)
                'dots': [f"{i}D" for i in range(1, 10)]        # 1D-9D (Circles)
            },
            'honor_tiles': {
                'winds': ['E', 'S', 'W', 'N'],                 # East, South, West, North
                'dragons': ['R', 'G', '0'],                    # Red, Green, White Dragons
                'flowers': ['F'],                               # Flowers (Jokers)
                'year_tiles': ['2024']                         # Year-specific tiles
            }
        }
        
        # Dragon Associations (Traditional)
        self.dragon_associations = {
            'C': 'R',  # Cracks/Characters match Red Dragon
            'B': 'G',  # Bams/Bamboo match Green Dragon  
            'D': '0'   # Dots/Circles match White Dragon
        }
        
        # Suit Requirements Definitions
        self.suit_requirements = {
            'any_1_suit': {
                'description': 'All numbered tiles must be from the same suit',
                'validation': 'All numbered tiles must be B, C, or D (not mixed)',
                'examples': ['All Bams', 'All Cracks', 'All Dots']
            },
            'any_2_suits': {
                'description': 'Numbered tiles can be from exactly 2 different suits',
                'validation': 'Must have tiles from exactly 2 suits (B+C, B+D, C+D)',
                'examples': ['Bams + Cracks', 'Bams + Dots', 'Cracks + Dots']
            },
            'any_3_suits': {
                'description': 'Numbered tiles can be from all 3 suits',
                'validation': 'Must have tiles from all 3 suits (B+C+D)',
                'examples': ['Bams + Cracks + Dots']
            },
            'any_1_or_2_suits': {
                'description': 'Numbered tiles can be from 1 or 2 suits',
                'validation': 'Can be all one suit OR exactly 2 suits',
                'examples': ['All Bams', 'Bams + Cracks', 'Cracks + Dots']
            },
            'any_2_or_3_suits': {
                'description': 'Numbered tiles can be from 2 or 3 suits',
                'validation': 'Must have tiles from 2 or 3 suits (not all one suit)',
                'examples': ['Bams + Cracks', 'Bams + Cracks + Dots']
            },
            'any_1_suit_matching_dragons': {
                'description': 'All numbered tiles from same suit, dragons must match that suit',
                'validation': 'One suit + matching dragons (C+R, B+G, D+0)',
                'examples': ['Cracks + Red Dragons', 'Bams + Green Dragons', 'Dots + White Dragons']
            },
            'any_1_suit_opposite_dragons': {
                'description': 'All numbered tiles from same suit, dragons must NOT match that suit',
                'validation': 'One suit + opposite dragons (C+G/0, B+R/0, D+R/G)',
                'examples': ['Cracks + Green/White Dragons', 'Bams + Red/White Dragons']
            },
            'any_2_suits_matching_dragons': {
                'description': 'Numbered tiles from 2 suits, dragons must match one of those suits',
                'validation': 'Two suits + dragons matching one of those suits',
                'examples': ['Bams+Cracks + Red Dragons', 'Bams+Dots + Green Dragons']
            },
            'any_3_dragons': {
                'description': 'Must use all 3 types of dragons',
                'validation': 'Must have Red, Green, and White dragons',
                'examples': ['R + G + 0']
            },
            'any_2_dragons': {
                'description': 'Must use exactly 2 types of dragons',
                'validation': 'Must have exactly 2 different dragon types',
                'examples': ['R + G', 'R + 0', 'G + 0']
            },
            'specific_numbers': {
                'description': 'Can only use the specific numbers shown in the pattern',
                'validation': 'Numbers must match exactly what is specified',
                'examples': ['Only 1,2,3,4,5', 'Only 3,6,9', 'Only 1,3,5,7,9']
            }
        }
        
        # Joker Usage Rules
        self.joker_rules = {
            'general': {
                'max_jokers': 8,
                'substitution': 'Can substitute for any tile except in Singles and Pairs',
                'representation': 'Must represent specific tile needed for pattern'
            },
            'restrictions': {
                'singles_and_pairs': 'Jokers cannot be used in Singles and Pairs category',
                'concealed_hands': 'Jokers allowed in both exposed (X) and concealed (C) hands'
            }
        }
        
        # Hand Categories
        self.hand_categories = {
            'X': {
                'name': 'Exposed',
                'description': 'Can have exposed melds',
                'restrictions': 'None - can be exposed or concealed'
            },
            'C': {
                'name': 'Concealed',
                'description': 'Must be concealed hand only',
                'restrictions': 'No exposed melds allowed'
            }
        }
        
        # 2024 Pattern Definitions - Complete Implementation
        self.year_patterns = {
            2024: {
                '2024_patterns': {
                    '2024_222_000_2222_4444': {
                        'name': '2024 222 000 2222 4444',
                        'pattern': '222 000 2222 4444',
                        'description': 'SUIT A, SUIT B (different suits)',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True,
                        'special_rules': ['All zeros must be White Dragons'],
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                            {'type': 'dragon', 'value': '0', 'count': 3, 'special': 'white_dragon'},
                            {'type': 'number', 'value': 2, 'count': 4, 'suit': 'B'},
                            {'type': 'number', 'value': 4, 'count': 4, 'suit': 'B'}
                        ],
                        'total_tiles': 14
                    },
                    '2024_FFFF_2222_0000_24': {
                        'name': '2024 FFFF 2222 0000 24',
                        'pattern': 'FFFF 2222 0000 24',
                        'description': 'SUIT A and SUIT B (any suits)',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True,
                        'special_rules': ['0000 must be White Dragons', '24 means one 2-tile and one 4-tile'],
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 4},
                            {'type': 'number', 'value': 2, 'count': 4, 'suit': 'A'},
                            {'type': 'dragon', 'value': '0', 'count': 4, 'special': 'white_dragon'},
                            {'type': 'number', 'value': 2, 'count': 1, 'suit': 'B'},
                            {'type': 'number', 'value': 4, 'count': 1, 'suit': 'B'}
                        ],
                        'total_tiles': 14
                    },
                    '2024_FF_2024_2222_2222': {
                        'name': '2024 FF 2024 2222 2222 (Option A)',
                        'pattern': 'FF 2024 2222 2222',
                        'description': 'Three different suits allowed',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'special_rules': ['In 2024, the 0 must be White Dragon'],
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'year', 'value': '2024', 'count': 1, 'special': 'white_dragon_0'},
                            {'type': 'number', 'value': 2, 'count': 4, 'suit': 'B'},
                            {'type': 'number', 'value': 2, 'count': 4, 'suit': 'C'}
                        ],
                        'total_tiles': 14
                    },
                    '2024_FF_2024_4444_4444': {
                        'name': '2024 FF 2024 4444 4444 (Option B)',
                        'pattern': 'FF 2024 4444 4444',
                        'description': 'Three different suits allowed',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'special_rules': ['In 2024, the 0 must be White Dragon'],
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'year', 'value': '2024', 'count': 1, 'special': 'white_dragon_0'},
                            {'type': 'number', 'value': 4, 'count': 4, 'suit': 'B'},
                            {'type': 'number', 'value': 4, 'count': 4, 'suit': 'C'}
                        ],
                        'total_tiles': 14
                    },
                    '2024_NN_EEE_2024_WWW_SS': {
                        'name': '2024 NN EEE 2024 WWW SS',
                        'pattern': 'NN EEE 2024 WWW SS',
                        'description': 'SUIT A can be any suit',
                        'points': 30,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True,
                        'special_rules': ['In 2024, the 0 must be White Dragon', 'Winds are fixed'],
                        'components': [
                            {'type': 'wind', 'value': 'N', 'count': 2},
                            {'type': 'wind', 'value': 'E', 'count': 3},
                            {'type': 'year', 'value': '2024', 'count': 1, 'special': 'white_dragon_0'},
                            {'type': 'wind', 'value': 'W', 'count': 3},
                            {'type': 'wind', 'value': 'S', 'count': 2}
                        ],
                        'total_tiles': 14
                    }
                },
                
                '2468_patterns': {
                    '2468_222_444_6666_8888_same': {
                        'name': '2468 222 444 6666 8888 (All Same Suit)',
                        'pattern': '222 444 6666 8888',
                        'description': 'ALL MUST BE SUIT A',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 6, 'count': 4, 'suit': 'A'},
                            {'type': 'number', 'value': 8, 'count': 4, 'suit': 'A'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_222_444_6666_8888_two': {
                        'name': '2468 222 444 6666 8888 (Two Suits)',
                        'pattern': '222 444 6666 8888',
                        'description': 'SUIT A and SUIT B',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 6, 'count': 4, 'suit': 'B'},
                            {'type': 'number', 'value': 8, 'count': 4, 'suit': 'B'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_22_444_44_666_8888': {
                        'name': '2468 22 444 44 666 8888',
                        'pattern': '22 444 44 666 8888',
                        'description': 'Three suits allowed',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 2, 'suit': 'B'},
                            {'type': 'number', 'value': 6, 'count': 3, 'suit': 'B'},
                            {'type': 'number', 'value': 8, 'count': 4, 'suit': 'C'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_22_44_666_888_DDDD': {
                        'name': '2468 22 44 666 888 DDDD',
                        'pattern': '22 44 666 888 DDDD',
                        'description': 'ALL MUST BE SUIT A WITH MATCHING DRAGON',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_matching_dragons',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 2, 'suit': 'A'},
                            {'type': 'number', 'value': 6, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 8, 'count': 3, 'suit': 'A'},
                            {'type': 'dragon', 'value': 'D', 'count': 4, 'matching': True}
                        ],
                        'total_tiles': 14
                    },
                    '2468_FFFF_4444_6666_24': {
                        'name': '2468 FFFF 4444 6666 24',
                        'pattern': 'FFFF 4444 6666 24',
                        'description': 'Three suits allowed',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'special_rules': ['24 means one 2-tile and one 4-tile'],
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 4},
                            {'type': 'number', 'value': 4, 'count': 4, 'suit': 'A'},
                            {'type': 'number', 'value': 6, 'count': 4, 'suit': 'B'},
                            {'type': 'number', 'value': 2, 'count': 1, 'suit': 'C'},
                            {'type': 'number', 'value': 4, 'count': 1, 'suit': 'C'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_FFFF_6666_8888_48': {
                        'name': '2468 FFFF 6666 8888 48',
                        'pattern': 'FFFF 6666 8888 48',
                        'description': 'Three suits allowed',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'special_rules': ['48 means one 4-tile and one 8-tile'],
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 4},
                            {'type': 'number', 'value': 6, 'count': 4, 'suit': 'A'},
                            {'type': 'number', 'value': 8, 'count': 4, 'suit': 'B'},
                            {'type': 'number', 'value': 4, 'count': 1, 'suit': 'C'},
                            {'type': 'number', 'value': 8, 'count': 1, 'suit': 'C'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_FF_2222_44_66_8888_same': {
                        'name': '2468 FF 2222 44 66 8888 (All Same)',
                        'pattern': 'FF 2222 44 66 8888',
                        'description': 'ALL SUIT A',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'number', 'value': 2, 'count': 4, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 2, 'suit': 'A'},
                            {'type': 'number', 'value': 6, 'count': 2, 'suit': 'A'},
                            {'type': 'number', 'value': 8, 'count': 4, 'suit': 'A'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_FF_2222_44_66_8888_mixed': {
                        'name': '2468 FF 2222 44 66 8888 (Mixed)',
                        'pattern': 'FF 2222 44 66 8888',
                        'description': 'Two suits allowed',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'number', 'value': 2, 'count': 4, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 2, 'suit': 'B'},
                            {'type': 'number', 'value': 6, 'count': 2, 'suit': 'B'},
                            {'type': 'number', 'value': 8, 'count': 4, 'suit': 'A'}
                        ],
                        'total_tiles': 14
                    },
                    '2468_FF_222_44_666_88_88': {
                        'name': '2468 FF 222 44 666 88 88',
                        'pattern': 'FF 222 44 666 88 88',
                        'description': 'Three suits allowed',
                        'points': 35,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 4, 'count': 2, 'suit': 'A'},
                            {'type': 'number', 'value': 6, 'count': 3, 'suit': 'A'},
                            {'type': 'number', 'value': 8, 'count': 2, 'suit': 'B'},
                            {'type': 'number', 'value': 8, 'count': 2, 'suit': 'C'}
                        ],
                        'total_tiles': 14
                                         }
                 },
                 
                 'any_like_numbers_patterns': {
                     'like_FFFF_111_1111_111': {
                         'name': 'Any Like Numbers FFFF 111 1111 111',
                         'pattern': 'FFFF 111 1111 111',
                         'description': 'Three suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can use any number 1-9 (all same number)'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 4},
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     'like_11_DDD_11_DDD_1111': {
                         'name': 'Any Like Numbers 11 DDD 11 DDD 1111',
                         'pattern': '11 DDD 11 DDD 1111',
                         'description': 'Three suits with matching dragons',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits_matching_dragons',
                         'joker_allowed': True,
                         'special_rules': ['Can use any number 1-9'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 3, 'matching': True},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'B'},
                             {'type': 'dragon', 'value': 'D', 'count': 3, 'matching': True},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     'like_FF_1111_NEWS_1111': {
                         'name': 'Any Like Numbers FF 1111 NEWS 1111',
                         'pattern': 'FF 1111 NEWS 1111',
                         'description': 'Two suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can use any number 1-9', 'NEWS means N-E-W-S (one of each wind)'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'A'},
                             {'type': 'wind', 'value': 'N', 'count': 1},
                             {'type': 'wind', 'value': 'E', 'count': 1},
                             {'type': 'wind', 'value': 'W', 'count': 1},
                             {'type': 'wind', 'value': 'S', 'count': 1},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 'addition_hands_patterns': {
                     'addition_FF_1111_6666_7777': {
                         'name': 'Addition FF 1111 6666 7777',
                         'pattern': 'FF 1111 6666 7777',
                         'description': 'ALL SUIT A',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Logic: 1111 + 6666 = 7777'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 7, 'count': 4, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'addition_FF_2222_5555_7777': {
                         'name': 'Addition FF 2222 5555 7777',
                         'pattern': 'FF 2222 5555 7777',
                         'description': 'ALL SUIT A',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Logic: 2222 + 5555 = 7777'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 2, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 7, 'count': 4, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'addition_FF_3333_4444_7777': {
                         'name': 'Addition FF 3333 4444 7777',
                         'pattern': 'FF 3333 4444 7777',
                         'description': 'ALL SUIT A',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Logic: 3333 + 4444 = 7777'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 7, 'count': 4, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 'quint_patterns': {
                     'quint_FF_11111_22_33333': {
                         'name': 'Quint FF 11111 22 33333',
                         'pattern': 'FF 11111 22 33333',
                         'description': 'ALL SUIT A, NUMBERS CAN BE ANY CONSECUTIVE NUMBERS',
                         'points': 40,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Consecutive Options: 123, 234, 345, 456, 567, 678, 789'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 1, 'count': 5, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 5, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'quint_11111_NNNN_88888': {
                         'name': 'Quint 11111 NNNN 88888',
                         'pattern': '11111 NNNN 88888',
                         'description': 'Two suits allowed',
                         'points': 40,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': False,
                         'special_rules': ['First number can be any 1-9', 'Second number must be different from first', 'Wind can be N, S, E, or W (all four same)'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 5, 'suit': 'A'},
                             {'type': 'wind', 'value': 'N', 'count': 4},
                             {'type': 'number', 'value': 8, 'count': 5, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'quint_11_22222_11_22222': {
                         'name': 'Quint 11 22222 11 22222',
                         'pattern': '11 22222 11 22222',
                         'description': 'Two suits allowed',
                         'points': 45,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': False,
                         'special_rules': ['Can be any consecutive numbers (12, 23, 34, 45, 56, 67, 78, 89)', 'SUIT A and SUIT B must use same numbers'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 5, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 2, 'count': 5, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'quint_FFFFF_DDDD_11111': {
                         'name': 'Quint FFFFF DDDD 11111',
                         'pattern': 'FFFFF DDDD 11111',
                         'description': 'Two suits allowed',
                         'points': 40,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Number can be any 1-9', 'Dragons must match SUIT A'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 5},
                             {'type': 'dragon', 'value': 'D', 'count': 4, 'matching': True},
                             {'type': 'number', 'value': 1, 'count': 5, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 'consecutive_run_patterns': {
                     'consec_111_22_3333_44_555': {
                         'name': 'Consecutive 111 22 3333 44 555 (Fixed Numbers)',
                         'pattern': '111 22 3333 44 555',
                         'description': 'ALL SUIT A',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Must use these exact number sequences only'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 3, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_11_222_DDDD_333_44': {
                         'name': 'Consecutive 11 222 DDDD 333 44',
                         'pattern': '11 222 DDDD 333 44',
                         'description': 'SUIT A + SUIT B dragons',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit_opposite_dragons',
                         'joker_allowed': True,
                         'special_rules': ['SUIT A can be any 4 consecutive numbers (1234, 2345, 3456, 4567, 5678, 6789)'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 4, 'opposite': True},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 2, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_FF_1111_2222_3333_same': {
                         'name': 'Consecutive FF 1111 2222 3333 (Same Suit)',
                         'pattern': 'FF 1111 2222 3333',
                         'description': 'ALL SUIT A',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 3 consecutive numbers (123, 234, 345, 456, 567, 678, 789)'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_FF_1111_2222_3333_diff': {
                         'name': 'Consecutive FF 1111 2222 3333 (Different Suits)',
                         'pattern': 'FF 1111 2222 3333',
                         'description': 'Three different suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 3 consecutive numbers'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_1_22_3333_1_22_3333': {
                         'name': 'Consecutive 1 22 3333 1 22 3333',
                         'pattern': '1 22 3333 1 22 3333',
                         'description': 'Two suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 3 consecutive numbers, SUIT A and B must use same numbers'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_11_22_333_444_DDDD': {
                         'name': 'Consecutive 11 22 333 444 DDDD',
                         'pattern': '11 22 333 444 DDDD',
                         'description': 'ALL SUIT A, INCLUDING SUIT A MATCHING DRAGONS',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit_matching_dragons',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 4 consecutive numbers (1234, 2345, 3456, 4567, 5678, 6789)'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 3, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 4, 'matching': True}
                         ],
                         'total_tiles': 14
                     },
                     'consec_FFFF_123_444_444': {
                         'name': 'Consecutive FFFF 123 444 444',
                         'pattern': 'FFFF 123 444 444',
                         'description': 'Three suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 4 consecutive numbers, SUIT A must be first 3 numbers, SUIT B and C must be the 4th number'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 4},
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 3, 'suit': 'B'},
                             {'type': 'number', 'value': 4, 'count': 3, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_111_222_3333_4444_same': {
                         'name': 'Consecutive 111 222 3333 4444 (Same Suit)',
                         'pattern': '111 222 3333 4444',
                         'description': 'ALL SUIT A',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 4 consecutive numbers'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 4, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_111_222_3333_4444_two': {
                         'name': 'Consecutive 111 222 3333 4444 (Two Suits)',
                         'pattern': '111 222 3333 4444',
                         'description': 'Two suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 4 consecutive numbers'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 4, 'count': 4, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'consec_111_222_111_222_33': {
                         'name': 'Consecutive 111 222 111 222 33',
                         'pattern': '111 222 111 222 33',
                         'description': 'Three suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 3 consecutive numbers, SUIT A and B must use same numbers'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'B'},
                             {'type': 'number', 'value': 2, 'count': 3, 'suit': 'B'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 '13579_patterns': {
                     '13579_111_33_5555_77_999_same': {
                         'name': '13579 111 33 5555 77 999 (Same Suit)',
                         'pattern': '111 33 5555 77 999',
                         'description': 'ALL SUIT A',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Must use odd numbers 1,3,5,7,9'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 7, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 9, 'count': 3, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     '13579_111_33_5555_77_999_mixed': {
                         'name': '13579 111 33 5555 77 999 (Mixed Suits)',
                         'pattern': '111 33 5555 77 999',
                         'description': 'Three suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Must use odd numbers 1,3,5,7,9'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 7, 'count': 2, 'suit': 'C'},
                             {'type': 'number', 'value': 9, 'count': 3, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     '13579_111_333_3333_5555': {
                         'name': '13579 111 333 3333 5555',
                         'pattern': '111 333 3333 5555',
                         'description': 'Two suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Must use consecutive odd numbers'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 5, 'count': 4, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     '13579_FF_11_333_5555_DDD': {
                         'name': '13579 FF 11 333 5555 DDD',
                         'pattern': 'FF 11 333 5555 DDD',
                         'description': 'ALL SUIT A, WITH MATCHING SUIT A DRAGONS',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit_matching_dragons',
                         'joker_allowed': True,
                         'special_rules': ['Must use odd numbers with matching dragons'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 4, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 3, 'matching': True}
                         ],
                         'total_tiles': 14
                     },
                     '13579_11_33_55_7777_9999': {
                         'name': '13579 11 33 55 7777 9999',
                         'pattern': '11 33 55 7777 9999',
                         'description': 'Three suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Must use all odd numbers 1,3,5,7,9'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 7, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 9, 'count': 4, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     '13579_FFFF_3333_5555_15': {
                         'name': '13579 FFFF 3333 5555 15',
                         'pattern': 'FFFF 3333 5555 15',
                         'description': 'Three suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['15 means one 1-tile and one 5-tile'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 4},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'C'},
                             {'type': 'number', 'value': 5, 'count': 1, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 'winds_dragons_patterns': {
                     'winds_NNNN_EEE_WWW_SSSS': {
                         'name': 'Winds NNNN EEE WWW SSSS',
                         'pattern': 'NNNN EEE WWW SSSS',
                         'description': 'All four winds in specified groupings',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'components': [
                             {'type': 'wind', 'value': 'N', 'count': 4},
                             {'type': 'wind', 'value': 'E', 'count': 3},
                             {'type': 'wind', 'value': 'W', 'count': 3},
                             {'type': 'wind', 'value': 'S', 'count': 4}
                         ],
                         'total_tiles': 14
                     },
                     'winds_FFFF_DDD_DDDD_DDD': {
                         'name': 'Winds FFFF DDD DDDD DDD',
                         'pattern': 'FFFF DDD DDDD DDD',
                         'description': 'Three different dragon suits',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_3_dragons',
                         'joker_allowed': True,
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 4},
                             {'type': 'dragon', 'value': 'D', 'count': 3},
                             {'type': 'dragon', 'value': 'D', 'count': 4},
                             {'type': 'dragon', 'value': 'D', 'count': 3}
                         ],
                         'total_tiles': 14
                     },
                     'winds_NNN_SSS_1111_2222': {
                         'name': 'Winds NNN SSS 1111 2222',
                         'pattern': 'NNN SSS 1111 2222',
                         'description': 'Two suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 2 consecutive numbers'],
                         'components': [
                             {'type': 'wind', 'value': 'N', 'count': 3},
                             {'type': 'wind', 'value': 'S', 'count': 3},
                             {'type': 'number', 'value': 1, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 4, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'winds_FF_NN_EEE_WWW_SSSS': {
                         'name': 'Winds FF NN EEE WWW SSSS',
                         'pattern': 'FF NN EEE WWW SSSS',
                         'description': 'Mixed winds with flowers',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'wind', 'value': 'N', 'count': 2},
                             {'type': 'wind', 'value': 'E', 'count': 3},
                             {'type': 'wind', 'value': 'W', 'count': 3},
                             {'type': 'wind', 'value': 'S', 'count': 4}
                         ],
                         'total_tiles': 14
                     },
                     'winds_NNNN_11_22_33_SSSS': {
                         'name': 'Winds NNNN 11 22 33 SSSS',
                         'pattern': 'NNNN 11 22 33 SSSS',
                         'description': 'ALL SUIT A',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit',
                         'joker_allowed': True,
                         'special_rules': ['Can be any 3 consecutive numbers'],
                         'components': [
                             {'type': 'wind', 'value': 'N', 'count': 4},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'wind', 'value': 'S', 'count': 4}
                         ],
                         'total_tiles': 14
                     },
                     'winds_FF_DDDD_NEWS_DDDD': {
                         'name': 'Winds FF DDDD NEWS DDDD',
                         'pattern': 'FF DDDD NEWS DDDD',
                         'description': 'Two different dragon suits',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_dragons',
                         'joker_allowed': True,
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'dragon', 'value': 'D', 'count': 4},
                             {'type': 'wind', 'value': 'N', 'count': 1},
                             {'type': 'wind', 'value': 'E', 'count': 1},
                             {'type': 'wind', 'value': 'W', 'count': 1},
                             {'type': 'wind', 'value': 'S', 'count': 1},
                             {'type': 'dragon', 'value': 'D', 'count': 4}
                         ],
                         'total_tiles': 14
                     },
                     'winds_NNN_EW_SSS_111_111': {
                         'name': 'Winds NNN EW SSS 111 111',
                         'pattern': 'NNN EW SSS 111 111',
                         'description': 'Two suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be any like numbers 1-9, SUIT A and B must be same number'],
                         'components': [
                             {'type': 'wind', 'value': 'N', 'count': 3},
                             {'type': 'wind', 'value': 'E', 'count': 1},
                             {'type': 'wind', 'value': 'W', 'count': 1},
                             {'type': 'wind', 'value': 'S', 'count': 3},
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 3, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 '369_patterns': {
                     '369_333_666_6666_9999': {
                         'name': '369 333 666 6666 9999',
                         'pattern': '333 666 6666 9999',
                         'description': 'Two/Three Suits',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_or_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Must use numbers 3, 6, 9'],
                         'components': [
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 9, 'count': 4, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     '369_FF_3_66_999_333_333': {
                         'name': '369 FF 3 66 999 333 333',
                         'pattern': 'FF 3 66 999 333 333',
                         'description': 'Three suits allowed',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Like pungs of 3, 6, or 9'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 3, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 9, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'B'},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     '369_FF_3333_6666_9999': {
                         'name': '369 FF 3333 6666 9999',
                         'pattern': 'FF 3333 6666 9999',
                         'description': 'ALL SUIT A or Three different suits',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_or_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Can be all same suit or three different suits'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2},
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 4, 'suit': 'B'},
                             {'type': 'number', 'value': 9, 'count': 4, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     '369_333_DDDD_333_DDDD': {
                         'name': '369 333 DDDD 333 DDDD',
                         'pattern': '333 DDDD 333 DDDD',
                         'description': 'Two suits with matching dragons',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_2_suits_matching_dragons',
                         'joker_allowed': True,
                         'special_rules': ['Pungs of 3, 6, or 9 with matching dragons, SUIT A and B numbers must be same'],
                         'components': [
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 4, 'matching': True},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'B'},
                             {'type': 'dragon', 'value': 'D', 'count': 4, 'matching': True}
                         ],
                         'total_tiles': 14
                     },
                     '369_3333_66_66_66_9999': {
                         'name': '369 3333 66 66 66 9999',
                         'pattern': '3333 66 66 66 9999',
                         'description': 'Three suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['3s and 9s must match (same suit)'],
                         'components': [
                             {'type': 'number', 'value': 3, 'count': 4, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 6, 'count': 2, 'suit': 'C'},
                             {'type': 'number', 'value': 9, 'count': 4, 'suit': 'A'}
                         ],
                         'total_tiles': 14
                     },
                     '369_FFFF_33_66_999_DDD': {
                         'name': '369 FFFF 33 66 999 DDD',
                         'pattern': 'FFFF 33 66 999 DDD',
                         'description': 'Numbers any 1 suit, any opposite dragon',
                         'points': 25,
                         'category': 'X',
                         'suit_requirement': 'any_1_suit_opposite_dragons',
                         'joker_allowed': True,
                         'special_rules': ['Numbers any 1 suit, any opposite dragon'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 4},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 9, 'count': 3, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 3, 'opposite': True}
                         ],
                         'total_tiles': 14
                     },
                     '369_333_666_333_666_99': {
                         'name': '369 333 666 333 666 99',
                         'pattern': '333 666 333 666 99',
                         'description': 'Three suits allowed',
                         'points': 30,
                         'category': 'X',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': True,
                         'special_rules': ['Must use numbers 3, 6, 9'],
                         'components': [
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 3, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 3, 'suit': 'B'},
                             {'type': 'number', 'value': 6, 'count': 3, 'suit': 'B'},
                             {'type': 'number', 'value': 9, 'count': 2, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     }
                 },
                 
                 'singles_and_pairs_patterns': {
                     'singles_FF_22_46_88_22_46_88': {
                         'name': 'Singles FF 22 46 88 22 46 88',
                         'pattern': 'FF 22 46 88 22 46 88',
                         'description': 'Two suits allowed',
                         'points': 50,
                         'category': 'C',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': False,
                         'special_rules': ['Specific numbers 2, 4, 6, 8 only', 'NO FLOWERS ALLOWED despite "FF" notation'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2, 'not_allowed': True},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 8, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 4, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 6, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 8, 'count': 2, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'singles_FF_11_33_55_55_77_99': {
                         'name': 'Singles FF 11 33 55 55 77 99',
                         'pattern': 'FF 11 33 55 55 77 99',
                         'description': 'Two suits allowed',
                         'points': 50,
                         'category': 'C',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': False,
                         'special_rules': ['Odd numbers only', 'NO FLOWERS ALLOWED despite "FF" notation'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2, 'not_allowed': True},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 7, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 9, 'count': 2, 'suit': 'B'}
                         ],
                         'total_tiles': 14
                     },
                     'singles_112_11223_112233': {
                         'name': 'Singles 112 11223 112233',
                         'pattern': '112 11223 112233',
                         'description': 'Three suits required',
                         'points': 50,
                         'category': 'C',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': False,
                         'special_rules': ['Specific number patterns only'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 1, 'suit': 'A'},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'B'},
                             {'type': 'number', 'value': 3, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'C'},
                             {'type': 'number', 'value': 1, 'count': 1, 'suit': 'C'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'C'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     'singles_FF_33_66_99_369_369': {
                         'name': 'Singles FF 33 66 99 369 369',
                         'pattern': 'FF 33 66 99 369 369',
                         'description': 'Three suits allowed',
                         'points': 50,
                         'category': 'C',
                         'suit_requirement': 'any_3_suits',
                         'joker_allowed': False,
                         'special_rules': ['Must use 3, 6, 9 pattern', 'NO FLOWERS ALLOWED despite "FF" notation'],
                         'components': [
                             {'type': 'flower', 'value': 'F', 'count': 2, 'not_allowed': True},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 6, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 9, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 6, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 9, 'count': 1, 'suit': 'B'},
                             {'type': 'number', 'value': 3, 'count': 1, 'suit': 'C'},
                             {'type': 'number', 'value': 6, 'count': 1, 'suit': 'C'},
                             {'type': 'number', 'value': 9, 'count': 1, 'suit': 'C'}
                         ],
                         'total_tiles': 14
                     },
                     'singles_11_22_33_44_55_DD_DD': {
                         'name': 'Singles 11 22 33 44 55 DD DD',
                         'pattern': '11 22 33 44 55 DD DD',
                         'description': 'SUIT A + two different dragon suits',
                         'points': 50,
                         'category': 'C',
                         'suit_requirement': 'any_1_suit_opposite_dragons',
                         'joker_allowed': False,
                         'special_rules': ['Can be any 5 consecutive numbers (12345, 23456, 34567, 45678, 56789)'],
                         'components': [
                             {'type': 'number', 'value': 1, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 2, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 3, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 4, 'count': 2, 'suit': 'A'},
                             {'type': 'number', 'value': 5, 'count': 2, 'suit': 'A'},
                             {'type': 'dragon', 'value': 'D', 'count': 2, 'opposite': True},
                             {'type': 'dragon', 'value': 'D', 'count': 2, 'opposite': True}
                         ],
                         'total_tiles': 14
                     },
                     'singles_2024_NN_EW_SS_2024': {
                         'name': 'Singles 2024 NN EW SS 2024',
                         'pattern': '2024 NN EW SS 2024',
                         'description': 'Two suits allowed',
                         'points': 75,
                         'category': 'C',
                         'suit_requirement': 'any_2_suits',
                         'joker_allowed': False,
                         'special_rules': ['In both 2024s, the 0 must be White Dragon'],
                         'components': [
                             {'type': 'year', 'value': '2024', 'count': 1, 'special': 'white_dragon_0'},
                             {'type': 'wind', 'value': 'N', 'count': 2},
                             {'type': 'wind', 'value': 'E', 'count': 1},
                             {'type': 'wind', 'value': 'W', 'count': 1},
                             {'type': 'wind', 'value': 'S', 'count': 2},
                             {'type': 'year', 'value': '2024', 'count': 1, 'special': 'white_dragon_0'}
                         ],
                         'total_tiles': 14
                     }
                 }
             }
         }
    
    def get_pattern_by_id(self, pattern_id: str, year: int = 2024) -> Dict[str, Any]:
        """Get a specific pattern by its ID"""
        year_patterns = self.year_patterns.get(year, {})
        for category in year_patterns.values():
            if pattern_id in category:
                return category[pattern_id]
        return None
    
    def get_all_patterns(self, year: int = 2024) -> Dict[str, Dict[str, Any]]:
        """Get all patterns for a specific year"""
        year_patterns = self.year_patterns.get(year, {})
        all_patterns = {}
        for category_name, category_patterns in year_patterns.items():
            all_patterns.update(category_patterns)
        return all_patterns
    
    def get_patterns_by_category(self, category: str, year: int = 2024) -> Dict[str, Dict[str, Any]]:
        """Get all patterns in a specific category"""
        year_patterns = self.year_patterns.get(year, {})
        category_key = f"{category}_patterns"
        return year_patterns.get(category_key, {})
    
    def validate_suit_requirement(self, tiles: List[str], requirement: str) -> bool:
        """Validate if tiles meet a specific suit requirement"""
        # Implementation would go here
        pass
    
    def get_suit_requirement_info(self, requirement: str) -> Dict[str, Any]:
        """Get detailed information about a suit requirement"""
        return self.suit_requirements.get(requirement, {})

# Global instance
mahjong_rules = MahjongRules() 