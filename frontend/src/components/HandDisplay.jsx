import React from 'react';

const HandDisplay = ({ tiles = [], handAnalysis = null, selectedYear = 2024 }) => {
  // Tile display names for American Mahjong
  const tileNames = {
    // Bams (Bamboo)
    '1b': '1 Bam', '2b': '2 Bam', '3b': '3 Bam', '4b': '4 Bam', '5b': '5 Bam',
    '6b': '6 Bam', '7b': '7 Bam', '8b': '8 Bam', '9b': '9 Bam',
    // Cracks (Characters)
    '1c': '1 Crack', '2c': '2 Crack', '3c': '3 Crack', '4c': '4 Crack', '5c': '5 Crack',
    '6c': '6 Crack', '7c': '7 Crack', '8c': '8 Crack', '9c': '9 Crack',
    // Dots (Circles)
    '1d': '1 Dot', '2d': '2 Dot', '3d': '3 Dot', '4d': '4 Dot', '5d': '5 Dot',
    '6d': '6 Dot', '7d': '7 Dot', '8d': '8 Dot', '9d': '9 Dot',
    // Winds
    'E': 'East', 'S': 'South', 'W': 'West', 'N': 'North',
    // Dragons
    'R': 'Red Dragon', 'G': 'Green Dragon', 'W': 'White Dragon',
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
    if (tile.startsWith('1b') || tile.startsWith('2b') || tile.startsWith('3b') || 
        tile.startsWith('4b') || tile.startsWith('5b') || tile.startsWith('6b') || 
        tile.startsWith('7b') || tile.startsWith('8b') || tile.startsWith('9b')) return 'bams';
    if (tile.startsWith('1c') || tile.startsWith('2c') || tile.startsWith('3c') || 
        tile.startsWith('4c') || tile.startsWith('5c') || tile.startsWith('6c') || 
        tile.startsWith('7c') || tile.startsWith('8c') || tile.startsWith('9c')) return 'cracks';
    if (tile.startsWith('1d') || tile.startsWith('2d') || tile.startsWith('3d') || 
        tile.startsWith('4d') || tile.startsWith('5d') || tile.startsWith('6d') || 
        tile.startsWith('7d') || tile.startsWith('8d') || tile.startsWith('9d')) return 'dots';
    if (['E', 'S', 'W', 'N'].includes(tile)) return 'winds';
    if (['R', 'G', 'W'].includes(tile)) return 'dragons';
    if (tile.startsWith('F')) return 'flowers';
    if (tile.startsWith('J')) return 'jokers';
    if (tile.startsWith('B')) return 'blanks';
    return 'blanks';
  };

  const getTileColor = (tile) => {
    const suit = getSuitForTile(tile);
    return suitColors[suit];
  };

  const getHandStrengthColor = (strength) => {
    if (strength.includes('Ready')) return 'text-green-600';
    if (strength.includes('Near')) return 'text-yellow-600';
    if (strength.includes('Developing')) return 'text-orange-600';
    return 'text-red-600';
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-bold text-gray-800">Current Hand</h3>
          <div className="text-sm text-gray-600">
            American Mahjong {selectedYear} Rules
          </div>
        </div>
        
        {/* Hand Analysis Summary */}
        {handAnalysis && (
          <div className="mb-6 p-4 bg-gray-50 rounded-lg">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="text-center">
                <div className="text-sm text-gray-600">Hand Value</div>
                <div className="text-2xl font-bold text-blue-600">
                  {handAnalysis.hand_value || 'N/A'}
                </div>
                <div className="text-xs text-gray-500">
                  Points based on {selectedYear} rules
                </div>
              </div>
              
              <div className="text-center">
                <div className="text-sm text-gray-600">Hand Strength</div>
                <div className={`text-lg font-semibold ${getHandStrengthColor(handAnalysis.hand_strength)}`}>
                  {handAnalysis.hand_strength}
                </div>
              </div>
              
              <div className="text-center">
                <div className="text-sm text-gray-600">Potential Hands</div>
                <div className="text-lg font-semibold text-purple-600">
                  {handAnalysis.potential_hands?.length || 0}
                </div>
                <div className="text-xs text-gray-500">
                  {handAnalysis.potential_hands?.length > 0 ? 'Available' : 'None found'}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tiles Display */}
        <div className="mb-4">
          <h4 className="text-lg font-semibold text-gray-700 mb-3">Your 13 Tiles</h4>
          
          {tiles.length === 0 ? (
            <div className="text-center py-8 text-gray-500">
              <div className="text-4xl mb-2">🀄</div>
              <div>No tiles selected yet</div>
              <div className="text-sm">Select 13 tiles to analyze your hand</div>
            </div>
          ) : (
            <div className="grid grid-cols-13 gap-2 p-4 bg-gray-100 rounded-lg">
              {tiles.map((tile, index) => (
                <div
                  key={`${tile}-${index}`}
                  className={`${getTileColor(tile)} text-white rounded-lg p-3 text-center shadow-md`}
                >
                  <div className="text-sm font-bold">
                    {tileNames[tile] || tile}
                  </div>
                  <div className="text-xs opacity-75">
                    {tile}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Tile Distribution */}
        {tiles.length > 0 && (
          <div className="mb-4">
            <h4 className="text-md font-semibold text-gray-700 mb-2">Tile Distribution</h4>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {['bams', 'cracks', 'dots', 'winds', 'dragons', 'flowers', 'jokers', 'blanks'].map((suit) => {
                const suitTiles = tiles.filter(tile => getSuitForTile(tile) === suit);
                const suitName = suit.charAt(0).toUpperCase() + suit.slice(1);
                
                if (suitTiles.length === 0) return null;
                
                return (
                  <div key={suit} className="bg-gray-50 rounded-lg p-3">
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-semibold text-gray-700">{suitName}</span>
                      <span className="text-sm text-gray-500">{suitTiles.length} tiles</span>
                    </div>
                    <div className="flex flex-wrap gap-1">
                      {suitTiles.map((tile, index) => (
                        <div
                          key={`${tile}-${index}`}
                          className={`${getTileColor(tile)} text-white text-xs rounded px-1 py-0.5`}
                        >
                          {tile}
                        </div>
                      ))}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Potential Hands */}
        {handAnalysis?.potential_hands && handAnalysis.potential_hands.length > 0 && (
          <div className="mb-4">
            <h4 className="text-md font-semibold text-gray-700 mb-2">Potential Hands ({selectedYear} Rules)</h4>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              {handAnalysis.potential_hands.map((hand, index) => (
                <div key={index} className="bg-purple-50 border border-purple-200 rounded-lg p-3">
                  <div className="flex justify-between items-center">
                    <span className="font-semibold text-purple-800">{hand.name}</span>
                    <span className="text-sm text-purple-600">
                      {hand.points} pts
                    </span>
                  </div>
                  <div className="text-xs text-purple-600 mt-1">
                    {hand.description}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Tiles to Win */}
        {handAnalysis?.tiles_to_win && handAnalysis.tiles_to_win.length > 0 && (
          <div>
            <h4 className="text-md font-semibold text-gray-700 mb-2">Tiles to Win</h4>
            <div className="flex flex-wrap gap-2">
              {handAnalysis.tiles_to_win.map((tile, index) => (
                <div
                  key={index}
                  className={`${getTileColor(tile)} text-white rounded-lg px-3 py-1 text-sm font-semibold`}
                >
                  {tileNames[tile] || tile}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default HandDisplay; 