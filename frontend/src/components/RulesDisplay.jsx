import React from 'react';

const RulesDisplay = ({ selectedYear = 2024 }) => {
  // 2024 American Mahjong Rules
  const yearRules = {
    2024: {
      title: "2024 American Mahjong Rules",
      patterns: [
        {
          category: "2024 Patterns (25 points each unless noted)",
          hands: [
            { pattern: "222 000 2222 4444", description: "Any 2 Suits", points: 25, category: "X" },
            { pattern: "FFFF 2222 0000 24", description: "Any 2 Suits", points: 25, category: "X" },
            { pattern: "FF 2024 2222 2222", description: "Any 3 Suits, Like Kongs 2s or 4s", points: 25, category: "X" },
            { pattern: "NN EEE 2024 WWW SS", description: "2024 Any 1 Suit", points: 30, category: "C" }
          ]
        },
        {
          category: "2468 Patterns",
          hands: [
            { pattern: "222 444 6666 8888", description: "Any 1 or 2 Suits", points: 25, category: "X" },
            { pattern: "2 444 44 666 8888", description: "Any 3 Suits", points: 25, category: "X" },
            { pattern: "22 44 666 888 DDDD", description: "Any 1 Suit w Matching Dragons", points: 25, category: "X" },
            { pattern: "FFFF 4444 666 6666", description: "Any 3 Suits", points: 25, category: "X" },
            { pattern: "FF 2222 44 66 8888", description: "Any 1 or 2 Suits", points: 25, category: "X" },
            { pattern: "FF 222 44 666 88 88", description: "Any 3 Suits", points: 35, category: "C" }
          ]
        },
        {
          category: "Any Like Numbers",
          hands: [
            { pattern: "FFFF 111 1111 111", description: "Any 3 Suits", points: 25, category: "X" },
            { pattern: "11 DDD 11 DDD 1111", description: "Any 2 Suits, Pairs and Dragons Match", points: 25, category: "X" },
            { pattern: "FF 1111 NEWS 1111", description: "Any 2 Suits", points: 25, category: "X" }
          ]
        },
        {
          category: "Addition Hands (Lucky Sevens)",
          hands: [
            { pattern: "FF 1111 + 6666 = 7777", description: "Any 1 Suit", points: 25, category: "X" },
            { pattern: "FF 2222 + 5555 = 7777", description: "Any 1 Suit", points: 25, category: "X" },
            { pattern: "FF 3333 + 4444 = 7777", description: "Any 1 Suit", points: 25, category: "X" }
          ]
        },
        {
          category: "Quints (40-45 points)",
          hands: [
            { pattern: "FF 11111 22 33333", description: "Any 1 Suit, Any 3 Consec. Nos.", points: 40, category: "X" },
            { pattern: "11111 NNNN 88888", description: "Any 2 Suits, Quints Any 2 Non-Matching Nos., Any Wind", points: 40, category: "X" },
            { pattern: "11 22222 11 22222", description: "Any 2 Suits, Any 2 Consec. Nos.", points: 45, category: "X" },
            { pattern: "FFFFF DDDD 11111", description: "Any 2 Suits, Quint Any No.", points: 40, category: "X" }
          ]
        },
        {
          category: "Consecutive Run",
          hands: [
            { pattern: "111 22 3333 44 555", description: "These Nos. Only", points: 25, category: "X" },
            { pattern: "11 222 DDDD 333 44", description: "Any 4 Consec. Nos. in Any 1 Suit, Kong Opp. Dragons", points: 25, category: "X" },
            { pattern: "FF 1111 2222 3333", description: "Any 1 or 3 Suits, Any 3 Consec. Nos", points: 25, category: "X" },
            { pattern: "1 22 3333 1 22 3333", description: "Any 2 Suits, Any 3 Consec. Nos.", points: 30, category: "X" },
            { pattern: "11 22 333 444 DDDD", description: "Any 1 Suit, Any 4 Consec. Nos. w Matching Dragons", points: 25, category: "X" },
            { pattern: "FFFFF 123 444 444", description: "Any 3 Suits, Any 4 Consec. Nos.", points: 30, category: "X" },
            { pattern: "111 222 3333 4444", description: "Any 1 or 2 Suits, Any 4 Consec. Nos.", points: 30, category: "C" },
            { pattern: "111 222 111 222 33", description: "Any 3 Suits, Any 3 Consec. Nos.", points: 30, category: "C" }
          ]
        },
        {
          category: "13579 Patterns",
          hands: [
            { pattern: "111 33 5555 77 999", description: "Any 1 or 3 Suits", points: 25, category: "X" },
            { pattern: "111 333 3333 5555", description: "Any 2 or 3 Suits", points: 25, category: "X" },
            { pattern: "FF 11 333 5555 DDD", description: "Any 1 Suit w Matching Dragons", points: 25, category: "X" },
            { pattern: "11 33 55 7777 9999", description: "Any 3 Suits", points: 30, category: "X" },
            { pattern: "FFFF 3333 x 5555 = 15", description: "Any 3 Suits", points: 25, category: "X" },
            { pattern: "11 33 333 555 DDDD", description: "Any 3 Suits", points: 25, category: "X" },
            { pattern: "111 33 555 333 333", description: "Any 3 Suits, These Nos. Only", points: 35, category: "C" }
          ]
        },
        {
          category: "Winds - Dragons (25-30 points)",
          hands: [
            { pattern: "NNNN EEE WWW SSSS", description: "Any 2 Suits", points: 25, category: "X" },
            { pattern: "FFFF DDD DDDD DDD", description: "Any 3 Dragons", points: 25, category: "X" },
            { pattern: "NNN SSS 1111 2222", description: "Any 2 Suits, Any 2 Consec. Nos.", points: 25, category: "X" },
            { pattern: "FF NN EEE WWW SSSS", description: "Any 2 Suits", points: 25, category: "X" },
            { pattern: "NNNN 11 22 33 SSSS", description: "Any 1 Suit, Any 3 Consec. Nos.", points: 30, category: "X" },
            { pattern: "FF DDDD NEWS DDDD", description: "Any 2 Dragons", points: 25, category: "X" },
            { pattern: "NNN EW SSS 111 111", description: "Any 2 Suits, Any Like Nos.", points: 30, category: "C" }
          ]
        },
        {
          category: "369 Patterns",
          hands: [
            { pattern: "333 666 6666 9999", description: "Any 2 or 3 Suits", points: 25, category: "X" },
            { pattern: "FF 3 66 999 333 333", description: "Any 3 Suits, Like Pungs 3, 6 or 9", points: 25, category: "X" },
            { pattern: "FF 333 666 9999", description: "Any 1 or 3 Suits", points: 25, category: "X" },
            { pattern: "333 DDDD 333 DDDD", description: "Any 2 Suits, Pungs 3, 6 or 9 w Matching Dragons", points: 25, category: "X" },
            { pattern: "3333 66 66 66 9999", description: "Any 3 Suits, 3s and 9s Match", points: 30, category: "X" },
            { pattern: "FFFF 33 66 999 DDD", description: "Nos. Any 1 Suit, Any Opp. Dragon", points: 25, category: "X" },
            { pattern: "333 666 333 666 99", description: "Any 3 Suits", points: 30, category: "C" }
          ]
        },
        {
          category: "Singles and Pairs (50-75 points)",
          hands: [
            { pattern: "FF 22 46 88 22 46 88", description: "Any 2 Suits", points: 50, category: "C" },
            { pattern: "FF 11 33 55 55 77 99", description: "Any 2 Suits", points: 50, category: "C" },
            { pattern: "11 21123 112233", description: "Any 3 Suits, These Nos. Only", points: 50, category: "C" },
            { pattern: "FF 33 66 99 369 369", description: "Any 3 Suits", points: 50, category: "C" },
            { pattern: "11 22 33 44 55 DD DD", description: "Any 5 Consec. Nos. w Opp. Dragons", points: 50, category: "C" },
            { pattern: "2024 NN EW SS 2024", description: "Any 2 Suits", points: 75, category: "C" }
          ]
        }
      ]
    }
  };

  const currentRules = yearRules[selectedYear] || yearRules[2024];

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-xl font-bold text-gray-800">American Mahjong Rules - {selectedYear}</h3>
          <div className="text-sm text-gray-600">
            {currentRules.title}
          </div>
        </div>

        <div className="space-y-6">
          {currentRules.patterns.map((category, index) => (
            <div key={index} className="border border-gray-200 rounded-lg p-4">
              <h4 className="text-lg font-semibold text-gray-800 mb-3">
                {category.category}
              </h4>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {category.hands.map((hand, handIndex) => (
                  <div key={handIndex} className="bg-gray-50 border border-gray-200 rounded-lg p-3">
                    <div className="flex justify-between items-start mb-2">
                      <span className="font-mono text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded">
                        {hand.pattern}
                      </span>
                      <span className={`text-xs font-semibold px-2 py-1 rounded ${
                        hand.category === 'C' 
                          ? 'bg-purple-100 text-purple-800' 
                          : 'bg-green-100 text-green-800'
                      }`}>
                        {hand.points} pts ({hand.category})
                      </span>
                    </div>
                    <div className="text-xs text-gray-600">
                      {hand.description}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <h4 className="text-md font-semibold text-blue-800 mb-2">Legend</h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
            <div>
              <div className="font-semibold text-gray-700 mb-1">Tile Notation:</div>
              <div className="space-y-1 text-gray-600">
                <div>• 1B-9B: Bamboo tiles</div>
                <div>• 1C-9C: Character tiles</div>
                <div>• 1D-9D: Dot tiles</div>
                <div>• E,S,W,N: Winds</div>
                <div>• R,G,0: Dragons (Red, Green, White)</div>
                <div>• F: Flowers (Jokers)</div>
                <div>• 2024: Year tile</div>
              </div>
            </div>
            <div>
              <div className="font-semibold text-gray-700 mb-1">Categories:</div>
              <div className="space-y-1 text-gray-600">
                <div>• <span className="bg-green-100 text-green-800 px-1 rounded">X</span>: Exposed hands</div>
                <div>• <span className="bg-purple-100 text-purple-800 px-1 rounded">C</span>: Concealed hands only</div>
                <div>• Points: Fixed values per pattern</div>
                <div>• Suits: B=Bamboo, C=Characters, D=Dots</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RulesDisplay; 