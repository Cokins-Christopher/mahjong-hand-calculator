"""
American Mahjong Hand Evaluator
Implements comprehensive logic for evaluating American Mahjong hands including
hand patterns and scoring based on year-specific rules.
"""

from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Set, Optional
import logging
import re

logger = logging.getLogger(__name__)

class HandEvaluator:
    """Evaluates American Mahjong hands for patterns and scoring"""
    
    def __init__(self):
        # Define all valid American Mahjong tiles
        self.valid_tiles = {
            'bams': [f"{i}B" for i in range(1, 10)],  # 1B-9B (Bamboo)
            'cracks': [f"{i}C" for i in range(1, 10)],  # 1C-9C (Characters)
            'dots': [f"{i}D" for i in range(1, 10)],  # 1D-9D (Circles)
            'winds': ['E', 'S', 'W', 'N'],  # East, South, West, North
            'dragons': ['R', 'G', '0'],  # Red, Green, White Dragons
            'flowers': ['F'],  # Flowers (Jokers)
            'year_tiles': ['2024']  # Year-specific tiles
        }
        
        # Dragon associations for matching
        self.dragon_associations = {
            'C': 'R',  # Cracks/Characters match Red Dragon
            'B': 'G',  # Bams/Bamboo match Green Dragon
            'D': '0'   # Dots/Circles match White Dragon
        }
        
        # 2024 American Mahjong Rules
        self.year_rules = {
            2024: {
                'patterns': {
                    # 2024 Patterns (25 points each unless noted)
                    '2024_222_000_2222_4444': {
                        'pattern': '222 000 2222 4444',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    '2024_FFFF_2222_0000_24': {
                        'pattern': 'FFFF 2222 0000 24',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    '2024_FF_2024_2222_2222': {
                        'pattern': 'FF 2024 2222 2222',
                        'description': 'Any 3 Suits, Like Kongs 2s or 4s',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'like_kongs': True
                    },
                    '2024_NN_EEE_2024_WWW_SS': {
                        'pattern': 'NN EEE 2024 WWW SS',
                        'description': '2024 Any 1 Suit',
                        'points': 30,
                        'category': 'C',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': False
                    },
                    
                    # 2468 Patterns
                    '2468_222_444_6666_8888': {
                        'pattern': '222 444 6666 8888',
                        'description': 'Any 1 or 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_2_suits',
                        'joker_allowed': True
                    },
                    '2468_2_444_44_666_8888': {
                        'pattern': '2 444 44 666 8888',
                        'description': 'Any 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    '2468_22_44_666_888_DDDD': {
                        'pattern': '22 44 666 888 DDDD',
                        'description': 'Any 1 Suit w Matching Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_matching_dragons',
                        'joker_allowed': True
                    },
                    '2468_FFFF_4444_666_6666': {
                        'pattern': 'FFFF 4444 666 6666',
                        'description': 'Any 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    '2468_FF_2222_44_66_8888': {
                        'pattern': 'FF 2222 44 66 8888',
                        'description': 'Any 1 or 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_2_suits',
                        'joker_allowed': True
                    },
                    '2468_FF_222_44_666_88_88': {
                        'pattern': 'FF 222 44 666 88 88',
                        'description': 'Any 3 Suits',
                        'points': 35,
                        'category': 'C',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    
                    # Any Like Numbers
                    'like_FFFF_111_1111_111': {
                        'pattern': 'FFFF 111 1111 111',
                        'description': 'Any 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    'like_11_DDD_11_DDD_1111': {
                        'pattern': '11 DDD 11 DDD 1111',
                        'description': 'Any 2 Suits, Pairs and Dragons Match',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits_matching_dragons',
                        'joker_allowed': True
                    },
                    'like_FF_1111_NEWS_1111': {
                        'pattern': 'FF 1111 NEWS 1111',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    
                    # Addition Hands (Lucky Sevens)
                    'addition_FF_1111_6666_7777': {
                        'pattern': 'FF 1111 + 6666 = 7777',
                        'description': 'Any 1 Suit',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True
                    },
                    'addition_FF_2222_5555_7777': {
                        'pattern': 'FF 2222 + 5555 = 7777',
                        'description': 'Any 1 Suit',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True
                    },
                    'addition_FF_3333_4444_7777': {
                        'pattern': 'FF 3333 + 4444 = 7777',
                        'description': 'Any 1 Suit',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True
                    },
                    
                    # Quints (40-45 points)
                    'quint_FF_11111_22_33333': {
                        'pattern': 'FF 11111 22 33333',
                        'description': 'Any 1 Suit, Any 3 Consec. Nos.',
                        'points': 40,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True
                    },
                    'quint_11111_NNNN_88888': {
                        'pattern': '11111 NNNN 88888',
                        'description': 'Any 2 Suits, Quints Any 2 Non-Matching Nos., Any Wind',
                        'points': 40,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': False
                    },
                    'quint_11_22222_11_22222': {
                        'pattern': '11 22222 11 22222',
                        'description': 'Any 2 Suits, Any 2 Consec. Nos.',
                        'points': 45,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': False
                    },
                    'quint_FFFFF_DDDD_11111': {
                        'pattern': 'FFFFF DDDD 11111',
                        'description': 'Any 2 Suits, Quint Any No.',
                        'points': 40,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    
                    # Consecutive Run
                    'consec_111_22_3333_44_555': {
                        'pattern': '111 22 3333 44 555',
                        'description': 'These Nos. Only',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'specific_numbers',
                        'joker_allowed': True,
                        'specific_numbers': [1, 2, 3, 4, 5]
                    },
                    'consec_11_222_DDDD_333_44': {
                        'pattern': '11 222 DDDD 333 44',
                        'description': 'Any 4 Consec. Nos. in Any 1 Suit, Kong Opp. Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_opposite_dragons',
                        'joker_allowed': True
                    },
                    'consec_FF_1111_2222_3333': {
                        'pattern': 'FF 1111 2222 3333',
                        'description': 'Any 1 or 3 Suits, Any 3 Consec. Nos',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_3_suits',
                        'joker_allowed': True
                    },
                    'consec_1_22_3333_1_22_3333': {
                        'pattern': '1 22 3333 1 22 3333',
                        'description': 'Any 2 Suits, Any 3 Consec. Nos.',
                        'points': 30,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    'consec_11_22_333_444_DDDD': {
                        'pattern': '11 22 333 444 DDDD',
                        'description': 'Any 1 Suit, Any 4 Consec. Nos. w Matching Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_matching_dragons',
                        'joker_allowed': True
                    },
                    'consec_FFFFF_123_444_444': {
                        'pattern': 'FFFFF 123 444 444',
                        'description': 'Any 3 Suits, Any 4 Consec. Nos.',
                        'points': 30,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    'consec_111_222_3333_4444': {
                        'pattern': '111 222 3333 4444',
                        'description': 'Any 1 or 2 Suits, Any 4 Consec. Nos.',
                        'points': 30,
                        'category': 'C',
                        'suit_requirement': 'any_1_or_2_suits',
                        'joker_allowed': True
                    },
                    'consec_111_222_111_222_33': {
                        'pattern': '111 222 111 222 33',
                        'description': 'Any 3 Suits, Any 3 Consec. Nos.',
                        'points': 30,
                        'category': 'C',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    
                    # 13579 Patterns
                    '13579_111_33_5555_77_999': {
                        'pattern': '111 33 5555 77 999',
                        'description': 'Any 1 or 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_3_suits',
                        'joker_allowed': True
                    },
                    '13579_111_333_3333_5555': {
                        'pattern': '111 333 3333 5555',
                        'description': 'Any 2 or 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_or_3_suits',
                        'joker_allowed': True
                    },
                    '13579_FF_11_333_5555_DDD': {
                        'pattern': 'FF 11 333 5555 DDD',
                        'description': 'Any 1 Suit w Matching Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_matching_dragons',
                        'joker_allowed': True
                    },
                    '13579_11_33_55_7777_9999': {
                        'pattern': '11 33 55 7777 9999',
                        'description': 'Any 3 Suits',
                        'points': 30,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    '13579_FFFF_3333_5555': {
                        'pattern': 'FFFF 3333 x 5555 = 15',
                        'description': 'Any 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    '13579_11_33_333_555_DDDD': {
                        'pattern': '11 33 333 555 DDDD',
                        'description': 'Any 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    '13579_111_33_555_333_333': {
                        'pattern': '111 33 555 333 333',
                        'description': 'Any 3 Suits, These Nos. Only',
                        'points': 35,
                        'category': 'C',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'specific_numbers': [1, 3, 5]
                    },
                    
                    # Winds - Dragons (25-30 points)
                    'winds_NNNN_EEE_WWW_SSSS': {
                        'pattern': 'NNNN EEE WWW SSSS',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    'winds_FFFF_DDD_DDDD_DDD': {
                        'pattern': 'FFFF DDD DDDD DDD',
                        'description': 'Any 3 Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_dragons',
                        'joker_allowed': True
                    },
                    'winds_NNN_SSS_1111_2222': {
                        'pattern': 'NNN SSS 1111 2222',
                        'description': 'Any 2 Suits, Any 2 Consec. Nos.',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    'winds_FF_NN_EEE_WWW_SSSS': {
                        'pattern': 'FF NN EEE WWW SSSS',
                        'description': 'Any 2 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    'winds_NNNN_11_22_33_SSSS': {
                        'pattern': 'NNNN 11 22 33 SSSS',
                        'description': 'Any 1 Suit, Any 3 Consec. Nos.',
                        'points': 30,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit',
                        'joker_allowed': True
                    },
                    'winds_FF_DDDD_NEWS_DDDD': {
                        'pattern': 'FF DDDD NEWS DDDD',
                        'description': 'Any 2 Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_dragons',
                        'joker_allowed': True
                    },
                    'winds_NNN_EW_SSS_111_111': {
                        'pattern': 'NNN EW SSS 111 111',
                        'description': 'Any 2 Suits, Any Like Nos.',
                        'points': 30,
                        'category': 'C',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': True
                    },
                    
                    # 369 Patterns
                    '369_333_666_6666_9999': {
                        'pattern': '333 666 6666 9999',
                        'description': 'Any 2 or 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_or_3_suits',
                        'joker_allowed': True
                    },
                    '369_FF_3_66_999_333_333': {
                        'pattern': 'FF 3 66 999 333 333',
                        'description': 'Any 3 Suits, Like Pungs 3, 6 or 9',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'like_pungs': True
                    },
                    '369_FF_333_666_9999': {
                        'pattern': 'FF 333 666 9999',
                        'description': 'Any 1 or 3 Suits',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_or_3_suits',
                        'joker_allowed': True
                    },
                    '369_333_DDDD_333_DDDD': {
                        'pattern': '333 DDDD 333 DDDD',
                        'description': 'Any 2 Suits, Pungs 3, 6 or 9 w Matching Dragons',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_2_suits_matching_dragons',
                        'joker_allowed': True
                    },
                    '369_3333_66_66_66_9999': {
                        'pattern': '3333 66 66 66 9999',
                        'description': 'Any 3 Suits, 3s and 9s Match',
                        'points': 30,
                        'category': 'X',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True,
                        'matching_numbers': [3, 9]
                    },
                    '369_FFFF_33_66_999_DDD': {
                        'pattern': 'FFFF 33 66 999 DDD',
                        'description': 'Nos. Any 1 Suit, Any Opp. Dragon',
                        'points': 25,
                        'category': 'X',
                        'suit_requirement': 'any_1_suit_opposite_dragons',
                        'joker_allowed': True
                    },
                    '369_333_666_333_666_99': {
                        'pattern': '333 666 333 666 99',
                        'description': 'Any 3 Suits',
                        'points': 30,
                        'category': 'C',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': True
                    },
                    
                    # Singles and Pairs (50-75 points)
                    'singles_FF_22_46_88_22_46_88': {
                        'pattern': 'FF 22 46 88 22 46 88',
                        'description': 'Any 2 Suits',
                        'points': 50,
                        'category': 'C',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': False  # No jokers in Singles and Pairs
                    },
                    'singles_FF_11_33_55_55_77_99': {
                        'pattern': 'FF 11 33 55 55 77 99',
                        'description': 'Any 2 Suits',
                        'points': 50,
                        'category': 'C',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': False
                    },
                    'singles_11_21123_112233': {
                        'pattern': '11 21123 112233',
                        'description': 'Any 3 Suits, These Nos. Only',
                        'points': 50,
                        'category': 'C',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': False,
                        'specific_numbers': [1, 2, 3]
                    },
                    'singles_FF_33_66_99_369_369': {
                        'pattern': 'FF 33 66 99 369 369',
                        'description': 'Any 3 Suits',
                        'points': 50,
                        'category': 'C',
                        'suit_requirement': 'any_3_suits',
                        'joker_allowed': False
                    },
                    'singles_11_22_33_44_55_DD_DD': {
                        'pattern': '11 22 33 44 55 DD DD',
                        'description': 'Any 5 Consec. Nos. w Opp. Dragons',
                        'points': 50,
                        'category': 'C',
                        'suit_requirement': 'any_5_consec_opposite_dragons',
                        'joker_allowed': False
                    },
                    'singles_2024_NN_EW_SS_2024': {
                        'pattern': '2024 NN EW SS 2024',
                        'description': 'Any 2 Suits',
                        'points': 75,
                        'category': 'C',
                        'suit_requirement': 'any_2_suits',
                        'joker_allowed': False
                    }
                }
            }
        }
    
    def evaluate_hand(self, tiles: List[str], year: int = 2024) -> Dict:
        """
        Evaluate a 13-tile American Mahjong hand and return analysis
        
        Args:
            tiles: List of 13 tile strings (e.g., ["1B", "2B", "3B", ...])
            year: American Mahjong rules year
            
        Returns:
            Dictionary with hand analysis including patterns, scoring, etc.
        """
        try:
            # Validate input
            if len(tiles) != 13:
                raise ValueError("Hand must contain exactly 13 tiles")
            
            # Validate all tiles are valid
            self._validate_tiles(tiles)
            
            # Count tiles by suit
            tile_counts = Counter(tiles)
            
            # Find potential hands for the year
            potential_hands = self._find_potential_hands(tiles, year)
            
            # Find tiles needed to complete hands
            tiles_to_win = self._find_tiles_to_win(tiles, year)
            
            # Calculate hand value based on potential hands
            hand_value = self._calculate_hand_value(potential_hands)
            
            # Calculate hand strength
            hand_strength = self._calculate_hand_strength(tiles, hand_value)
            
            # Analyze hand structure
            hand_structure = self._analyze_hand_structure(tiles)
            
            return {
                "hand_value": hand_value,
                "potential_hands": potential_hands,
                "tiles_to_win": tiles_to_win,
                "hand_strength": hand_strength,
                "tile_distribution": dict(tile_counts),
                "hand_structure": hand_structure,
                "year": year
            }
            
        except Exception as e:
            logger.error(f"Error evaluating hand: {str(e)}")
            raise
    
    def _validate_tiles(self, tiles: List[str]) -> None:
        """Validate that all tiles are valid American Mahjong tiles"""
        all_valid_tiles = []
        for suit_tiles in self.valid_tiles.values():
            all_valid_tiles.extend(suit_tiles)
        
        invalid_tiles = [tile for tile in tiles if tile not in all_valid_tiles]
        if invalid_tiles:
            raise ValueError(f"Invalid tiles found: {invalid_tiles}")
    
    def _find_potential_hands(self, tiles: List[str], year: int) -> List[Dict]:
        """Find potential hands based on year-specific rules"""
        potential_hands = []
        
        # Get year patterns
        year_patterns = self.year_rules.get(year, {}).get('patterns', {})
        
        # Check each pattern
        for pattern_id, pattern_info in year_patterns.items():
            if self._check_pattern_match(tiles, pattern_info):
                potential_hands.append({
                    "name": pattern_id.replace('_', ' ').title(),
                    "points": pattern_info['points'],
                    "description": pattern_info['description'],
                    "category": pattern_info['category'],
                    "pattern": pattern_info['pattern'],
                    "pattern_id": pattern_id
                })
        
        return potential_hands
    
    def _check_pattern_match(self, tiles: List[str], pattern_info: Dict) -> bool:
        """Check if tiles match a specific pattern"""
        pattern = pattern_info['pattern']
        suit_requirement = pattern_info.get('suit_requirement', 'any')
        joker_allowed = pattern_info.get('joker_allowed', True)
        
        # Check joker usage
        joker_count = tiles.count('F')
        if not joker_allowed and joker_count > 0:
            return False
        
        # Parse pattern into components
        pattern_components = self._parse_pattern(pattern)
        
        # Check if tiles can satisfy the pattern
        if not self._can_satisfy_pattern(tiles, pattern_components, pattern_info):
            return False
        
        # Check suit requirements
        if not self._check_suit_requirements(tiles, suit_requirement, pattern_info):
            return False
        
        return True
    
    def _parse_pattern(self, pattern: str) -> List[Dict]:
        """Parse pattern string into structured components"""
        components = []
        
        # Split pattern by spaces
        parts = pattern.split()
        
        for part in parts:
            if part == 'F':
                components.append({'type': 'flower', 'count': 1})
            elif part == 'FF':
                components.append({'type': 'flower', 'count': 2})
            elif part == 'FFFF':
                components.append({'type': 'flower', 'count': 4})
            elif part == 'FFFFF':
                components.append({'type': 'flower', 'count': 5})
            elif part == '2024':
                components.append({'type': 'year', 'value': '2024'})
            elif part in ['E', 'S', 'W', 'N']:
                components.append({'type': 'wind', 'value': part})
            elif part in ['R', 'G', '0']:
                components.append({'type': 'dragon', 'value': part})
            elif part == 'DDDD':
                components.append({'type': 'dragon_kong', 'count': 4})
            elif part == 'DDD':
                components.append({'type': 'dragon_pung', 'count': 3})
            elif part == 'DD':
                components.append({'type': 'dragon_pair', 'count': 2})
            elif part == 'D':
                components.append({'type': 'dragon_single', 'count': 1})
            elif part == 'NEWS':
                components.append({'type': 'all_winds', 'count': 4})
            elif part == '24':
                components.append({'type': 'specific_numbers', 'numbers': [2, 4]})
            else:
                # Handle numbered patterns like "222", "1111", etc.
                if part.isdigit():
                    number = int(part[0])
                    count = len(part)
                    components.append({
                        'type': 'numbered_pattern',
                        'number': number,
                        'count': count
                    })
        
        return components
    
    def _can_satisfy_pattern(self, tiles: List[str], pattern_components: List[Dict], pattern_info: Dict) -> bool:
        """Check if tiles can satisfy the pattern components"""
        tile_counts = Counter(tiles)
        
        # Remove flowers from consideration for pattern matching
        flower_count = tile_counts.get('F', 0)
        available_tiles = {k: v for k, v in tile_counts.items() if k != 'F'}
        
        # Check each component
        for component in pattern_components:
            if component['type'] == 'flower':
                if flower_count < component['count']:
                    return False
            elif component['type'] == 'year':
                if available_tiles.get('2024', 0) < 1:
                    return False
            elif component['type'] == 'wind':
                if available_tiles.get(component['value'], 0) < 1:
                    return False
            elif component['type'] == 'dragon':
                if available_tiles.get(component['value'], 0) < 1:
                    return False
            elif component['type'] == 'dragon_kong':
                dragon_count = sum(available_tiles.get(d, 0) for d in ['R', 'G', '0'])
                if dragon_count < component['count']:
                    return False
            elif component['type'] == 'dragon_pung':
                dragon_count = sum(available_tiles.get(d, 0) for d in ['R', 'G', '0'])
                if dragon_count < component['count']:
                    return False
            elif component['type'] == 'dragon_pair':
                dragon_count = sum(available_tiles.get(d, 0) for d in ['R', 'G', '0'])
                if dragon_count < component['count']:
                    return False
            elif component['type'] == 'dragon_single':
                dragon_count = sum(available_tiles.get(d, 0) for d in ['R', 'G', '0'])
                if dragon_count < component['count']:
                    return False
            elif component['type'] == 'all_winds':
                wind_count = sum(available_tiles.get(w, 0) for w in ['E', 'S', 'W', 'N'])
                if wind_count < component['count']:
                    return False
            elif component['type'] == 'specific_numbers':
                # Check for specific numbers in any suit
                number_count = 0
                for tile, count in available_tiles.items():
                    if tile.endswith(('B', 'C', 'D')):
                        number = int(tile[0])
                        if number in component['numbers']:
                            number_count += count
                if number_count < 2:  # Need at least 2 of the specific numbers
                    return False
            elif component['type'] == 'numbered_pattern':
                # Check for numbered patterns (like "222", "1111")
                number = component['number']
                count_needed = component['count']
                
                # Count tiles with this number in any suit
                number_count = 0
                for tile, count in available_tiles.items():
                    if tile.endswith(('B', 'C', 'D')):
                        tile_number = int(tile[0])
                        if tile_number == number:
                            number_count += count
                
                if number_count < count_needed:
                    return False
        
        return True
    
    def _check_suit_requirements(self, tiles: List[str], suit_requirement: str, pattern_info: Dict) -> bool:
        """Check if tiles meet suit requirements"""
        numbered_tiles = [tile for tile in tiles if tile.endswith(('B', 'C', 'D'))]
        
        if not numbered_tiles:
            # No numbered tiles, check if pattern allows this
            return suit_requirement in ['any_3_dragons', 'any_2_dragons']
        
        suits_used = set(tile[-1] for tile in numbered_tiles)
        num_suits = len(suits_used)
        
        if suit_requirement == 'any_1_suit':
            return num_suits == 1
        elif suit_requirement == 'any_2_suits':
            return num_suits == 2
        elif suit_requirement == 'any_3_suits':
            return num_suits == 3
        elif suit_requirement == 'any_1_or_2_suits':
            return num_suits in [1, 2]
        elif suit_requirement == 'any_1_or_3_suits':
            return num_suits in [1, 3]
        elif suit_requirement == 'any_2_or_3_suits':
            return num_suits in [2, 3]
        elif suit_requirement == 'any_1_suit_matching_dragons':
            if num_suits != 1:
                return False
            # Check if dragons match the suit
            suit = list(suits_used)[0]
            matching_dragon = self.dragon_associations.get(suit)
            # Check if the matching dragon is in the tiles
            return matching_dragon in tiles
        elif suit_requirement == 'any_2_suits_matching_dragons':
            if num_suits != 2:
                return False
            # Check if dragons match one of the suits
            for suit in suits_used:
                matching_dragon = self.dragon_associations.get(suit)
                if matching_dragon in tiles:
                    return True
            return False
        elif suit_requirement == 'any_1_suit_opposite_dragons':
            if num_suits != 1:
                return False
            # Check if dragons don't match the suit
            suit = list(suits_used)[0]
            matching_dragon = self.dragon_associations.get(suit)
            # Check if there's a dragon that doesn't match the suit
            for dragon in ['R', 'G', '0']:
                if dragon in tiles and dragon != matching_dragon:
                    return True
            return False
        elif suit_requirement == 'any_5_consec_opposite_dragons':
            # Check for 5 consecutive numbers
            numbers = [int(tile[0]) for tile in numbered_tiles]
            numbers.sort()
            consecutive_count = 1
            max_consecutive = 1
            for i in range(1, len(numbers)):
                if numbers[i] == numbers[i-1] + 1:
                    consecutive_count += 1
                    max_consecutive = max(max_consecutive, consecutive_count)
                else:
                    consecutive_count = 1
            return max_consecutive >= 5
        elif suit_requirement == 'specific_numbers':
            # Check for specific numbers mentioned in pattern
            specific_numbers = pattern_info.get('specific_numbers', [])
            if not specific_numbers:
                return True
            numbers = [int(tile[0]) for tile in numbered_tiles]
            return all(num in numbers for num in specific_numbers)
        elif suit_requirement == 'any_3_dragons':
            dragon_count = sum(1 for tile in tiles if tile in ['R', 'G', '0'])
            return dragon_count >= 3
        elif suit_requirement == 'any_2_dragons':
            dragon_count = sum(1 for tile in tiles if tile in ['R', 'G', '0'])
            return dragon_count >= 2
        
        return True  # Default to allowing any suit combination
    
    def _calculate_hand_value(self, potential_hands: List[Dict]) -> int:
        """Calculate hand value based on potential hands"""
        if not potential_hands:
            return 0
        
        # Return the highest scoring potential hand
        return max(hand['points'] for hand in potential_hands)
    
    def _find_tiles_to_win(self, tiles: List[str], year: int) -> List[str]:
        """Find tiles that would help complete hands"""
        helpful_tiles = []
        
        # Add tiles that could form pairs with existing singles
        tile_counts = Counter(tiles)
        singles = [tile for tile, count in tile_counts.items() if count == 1]
        
        for single in singles:
            helpful_tiles.append(single)  # Another of the same tile
        
        # Add special tiles that are often needed
        special_tiles = ['R', 'G', '0', 'F', '2024']
        for tile in special_tiles:
            if tile not in tiles:
                helpful_tiles.append(tile)
        
        # Add tiles that could form sequences
        for tile in tiles:
            if tile.endswith(('B', 'C', 'D')):
                number = int(tile[0])
                suit = tile[-1]
                
                # Add tiles that could form sequences
                if number > 1:
                    helpful_tiles.append(f"{number-1}{suit}")
                if number < 9:
                    helpful_tiles.append(f"{number+1}{suit}")
        
        # Remove duplicates and limit results
        helpful_tiles = list(set(helpful_tiles))[:8]
        
        return helpful_tiles
    
    def _calculate_hand_strength(self, tiles: List[str], hand_value: int) -> str:
        """Calculate overall hand strength"""
        if hand_value >= 50:
            return "Excellent"
        elif hand_value >= 35:
            return "Strong"
        elif hand_value >= 25:
            return "Developing"
        else:
            return "Weak"
    
    def _analyze_hand_structure(self, tiles: List[str]) -> Dict:
        """Analyze the structure of the hand"""
        tile_counts = Counter(tiles)
        
        # Count by type
        numbered_tiles = [tile for tile in tiles if tile.endswith(('B', 'C', 'D'))]
        wind_tiles = [tile for tile in tiles if tile in ['E', 'S', 'W', 'N']]
        dragon_tiles = [tile for tile in tiles if tile in ['R', 'G', '0']]
        flower_tiles = [tile for tile in tiles if tile == 'F']
        year_tiles = [tile for tile in tiles if tile == '2024']
        
        # Analyze suits
        suits_used = set(tile[-1] for tile in numbered_tiles)
        
        # Find pairs, triplets, etc.
        pairs = [tile for tile, count in tile_counts.items() if count == 2]
        triplets = [tile for tile, count in tile_counts.items() if count == 3]
        quads = [tile for tile, count in tile_counts.items() if count == 4]
        
        # Find potential sequences
        sequences = self._find_potential_sequences(numbered_tiles)
        
        return {
            "numbered_tiles": len(numbered_tiles),
            "wind_tiles": len(wind_tiles),
            "dragon_tiles": len(dragon_tiles),
            "flower_tiles": len(flower_tiles),
            "year_tiles": len(year_tiles),
            "suits_used": list(suits_used),
            "num_suits": len(suits_used),
            "pairs": pairs,
            "triplets": triplets,
            "quads": quads,
            "potential_sequences": sequences
        }
    
    def _find_potential_sequences(self, numbered_tiles: List[str]) -> List[List[str]]:
        """Find potential sequences in numbered tiles"""
        sequences = []
        
        # Group by suit
        by_suit = defaultdict(list)
        for tile in numbered_tiles:
            suit = tile[-1]
            number = int(tile[0])
            by_suit[suit].append((number, tile))
        
        # Find sequences in each suit
        for suit, tiles in by_suit.items():
            tiles.sort()  # Sort by number
            numbers = [num for num, _ in tiles]
            
            # Find consecutive sequences
            for i in range(len(numbers) - 2):
                if numbers[i+1] == numbers[i] + 1 and numbers[i+2] == numbers[i] + 2:
                    sequence = [tiles[i][1], tiles[i+1][1], tiles[i+2][1]]
                    sequences.append(sequence)
        
        return sequences 