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
            # Flowers are wild cards - very valuable
            'flowers': 8,
            # Year tiles are very valuable
            'year_tiles': 10,
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
            'flowers': 2.0,  # Flowers (wild cards)
            'year_tiles': 2.5, # Year tiles (very valuable)
            'blanks': 0.5   # Blanks (least valuable)
        }
        
        # Dragon associations for matching
        self.dragon_associations = {
            'C': 'R',  # Cracks/Characters match Red Dragon
            'B': 'G',  # Bams/Bamboo match Green Dragon
            'D': '0'   # Dots/Circles match White Dragon
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
            
            # Generate strategic advice
            strategic_advice = self._generate_strategic_advice(tiles, hand_analysis, year)
            
            return {
                "best_discard": best_discard,
                "best_draws": best_draws,
                "reasoning": reasoning,
                "strategic_advice": strategic_advice
            }
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return {
                "best_discard": None,
                "best_draws": [],
                "reasoning": "Unable to generate recommendations",
                "strategic_advice": "Unable to generate strategic advice"
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
        if tile == 'F':
            score += self.tile_values['flowers']
        elif tile == '2024':
            score += self.tile_values['year_tiles']
        elif tile in ['R', 'G', '0']:
            score += self.tile_values['dragons']
        elif tile in ['E', 'S', 'W', 'N']:
            score += self.tile_values['winds']
        elif tile.endswith(('B', 'C', 'D')):
            score += self.tile_values['numbered']
        else:
            score += self.tile_values['blanks']
        
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
        
        # Consider hand structure
        structure_value = self._calculate_structure_value(tile, all_tiles, hand_analysis)
        score += structure_value
        
        return score
    
    def _calculate_sequence_potential(self, tile: str, all_tiles: List[str]) -> float:
        """Calculate how valuable a tile is for forming sequences"""
        if not tile.endswith(('B', 'C', 'D')):
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
        score = 0.0
        
        # Example year-specific logic for 2024
        if year == 2024:
            # 2024 patterns favor certain tiles
            if tile == '2024':
                score += 5  # Year tile is very valuable
            if tile in ['R', 'G', '0']:  # Dragons
                score += 2
            if tile == 'F':  # Flowers
                score += 3
            if tile.endswith(('B', 'C', 'D')):  # Numbered tiles
                number = int(tile[0])
                if number in [2, 4, 6, 8]:  # Even numbers for 2468 patterns
                    score += 1
                if number in [1, 3, 5, 7, 9]:  # Odd numbers for 13579 patterns
                    score += 1
                if number in [3, 6, 9]:  # 369 patterns
                    score += 1
        
        return score
    
    def _calculate_structure_value(self, tile: str, all_tiles: List[str], hand_analysis: Dict) -> float:
        """Calculate value based on current hand structure"""
        score = 0.0
        
        # Get hand structure info
        hand_structure = hand_analysis.get('hand_structure', {})
        num_suits = hand_structure.get('num_suits', 0)
        suits_used = hand_structure.get('suits_used', [])
        
        # If we have a single suit, favor keeping tiles in that suit
        if num_suits == 1 and tile.endswith(('B', 'C', 'D')):
            suit = tile[-1]
            if suit in suits_used:
                score += 2  # Keep tiles in the same suit
        
        # If we have multiple suits, consider which to focus on
        if num_suits > 1 and tile.endswith(('B', 'C', 'D')):
            suit = tile[-1]
            # Check if this suit has more tiles
            suit_count = sum(1 for t in all_tiles if t.endswith(suit))
            if suit_count >= 4:  # If this suit has many tiles, keep it
                score += 1
        
        # Consider dragon associations
        if tile.endswith(('B', 'C', 'D')):
            suit = tile[-1]
            matching_dragon = self.dragon_associations.get(suit)
            if matching_dragon in all_tiles:
                score += 1  # Keep tiles that match existing dragons
        
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
            if tile.endswith(('B', 'C', 'D')):
                number = int(tile[0])
                suit = tile[-1]
                
                # Add tiles that could form sequences
                if number > 1:
                    helpful_tiles.append(f"{number-1}{suit}")
                if number < 9:
                    helpful_tiles.append(f"{number+1}{suit}")
        
        # Add special tiles that are often valuable
        special_tiles = ['R', 'G', '0', 'F', '2024']
        for tile in special_tiles:
            if tile not in tiles:
                helpful_tiles.append(tile)
        
        # Add tiles that could help with year-specific patterns
        if year == 2024:
            # Add tiles for 2468 patterns
            for number in [2, 4, 6, 8]:
                for suit in ['B', 'C', 'D']:
                    tile = f"{number}{suit}"
                    if tile not in tiles:
                        helpful_tiles.append(tile)
            
            # Add tiles for 13579 patterns
            for number in [1, 3, 5, 7, 9]:
                for suit in ['B', 'C', 'D']:
                    tile = f"{number}{suit}"
                    if tile not in tiles:
                        helpful_tiles.append(tile)
            
            # Add tiles for 369 patterns
            for number in [3, 6, 9]:
                for suit in ['B', 'C', 'D']:
                    tile = f"{number}{suit}"
                    if tile not in tiles:
                        helpful_tiles.append(tile)
        
        return list(set(helpful_tiles))
    
    def _calculate_draw_score(self, tile: str, current_tiles: List[str], hand_analysis: Dict, year: int) -> float:
        """Calculate how valuable it would be to draw this tile"""
        score = 0.0
        
        # Base value
        if tile == 'F':
            score += 8  # Flowers are very valuable
        elif tile == '2024':
            score += 10  # Year tiles are very valuable
        elif tile in ['R', 'G', '0']:
            score += 6  # Dragons are very valuable
        elif tile in ['E', 'S', 'W', 'N']:
            score += 4  # Winds are valuable
        elif tile.endswith(('B', 'C', 'D')):
            score += 2  # Numbered tiles
        else:
            score += 1  # Other tiles
        
        # Check if it would form a pair
        tile_counts = Counter(current_tiles)
        if tile in tile_counts:
            count = tile_counts[tile]
            if count == 1:
                score += 3  # Would form a pair
            elif count == 2:
                score += 6  # Would form a triplet
            elif count == 3:
                score += 10  # Would form a quad
        
        # Check if it would help form sequences
        sequence_help = self._calculate_sequence_help(tile, current_tiles)
        score += sequence_help
        
        # Year-specific bonus
        year_bonus = self._calculate_year_specific_value(tile, current_tiles, year)
        score += year_bonus
        
        # Hand structure bonus
        structure_bonus = self._calculate_structure_value(tile, current_tiles, hand_analysis)
        score += structure_bonus
        
        return score
    
    def _calculate_sequence_help(self, tile: str, current_tiles: List[str]) -> float:
        """Calculate how much a tile would help form sequences"""
        if not tile.endswith(('B', 'C', 'D')):
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
            if best_discard == 'F':
                reasoning_parts.append(f"Discard {best_discard} - While flowers are valuable, this one doesn't fit your current strategy")
            elif best_discard == '2024':
                reasoning_parts.append(f"Discard {best_discard} - Year tiles are valuable but this one doesn't fit your hand structure")
            elif best_discard in ['R', 'G', '0']:
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
        elif hand_value >= 25:
            reasoning_parts.append("Your hand is developing - focus on building sequences and pairs")
        else:
            reasoning_parts.append("Your hand needs work - focus on building basic structure")
        
        # Add year-specific advice
        reasoning_parts.append(f"Remember that {year} rules may favor certain patterns - check the official card for specific hands")
        
        return " ".join(reasoning_parts)
    
    def _generate_strategic_advice(self, tiles: List[str], hand_analysis: Dict, year: int) -> str:
        """Generate strategic advice based on hand analysis"""
        advice_parts = []
        
        # Get hand structure
        hand_structure = hand_analysis.get('hand_structure', {})
        num_suits = hand_structure.get('num_suits', 0)
        flower_count = hand_structure.get('flower_tiles', 0)
        dragon_count = hand_structure.get('dragon_tiles', 0)
        year_count = hand_structure.get('year_tiles', 0)
        
        # Suit strategy
        if num_suits == 1:
            advice_parts.append("Focus on single-suit patterns - you have a good foundation")
        elif num_suits == 2:
            advice_parts.append("Consider two-suit patterns or expand to three suits")
        elif num_suits == 3:
            advice_parts.append("You have good suit diversity - consider three-suit patterns")
        else:
            advice_parts.append("Build toward a specific suit strategy")
        
        # Special tile strategy
        if flower_count >= 4:
            advice_parts.append("You have many flowers - focus on patterns that use them effectively")
        elif flower_count >= 2:
            advice_parts.append("You have some flowers - use them strategically")
        else:
            advice_parts.append("Consider drawing flowers for flexibility")
        
        if dragon_count >= 2:
            advice_parts.append("You have dragons - consider dragon-heavy patterns")
        
        if year_count >= 1:
            advice_parts.append("You have year tiles - focus on 2024-specific patterns")
        
        # Pattern-specific advice for 2024
        if year == 2024:
            numbered_tiles = [tile for tile in tiles if tile.endswith(('B', 'C', 'D'))]
            numbers = [int(tile[0]) for tile in numbered_tiles]
            
            even_count = sum(1 for n in numbers if n % 2 == 0)
            odd_count = sum(1 for n in numbers if n % 2 == 1)
            
            if even_count >= 6:
                advice_parts.append("You have many even numbers - consider 2468 patterns")
            if odd_count >= 6:
                advice_parts.append("You have many odd numbers - consider 13579 patterns")
            
            if any(n in [3, 6, 9] for n in numbers):
                advice_parts.append("You have 3, 6, or 9 tiles - consider 369 patterns")
        
        return " ".join(advice_parts) 