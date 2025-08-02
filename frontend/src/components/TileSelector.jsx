import React, { useState, useEffect } from 'react';

const TileSelector = ({ onTilesChange, selectedTiles = [], onYearChange, selectedYear = 2024 }) => {
  const [tiles, setTiles] = useState(selectedTiles);
  const [showSelector, setShowSelector] = useState(false);
  const [year, setYear] = useState(selectedYear);

  // American Mahjong tile sets
  const allTiles = {
    bams: ['1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b'],
    cracks: ['1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c'],
    dots: ['1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d'],
    winds: ['E', 'S', 'W', 'N'],
    dragons: ['R', 'G', 'W'], // Red, Green, White
    flowers: ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'],
    jokers: ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10'],
    blanks: ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
  };

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

  // Available years for American Mahjong rules
  const availableYears = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014];

  useEffect(() => {
    onTilesChange(tiles);
  }, [tiles, onTilesChange]);

  useEffect(() => {
    onYearChange(year);
  }, [year, onYearChange]);

  const addTile = (tile) => {
    if (tiles.length < 13) {
      setTiles([...tiles, tile]);
    }
  };

  const removeTile = (index) => {
    const newTiles = tiles.filter((_, i) => i !== index);
    setTiles(newTiles);
  };

  const clearTiles = () => {
    setTiles([]);
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

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      {/* Year Selection */}
      <div className="mb-6 bg-white rounded-lg shadow p-4">
        <h3 className="text-lg font-semibold text-gray-800 mb-3">American Mahjong Rules Year</h3>
        <div className="flex items-center space-x-4">
          <label htmlFor="year-select" className="text-sm font-medium text-gray-700">
            Select Year:
          </label>
          <select
            id="year-select"
            value={year}
            onChange={(e) => setYear(parseInt(e.target.value))}
            className="border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {availableYears.map(y => (
              <option key={y} value={y}>{y}</option>
            ))}
          </select>
          <span className="text-sm text-gray-500">
            Rules change annually in American Mahjong
          </span>
        </div>
      </div>

      {/* Selected Tiles Display */}
      <div className="mb-6">
        <div className="flex justify-between items-center mb-2">
          <h3 className="text-lg font-semibold text-gray-800">
            Selected Tiles ({tiles.length}/13)
          </h3>
          <div className="space-x-2">
            <button
              onClick={() => setShowSelector(!showSelector)}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
            >
              {showSelector ? 'Hide Selector' : 'Add Tiles'}
            </button>
            <button
              onClick={clearTiles}
              className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600 transition-colors"
            >
              Clear All
            </button>
          </div>
        </div>
        
        {/* Selected tiles grid */}
        <div className="grid grid-cols-13 gap-2 p-4 bg-gray-100 rounded-lg min-h-[80px]">
          {tiles.map((tile, index) => (
            <div
              key={`${tile}-${index}`}
              className={`relative ${getTileColor(tile)} text-white rounded-lg p-2 text-center cursor-pointer hover:opacity-80 transition-opacity`}
              onClick={() => removeTile(index)}
              title={`Remove ${tileNames[tile] || tile}`}
            >
              <div className="text-xs font-bold">
                {tileNames[tile] || tile}
              </div>
              <div className="text-xs opacity-75">
                {tile}
              </div>
              <div className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                ×
              </div>
            </div>
          ))}
          
          {/* Empty slots */}
          {Array.from({ length: 13 - tiles.length }).map((_, index) => (
            <div
              key={`empty-${index}`}
              className="border-2 border-dashed border-gray-300 rounded-lg p-2 text-center text-gray-400"
            >
              Empty
            </div>
          ))}
        </div>
      </div>

      {/* Tile Selector */}
      {showSelector && (
        <div className="mb-6">
          <h4 className="text-md font-semibold text-gray-700 mb-3">Select Tiles</h4>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {Object.entries(allTiles).map(([suit, suitTiles]) => (
              <div key={suit} className="bg-white rounded-lg shadow p-4">
                <h5 className="font-semibold text-gray-800 mb-3 capitalize">
                  {suit} Tiles
                </h5>
                <div className="grid grid-cols-3 gap-2">
                  {suitTiles.map((tile) => (
                    <button
                      key={tile}
                      onClick={() => addTile(tile)}
                      disabled={tiles.length >= 13}
                      className={`${suitColors[suit]} text-white rounded-lg p-2 text-center hover:opacity-80 transition-opacity disabled:opacity-50 disabled:cursor-not-allowed`}
                      title={tileNames[tile] || tile}
                    >
                      <div className="text-xs font-bold">
                        {tileNames[tile] || tile}
                      </div>
                      <div className="text-xs opacity-75">
                        {tile}
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Quick Add Buttons */}
      <div className="mb-4">
        <h4 className="text-md font-semibold text-gray-700 mb-2">Quick Add</h4>
        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => {
              const sampleHand = ['1b', '2b', '3b', '1c', '2c', '3c', '1d', '2d', '3d', 'E', 'S', 'W', 'N'];
              setTiles(sampleHand);
            }}
            className="px-3 py-1 bg-green-500 text-white rounded text-sm hover:bg-green-600 transition-colors"
          >
            Sample Hand
          </button>
          <button
            onClick={() => {
              const dragonHand = ['R', 'G', 'W', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', 'E'];
              setTiles(dragonHand);
            }}
            className="px-3 py-1 bg-purple-500 text-white rounded text-sm hover:bg-purple-600 transition-colors"
          >
            Dragon Hand
          </button>
          <button
            onClick={() => {
              const flowerHand = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'J1', 'J2', 'J3', 'J4', 'J5'];
              setTiles(flowerHand);
            }}
            className="px-3 py-1 bg-pink-500 text-white rounded text-sm hover:bg-pink-600 transition-colors"
          >
            Flower Hand
          </button>
        </div>
      </div>
    </div>
  );
};

export default TileSelector; 