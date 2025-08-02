import React from 'react';

const RecommendationPanel = ({ recommendations = null, isLoading = false, error = null, selectedYear = 2024 }) => {
  // Tile display names for American Mahjong
  const tileNames = {
    // Bams (Bamboo)
    '1B': '1 Bam', '2B': '2 Bam', '3B': '3 Bam', '4B': '4 Bam', '5B': '5 Bam',
    '6B': '6 Bam', '7B': '7 Bam', '8B': '8 Bam', '9B': '9 Bam',
    // Cracks (Characters)
    '1C': '1 Crack', '2C': '2 Crack', '3C': '3 Crack', '4C': '4 Crack', '5C': '5 Crack',
    '6C': '6 Crack', '7C': '7 Crack', '8C': '8 Crack', '9C': '9 Crack',
    // Dots (Circles)
    '1D': '1 Dot', '2D': '2 Dot', '3D': '3 Dot', '4D': '4 Dot', '5D': '5 Dot',
    '6D': '6 Dot', '7D': '7 Dot', '8D': '8 Dot', '9D': '9 Dot',
    // Winds
    'E': 'East', 'S': 'South', 'W': 'West', 'N': 'North',
    // Dragons
    'R': 'Red Dragon', 'G': 'Green Dragon', '0': 'White Dragon',
    // Flowers
    'F1': 'Flower 1', 'F2': 'Flower 2', 'F3': 'Flower 3', 'F4': 'Flower 4',
    'F5': 'Flower 5', 'F6': 'Flower 6', 'F7': 'Flower 7', 'F8': 'Flower 8',
    // Jokers
    'J1': 'Joker 1', 'J2': 'Joker 2', 'J3': 'Joker 3', 'J4': 'Joker 4', 'J5': 'Joker 5',
    'J6': 'Joker 6', 'J7': 'Joker 7', 'J8': 'Joker 8', 'J9': 'Joker 9', 'J10': 'Joker 10',
    // Blanks
    'B1': 'Blank 1', 'B2': 'Blank 2', 'B3': 'Blank 3', 'B4': 'Blank 4', 'B5': 'Blank 5', 'B6': 'Blank 6'
  };

  // Suit colors for American Mahjong
  const suitColors = {
    bams: 'bg-green-500',
    cracks: 'bg-blue-500',
    dots: 'bg-red-500',
    winds: 'bg-yellow-500',
    dragons: 'bg-purple-500',
    flowers: 'bg-pink-500',
    jokers: 'bg-gray-500',
    blanks: 'bg-gray-300'
  };

  const getSuitForTile = (tile) => {
    if (tile.endsWith('B')) return 'bams';
    if (tile.endsWith('C')) return 'cracks';
    if (tile.endsWith('D')) return 'dots';
    if (['E', 'S', 'W', 'N'].includes(tile)) return 'winds';
    if (['R', 'G', '0'].includes(tile)) return 'dragons';
    if (tile.startsWith('F')) return 'flowers';
    if (tile.startsWith('J')) return 'jokers';
    if (tile.startsWith('B')) return 'blanks';
    return 'blanks';
  };

  const getTileColor = (tile) => {
    const suit = getSuitForTile(tile);
    return suitColors[suit];
  };

  if (isLoading) {
    return (
      <div className="w-full max-w-4xl mx-auto p-4">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold text-gray-800 mb-4">AI Recommendations</h3>
          <div className="flex items-center justify-center py-8">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
            <span className="ml-3 text-gray-600">Analyzing your hand...</span>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="w-full max-w-4xl mx-auto p-4">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold text-gray-800 mb-4">AI Recommendations</h3>
          <div className="bg-red-50 border border-red-200 rounded-lg p-4">
            <div className="flex items-center">
              <div className="text-red-500 text-xl mr-2">⚠️</div>
              <div>
                <div className="text-red-800 font-semibold">Error</div>
                <div className="text-red-600 text-sm">{error}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!recommendations) {
    return (
      <div className="w-full max-w-4xl mx-auto p-4">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold text-gray-800 mb-4">AI Recommendations</h3>
          <div className="text-center py-8 text-gray-500">
            <div className="text-4xl mb-2">🤖</div>
            <div>No recommendations yet</div>
            <div className="text-sm">Select 13 tiles and analyze your hand to get AI recommendations</div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-bold text-gray-800">AI Recommendations</h3>
          <div className="text-sm text-gray-600">
            American Mahjong {selectedYear} Rules
          </div>
        </div>
        
        {/* Strategic Advice */}
        {recommendations.strategic_advice && (
          <div className="mb-6">
            <h4 className="text-lg font-semibold text-gray-700 mb-3 flex items-center">
              <span className="text-purple-500 mr-2">🎯</span>
              Strategic Advice
            </h4>
            <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
              <div className="text-purple-800">
                {recommendations.strategic_advice}
              </div>
            </div>
          </div>
        )}

        {/* Best Discard */}
        {recommendations.best_discard && (
          <div className="mb-6">
            <h4 className="text-lg font-semibold text-gray-700 mb-3 flex items-center">
              <span className="text-red-500 mr-2">🗑️</span>
              Recommended Discard
            </h4>
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <div className={`${getTileColor(recommendations.best_discard)} text-white rounded-lg p-3 text-center mr-4`}>
                    <div className="text-sm font-bold">
                      {tileNames[recommendations.best_discard] || recommendations.best_discard}
                    </div>
                    <div className="text-xs opacity-75">
                      {recommendations.best_discard}
                    </div>
                  </div>
                  <div>
                    <div className="font-semibold text-red-800">
                      Discard this tile
                    </div>
                    <div className="text-sm text-red-600">
                      This tile has the lowest potential for improving your hand
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Best Draws */}
        {recommendations.best_draws && recommendations.best_draws.length > 0 && (
          <div className="mb-6">
            <h4 className="text-lg font-semibold text-gray-700 mb-3 flex items-center">
              <span className="text-green-500 mr-2">🎯</span>
              Best Draws
            </h4>
            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
              <div className="mb-3">
                <div className="text-sm text-green-600 mb-2">
                  These tiles would help improve your hand the most:
                </div>
                <div className="flex flex-wrap gap-2">
                  {recommendations.best_draws.map((tile, index) => (
                    <div
                      key={index}
                      className={`${getTileColor(tile)} text-white rounded-lg px-3 py-2 text-sm font-semibold flex items-center`}
                    >
                      <span className="mr-1">#{index + 1}</span>
                      <span>{tileNames[tile] || tile}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Reasoning */}
        {recommendations.reasoning && (
          <div className="mb-6">
            <h4 className="text-lg font-semibold text-gray-700 mb-3 flex items-center">
              <span className="text-blue-500 mr-2">💡</span>
              AI Reasoning
            </h4>
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <div className="text-blue-800">
                {recommendations.reasoning}
              </div>
            </div>
          </div>
        )}

        {/* Strategy Tips for American Mahjong */}
        <div>
          <h4 className="text-lg font-semibold text-gray-700 mb-3 flex items-center">
            <span className="text-orange-500 mr-2">📚</span>
            American Mahjong Strategy Tips
          </h4>
          <div className="bg-orange-50 border border-orange-200 rounded-lg p-4">
            <div className="space-y-2 text-sm text-orange-800">
              <div className="flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                <span>Focus on building hands that match the {selectedYear} card patterns</span>
              </div>
              <div className="flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                <span>Jokers are wild cards - use them strategically to complete hands</span>
              </div>
              <div className="flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                <span>Flowers and Dragons are often key to high-scoring hands</span>
              </div>
              <div className="flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                <span>Keep track of exposed tiles to avoid discarding needed pieces</span>
              </div>
              <div className="flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                <span>Consider the year-specific rules when planning your strategy</span>
              </div>
              <div className="flex items-start">
                <span className="text-orange-500 mr-2">•</span>
                <span>Higher point patterns (40-75 pts) are more valuable but harder to complete</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecommendationPanel; 