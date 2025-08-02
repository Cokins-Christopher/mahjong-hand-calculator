"""
American Mahjong Hand Evaluator
Implements core logic for evaluating American Mahjong hands including
hand patterns and scoring based on year-specific rules.
"""

from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Set
import logging

logger = logging.getLogger(__name__)

class HandEvaluator:
    """Evaluates American Mahjong hands for patterns and scoring"""
    
    def __init__(self):
        # Define all valid American Mahjong tiles
        self.valid_tiles = {
            'bams': [f"{i}b" for i in range(1, 10)],  # 1b-9b (Bamboo)
            'cracks': [f"{i}c" for i in range(1, 10)],  # 1c-9c (Characters)
            'dots': [f"{i}d" for i in range(1, 10)],  # 1d-9d (Circles)
            'winds': ['E', 'S', 'W', 'N'],  # East, South, West, North
            'dragons': ['R', 'G', 'W'],  # Red, Green, White Dragons
            'flowers': [f"F{i}" for i in range(1, 9)],  # F1-F8
            'jokers': [f"J{i}" for i in range(1, 11)],  # J1-J10
            'blanks': [f"B{i}" for i in range(1, 7)]  # B1-B6
        }
        
        # Year-specific hand patterns (simplified examples)
        self.year_patterns = {
            2024: {
                'pairs': ['R', 'G', 'W', 'E', 'S', 'W', 'N'],
                'sequences': ['1b2b3b', '4c5c6c', '7d8d9d'],
                'special_hands': ['F1F2F3F4', 'J1J2J3J4']
            },
            2023: {
                'pairs': ['R', 'G', 'W', 'E', 'S', 'W', 'N'],
                'sequences': ['1b2b3b', '4c5c6c', '7d8d9d'],
                'special_hands': ['F5F6F7F8', 'J5J6J7J8']
            },
            # Add more years as needed
        }
    
    def evaluate_hand(self, tiles: List[str], year: int = 2024) -> Dict:
        """
        Evaluate a 13-tile American Mahjong hand and return analysis
        
        Args:
            tiles: List of 13 tile strings (e.g., ["1b", "2b", "3b", ...])
            year: American Mahjong rules year
            
        Returns:
            Dictionary with hand analysis including patterns, scoring, etc.
        """
        try:
            # Validate input
            if len(tiles) != 13:
                raise ValueError("Hand must contain exactly 13 tiles")
            
            # Count tiles by suit
            tile_counts = Counter(tiles)
            
            # Calculate hand value based on year
            hand_value = self._calculate_hand_value(tiles, year)
            
            # Find potential hands for the year
            potential_hands = self._find_potential_hands(tiles, year)
            
            # Find tiles needed to complete hands
            tiles_to_win = self._find_tiles_to_win(tiles, year)
            
            # Calculate hand strength
            hand_strength = self._calculate_hand_strength(tiles, hand_value)
            
            return {
                "hand_value": hand_value,
                "potential_hands": potential_hands,
                "tiles_to_win": tiles_to_win,
                "hand_strength": hand_strength,
                "tile_distribution": dict(tile_counts),
                "year": year
            }
            
        except Exception as e:
            logger.error(f"Error evaluating hand: {str(e)}")
            raise
    
    def _calculate_hand_value(self, tiles: List[str], year: int) -> int:
        """
        Calculate hand value based on American Mahjong scoring
        """
        # Simplified scoring - in practice this would be much more complex
        # and year-specific
        
        value = 0
        
        # Count pairs
        tile_counts = Counter(tiles)
        pairs = sum(1 for count in tile_counts.values() if count >= 2)
        value += pairs * 5
        
        # Count sequences
        sequences = self._count_sequences(tiles)
        value += sequences * 10
        
        # Count special tiles
        special_tiles = ['R', 'G', 'W', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']
        special_count = sum(1 for tile in tiles if tile in special_tiles)
        value += special_count * 3
        
        # Count jokers
        joker_count = sum(1 for tile in tiles if tile.startswith('J'))
        value += joker_count * 2
        
        return value
    
    def _count_sequences(self, tiles: List[str]) -> int:
        """Count potential sequences in the hand"""
        sequences = 0
        
        # Group tiles by suit
        suits = defaultdict(list)
        for tile in tiles:
            if tile.endswith('b'):
                suits['bams'].append(int(tile[0]))
            elif tile.endswith('c'):
                suits['cracks'].append(int(tile[0]))
            elif tile.endswith('d'):
                suits['dots'].append(int(tile[0]))
        
        # Count sequences for each suit
        for suit_tiles in suits.values():
            suit_tiles.sort()
            for i in range(len(suit_tiles) - 2):
                if suit_tiles[i+1] == suit_tiles[i] + 1 and suit_tiles[i+2] == suit_tiles[i] + 2:
                    sequences += 1
                    break  # Count only one sequence per suit for simplicity
        
        return sequences
    
    def _find_potential_hands(self, tiles: List[str], year: int) -> List[Dict]:
        """Find potential hands based on year-specific rules"""
        potential_hands = []
        
        # Get year patterns
        patterns = self.year_patterns.get(year, self.year_patterns[2024])
        
        # Check for dragon hands
        dragon_tiles = ['R', 'G', 'W']
        dragon_count = sum(1 for tile in tiles if tile in dragon_tiles)
        if dragon_count >= 2:
            potential_hands.append({
                "name": "Dragon Hand",
                "points": 25,
                "description": f"Has {dragon_count} dragon tiles"
            })
        
        # Check for flower hands
        flower_tiles = [f"F{i}" for i in range(1, 9)]
        flower_count = sum(1 for tile in tiles if tile in flower_tiles)
        if flower_count >= 3:
            potential_hands.append({
                "name": "Flower Hand",
                "points": 20,
                "description": f"Has {flower_count} flower tiles"
            })
        
        # Check for joker hands
        joker_count = sum(1 for tile in tiles if tile.startswith('J'))
        if joker_count >= 2:
            potential_hands.append({
                "name": "Joker Hand",
                "points": 15,
                "description": f"Has {joker_count} joker tiles"
            })
        
        # Check for wind hands
        wind_tiles = ['E', 'S', 'W', 'N']
        wind_count = sum(1 for tile in tiles if tile in wind_tiles)
        if wind_count >= 3:
            potential_hands.append({
                "name": "Wind Hand",
                "points": 18,
                "description": f"Has {wind_count} wind tiles"
            })
        
        # Check for sequence hands
        sequences = self._count_sequences(tiles)
        if sequences >= 2:
            potential_hands.append({
                "name": "Sequence Hand",
                "points": 12,
                "description": f"Has {sequences} sequences"
            })
        
        return potential_hands
    
    def _find_tiles_to_win(self, tiles: List[str], year: int) -> List[str]:
        """Find tiles that would help complete hands"""
        helpful_tiles = []
        
        # Add tiles that could form pairs with existing tiles
        tile_counts = Counter(tiles)
        for tile, count in tile_counts.items():
            if count == 1:  # Single tile
                helpful_tiles.append(tile)
        
        # Add tiles that could form sequences
        for tile in tiles:
            if tile.endswith(('b', 'c', 'd')):
                number = int(tile[0])
                suit = tile[-1]
                
                # Add adjacent numbers for potential sequences
                if number > 1:
                    helpful_tiles.append(f"{number-1}{suit}")
                if number < 9:
                    helpful_tiles.append(f"{number+1}{suit}")
        
        # Add special tiles that are often needed
        special_tiles = ['R', 'G', 'W', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']
        for tile in special_tiles:
            if tile not in tiles:
                helpful_tiles.append(tile)
        
        # Remove duplicates and limit results
        helpful_tiles = list(set(helpful_tiles))[:8]
        
        return helpful_tiles
    
    def _calculate_hand_strength(self, tiles: List[str], hand_value: int) -> str:
        """Calculate overall hand strength"""
        if hand_value >= 50:
            return "Excellent"
        elif hand_value >= 35:
            return "Strong"
        elif hand_value >= 20:
            return "Developing"
        else:
            return "Weak" 