"""
American Mahjong Tile Calculator
Provides recommendations for discards and draws based on American Mahjong hand analysis.
"""

from collections import Counter, defaultdict
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)

class TileCalculator:
    """Calculates optimal discards and draws for American Mahjong hands"""
    
    def __init__(self):
        # Tile values for American Mahjong scoring
        self.tile_values = {
            # Numbered tiles (1-9) in each suit
            'numbered': 2,
            # Winds are valuable
            'winds': 4,
            # Dragons are very valuable
            'dragons': 6,
            # Flowers are valuable
            'flowers': 5,
            # Jokers are wild cards - very valuable
            'jokers': 8,
            # Blanks are least valuable
            'blanks': 1
        }
        
        # Suit preferences for American Mahjong
        self.suit_preferences = {
            'bams': 1.0,   # Bamboo
            'cracks': 1.0, # Characters
            'dots': 1.0,   # Circles
            'winds': 1.2,  # Winds (slightly more valuable)
            'dragons': 1.5, # Dragons (very valuable)
            'flowers': 1.3, # Flowers (valuable)
            'jokers': 2.0,  # Jokers (wild cards)
            'blanks': 0.5   # Blanks (least valuable)
        }
    
    def get_recommendations(self, tiles: List[str], hand_analysis: Dict, year: int = 2024) -> Dict:
        """
        Generate recommendations for discards and draws
        
        Args:
            tiles: Current 13-tile hand
            hand_analysis: Analysis from HandEvaluator
            year: American Mahjong rules year
            
        Returns:
            Dictionary with discard and draw recommendations
        """
        try:
            # Find best discard
            best_discard = self._find_best_discard(tiles, hand_analysis, year)
            
            # Find best draws
            best_draws = self._find_best_draws(tiles, hand_analysis, year)
            
            # Generate reasoning
            reasoning = self._generate_reasoning(tiles, best_discard, best_draws, hand_analysis, year)
            
            return {
                "best_discard": best_discard,
                "best_draws": best_draws,
                "reasoning": reasoning
            }
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return {
                "best_discard": None,
                "best_draws": [],
                "reasoning": "Unable to generate recommendations"
            }
    
    def _find_best_discard(self, tiles: List[str], hand_analysis: Dict, year: int) -> str:
        """Find the best tile to discard from the current hand"""
        if not tiles:
            return None
        
        # Score each tile for discard value
        discard_scores = {}
        
        for tile in tiles:
            score = self._calculate_discard_score(tile, tiles, hand_analysis, year)
            discard_scores[tile] = score
        
        # Find tile with lowest score (worst tile to keep)
        worst_tile = min(discard_scores.keys(), key=lambda t: discard_scores[t])
        
        return worst_tile
    
    def _calculate_discard_score(self, tile: str, all_tiles: List[str], hand_analysis: Dict, year: int) -> float:
        """Calculate how good it would be to discard this tile (lower = better to discard)"""
        score = 0.0
        
        # Base tile value
        if tile.startswith('J'):
            score += self.tile_values['jokers']
        elif tile in ['R', 'G', 'W']:
            score += self.tile_values['dragons']
        elif tile in ['E', 'S', 'W', 'N']:
            score += self.tile_values['winds']
        elif tile.startswith('F'):
            score += self.tile_values['flowers']
        elif tile.startswith('B'):
            score += self.tile_values['blanks']
        else:
            score += self.tile_values['numbered']
        
        # Consider tile frequency
        tile_counts = Counter(all_tiles)
        count = tile_counts[tile]
        
        if count == 1:
            score -= 3  # Single tiles are easier to discard
        elif count == 2:
            score += 2  # Pairs are valuable
        elif count >= 3:
            score += 8  # Triplets are very valuable
        
        # Consider potential sequences
        sequence_value = self._calculate_sequence_potential(tile, all_tiles)
        score += sequence_value
        
        # Consider year-specific patterns
        year_value = self._calculate_year_specific_value(tile, all_tiles, year)
        score += year_value
        
        return score
    
    def _calculate_sequence_potential(self, tile: str, all_tiles: List[str]) -> float:
        """Calculate how valuable a tile is for forming sequences"""
        if not tile.endswith(('b', 'c', 'd')):
            return 0  # Only numbered tiles can form sequences
        
        number = int(tile[0])
        suit = tile[-1]
        
        # Check for adjacent tiles
        adjacent_tiles = []
        if number > 1:
            adjacent_tiles.append(f"{number-1}{suit}")
        if number < 9:
            adjacent_tiles.append(f"{number+1}{suit}")
        
        # Check for tiles 2 away (for 123, 234, etc.)
        two_away_tiles = []
        if number > 2:
            two_away_tiles.append(f"{number-2}{suit}")
        if number < 8:
            two_away_tiles.append(f"{number+2}{suit}")
        
        # Count how many adjacent tiles exist
        adjacent_count = sum(1 for t in adjacent_tiles if t in all_tiles)
        two_away_count = sum(1 for t in two_away_tiles if t in all_tiles)
        
        # Score based on sequence potential
        if adjacent_count == 2:
            return 6  # Can form immediate sequence
        elif adjacent_count == 1:
            return 3  # Part of potential sequence
        elif two_away_count > 0:
            return 1  # Could form sequence with one more tile
        else:
            return 0
    
    def _calculate_year_specific_value(self, tile: str, all_tiles: List[str], year: int) -> float:
        """Calculate value based on year-specific patterns"""
        # This is a simplified implementation
        # In practice, this would check against the actual year card patterns
        
        score = 0.0
        
        # Example year-specific logic
        if year == 2024:
            # 2024 might favor certain patterns
            if tile in ['R', 'G', 'W']:  # Dragons
                score += 2
            if tile.startswith('F'):  # Flowers
                score += 1
        elif year == 2023:
            # 2023 might favor different patterns
            if tile.startswith('J'):  # Jokers
                score += 2
            if tile in ['E', 'S', 'W', 'N']:  # Winds
                score += 1
        
        return score
    
    def _find_best_draws(self, tiles: List[str], hand_analysis: Dict, year: int) -> List[str]:
        """Find the best tiles to draw to improve the hand"""
        # Get tiles that would help complete the hand
        tiles_to_win = hand_analysis.get('tiles_to_win', [])
        
        # Add additional helpful tiles based on hand structure
        helpful_tiles = self._find_helpful_tiles(tiles, hand_analysis, year)
        
        # Combine and prioritize
        all_helpful = list(set(tiles_to_win + helpful_tiles))
        
        # Score each helpful tile
        draw_scores = {}
        for tile in all_helpful:
            score = self._calculate_draw_score(tile, tiles, hand_analysis, year)
            draw_scores[tile] = score
        
        # Return top 8 most helpful tiles
        sorted_tiles = sorted(draw_scores.keys(), key=lambda t: draw_scores[t], reverse=True)
        return sorted_tiles[:8]
    
    def _find_helpful_tiles(self, tiles: List[str], hand_analysis: Dict, year: int) -> List[str]:
        """Find tiles that would help improve the hand"""
        helpful_tiles = []
        
        # Find tiles that could form pairs with existing singles
        tile_counts = Counter(tiles)
        singles = [tile for tile, count in tile_counts.items() if count == 1]
        
        for single in singles:
            helpful_tiles.append(single)  # Another of the same tile
        
        # Find tiles that could form sequences
        for tile in tiles:
            if tile.endswith(('b', 'c', 'd')):
                number = int(tile[0])
                suit = tile[-1]
                
                # Add tiles that could form sequences
                if number > 1:
                    helpful_tiles.append(f"{number-1}{suit}")
                if number < 9:
                    helpful_tiles.append(f"{number+1}{suit}")
        
        # Add special tiles that are often valuable
        special_tiles = ['R', 'G', 'W', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']
        for tile in special_tiles:
            if tile not in tiles:
                helpful_tiles.append(tile)
        
        return list(set(helpful_tiles))
    
    def _calculate_draw_score(self, tile: str, current_tiles: List[str], hand_analysis: Dict, year: int) -> float:
        """Calculate how valuable it would be to draw this tile"""
        score = 0.0
        
        # Base value
        if tile.startswith('J'):
            score += 8  # Jokers are very valuable
        elif tile in ['R', 'G', 'W']:
            score += 6  # Dragons are very valuable
        elif tile in ['E', 'S', 'W', 'N']:
            score += 4  # Winds are valuable
        elif tile.startswith('F'):
            score += 5  # Flowers are valuable
        elif tile.startswith('B'):
            score += 1  # Blanks are least valuable
        else:
            score += 2  # Numbered tiles
        
        # Check if it would form a pair
        tile_counts = Counter(current_tiles)
        if tile in tile_counts:
            count = tile_counts[tile]
            if count == 1:
                score += 3  # Would form a pair
            elif count == 2:
                score += 6  # Would form a triplet
        
        # Check if it would help form sequences
        sequence_help = self._calculate_sequence_help(tile, current_tiles)
        score += sequence_help
        
        # Year-specific bonus
        year_bonus = self._calculate_year_specific_value(tile, current_tiles, year)
        score += year_bonus
        
        return score
    
    def _calculate_sequence_help(self, tile: str, current_tiles: List[str]) -> float:
        """Calculate how much a tile would help form sequences"""
        if not tile.endswith(('b', 'c', 'd')):
            return 0
        
        number = int(tile[0])
        suit = tile[-1]
        
        # Check for existing adjacent tiles
        adjacent_tiles = []
        if number > 1:
            adjacent_tiles.append(f"{number-1}{suit}")
        if number < 9:
            adjacent_tiles.append(f"{number+1}{suit}")
        
        # Count how many adjacent tiles exist
        adjacent_count = sum(1 for t in adjacent_tiles if t in current_tiles)
        
        if adjacent_count == 2:
            return 5  # Would complete a sequence
        elif adjacent_count == 1:
            return 2  # Would be part of a potential sequence
        else:
            return 0.5  # Minimal help
    
    def _generate_reasoning(self, tiles: List[str], best_discard: str, best_draws: List[str], hand_analysis: Dict, year: int) -> str:
        """Generate human-readable reasoning for recommendations"""
        reasoning_parts = []
        
        if best_discard:
            # Explain why this tile should be discarded
            if best_discard.startswith('B'):
                reasoning_parts.append(f"Discard {best_discard} - Blank tiles have the lowest value")
            elif best_discard.startswith('J'):
                reasoning_parts.append(f"Discard {best_discard} - While jokers are valuable, this one doesn't fit your current strategy")
            elif best_discard in ['R', 'G', 'W']:
                reasoning_parts.append(f"Discard {best_discard} - Dragon tiles are valuable but this one doesn't fit your hand structure")
            elif best_discard in ['E', 'S', 'W', 'N']:
                reasoning_parts.append(f"Discard {best_discard} - Wind tiles are valuable but this one doesn't fit your current pattern")
            else:
                reasoning_parts.append(f"Discard {best_discard} - This tile has the lowest potential for improving your hand")
        
        # Explain draw recommendations
        if best_draws:
            draw_explanation = f"Best draws: {', '.join(best_draws[:4])}"
            reasoning_parts.append(draw_explanation)
        
        # Add hand strength context
        hand_value = hand_analysis.get('hand_value', 0)
        if hand_value >= 50:
            reasoning_parts.append("Your hand is excellent - focus on completing high-value patterns")
        elif hand_value >= 35:
            reasoning_parts.append("Your hand is strong - focus on completing your best patterns")
        elif hand_value >= 20:
            reasoning_parts.append("Your hand is developing - focus on building sequences and pairs")
        else:
            reasoning_parts.append("Your hand needs work - focus on building basic structure")
        
        # Add year-specific advice
        reasoning_parts.append(f"Remember that {year} rules may favor certain patterns - check the official card for specific hands")
        
        return " ".join(reasoning_parts) 