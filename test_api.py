import requests
import json

# Test the API endpoints
base_url = "http://localhost:5000/api"

def test_get_patterns():
    """Test the get-patterns endpoint"""
    try:
        response = requests.get(f"{base_url}/get-patterns?year=2024")
        print(f"GET /get-patterns status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Patterns returned: {len(data.get('patterns', []))}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

def test_validate_tiles():
    """Test the validate-tiles endpoint"""
    try:
        # Test with valid tiles
        tiles = ["1B", "2B", "3B", "1C", "2C", "3C", "1D", "2D", "3D", "E", "S", "W", "N"]
        response = requests.post(f"{base_url}/validate-tiles", json={"tiles": tiles})
        print(f"POST /validate-tiles status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Validation result: {data.get('valid', False)}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

def test_get_tile_info():
    """Test the get-tile-info endpoint"""
    try:
        response = requests.get(f"{base_url}/get-tile-info")
        print(f"GET /get-tile-info status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Tile categories: {list(data.get('tile_categories', {}).keys())}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    print("Testing API endpoints...")
    test_get_patterns()
    test_validate_tiles()
    test_get_tile_info()
    print("API testing complete!") 