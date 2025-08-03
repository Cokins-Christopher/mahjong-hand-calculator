#!/usr/bin/env python3
"""
Test script for the 2024 American Mahjong Backend Implementation
Tests the comprehensive rules implementation including White Dragon handling,
suit requirements, and pattern matching.
"""

import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from src.mahjong.hand_evaluator import HandEvaluator
from src.mahjong.tile_calculator import TileCalculator
from src.mahjong.rules_specification import mahjong_rules

def test_2024_rules_implementation():
    """Test the comprehensive 2024 American Mahjong rules implementation"""
    
    print("Testing 2024 American Mahjong Rules Implementation")
    print("=" * 60)
    
    # Initialize evaluator and calculator
    evaluator = HandEvaluator()
    calculator = TileCalculator()
    
    # Test 1: Basic 2024 pattern with White Dragon
    print("\nTest 1: 2024 Pattern with White Dragon")
    print("-" * 40)
    
    # Hand that should match "2024 222 000 2222 4444"
    test_hand_1 = [
        "2B", "2B", "2B",  # 222 (SUIT A)
        "0", "0", "0",     # 000 (White Dragons)
        "2C", "2C", "2C", "2C",  # 2222 (SUIT B)
        "4C", "4C", "4C"   # 444 (SUIT B) - removed one 4
    ]
    
    try:
        result_1 = evaluator.evaluate_hand(test_hand_1, 2024)
        print(f"Hand: {test_hand_1}")
        print(f"Potential hands: {len(result_1['potential_hands'])}")
        for hand in result_1['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_1['hand_value']}")
        print(f"Hand strength: {result_1['hand_strength']}")
    except Exception as e:
        print(f"Error in test 1: {e}")
    
    # Test 2: 2468 pattern with matching dragons
    print("\nTest 2: 2468 Pattern with Matching Dragons")
    print("-" * 40)
    
    # Hand that should match "2468 22 44 666 888 DDDD" (ALL SUIT A WITH MATCHING DRAGON)
    test_hand_2 = [
        "2B", "2B",        # 22 (SUIT A)
        "4B", "4B",        # 44 (SUIT A)
        "6B", "6B", "6B",  # 666 (SUIT A)
        "8B", "8B", "8B",  # 888 (SUIT A)
        "G", "G", "G"      # DDD (Green Dragons matching Bams) - removed one G
    ]
    
    try:
        result_2 = evaluator.evaluate_hand(test_hand_2, 2024)
        print(f"Hand: {test_hand_2}")
        print(f"Potential hands: {len(result_2['potential_hands'])}")
        for hand in result_2['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_2['hand_value']}")
        print(f"Hand strength: {result_2['hand_strength']}")
    except Exception as e:
        print(f"Error in test 2: {e}")
    
    # Test 3: Any Like Numbers pattern
    print("\nTest 3: Any Like Numbers Pattern")
    print("-" * 40)
    
    # Hand that should match "FFFF 111 1111 111" (Three suits allowed)
    test_hand_3 = [
        "F", "F", "F", "F",  # FFFF
        "1B", "1B", "1B",    # 111 (SUIT A)
        "1C", "1C", "1C", "1C",  # 1111 (SUIT B)
        "1D", "1D"           # 11 (SUIT C) - removed one 1D
    ]
    
    try:
        result_3 = evaluator.evaluate_hand(test_hand_3, 2024)
        print(f"Hand: {test_hand_3}")
        print(f"Potential hands: {len(result_3['potential_hands'])}")
        for hand in result_3['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_3['hand_value']}")
        print(f"Hand strength: {result_3['hand_strength']}")
    except Exception as e:
        print(f"Error in test 3: {e}")
    
    # Test 4: Addition Hands (Lucky Sevens)
    print("\nTest 4: Addition Hands (Lucky Sevens)")
    print("-" * 40)
    
    # Hand that should match "FF 1111 6666 7777" (ALL SUIT A)
    test_hand_4 = [
        "F", "F",            # FF
        "1B", "1B", "1B", "1B",  # 1111 (SUIT A)
        "6B", "6B", "6B", "6B",  # 6666 (SUIT A)
        "7B", "7B", "7B"    # 777 (SUIT A) - removed one 7B
    ]
    
    try:
        result_4 = evaluator.evaluate_hand(test_hand_4, 2024)
        print(f"Hand: {test_hand_4}")
        print(f"Potential hands: {len(result_4['potential_hands'])}")
        for hand in result_4['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_4['hand_value']}")
        print(f"Hand strength: {result_4['hand_strength']}")
    except Exception as e:
        print(f"Error in test 4: {e}")
    
    # Test 5: Quints pattern
    print("\nTest 5: Quints Pattern")
    print("-" * 40)
    
    # Hand that should match "FF 11111 22 33333" (ALL SUIT A, NUMBERS CAN BE ANY CONSECUTIVE NUMBERS)
    test_hand_5 = [
        "F", "F",            # FF
        "1B", "1B", "1B", "1B", "1B",  # 11111 (SUIT A)
        "2B", "2B",          # 22 (SUIT A)
        "3B", "3B", "3B", "3B"   # 3333 (SUIT A) - removed one 3B
    ]
    
    try:
        result_5 = evaluator.evaluate_hand(test_hand_5, 2024)
        print(f"Hand: {test_hand_5}")
        print(f"Potential hands: {len(result_5['potential_hands'])}")
        for hand in result_5['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_5['hand_value']}")
        print(f"Hand strength: {result_5['hand_strength']}")
    except Exception as e:
        print(f"Error in test 5: {e}")
    
    # Test 6: Consecutive Run pattern
    print("\nTest 6: Consecutive Run Pattern")
    print("-" * 40)
    
    # Hand that should match "FF 1111 2222 3333" (ALL SUIT A)
    test_hand_6 = [
        "F", "F",            # FF
        "1B", "1B", "1B", "1B",  # 1111 (SUIT A)
        "2B", "2B", "2B", "2B",  # 2222 (SUIT A)
        "3B", "3B", "3B"    # 333 (SUIT A) - removed one 3B
    ]
    
    try:
        result_6 = evaluator.evaluate_hand(test_hand_6, 2024)
        print(f"Hand: {test_hand_6}")
        print(f"Potential hands: {len(result_6['potential_hands'])}")
        for hand in result_6['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_6['hand_value']}")
        print(f"Hand strength: {result_6['hand_strength']}")
    except Exception as e:
        print(f"Error in test 6: {e}")
    
    # Test 7: 13579 pattern
    print("\nTest 7: 13579 Pattern")
    print("-" * 40)
    
    # Hand that should match "111 33 5555 77 999" (ALL SUIT A)
    test_hand_7 = [
        "1B", "1B", "1B",        # 111 (SUIT A)
        "3B", "3B",              # 33 (SUIT A)
        "5B", "5B", "5B", "5B",  # 5555 (SUIT A)
        "7B", "7B",              # 77 (SUIT A)
        "9B", "9B"               # 99 (SUIT A) - removed one 9B
    ]
    
    try:
        result_7 = evaluator.evaluate_hand(test_hand_7, 2024)
        print(f"Hand: {test_hand_7}")
        print(f"Potential hands: {len(result_7['potential_hands'])}")
        for hand in result_7['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_7['hand_value']}")
        print(f"Hand strength: {result_7['hand_strength']}")
    except Exception as e:
        print(f"Error in test 7: {e}")
    
    # Test 8: Winds-Dragons pattern
    print("\nTest 8: Winds-Dragons Pattern")
    print("-" * 40)
    
    # Hand that should match "NNNN EEE WWW SSSS"
    test_hand_8 = [
        "N", "N", "N", "N",      # NNNN
        "E", "E", "E",           # EEE
        "W", "W", "W",           # WWW
        "S", "S", "S"            # SSS - removed one S
    ]
    
    try:
        result_8 = evaluator.evaluate_hand(test_hand_8, 2024)
        print(f"Hand: {test_hand_8}")
        print(f"Potential hands: {len(result_8['potential_hands'])}")
        for hand in result_8['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_8['hand_value']}")
        print(f"Hand strength: {result_8['hand_strength']}")
    except Exception as e:
        print(f"Error in test 8: {e}")
    
    # Test 9: 369 pattern
    print("\nTest 9: 369 Pattern")
    print("-" * 40)
    
    # Hand that should match "333 666 6666 9999" (Two/Three Suits)
    test_hand_9 = [
        "3B", "3B", "3B",        # 333 (SUIT A)
        "6B", "6B", "6B",        # 666 (SUIT A)
        "6C", "6C", "6C", "6C",  # 6666 (SUIT B)
        "9C", "9C", "9C"         # 999 (SUIT B) - removed one 9C
    ]
    
    try:
        result_9 = evaluator.evaluate_hand(test_hand_9, 2024)
        print(f"Hand: {test_hand_9}")
        print(f"Potential hands: {len(result_9['potential_hands'])}")
        for hand in result_9['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_9['hand_value']}")
        print(f"Hand strength: {result_9['hand_strength']}")
    except Exception as e:
        print(f"Error in test 9: {e}")
    
    # Test 10: Singles and Pairs pattern (NO FLOWERS ALLOWED)
    print("\nTest 10: Singles and Pairs Pattern (NO FLOWERS)")
    print("-" * 40)
    
    # Hand that should match "11 22 33 44 55 DD DD" (SUIT A + two different dragon suits)
    test_hand_10 = [
        "1B", "1B",              # 11 (SUIT A)
        "2B", "2B",              # 22 (SUIT A)
        "3B", "3B",              # 33 (SUIT A)
        "4B", "4B",              # 44 (SUIT A)
        "5B", "5B",              # 55 (SUIT A)
        "R", "R",                # DD (Red Dragons)
        "G"                      # D (Green Dragons) - removed one G
    ]
    
    try:
        result_10 = evaluator.evaluate_hand(test_hand_10, 2024)
        print(f"Hand: {test_hand_10}")
        print(f"Potential hands: {len(result_10['potential_hands'])}")
        for hand in result_10['potential_hands']:
            print(f"  - {hand['name']}: {hand['points']} points")
        print(f"Hand value: {result_10['hand_value']}")
        print(f"Hand strength: {result_10['hand_strength']}")
    except Exception as e:
        print(f"Error in test 10: {e}")
    
    # Test 11: Rules specification access
    print("\nTest 11: Rules Specification Access")
    print("-" * 40)
    
    try:
        # Test getting all patterns
        all_patterns = mahjong_rules.get_all_patterns(2024)
        print(f"Total patterns for 2024: {len(all_patterns)}")
        
        # Test getting patterns by category
        patterns_2024 = mahjong_rules.get_patterns_by_category('2024', 2024)
        print(f"2024 patterns: {len(patterns_2024)}")
        
        patterns_2468 = mahjong_rules.get_patterns_by_category('2468', 2024)
        print(f"2468 patterns: {len(patterns_2468)}")
        
        patterns_quint = mahjong_rules.get_patterns_by_category('quint', 2024)
        print(f"Quint patterns: {len(patterns_quint)}")
        
        # Test getting specific pattern
        pattern = mahjong_rules.get_pattern_by_id('2024_222_000_2222_4444', 2024)
        if pattern:
            print(f"Found pattern: {pattern['name']} - {pattern['points']} points")
        else:
            print("Pattern not found")
            
    except Exception as e:
        print(f"Error in test 11: {e}")
    
    # Test 12: Tile Calculator recommendations
    print("\nTest 12: Tile Calculator Recommendations")
    print("-" * 40)
    
    try:
        # Use test hand 1 for recommendations
        result_1 = evaluator.evaluate_hand(test_hand_1, 2024)
        recommendations = calculator.get_recommendations(test_hand_1, result_1, 2024)
        
        print(f"Best discard: {recommendations['best_discard']}")
        print(f"Best draws: {recommendations['best_draws'][:4]}")
        print(f"Reasoning: {recommendations['reasoning']}")
        print(f"Strategic advice: {recommendations['strategic_advice']}")
        
    except Exception as e:
        print(f"Error in test 12: {e}")
    
    print("\n" + "=" * 60)
    print("Testing Complete!")
    print("The comprehensive 2024 American Mahjong rules implementation")
    print("has been tested with various pattern types and scenarios.")

if __name__ == "__main__":
    test_2024_rules_implementation() 