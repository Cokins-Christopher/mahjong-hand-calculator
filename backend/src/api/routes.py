from flask import Blueprint, request, jsonify
from src.mahjong.hand_evaluator import HandEvaluator
from src.mahjong.tile_calculator import TileCalculator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__)

@api_bp.route('/evaluate-hand', methods=['POST'])
def evaluate_hand():
    """
    Evaluate a 13-tile American Mahjong hand and provide recommendations
    
    Expected JSON payload:
    {
        "tiles": ["1b", "2b", "3b", "4c", "5c", "6c", "7d", "8d", "9d", "E", "S", "W", "N"],
        "year": 2024
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'tiles' not in data:
            return jsonify({"error": "Missing 'tiles' field in request"}), 400
        
        tiles = data['tiles']
        year = data.get('year', 2024)  # Default to 2024 if not specified
        
        # Validate input
        if not isinstance(tiles, list) or len(tiles) != 13:
            return jsonify({"error": "Must provide exactly 13 tiles"}), 400
        
        # Initialize evaluators
        evaluator = HandEvaluator()
        calculator = TileCalculator()
        
        # Evaluate the hand
        hand_analysis = evaluator.evaluate_hand(tiles, year)
        
        # Get recommendations
        recommendations = calculator.get_recommendations(tiles, hand_analysis, year)
        
        response = {
            "hand_analysis": hand_analysis,
            "recommendations": recommendations
        }
        
        logger.info(f"Hand evaluated successfully for year {year}: {tiles}")
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error evaluating hand: {str(e)}")
        return jsonify({"error": "Failed to evaluate hand"}), 500

@api_bp.route('/recognize-tiles', methods=['POST'])
def recognize_tiles():
    """
    Placeholder for image recognition functionality
    Will be implemented with OpenCV in the future
    """
    try:
        # This is a placeholder for future image recognition
        return jsonify({
            "message": "Image recognition not yet implemented",
            "status": "placeholder"
        })
        
    except Exception as e:
        logger.error(f"Error in tile recognition: {str(e)}")
        return jsonify({"error": "Failed to recognize tiles"}), 500

@api_bp.route('/validate-tiles', methods=['POST'])
def validate_tiles():
    """
    Validate if a list of tiles is valid according to American Mahjong rules
    """
    try:
        data = request.get_json()
        
        if not data or 'tiles' not in data:
            return jsonify({"error": "Missing 'tiles' field in request"}), 400
        
        tiles = data['tiles']
        
        # Basic validation for American Mahjong tiles
        valid_tiles = [
            # Bams (Bamboo) - 1b-9b
            "1b", "2b", "3b", "4b", "5b", "6b", "7b", "8b", "9b",
            # Cracks (Characters) - 1c-9c
            "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c",
            # Dots (Circles) - 1d-9d
            "1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d",
            # Winds
            "E", "S", "W", "N",
            # Dragons
            "R", "G", "W",
            # Flowers
            "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
            # Jokers
            "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10",
            # Blanks
            "B1", "B2", "B3", "B4", "B5", "B6"
        ]
        
        invalid_tiles = [tile for tile in tiles if tile not in valid_tiles]
        
        if invalid_tiles:
            return jsonify({
                "valid": False,
                "invalid_tiles": invalid_tiles,
                "error": "Invalid tile notation for American Mahjong"
            }), 400
        
        return jsonify({
            "valid": True,
            "message": "All tiles are valid American Mahjong tiles"
        })
        
    except Exception as e:
        logger.error(f"Error validating tiles: {str(e)}")
        return jsonify({"error": "Failed to validate tiles"}), 500 