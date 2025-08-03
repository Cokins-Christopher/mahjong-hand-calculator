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
            'flowers': ['F'],  # Flowers
            'jokers': ['J'],  # Jokers
            'blanks': [f"B{i}" for i in range(1, 7)],  # B1-B6 (Blanks)
            'year_tiles': ['2024']  # Year-specific tiles
        }
        
        # Dragon associations for matching
        self.dragon_associations = {
            'C': 'R',  # Cracks/Characters match Red Dragon
            'B': 'G',  # Bams/Bamboo match Green Dragon
            'D': '0'   # Dots/Circles match White Dragon
        }
        
        # Import rules from rules specification
        from .rules_specification import mahjong_rules
        self.rules = mahjong_rules
    
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
        
        # Get year patterns from rules
        year_patterns = self.rules.get_all_patterns(year)
        
        # Check each pattern
        for pattern_id, pattern_info in year_patterns.items():
            if self._check_pattern_match(tiles, pattern_info, year):
                potential_hands.append({
                    "name": pattern_info['name'],
                    "points": pattern_info['points'],
                    "description": pattern_info['description'],
                    "category": pattern_info['category'],
                    "pattern": pattern_info['pattern'],
                    "pattern_id": pattern_id,
                    "special_rules": pattern_info.get('special_rules', [])
                })
        
        return potential_hands
    
    def _check_pattern_match(self, tiles: List[str], pattern_info: Dict, year: int) -> bool:
        """Check if tiles match a specific pattern"""
        pattern = pattern_info['pattern']
        suit_requirement = pattern_info.get('suit_requirement', 'any')
        joker_allowed = pattern_info.get('joker_allowed', True)
        
        # Check joker usage
        joker_count = tiles.count('J')
        if not joker_allowed and joker_count > 0:
            return False
        
        # Parse pattern into components
        pattern_components = self._parse_pattern(pattern, year)
        
        # Check if tiles can satisfy the pattern
        if not self._can_satisfy_pattern(tiles, pattern_components, pattern_info, year):
            return False
        
        # Check suit requirements
        if not self._check_suit_requirements(tiles, suit_requirement, pattern_info):
            return False
        
        return True
    
    def _parse_pattern(self, pattern: str, year: int) -> List[Dict]:
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
                # Special handling for 2024 year tile
                if year == 2024:
                    components.append({'type': 'year', 'value': '2024', 'special': 'white_dragon_0'})
                else:
                    components.append({'type': 'year', 'value': '2024'})
            elif part in ['E', 'S', 'W', 'N']:
                components.append({'type': 'wind', 'value': part})
            elif part in ['R', 'G', '0']:
                # Special handling for White Dragon in 2024
                if part == '0' and year == 2024:
                    components.append({'type': 'dragon', 'value': part, 'special': 'white_dragon'})
                else:
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
            elif part in ['24', '48', '15', '35']:
                # Handle specific number combinations
                numbers = [int(digit) for digit in part]
                components.append({'type': 'specific_numbers', 'numbers': numbers})
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
    
    def _can_satisfy_pattern(self, tiles: List[str], pattern_components: List[Dict], pattern_info: Dict, year: int) -> bool:
        """Check if tiles can satisfy the pattern components"""
        tile_counts = Counter(tiles)
        
        # Remove flowers and jokers from consideration for pattern matching
        flower_count = tile_counts.get('F', 0)
        joker_count = tile_counts.get('J', 0)
        available_tiles = {k: v for k, v in tile_counts.items() if k not in ['F', 'J']}
        
        # Check each component
        for component in pattern_components:
            if component['type'] == 'flower':
                if flower_count < component['count']:
                    return False
            elif component['type'] == 'joker':
                if joker_count < component['count']:
                    return False
            elif component['type'] == 'year':
                if available_tiles.get('2024', 0) < 1:
                    return False
                # Special handling for 2024 year tile
                if component.get('special') == 'white_dragon_0' and year == 2024:
                    # In 2024, the 0 in 2024 must be White Dragon
                    if available_tiles.get('0', 0) < 1:
                        return False
            elif component['type'] == 'wind':
                if available_tiles.get(component['value'], 0) < 1:
                    return False
            elif component['type'] == 'dragon':
                if available_tiles.get(component['value'], 0) < 1:
                    return False
                # Special handling for White Dragon in 2024
                if component.get('special') == 'white_dragon' and year == 2024:
                    if component['value'] != '0':
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
                if number_count < len(component['numbers']):  # Need at least one of each number
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
        special_tiles = ['R', 'G', '0', 'F', 'J', '2024']
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
        joker_tiles = [tile for tile in tiles if tile == 'J']
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
            "joker_tiles": len(joker_tiles),
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