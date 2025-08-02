"""
American Mahjong Rules Specification
Comprehensive rules and pattern definitions for American Mahjong
"""

from typing import Dict, List, Any

class MahjongRules:
    """Comprehensive American Mahjong rules specification"""
    
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
        
        # 2024 Pattern Definitions
        self.year_patterns = {
            2024: {
                '2024_patterns': {
                    '2024_222_000_2222_4444': {
                        'name': '2024 222 000 2222 4444',
                        'pattern': '222 000 2222 4444',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 3},
                            {'type': 'dragon', 'value': '0', 'count': 3},
                            {'type': 'number', 'value': 2, 'count': 4},
                            {'type': 'number', 'value': 4, 'count': 4}
                        ],
                        'total_tiles': 14,
                        'notes': 'Uses White Dragon (0) and numbers 2 and 4'
                    },
                    '2024_FFFF_2222_0000_24': {
                        'name': '2024 FFFF 2222 0000 24',
                        'pattern': 'FFFF 2222 0000 24',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 4},
                            {'type': 'number', 'value': 2, 'count': 4},
                            {'type': 'dragon', 'value': '0', 'count': 4},
                            {'type': 'number', 'value': 2, 'count': 1},
                            {'type': 'number', 'value': 4, 'count': 1}
                        ],
                        'total_tiles': 14,
                        'notes': 'Heavy use of flowers and White Dragons'
                    },
                    '2024_FF_2024_2222_2222': {
                        'name': '2024 FF 2024 2222 2222',
                        'pattern': 'FF 2024 2222 2222',
                        'description': 'Any 3 Suits, Like Kongs 2s or 4s',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'like_kongs': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'year', 'value': '2024', 'count': 1},
                            {'type': 'number', 'value': 2, 'count': 4},
                            {'type': 'number', 'value': 2, 'count': 4},
                            {'type': 'number', 'value': 2, 'count': 2}
                        ],
                        'total_tiles': 14,
                        'notes': 'Like Kongs means all 2s must be same number'
                    },
                    '2024_NN_EEE_2024_WWW_SS': {
                        'name': '2024 NN EEE 2024 WWW SS',
                        'pattern': 'NN EEE 2024 WWW SS',
                        'description': '2024 Any 1 Suit',
                        'points': 30,
                        'category': 'C',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': False,
                        'components': [
                            {'type': 'wind', 'value': 'N', 'count': 2},
                            {'type': 'wind', 'value': 'E', 'count': 3},
                            {'type': 'year', 'value': '2024', 'count': 1},
                            {'type': 'wind', 'value': 'W', 'count': 3},
                            {'type': 'wind', 'value': 'S', 'count': 2}
                        ],
                        'total_tiles': 14,
                        'notes': 'Concealed hand with all winds and year tile'
                    }
                },
                
                '2468_patterns': {
                    '2468_222_444_6666_8888': {
                        'name': '2468 222 444 6666 8888',
                        'pattern': '222 444 6666 8888',
                        'description': 'Any 1 or 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_2_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 3},
                            {'type': 'number', 'value': 4, 'count': 3},
                            {'type': 'number', 'value': 6, 'count': 4},
                            {'type': 'number', 'value': 8, 'count': 4}
                        ],
                        'total_tiles': 14,
                        'notes': 'Even numbers only: 2,4,6,8'
                    },
                    '2468_22_44_666_888_DDDD': {
                        'name': '2468 22 44 666 888 DDDD',
                        'pattern': '22 44 666 888 DDDD',
                        'description': 'Any 1 Suit w Matching Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_matching_dragons',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 2, 'count': 2},
                            {'type': 'number', 'value': 4, 'count': 2},
                            {'type': 'number', 'value': 6, 'count': 3},
                            {'type': 'number', 'value': 8, 'count': 3},
                            {'type': 'dragon', 'value': 'D', 'count': 4}
                        ],
                        'total_tiles': 14,
                        'notes': 'Dragons must match the suit being used'
                    }
                },
                
                'wind_patterns': {
                    'winds_NNNN_EEE_WWW_SSSS': {
                        'name': 'Winds NNNN EEE WWW SSSS',
                        'pattern': 'NNNN EEE WWW SSSS',
                        'description': 'Any 2 Suits',
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
                        'total_tiles': 14,
                        'notes': 'All 4 winds in different quantities'
                    },
                    'winds_FFFF_DDD_DDDD_DDD': {
                        'name': 'Winds FFFF DDD DDDD DDD',
                        'pattern': 'FFFF DDD DDDD DDD',
                        'description': 'Any 3 Dragons',
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
                        'total_tiles': 14,
                        'notes': 'Must use all 3 dragon types (R,G,0)'
                    }
                },
                
                'consecutive_patterns': {
                    'consec_111_22_3333_44_555': {
                        'name': 'Consecutive 111 22 3333 44 555',
                        'pattern': '111 22 3333 44 555',
                        'description': 'These Nos. Only',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'specific_numbers',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'number', 'value': 1, 'count': 3},
                            {'type': 'number', 'value': 2, 'count': 2},
                            {'type': 'number', 'value': 3, 'count': 4},
                            {'type': 'number', 'value': 4, 'count': 2},
                            {'type': 'number', 'value': 5, 'count': 3}
                        ],
                        'total_tiles': 14,
                        'notes': 'Consecutive numbers 1-5 in specific quantities'
                    },
                    'consec_FF_1111_2222_3333': {
                        'name': 'Consecutive FF 1111 2222 3333',
                        'pattern': 'FF 1111 2222 3333',
                        'description': 'Any 1 or 3 Suits, Any 3 Consec. Nos',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_3_suits',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'number', 'value': 1, 'count': 4},
                            {'type': 'number', 'value': 2, 'count': 4},
                            {'type': 'number', 'value': 3, 'count': 4}
                        ],
                        'total_tiles': 14,
                        'notes': 'Any 3 consecutive numbers (could be 1-2-3, 2-3-4, etc.)'
                    }
                },
                
                'quint_patterns': {
                    'quint_FF_11111_22_33333': {
                        'name': 'Quint FF 11111 22 33333',
                        'pattern': 'FF 11111 22 33333',
                        'description': 'Any 1 Suit, Any 3 Consec. Nos.',
                        'points': 40,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'number', 'value': 1, 'count': 5},
                            {'type': 'number', 'value': 2, 'count': 2},
                            {'type': 'number', 'value': 3, 'count': 5}
                        ],
                        'total_tiles': 14,
                        'notes': 'Quint means 5 of the same tile (11111 = 5 ones)'
                    }
                },
                
                'singles_and_pairs': {
                    'singles_FF_22_46_88_22_46_88': {
                        'name': 'Singles FF 22 46 88 22 46 88',
                        'pattern': 'FF 22 46 88 22 46 88',
                        'description': 'Any 2 Suits',
                        'points': 50,
                        'category': 'C',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': False,
                        'components': [
                            {'type': 'flower', 'value': 'F', 'count': 2},
                            {'type': 'number', 'value': 2, 'count': 2},
                            {'type': 'number', 'value': 4, 'count': 1},
                            {'type': 'number', 'value': 6, 'count': 1},
                            {'type': 'number', 'value': 8, 'count': 2},
                            {'type': 'number', 'value': 2, 'count': 2},
                            {'type': 'number', 'value': 4, 'count': 1},
                            {'type': 'number', 'value': 6, 'count': 1},
                            {'type': 'number', 'value': 8, 'count': 2}
                        ],
                        'total_tiles': 14,
                        'notes': 'Singles and Pairs - no jokers allowed'
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