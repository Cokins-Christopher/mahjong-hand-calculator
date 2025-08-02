from flask import Flask, request, jsonify
from flask_cors import CORS
from src.api.routes import api_bp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Enable CORS for all routes - allow requests from frontend
    CORS(app, origins=["http://localhost:3000"], supports_credentials=True)
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def health_check():
        """Health check endpoint"""
        return jsonify({
            "status": "healthy",
            "message": "Mahjong Hand Calculator API is running",
            "version": "1.0.0"
        })
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Endpoint not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"Starting Mahjong Hand Calculator API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug) 