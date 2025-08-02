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
        "tiles": ["1B", "2B", "3B", "4C", "5C", "6C", "7D", "8D", "9D", "E", "S", "W", "N"],
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
        if not isinstance(tiles, list):
            return jsonify({"error": "Tiles must be a list"}), 400
        
        if len(tiles) != 13:
            return jsonify({"error": f"Must provide exactly 13 tiles, got {len(tiles)}"}), 400
        
        # Validate tile format
        invalid_tiles = []
        for tile in tiles:
            if not isinstance(tile, str):
                invalid_tiles.append(f"Tile must be string, got {type(tile)}")
            elif not _is_valid_tile_format(tile):
                invalid_tiles.append(f"Invalid tile format: {tile}")
        
        if invalid_tiles:
            return jsonify({"error": "Invalid tiles found", "details": invalid_tiles}), 400
        
        # Initialize evaluators
        evaluator = HandEvaluator()
        calculator = TileCalculator()
        
        # Evaluate the hand
        hand_analysis = evaluator.evaluate_hand(tiles, year)
        
        # Get recommendations
        recommendations = calculator.get_recommendations(tiles, hand_analysis, year)
        
        response = {
            "hand_analysis": hand_analysis,
            "recommendations": recommendations,
            "validation": {
                "tile_count": len(tiles),
                "year": year,
                "all_tiles_valid": True
            }
        }
        
        logger.info(f"Hand evaluated successfully for year {year}: {tiles}")
        return jsonify(response)
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({"error": str(e)}), 400
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
        
        if not isinstance(tiles, list):
            return jsonify({"error": "Tiles must be a list"}), 400
        
        # Basic validation for American Mahjong tiles
        valid_tiles = [
            # Bams (Bamboo) - 1B-9B
            "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B",
            # Cracks (Characters) - 1C-9C
            "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C",
            # Dots (Circles) - 1D-9D
            "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D",
            # Winds
            "E", "S", "W", "N",
            # Dragons
            "R", "G", "0",
            # Flowers (Jokers)
            "F",
            # Year tiles
            "2024"
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
            "message": "All tiles are valid American Mahjong tiles",
            "tile_count": len(tiles)
        })
        
    except Exception as e:
        logger.error(f"Error validating tiles: {str(e)}")
        return jsonify({"error": "Failed to validate tiles"}), 500

@api_bp.route('/get-patterns', methods=['GET'])
def get_patterns():
    """
    Get available patterns for a specific year
    """
    try:
        year = request.args.get('year', 2024, type=int)
        
        evaluator = HandEvaluator()
        year_rules = evaluator.year_rules.get(year, {})
        patterns = year_rules.get('patterns', {})
        
        # Format patterns for API response
        formatted_patterns = []
        for pattern_id, pattern_info in patterns.items():
            formatted_patterns.append({
                "id": pattern_id,
                "name": pattern_id.replace('_', ' ').title(),
                "pattern": pattern_info['pattern'],
                "description": pattern_info['description'],
                "points": pattern_info['points'],
                "category": pattern_info['category'],
                "suit_requirement": pattern_info.get('suit_requirement', 'any'),
                "joker_allowed": pattern_info.get('joker_allowed', True)
            })
        
        return jsonify({
            "year": year,
            "patterns": formatted_patterns,
            "total_patterns": len(formatted_patterns)
        })
        
    except Exception as e:
        logger.error(f"Error getting patterns: {str(e)}")
        return jsonify({"error": "Failed to get patterns"}), 500

@api_bp.route('/get-tile-info', methods=['GET'])
def get_tile_info():
    """
    Get information about American Mahjong tiles
    """
    try:
        evaluator = HandEvaluator()
        
        return jsonify({
            "tile_categories": {
                "bams": evaluator.valid_tiles['bams'],
                "cracks": evaluator.valid_tiles['cracks'],
                "dots": evaluator.valid_tiles['dots'],
                "winds": evaluator.valid_tiles['winds'],
                "dragons": evaluator.valid_tiles['dragons'],
                "flowers": evaluator.valid_tiles['flowers'],
                "year_tiles": evaluator.valid_tiles['year_tiles']
            },
            "dragon_associations": evaluator.dragon_associations,
            "total_tiles": sum(len(tiles) for tiles in evaluator.valid_tiles.values())
        })
        
    except Exception as e:
        logger.error(f"Error getting tile info: {str(e)}")
        return jsonify({"error": "Failed to get tile info"}), 500

def _is_valid_tile_format(tile: str) -> bool:
    """Check if a tile string has valid format"""
    if not isinstance(tile, str):
        return False
    
    # Check for numbered tiles (1B-9B, 1C-9C, 1D-9D)
    if len(tile) == 2 and tile[0].isdigit() and tile[1] in ['B', 'C', 'D']:
        number = int(tile[0])
        return 1 <= number <= 9
    
    # Check for winds
    if tile in ['E', 'S', 'W', 'N']:
        return True
    
    # Check for dragons
    if tile in ['R', 'G', '0']:
        return True
    
    # Check for flowers
    if tile == 'F':
        return True
    
    # Check for year tiles
    if tile == '2024':
        return True
    
    return False 