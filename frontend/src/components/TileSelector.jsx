import React, { useState, useEffect } from 'react';

const TileSelector = ({ onTilesChange, selectedTiles = [], onYearChange, selectedYear = 2024 }) => {
  const [tiles, setTiles] = useState(selectedTiles);
  const [showSelector, setShowSelector] = useState(false);
  const [year, setYear] = useState(selectedYear);

  // American Mahjong tile sets - using uppercase notation to match backend
  const allTiles = {
    bams: ['1B', '2B', '3B', '4B', '5B', '6B', '7B', '8B', '9B'],
    cracks: ['1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C'],
    dots: ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D'],
    winds: ['E', 'S', 'W', 'N'],
    dragons: ['R', 'G', '0'], // Red, Green, White (using '0' for White Dragon)
    flowers: ['F'], // Single flower tile
    jokers: ['J'], // Single joker tile
    blanks: ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
  };

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
    'F': 'Flower',
    // Jokers
    'J': 'Joker',
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
    if (tile.endsWith('B')) return 'bams';
    if (tile.endsWith('C')) return 'cracks';
    if (tile.endsWith('D')) return 'dots';
    if (['E', 'S', 'W', 'N'].includes(tile)) return 'winds';
    if (['R', 'G', '0'].includes(tile)) return 'dragons';
    if (tile === 'F') return 'flowers';
    if (tile === 'J') return 'jokers';
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
              const sampleHand = ['1B', '2B', '3B', '1C', '2C', '3C', '1D', '2D', '3D', 'E', 'S', 'W', 'N'];
              setTiles(sampleHand);
            }}
            className="px-3 py-1 bg-green-500 text-white rounded text-sm hover:bg-green-600 transition-colors"
          >
            Sample Hand
          </button>
          <button
            onClick={() => {
              const dragonHand = ['R', 'G', '0', '1B', '2B', '3B', '4B', '5B', '6B', '7B', '8B', '9B', 'E'];
              setTiles(dragonHand);
            }}
            className="px-3 py-1 bg-purple-500 text-white rounded text-sm hover:bg-purple-600 transition-colors"
          >
            Dragon Hand
          </button>
          <button
            onClick={() => {
              const flowerHand = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'J', 'J', 'J', 'J', 'J'];
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