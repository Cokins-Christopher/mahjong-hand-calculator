import axios from 'axios';

// Create axios instance with base configuration
const api = axios.create({
  baseURL: 'http://localhost:5000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API service class
class MahjongAPI {
  /**
   * Evaluate a 13-tile hand
   * @param {string[]} tiles - Array of 13 tile strings
   * @param {number} year - American Mahjong rules year
   * @returns {Promise<Object>} Hand analysis and recommendations
   */
  static async evaluateHand(tiles, year = 2024) {
    try {
      const response = await api.post('/evaluate-hand', { tiles, year });
      return response.data;
    } catch (error) {
      console.error('Error evaluating hand:', error);
      throw new Error(error.response?.data?.error || 'Failed to evaluate hand');
    }
  }

  /**
   * Validate tiles
   * @param {string[]} tiles - Array of tile strings to validate
   * @returns {Promise<Object>} Validation result
   */
  static async validateTiles(tiles) {
    try {
      const response = await api.post('/validate-tiles', { tiles });
      return response.data;
    } catch (error) {
      console.error('Error validating tiles:', error);
      throw new Error(error.response?.data?.error || 'Failed to validate tiles');
    }
  }

  /**
   * Get all patterns for a specific year
   * @param {number} year - American Mahjong rules year
   * @returns {Promise<Object>} Patterns data
   */
  static async getPatterns(year = 2024) {
    try {
      const response = await api.get(`/get-patterns?year=${year}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching patterns:', error);
      throw new Error(error.response?.data?.error || 'Failed to fetch patterns');
    }
  }

  /**
   * Get tile information and dragon associations
   * @returns {Promise<Object>} Tile information
   */
  static async getTileInfo() {
    try {
      const response = await api.get('/get-tile-info');
      return response.data;
    } catch (error) {
      console.error('Error fetching tile info:', error);
      throw new Error(error.response?.data?.error || 'Failed to fetch tile information');
    }
  }

  /**
   * Health check
   * @returns {Promise<Object>} API status
   */
  static async healthCheck() {
    try {
      const response = await axios.get('http://localhost:5000/');
      return response.data;
    } catch (error) {
      console.error('Error checking API health:', error);
      throw new Error('API is not responding');
    }
  }

  /**
   * Recognize tiles from image (placeholder for future implementation)
   * @param {File} imageFile - Image file to analyze
   * @returns {Promise<Object>} Recognition result
   */
  static async recognizeTiles(imageFile) {
    try {
      const formData = new FormData();
      formData.append('image', imageFile);
      
      const response = await api.post('/recognize-tiles', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Error recognizing tiles:', error);
      throw new Error(error.response?.data?.error || 'Failed to recognize tiles');
    }
  }
}

export default MahjongAPI; 