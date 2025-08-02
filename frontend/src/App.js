import React, { useState, useEffect } from 'react';
import TileSelector from './components/TileSelector';
import HandDisplay from './components/HandDisplay';
import RecommendationPanel from './components/RecommendationPanel';
import MahjongAPI from './services/api';

function App() {
  const [selectedTiles, setSelectedTiles] = useState([]);
  const [selectedYear, setSelectedYear] = useState(2024);
  const [handAnalysis, setHandAnalysis] = useState(null);
  const [recommendations, setRecommendations] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  // Check API health on component mount
  useEffect(() => {
    checkApiHealth();
  }, []);

  const checkApiHealth = async () => {
    try {
      await MahjongAPI.healthCheck();
      setApiStatus('healthy');
    } catch (err) {
      setApiStatus('unhealthy');
      console.error('API health check failed:', err);
    }
  };

  const handleTilesChange = (tiles) => {
    setSelectedTiles(tiles);
    setError(null);
    
    // Clear previous analysis if tiles are removed
    if (tiles.length < 13) {
      setHandAnalysis(null);
      setRecommendations(null);
    }
  };

  const handleYearChange = (year) => {
    setSelectedYear(year);
    // Clear analysis when year changes
    setHandAnalysis(null);
    setRecommendations(null);
  };

  const analyzeHand = async () => {
    if (selectedTiles.length !== 13) {
      setError("Please select exactly 13 tiles before analyzing");
      return;
    }

    setIsLoading(true);
    setError(null);
    
    try {
      // Validate tiles first
      const validation = await MahjongAPI.validateTiles(selectedTiles);
      if (!validation.valid) {
        throw new Error(`Invalid tiles: ${validation.invalid_tiles?.join(', ')}`);
      }

      // Evaluate hand with year parameter
      const result = await MahjongAPI.evaluateHand(selectedTiles, selectedYear);
      
      setHandAnalysis(result.hand_analysis);
      setRecommendations(result.recommendations);
      
    } catch (err) {
      setError(err.message);
      setHandAnalysis(null);
      setRecommendations(null);
    } finally {
      setIsLoading(false);
    }
  };

  const retryAnalysis = () => {
    if (selectedTiles.length === 13) {
      analyzeHand();
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <div className="text-3xl mr-3">🀄</div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">American Mahjong Hand Calculator</h1>
                <p className="text-sm text-gray-600">Analyze your hand and get strategic recommendations</p>
              </div>
            </div>
            
            {/* API Status */}
            <div className="flex items-center">
              <div className={`w-3 h-3 rounded-full mr-2 ${
                apiStatus === 'healthy' ? 'bg-green-500' : 
                apiStatus === 'unhealthy' ? 'bg-red-500' : 'bg-yellow-500'
              }`}></div>
              <span className="text-sm text-gray-600">
                {apiStatus === 'healthy' ? 'API Connected' : 
                 apiStatus === 'unhealthy' ? 'API Disconnected' : 'Checking API...'}
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-6">
        {/* API Error Banner */}
        {apiStatus === 'unhealthy' && (
          <div className="mb-6 mx-4">
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <div className="text-red-500 text-xl mr-2">⚠️</div>
                  <div>
                    <div className="text-red-800 font-semibold">Backend API Not Available</div>
                    <div className="text-red-600 text-sm">
                      Make sure the Flask backend is running on http://localhost:5000
                    </div>
                  </div>
                </div>
                <button
                  onClick={checkApiHealth}
                  className="px-3 py-1 bg-red-500 text-white rounded text-sm hover:bg-red-600 transition-colors"
                >
                  Retry Connection
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Tile Selector */}
        <TileSelector 
          onTilesChange={handleTilesChange}
          selectedTiles={selectedTiles}
          onYearChange={handleYearChange}
          selectedYear={selectedYear}
        />

        {/* Find Hand Button */}
        {selectedTiles.length === 13 && (
          <div className="w-full max-w-4xl mx-auto p-4">
            <div className="text-center">
              <button
                onClick={analyzeHand}
                disabled={isLoading || apiStatus === 'unhealthy'}
                className="px-8 py-3 bg-blue-500 text-white rounded-lg text-lg font-semibold hover:bg-blue-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isLoading ? (
                  <div className="flex items-center">
                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                    Analyzing Hand...
                  </div>
                ) : (
                  'Find Hand'
                )}
              </button>
              {apiStatus === 'unhealthy' && (
                <p className="text-sm text-red-600 mt-2">
                  Cannot analyze hand - API is not connected
                </p>
              )}
            </div>
          </div>
        )}

        {/* Hand Display */}
        <HandDisplay 
          tiles={selectedTiles}
          handAnalysis={handAnalysis}
          selectedYear={selectedYear}
        />

        {/* Recommendation Panel */}
        <RecommendationPanel 
          recommendations={recommendations}
          isLoading={isLoading}
          error={error}
          selectedYear={selectedYear}
        />

        {/* Error Retry Button */}
        {error && selectedTiles.length === 13 && (
          <div className="w-full max-w-4xl mx-auto p-4">
            <div className="text-center">
              <button
                onClick={retryAnalysis}
                className="px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
              >
                Retry Analysis
              </button>
            </div>
          </div>
        )}

        {/* Instructions */}
        {selectedTiles.length === 0 && (
          <div className="w-full max-w-4xl mx-auto p-4">
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-blue-800 mb-3">How to Use</h3>
              <div className="space-y-2 text-blue-700">
                <div className="flex items-start">
                  <span className="text-blue-500 mr-2">1.</span>
                  <span>Select the year for American Mahjong rules (they change annually)</span>
                </div>
                <div className="flex items-start">
                  <span className="text-blue-500 mr-2">2.</span>
                  <span>Click "Add Tiles" to open the tile selector</span>
                </div>
                <div className="flex items-start">
                  <span className="text-blue-500 mr-2">3.</span>
                  <span>Select exactly 13 tiles to form your hand</span>
                </div>
                <div className="flex items-start">
                  <span className="text-blue-500 mr-2">4.</span>
                  <span>Click "Find Hand" to analyze your hand based on {selectedYear} rules</span>
                </div>
                <div className="flex items-start">
                  <span className="text-blue-500 mr-2">5.</span>
                  <span>Use the recommendations to improve your strategy</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t mt-12">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <div className="text-center text-gray-600">
            <p className="text-sm">
              American Mahjong Hand Calculator - Built with React, Flask, and AI
            </p>
            <p className="text-xs mt-1">
              Follows American Mahjong Association rules for {selectedYear}
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
