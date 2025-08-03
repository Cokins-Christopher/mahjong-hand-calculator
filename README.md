# American Mahjong Hand Calculator

A comprehensive American Mahjong hand analysis tool that helps players evaluate their hands and get strategic recommendations. Built with React.js frontend and Python Flask backend, following American Mahjong Association rules for 2024.

## 🎯 Features

- **Manual Tile Input**: Intuitive tile selector with drag & drop interface
- **Hand Evaluation**: Calculate hand value and identify potential patterns
- **AI Recommendations**: Get strategic advice on best discards and draws
- **Real-time Analysis**: Automatic hand analysis when 13 tiles are selected
- **Responsive Design**: Mobile-friendly interface
- **Tile Recognition**: Placeholder for future image recognition feature

## 🏗️ Tech Stack

### Frontend
- **React.js 19+** - Modern React with hooks
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API communication
- **Heroicons** - Beautiful SVG icons

### Backend
- **Python 3.8+** - Core language
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **OpenCV** - Image processing (for future features)
- **NumPy** - Numerical computing

## 📋 Prerequisites

- **Node.js 18+** - For React development
- **Python 3.8+** - For Flask backend
- **npm** or **yarn** - Package managers

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd mahjong-hand-calculator
```

### 2. Backend Setup

Navigate to the backend directory and set up the Python environment:

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

The backend will start on `http://localhost:5000`

### 3. Frontend Setup

In a new terminal, navigate to the frontend directory:

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will start on `http://localhost:3000`

### 4. Verify Setup

1. Open `http://localhost:3000` in your browser
2. Check that the API status shows "Connected"
3. Try selecting 13 tiles to test the hand analysis

## 🎮 How to Use

### Basic Usage

1. **Select Tiles**: Click "Add Tiles" to open the tile selector
2. **Build Your Hand**: Select exactly 13 tiles to form your hand
3. **Get Analysis**: The AI automatically analyzes your hand when 13 tiles are selected
4. **View Recommendations**: See discard suggestions and best draws
5. **Follow Strategy**: Use the recommendations to improve your game

### Tile Notation

The app uses American Mahjong tile notation:

- **Bams (Bamboo)**: `1B`, `2B`, `3B`, ..., `9B`
- **Cracks (Characters)**: `1C`, `2C`, `3C`, ..., `9C`
- **Dots (Circles)**: `1D`, `2D`, `3D`, ..., `9D`
- **Winds**: `E` (East), `S` (South), `W` (West), `N` (North)
- **Dragons**: `R` (Red), `G` (Green), `0` (White)
- **Flowers**: `F`
- **Jokers**: `J`
- **Year Tiles**: `2024`

### Hand Analysis Features

- **Pattern Recognition**: Identify potential winning patterns
- **Hand Value Calculation**: Calculate points based on patterns
- **Tile Distribution**: Visual breakdown by suit
- **Strategic Recommendations**: Best discards and draws

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📁 Project Structure

```
mahjong-hand-calculator/
├── frontend/                 # React.js frontend
│   ├── public/              # Static files
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── TileSelector.jsx
│   │   │   ├── HandDisplay.jsx
│   │   │   └── RecommendationPanel.jsx
│   │   ├── services/        # API services
│   │   │   └── api.js
│   │   └── App.js          # Main app component
│   ├── package.json
│   └── tailwind.config.js
├── backend/                  # Python Flask backend
│   ├── src/
│   │   ├── api/            # API routes
│   │   │   └── routes.py
│   │   └── mahjong/        # Core Mahjong logic
│   │       ├── hand_evaluator.py
│   │       └── tile_calculator.py
│   ├── tests/              # Unit tests
│   │   └── test_hand_evaluator.py
│   ├── app.py              # Main Flask app
│   └── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 API Endpoints

### Hand Evaluation
- **POST** `/api/evaluate-hand`
  - Body: `{"tiles": ["1B", "2B", "3B", ...]}`
  - Returns: Hand analysis and recommendations

### Tile Validation
- **POST** `/api/validate-tiles`
  - Body: `{"tiles": ["1B", "2B", "3B", ...]}`
  - Returns: Validation result

### Health Check
- **GET** `/`
  - Returns: API status

## 🎯 American Mahjong Rules

This calculator follows **American Mahjong Association** rules for 2024:

- **13-tile hands** (plus 1 draw for 14-tile complete hands)
- **Pattern recognition** (60+ official patterns)
- **Point calculation** based on pattern complexity
- **American tile notation** (1B-9B, 1C-9C, 1D-9D, Winds, Dragons, Flowers, Jokers)

### Supported Pattern Categories
- **2024 Patterns** - Year-specific patterns
- **2468 Patterns** - Even number combinations
- **Any Like Numbers** - Same numbers across suits
- **Addition Hands** - Mathematical combinations
- **Quint Patterns** - Five-of-a-kind combinations
- **Consecutive Run** - Sequential number patterns
- **13579 Patterns** - Odd number combinations
- **Winds & Dragons** - Honor tile patterns
- **369 Patterns** - Specific number combinations
- **Singles and Pairs** - Mixed tile patterns
- And more...

## 🚧 Future Features

- [ ] **Image Recognition**: Upload photos of tiles for automatic detection
- [ ] **Advanced Pattern Detection**: More complex winning pattern recognition
- [ ] **Game State Tracking**: Track discards and draws throughout the game
- [ ] **Multiplayer Support**: Real-time game analysis
- [ ] **Statistics**: Track hand performance over time
- [ ] **Tutorial Mode**: Learn American Mahjong rules and strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **American Mahjong Association** - For the official 2024 rules
- **Mahjong Community** - For feedback and testing
- **React Team** - For the amazing frontend framework
- **Flask Team** - For the lightweight Python web framework
- **Tailwind CSS** - For the utility-first CSS framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include your operating system and browser information

---

**Happy Mahjong! 🀄** 