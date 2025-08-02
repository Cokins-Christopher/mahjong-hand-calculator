"""
Tests for American Mahjong Hand Evaluator
Tests the comprehensive implementation of American Mahjong rules and patterns.
"""

import unittest
from src.mahjong.hand_evaluator import HandEvaluator
from src.mahjong.tile_calculator import TileCalculator

class TestHandEvaluator(unittest.TestCase):
    """Test cases for HandEvaluator"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.evaluator = HandEvaluator()
        self.calculator = TileCalculator()
    
    def test_valid_tiles(self):
        """Test that all valid tiles are recognized"""
        # Test numbered tiles
        for suit in ['B', 'C', 'D']:
            for number in range(1, 10):
                tile = f"{number}{suit}"
                self.assertIn(tile, self.evaluator.valid_tiles['bams' if suit == 'B' else 'cracks' if suit == 'C' else 'dots'])
        
        # Test winds
        for wind in ['E', 'S', 'W', 'N']:
            self.assertIn(wind, self.evaluator.valid_tiles['winds'])
        
        # Test dragons
        for dragon in ['R', 'G', '0']:
            self.assertIn(dragon, self.evaluator.valid_tiles['dragons'])
        
        # Test flowers
        self.assertIn('F', self.evaluator.valid_tiles['flowers'])
        
        # Test year tiles
        self.assertIn('2024', self.evaluator.valid_tiles['year_tiles'])
    
    def test_dragon_associations(self):
        """Test dragon associations"""
        self.assertEqual(self.evaluator.dragon_associations['C'], 'R')  # Cracks match Red Dragon
        self.assertEqual(self.evaluator.dragon_associations['B'], 'G')  # Bams match Green Dragon
        self.assertEqual(self.evaluator.dragon_associations['D'], '0')  # Dots match White Dragon
    
    def test_validate_tiles(self):
        """Test tile validation"""
        # Valid tiles
        valid_hand = ["1B", "2B", "3B", "4C", "5C", "6C", "7D", "8D", "9D", "E", "S", "W", "N", "F"]
        self.evaluator._validate_tiles(valid_hand)  # Should not raise exception
        
        # Invalid tiles
        invalid_hand = ["1B", "2B", "3B", "4C", "5C", "6C", "7D", "8D", "9D", "E", "S", "W", "N", "INVALID"]
        with self.assertRaises(ValueError):
            self.evaluator._validate_tiles(invalid_hand)
    
    def test_parse_pattern(self):
        """Test pattern parsing"""
        # Test flower patterns
        pattern = "FFFF 2222 0000 24"
        components = self.evaluator._parse_pattern(pattern)
        
        # Should have 4 components: FFFF, 2222, 0000, 24
        self.assertEqual(len(components), 4)
        
        # Check FFFF component
        flower_component = components[0]
        self.assertEqual(flower_component['type'], 'flower')
        self.assertEqual(flower_component['count'], 4)
        
        # Check 2222 component
        number_component = components[1]
        self.assertEqual(number_component['type'], 'numbered_pattern')
        self.assertEqual(number_component['number'], 2)
        self.assertEqual(number_component['count'], 4)
        
        # Check 0000 component (White Dragon)
        dragon_component = components[2]
        self.assertEqual(dragon_component['type'], 'numbered_pattern')
        self.assertEqual(dragon_component['number'], 0)
        self.assertEqual(dragon_component['count'], 4)
        
        # Check 24 component
        specific_component = components[3]
        self.assertEqual(specific_component['type'], 'specific_numbers')
        self.assertEqual(specific_component['numbers'], [2, 4])
    
    def test_suit_requirements(self):
        """Test suit requirement checking"""
        # Test single suit requirement
        single_suit_tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1B", "2B", "3B", "4B", "5B"]
        self.assertTrue(self.evaluator._check_suit_requirements(single_suit_tiles, 'any_1_suit', {}))
        
        # Test two suit requirement
        two_suit_tiles = ["1B", "2B", "3B", "4B", "5B", "1C", "2C", "3C", "4C", "5C", "1B", "2B", "3B", "4B"]
        self.assertTrue(self.evaluator._check_suit_requirements(two_suit_tiles, 'any_2_suits', {}))
        
        # Test three suit requirement
        three_suit_tiles = ["1B", "2B", "3B", "1C", "2C", "3C", "1D", "2D", "3D", "4B", "5B", "6B", "7B", "8B"]
        self.assertTrue(self.evaluator._check_suit_requirements(three_suit_tiles, 'any_3_suits', {}))
    
    def test_matching_dragons(self):
        """Test matching dragon requirements"""
        # Test matching dragons with Cracks
        matching_cracks = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "1C", "2C", "3C", "4C", "R"]
        self.assertTrue(self.evaluator._check_suit_requirements(matching_cracks, 'any_1_suit_matching_dragons', {}))
        
        # Test matching dragons with Bams
        matching_bams = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1B", "2B", "3B", "4B", "G"]
        self.assertTrue(self.evaluator._check_suit_requirements(matching_bams, 'any_1_suit_matching_dragons', {}))
        
        # Test matching dragons with Dots
        matching_dots = ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "1D", "2D", "3D", "4D", "0"]
        self.assertTrue(self.evaluator._check_suit_requirements(matching_dots, 'any_1_suit_matching_dragons', {}))
    
    def test_opposite_dragons(self):
        """Test opposite dragon requirements"""
        # Test opposite dragons (using Cracks with non-matching dragon)
        opposite_dragons = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "1C", "2C", "3C", "4C", "G"]
        self.assertTrue(self.evaluator._check_suit_requirements(opposite_dragons, 'any_1_suit_opposite_dragons', {}))
    
    def test_consecutive_numbers(self):
        """Test consecutive number requirements"""
        # Test 5 consecutive numbers
        consecutive_tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1B", "2B", "3B", "4B", "5B"]
        self.assertTrue(self.evaluator._check_suit_requirements(consecutive_tiles, 'any_5_consec_opposite_dragons', {}))
    
    def test_specific_numbers(self):
        """Test specific number requirements"""
        # Test specific numbers [1, 2, 3]
        specific_tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1B", "2B", "3B", "4B", "5B"]
        pattern_info = {'specific_numbers': [1, 2, 3]}
        self.assertTrue(self.evaluator._check_suit_requirements(specific_tiles, 'specific_numbers', pattern_info))
    
    def test_dragon_counts(self):
        """Test dragon count requirements"""
        # Test 3 dragons
        three_dragons = ["R", "G", "0", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1B", "2B"]
        self.assertTrue(self.evaluator._check_suit_requirements(three_dragons, 'any_3_dragons', {}))
        
        # Test 2 dragons
        two_dragons = ["R", "G", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1B", "2B", "3B"]
        self.assertTrue(self.evaluator._check_suit_requirements(two_dragons, 'any_2_dragons', {}))
    
    def test_can_satisfy_pattern(self):
        """Test pattern satisfaction checking"""
        # Test pattern with flowers
        tiles_with_flowers = ["F", "F", "F", "F", "2B", "2B", "2B", "2B", "0", "0", "0", "0", "2C", "4C"]
        pattern_components = [
            {'type': 'flower', 'count': 4},
            {'type': 'numbered_pattern', 'number': 2, 'count': 4},
            {'type': 'dragon_kong', 'count': 4},  # White Dragon kong instead of numbered pattern
            {'type': 'specific_numbers', 'numbers': [2, 4]}
        ]
        self.assertTrue(self.evaluator._can_satisfy_pattern(tiles_with_flowers, pattern_components, {}))
    
    def test_hand_structure_analysis(self):
        """Test hand structure analysis"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        structure = self.evaluator._analyze_hand_structure(tiles)
        
        self.assertEqual(structure['numbered_tiles'], 9)
        self.assertEqual(structure['wind_tiles'], 4)
        self.assertEqual(structure['dragon_tiles'], 0)
        self.assertEqual(structure['flower_tiles'], 1)
        self.assertEqual(structure['year_tiles'], 0)
        self.assertEqual(structure['num_suits'], 1)
        self.assertEqual(structure['suits_used'], ['B'])
    
    def test_find_potential_sequences(self):
        """Test sequence finding"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "1C", "2C", "3C", "4C", "5C"]
        sequences = self.evaluator._find_potential_sequences([tile for tile in tiles if tile.endswith(('B', 'C', 'D'))])
        
        # Should find sequences like 1B-2B-3B, 2B-3B-4B, etc.
        self.assertGreater(len(sequences), 0)
    
    def test_evaluate_hand_basic(self):
        """Test basic hand evaluation"""
        # A simple hand with some potential
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        
        analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        self.assertIn('hand_value', analysis)
        self.assertIn('potential_hands', analysis)
        self.assertIn('tiles_to_win', analysis)
        self.assertIn('hand_strength', analysis)
        self.assertIn('tile_distribution', analysis)
        self.assertIn('hand_structure', analysis)
        self.assertIn('year', analysis)
    
    def test_evaluate_hand_invalid(self):
        """Test hand evaluation with invalid input"""
        # Too few tiles
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_hand(["1B", "2B", "3B"], 2024)
        
        # Too many tiles
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_hand(["1B"] * 15, 2024)
        
        # Invalid tiles
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_hand(["1B"] * 13 + ["INVALID"], 2024)

class TestTileCalculator(unittest.TestCase):
    """Test cases for TileCalculator"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calculator = TileCalculator()
        self.evaluator = HandEvaluator()
    
    def test_calculate_discard_score(self):
        """Test discard score calculation"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        hand_analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        # Test scoring for different tile types
        flower_score = self.calculator._calculate_discard_score("F", tiles, hand_analysis, 2024)
        dragon_score = self.calculator._calculate_discard_score("R", tiles, hand_analysis, 2024)
        numbered_score = self.calculator._calculate_discard_score("1B", tiles, hand_analysis, 2024)
        
        # Flowers should have higher score than numbered tiles
        self.assertGreater(flower_score, numbered_score)
        # Dragons should have higher score than numbered tiles
        self.assertGreater(dragon_score, numbered_score)
    
    def test_calculate_draw_score(self):
        """Test draw score calculation"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        hand_analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        # Test scoring for different tile types
        flower_score = self.calculator._calculate_draw_score("F", tiles, hand_analysis, 2024)
        year_score = self.calculator._calculate_draw_score("2024", tiles, hand_analysis, 2024)
        numbered_score = self.calculator._calculate_draw_score("1B", tiles, hand_analysis, 2024)
        
        # Year tiles should have highest score
        self.assertGreater(year_score, flower_score)
        self.assertGreater(flower_score, numbered_score)
    
    def test_find_best_discard(self):
        """Test finding best discard"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        hand_analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        best_discard = self.calculator._find_best_discard(tiles, hand_analysis, 2024)
        
        # Should return a tile from the hand
        self.assertIn(best_discard, tiles)
    
    def test_find_best_draws(self):
        """Test finding best draws"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        hand_analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        best_draws = self.calculator._find_best_draws(tiles, hand_analysis, 2024)
        
        # Should return a list of helpful tiles
        self.assertIsInstance(best_draws, list)
        self.assertLessEqual(len(best_draws), 8)  # Should limit to 8 recommendations
    
    def test_get_recommendations(self):
        """Test getting full recommendations"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        hand_analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        recommendations = self.calculator.get_recommendations(tiles, hand_analysis, 2024)
        
        self.assertIn('best_discard', recommendations)
        self.assertIn('best_draws', recommendations)
        self.assertIn('reasoning', recommendations)
        self.assertIn('strategic_advice', recommendations)
    
    def test_generate_strategic_advice(self):
        """Test strategic advice generation"""
        tiles = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "E", "S", "W", "N", "F"]
        hand_analysis = self.evaluator.evaluate_hand(tiles, 2024)
        
        advice = self.calculator._generate_strategic_advice(tiles, hand_analysis, 2024)
        
        # Should return a string with advice
        self.assertIsInstance(advice, str)
        self.assertGreater(len(advice), 0)

if __name__ == '__main__':
    unittest.main() 