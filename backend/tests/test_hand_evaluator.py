"""
Unit tests for HandEvaluator
"""

import unittest
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mahjong.hand_evaluator import HandEvaluator

class TestHandEvaluator(unittest.TestCase):
    """Test cases for HandEvaluator"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.evaluator = HandEvaluator()
    
    def test_evaluate_hand_valid_input(self):
        """Test hand evaluation with valid 13-tile input"""
        tiles = ["1m", "2m", "3m", "4p", "5p", "6p", "7s", "8s", "9s", "1z", "2z", "3z", "4z"]
        
        result = self.evaluator.evaluate_hand(tiles)
        
        # Check that all required fields are present
        self.assertIn('shanten', result)
        self.assertIn('winning_hands', result)
        self.assertIn('tiles_to_win', result)
        self.assertIn('hand_strength', result)
        self.assertIn('tile_distribution', result)
        
        # Check that shanten is a valid integer
        self.assertIsInstance(result['shanten'], int)
        self.assertGreaterEqual(result['shanten'], 0)
        self.assertLessEqual(result['shanten'], 8)  # Reasonable upper bound
    
    def test_evaluate_hand_invalid_length(self):
        """Test hand evaluation with invalid number of tiles"""
        tiles = ["1m", "2m", "3m"]  # Only 3 tiles
        
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_hand(tiles)
    
    def test_tanyao_detection(self):
        """Test detection of Tanyao (All Simples) yaku"""
        # Valid Tanyao hand (no terminals or honors)
        tanyao_tiles = ["2m", "3m", "4m", "5p", "6p", "7p", "2s", "3s", "4s", "5m", "6m", "7m", "8p"]
        
        result = self.evaluator.evaluate_hand(tanyao_tiles)
        
        # Check if Tanyao is in the winning hands
        yaku_types = [yaku['type'] for yaku in result['winning_hands']]
        self.assertIn('Tanyao', yaku_types)
    
    def test_yakuhai_detection(self):
        """Test detection of Yakuhai (Value Honor) yaku"""
        # Hand with dragon tiles
        yakuhai_tiles = ["1m", "2m", "3m", "4p", "5p", "6p", "7s", "8s", "9s", "5z", "6z", "7z", "1z"]
        
        result = self.evaluator.evaluate_hand(yakuhai_tiles)
        
        # Check if Yakuhai is in the winning hands
        yaku_types = [yaku['type'] for yaku in result['winning_hands']]
        self.assertIn('Yakuhai', yaku_types)
    
    def test_honitsu_detection(self):
        """Test detection of Honitsu (Half Flush) yaku"""
        # Hand with one suit plus honors
        honitsu_tiles = ["1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m", "1z", "2z", "3z", "4z"]
        
        result = self.evaluator.evaluate_hand(honitsu_tiles)
        
        # Check if Honitsu is in the winning hands
        yaku_types = [yaku['type'] for yaku in result['winning_hands']]
        self.assertIn('Honitsu', yaku_types)
    
    def test_chinitsu_detection(self):
        """Test detection of Chinitsu (Full Flush) yaku"""
        # Hand with all tiles from same suit
        chinitsu_tiles = ["1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m", "1m", "2m", "3m", "4m"]
        
        result = self.evaluator.evaluate_hand(chinitsu_tiles)
        
        # Check if Chinitsu is in the winning hands
        yaku_types = [yaku['type'] for yaku in result['winning_hands']]
        self.assertIn('Chinitsu', yaku_types)
    
    def test_sequence_counting(self):
        """Test sequence counting logic"""
        # Hand with clear sequences
        sequence_tiles = ["1m", "2m", "3m", "4p", "5p", "6p", "7s", "8s", "9s", "1z", "2z", "3z", "4z"]
        
        sequences = self.evaluator._count_sequences(sequence_tiles)
        
        # Should find at least one sequence (123m)
        self.assertGreaterEqual(sequences, 1)
    
    def test_shanten_calculation(self):
        """Test shanten calculation for different hand types"""
        # Test a hand that should be close to tenpai
        near_tenpai_tiles = ["1m", "1m", "2m", "3m", "4p", "5p", "6p", "7s", "8s", "9s", "1z", "2z", "3z"]
        
        result = self.evaluator.evaluate_hand(near_tenpai_tiles)
        
        # Should be close to tenpai (shanten <= 2)
        self.assertLessEqual(result['shanten'], 2)
    
    def test_tiles_to_win(self):
        """Test finding tiles that would help complete the hand"""
        tiles = ["1m", "2m", "3m", "4p", "5p", "6p", "7s", "8s", "9s", "1z", "2z", "3z", "4z"]
        
        result = self.evaluator.evaluate_hand(tiles)
        
        # Should return a list of helpful tiles
        self.assertIsInstance(result['tiles_to_win'], list)
        
        # If not in tenpai, should suggest some tiles
        if result['shanten'] > 0:
            self.assertGreater(len(result['tiles_to_win']), 0)

if __name__ == '__main__':
    unittest.main() 