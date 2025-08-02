#!/usr/bin/env python3
"""
Simple test script to verify the backend functionality
"""

import sys
import os

# Add the backend src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend', 'src'))

try:
    from mahjong.hand_evaluator import HandEvaluator
    from mahjong.tile_calculator import TileCalculator
    
    print("✅ Backend modules imported successfully")
    
    # Test hand evaluator
    evaluator = HandEvaluator()
    test_tiles = ["1m", "2m", "3m", "4p", "5p", "6p", "7s", "8s", "9s", "1z", "2z", "3z", "4z"]
    
    try:
        result = evaluator.evaluate_hand(test_tiles)
        print("✅ Hand evaluation works")
        print(f"   Shanten: {result['shanten']}")
        print(f"   Hand strength: {result['hand_strength']}")
        print(f"   Potential yaku: {len(result['winning_hands'])}")
    except Exception as e:
        print(f"❌ Hand evaluation failed: {e}")
    
    # Test tile calculator
    calculator = TileCalculator()
    try:
        recommendations = calculator.get_recommendations(test_tiles, result)
        print("✅ Tile calculator works")
        print(f"   Best discard: {recommendations['best_discard']}")
        print(f"   Best draws: {recommendations['best_draws'][:3]}")
    except Exception as e:
        print(f"❌ Tile calculator failed: {e}")
    
    print("\n🎉 Backend functionality verified!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you're in the project root directory")
except Exception as e:
    print(f"❌ Error: {e}")

print("\nTo start the backend server:")
print("cd backend")
print("python app.py") 