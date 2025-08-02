import React from 'react';

const RelevantPatterns = ({ tiles = [], patterns = [], selectedYear = 2024 }) => {
  // Helper function to get tile suit
  const getTileSuit = (tile) => {
    if (tile.endsWith('B')) return 'B';
    if (tile.endsWith('C')) return 'C';
    if (tile.endsWith('D')) return 'D';
    return null;
  };

  // Helper function to get tile number
  const getTileNumber = (tile) => {
    const match = tile.match(/^(\d+)/);
    return match ? parseInt(match[1]) : null;
  };

  // Analyze hand composition in detail
  const analyzeHand = () => {
    const analysis = {
      suits: new Set(),
      numbers: new Set(),
      dragons: [],
      winds: [],
      flowers: [],
      yearTiles: [],
      tileCounts: {},
      numberCounts: {},
      suitCounts: { B: 0, C: 0, D: 0 },
      consecutiveRuns: [],
      windCombinations: []
    };

    tiles.forEach(tile => {
      const suit = getTileSuit(tile);
      const number = getTileNumber(tile);
      
      // Count tiles
      analysis.tileCounts[tile] = (analysis.tileCounts[tile] || 0) + 1;
      
      if (suit) {
        analysis.suits.add(suit);
        analysis.suitCounts[suit]++;
        if (number) {
          analysis.numbers.add(number);
          analysis.numberCounts[number] = (analysis.numberCounts[number] || 0) + 1;
        }
      } else if (['R', 'G', '0'].includes(tile)) {
        analysis.dragons.push(tile);
      } else if (['E', 'S', 'W', 'N'].includes(tile)) {
        analysis.winds.push(tile);
      } else if (tile.startsWith('F')) {
        analysis.flowers.push(tile);
      } else if (tile === '2024') {
        analysis.yearTiles.push(tile);
      }
    });

    // Find consecutive runs
    const sortedNumbers = Array.from(analysis.numbers).sort((a, b) => a - b);
    for (let i = 0; i < sortedNumbers.length - 2; i++) {
      if (sortedNumbers[i + 1] === sortedNumbers[i] + 1 && 
          sortedNumbers[i + 2] === sortedNumbers[i] + 2) {
        analysis.consecutiveRuns.push([sortedNumbers[i], sortedNumbers[i + 1], sortedNumbers[i + 2]]);
      }
    }

    // Find wind combinations
    if (analysis.winds.length >= 2) {
      analysis.windCombinations = analysis.winds;
    }

    return analysis;
  };

  // Calculate pattern match score and completion percentage
  const calculatePatternMatch = (pattern, handAnalysis) => {
    const patternStr = pattern.pattern_string || pattern.pattern;
    if (!patternStr) return { score: 0, completion: 0, matchedTiles: [], missingTiles: [] };

    let score = 0;
    let totalRequired = 0;
    const matchedTiles = [];
    const missingTiles = [];

    // Parse pattern components
    const components = patternStr.split(' ').filter(c => c.length > 0);
    
    for (const component of components) {
      if (component === '2024') {
        totalRequired++;
        if (handAnalysis.yearTiles.length > 0) {
          score++;
          matchedTiles.push('2024');
        } else {
          missingTiles.push('2024');
        }
      } else if (component === 'DDDD') {
        totalRequired += 4;
        const dragonCount = Math.min(handAnalysis.dragons.length, 4);
        score += dragonCount;
        if (dragonCount > 0) {
          matchedTiles.push(...handAnalysis.dragons.slice(0, dragonCount));
        }
        if (dragonCount < 4) {
          missingTiles.push(...Array(4 - dragonCount).fill('Dragon'));
        }
      } else if (component === 'NEWS') {
        totalRequired += 4;
        const windCount = Math.min(handAnalysis.winds.length, 4);
        score += windCount;
        if (windCount > 0) {
          matchedTiles.push(...handAnalysis.winds.slice(0, windCount));
        }
        if (windCount < 4) {
          missingTiles.push(...Array(4 - windCount).fill('Wind'));
        }
      } else if (component === 'FFFF') {
        totalRequired += 4;
        const flowerCount = Math.min(handAnalysis.flowers.length, 4);
        score += flowerCount;
        if (flowerCount > 0) {
          matchedTiles.push(...handAnalysis.flowers.slice(0, flowerCount));
        }
        if (flowerCount < 4) {
          missingTiles.push(...Array(4 - flowerCount).fill('Flower'));
        }
      } else if (component.match(/^(\d+)$/)) {
        // Single number requirement
        const number = parseInt(component);
        totalRequired++;
        if (handAnalysis.numberCounts[number] > 0) {
          score++;
          matchedTiles.push(`${number}`);
        } else {
          missingTiles.push(`${number}`);
        }
      } else if (component.match(/^(\d+)([BCD])$/)) {
        // Numbered tile requirement
        const match = component.match(/^(\d+)([BCD])$/);
        const number = parseInt(match[1]);
        const suit = match[2];
        totalRequired++;
        const tileKey = `${number}${suit}`;
        if (handAnalysis.tileCounts[tileKey] > 0) {
          score++;
          matchedTiles.push(tileKey);
        } else {
          missingTiles.push(tileKey);
        }
      } else if (component.match(/^(\d+){2,}$/)) {
        // Multiple of same number (like 22, 333, 4444)
        const number = parseInt(component[0]);
        const count = component.length;
        totalRequired += count;
        const available = handAnalysis.numberCounts[number] || 0;
        const matched = Math.min(available, count);
        score += matched;
        if (matched > 0) {
          matchedTiles.push(...Array(matched).fill(`${number}`));
        }
        if (matched < count) {
          missingTiles.push(...Array(count - matched).fill(`${number}`));
        }
      }
    }

    // Calculate completion percentage based on 14 total tiles
    const completion = totalRequired > 0 ? (score / totalRequired) * 100 : 0;
    
    return {
      score,
      completion: Math.round(completion),
      matchedTiles,
      missingTiles,
      totalRequired
    };
  };

  // Get pattern category and priority
  const getPatternCategory = (pattern) => {
    const patternStr = pattern.pattern_string || pattern.pattern;
    
    if (patternStr.includes('2024')) return '2024 Patterns';
    if (patternStr.includes('NEWS') || patternStr.includes('NNNN') || patternStr.includes('EEEE')) return 'Wind Patterns';
    if (patternStr.includes('DDDD') || patternStr.includes('DDD')) return 'Dragon Patterns';
    if (patternStr.includes('FFFF')) return 'Flower Patterns';
    if (patternStr.includes('111') || patternStr.includes('222') || patternStr.includes('333')) return 'Consecutive Patterns';
    if (patternStr.includes('369')) return '369 Patterns';
    if (patternStr.includes('13579')) return '13579 Patterns';
    if (patternStr.includes('2468')) return '2468 Patterns';
    if (patternStr.includes('Quints') || patternStr.includes('11111')) return 'Quint Patterns';
    if (patternStr.includes('Singles') || patternStr.includes('FF 22')) return 'Singles & Pairs';
    
    return 'Other Patterns';
  };

  // Get category color
  const getCategoryColor = (category) => {
    const colors = {
      '2024 Patterns': 'bg-red-100 text-red-800',
      'Wind Patterns': 'bg-blue-100 text-blue-800',
      'Dragon Patterns': 'bg-green-100 text-green-800',
      'Flower Patterns': 'bg-yellow-100 text-yellow-800',
      'Consecutive Patterns': 'bg-purple-100 text-purple-800',
      '369 Patterns': 'bg-indigo-100 text-indigo-800',
      '13579 Patterns': 'bg-pink-100 text-pink-800',
      '2468 Patterns': 'bg-orange-100 text-orange-800',
      'Quint Patterns': 'bg-teal-100 text-teal-800',
      'Singles & Pairs': 'bg-gray-100 text-gray-800',
      'Other Patterns': 'bg-gray-100 text-gray-800'
    };
    return colors[category] || 'bg-gray-100 text-gray-800';
  };

  // Only show component if tiles are selected
  if (tiles.length === 0) {
    return null;
  }

  const handAnalysis = analyzeHand();
  
  // Calculate match scores for all patterns
  const patternsWithScores = patterns.map(pattern => {
    const match = calculatePatternMatch(pattern, handAnalysis);
    const category = getPatternCategory(pattern);
    
    return {
      ...pattern,
      match,
      category
    };
  });

  // Filter patterns with at least some relevance and sort by completion percentage
  const relevantPatterns = patternsWithScores
    .filter(p => p.match.completion > 0)
    .sort((a, b) => b.match.completion - a.match.completion);

  // Group patterns by category
  const groupedPatterns = relevantPatterns.reduce((acc, pattern) => {
    if (!acc[pattern.category]) acc[pattern.category] = [];
    acc[pattern.category].push(pattern);
    return acc;
  }, {});

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-bold text-gray-800">Relevant Patterns</h3>
          <div className="text-sm text-gray-600">
            Based on your {tiles.length} tiles ({selectedYear} Rules)
          </div>
        </div>

        {/* Hand Analysis Summary */}
        <div className="mb-6 p-4 bg-gray-50 rounded-lg">
          <h4 className="text-md font-semibold text-gray-700 mb-3">Your Hand Composition</h4>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div>
              <span className="font-semibold">Suits:</span>
              <span className="ml-2 text-gray-600">
                {Array.from(handAnalysis.suits).join(', ') || 'None'}
              </span>
            </div>
            <div>
              <span className="font-semibold">Numbers:</span>
              <span className="ml-2 text-gray-600">
                {Array.from(handAnalysis.numbers).sort().join(', ') || 'None'}
              </span>
            </div>
            <div>
              <span className="font-semibold">Dragons:</span>
              <span className="ml-2 text-gray-600">
                {handAnalysis.dragons.length || 'None'}
              </span>
            </div>
            <div>
              <span className="font-semibold">Winds:</span>
              <span className="ml-2 text-gray-600">
                {handAnalysis.winds.length || 'None'}
              </span>
            </div>
            <div>
              <span className="font-semibold">Flowers:</span>
              <span className="ml-2 text-gray-600">
                {handAnalysis.flowers.length || 'None'}
              </span>
            </div>
            <div>
              <span className="font-semibold">Year Tiles:</span>
              <span className="ml-2 text-gray-600">
                {handAnalysis.yearTiles.length || 'None'}
              </span>
            </div>
            {handAnalysis.consecutiveRuns.length > 0 && (
              <div>
                <span className="font-semibold">Consecutive Runs:</span>
                <span className="ml-2 text-gray-600">
                  {handAnalysis.consecutiveRuns.map(run => run.join('-')).join(', ')}
                </span>
              </div>
            )}
            {handAnalysis.windCombinations.length > 0 && (
              <div>
                <span className="font-semibold">Wind Combo:</span>
                <span className="ml-2 text-gray-600">
                  {handAnalysis.windCombinations.join(', ')}
                </span>
              </div>
            )}
          </div>
        </div>

        {/* Relevant Patterns */}
        {Object.keys(groupedPatterns).length > 0 ? (
          <div className="space-y-4">
            {Object.entries(groupedPatterns).map(([category, patterns]) => (
              <div key={category} className="border border-gray-200 rounded-lg p-4">
                <h4 className="text-lg font-semibold text-gray-800 mb-3">
                  {category}
                </h4>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                  {patterns.map((pattern, index) => (
                    <div key={index} className="bg-gray-50 border border-gray-200 rounded-lg p-3">
                      {/* Pattern Name */}
                      <div className="mb-2">
                        <h5 className="font-semibold text-gray-800 text-sm">
                          {pattern.name || pattern.id}
                        </h5>
                      </div>
                      
                      <div className="flex justify-between items-start mb-2">
                        <span className="font-mono text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded">
                          {pattern.pattern_string || pattern.pattern}
                        </span>
                        <span className={`text-xs font-semibold px-2 py-1 rounded ${
                          pattern.category === 'C' 
                            ? 'bg-purple-100 text-purple-800' 
                            : 'bg-green-100 text-green-800'
                        }`}>
                          {pattern.points} pts ({pattern.category})
                        </span>
                      </div>
                      
                      {/* Completion Progress */}
                      <div className="mb-2">
                        <div className="flex justify-between text-xs text-gray-600 mb-1">
                          <span>Completion: {pattern.match.completion}%</span>
                          <span>{tiles.length}/14 tiles</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                          <div 
                            className={`h-2 rounded-full ${
                              pattern.match.completion >= 80 ? 'bg-green-500' :
                              pattern.match.completion >= 60 ? 'bg-yellow-500' :
                              pattern.match.completion >= 40 ? 'bg-orange-500' : 'bg-red-500'
                            }`}
                            style={{ width: `${pattern.match.completion}%` }}
                          ></div>
                        </div>
                      </div>
                      
                      <div className="text-xs text-gray-600 mb-2">
                        {pattern.description}
                      </div>
                      
                      {/* Matched Tiles */}
                      {pattern.match.matchedTiles.length > 0 && (
                        <div className="text-xs text-gray-500 mb-1">
                          <span className="font-semibold text-green-600">✓ Matched:</span> {pattern.match.matchedTiles.join(', ')}
                        </div>
                      )}
                      
                      {/* Missing Tiles */}
                      {pattern.match.missingTiles.length > 0 && (
                        <div className="text-xs text-gray-500 mb-1">
                          <span className="font-semibold text-red-600">✗ Need:</span> {pattern.match.missingTiles.join(', ')}
                        </div>
                      )}
                      
                      {pattern.suit_requirement && (
                        <div className="text-xs text-gray-500">
                          <span className="font-semibold">Suit:</span> {pattern.suit_requirement}
                        </div>
                      )}
                      {pattern.joker_allowed !== undefined && (
                        <div className="text-xs text-gray-500">
                          <span className="font-semibold">Jokers:</span> {pattern.joker_allowed ? 'Allowed' : 'Not allowed'}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-8 text-gray-500">
            <div className="text-4xl mb-2">🔍</div>
            <div>No relevant patterns found</div>
            <div className="text-sm">Try adding more tiles or different combinations</div>
          </div>
        )}

        {/* Pattern Tips */}
        <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <h4 className="text-md font-semibold text-blue-800 mb-2">Pattern Matching Tips</h4>
          <div className="space-y-2 text-sm text-blue-700">
            <div className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
              <span>Patterns are ranked by completion percentage - focus on those with 60%+ completion</span>
            </div>
            <div className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
              <span>Green progress bars indicate high completion (80%+) - these are your best options</span>
            </div>
            <div className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
              <span>Look for patterns that use tiles you already have in abundance</span>
            </div>
            <div className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
              <span>Consider drawing the missing tiles shown in red to complete high-scoring patterns</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RelevantPatterns; 