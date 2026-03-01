"""
Manual test script for FastAPI endpoints.

This script demonstrates how to test the API endpoints manually.
Run the server first with: python backend/run_server.py

Then run this script: python backend/api/test_api_manual.py
"""

import pytest

# Skip this module in automated test suites
pytest.skip("Manual API tests skipped in automated suite", allow_module_level=True)

import requests
import json


BASE_URL = "http://localhost:8000"


def test_health_check():
    """Test the health check endpoint."""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_query_endpoint():
    """Test the /api/query endpoint."""
    print("\n=== Testing Query Endpoint ===")
    
    payload = {
        "query_text": "What is photosynthesis?"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/query",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Response ID: {data['response_id']}")
        print(f"Confidence Score: {data['confidence']['score']}")
        print(f"Should Warn: {data['confidence']['should_warn']}")
        print(f"Response Text (first 100 chars): {data['response_text'][:100]}...")
        print(f"Breakdown: {json.dumps(data['confidence']['breakdown'], indent=2)}")
        return data
    else:
        print(f"Error: {response.json()}")
        return None


def test_challenge_endpoint(response_data):
    """Test the /api/challenge endpoint."""
    print("\n=== Testing Challenge Endpoint ===")
    
    if not response_data:
        print("Skipping - no response data from query endpoint")
        return None
    
    payload = {
        "response_id": response_data["response_id"],
        "response_text": response_data["response_text"],
        "query_text": "What is photosynthesis?"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/challenge",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Challenge ID: {data['challenge_id']}")
        print(f"Question: {data['question_text']}")
        print(f"Related Response ID: {data['related_response_id']}")
        return data
    else:
        print(f"Error: {response.json()}")
        return None


def test_simplify_endpoint(response_data):
    """Test the /api/simplify endpoint."""
    print("\n=== Testing Simplify Endpoint ===")
    
    if not response_data:
        print("Skipping - no response data from query endpoint")
        return None
    
    payload = {
        "text": response_data["response_text"],
        "response_id": response_data["response_id"]
    }
    
    response = requests.post(
        f"{BASE_URL}/api/simplify",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Response ID: {data['response_id']}")
        print(f"Original (first 100 chars): {data['original_text'][:100]}...")
        print(f"Simplified (first 100 chars): {data['simplified_text'][:100]}...")
        return data
    else:
        print(f"Error: {response.json()}")
        return None


def main():
    """Run all tests."""
    print("=" * 60)
    print("FastAPI Endpoint Manual Tests")
    print("=" * 60)
    print("\nMake sure the server is running:")
    print("  python backend/run_server.py --reload")
    print("\nPress Enter to continue...")
    input()
    
    try:
        # Test health check
        if not test_health_check():
            print("\n❌ Health check failed. Is the server running?")
            return
        
        # Test query endpoint
        response_data = test_query_endpoint()
        
        # Test challenge endpoint
        if response_data:
            test_challenge_endpoint(response_data)
        
        # Test simplify endpoint
        if response_data:
            test_simplify_endpoint(response_data)
        
        print("\n" + "=" * 60)
        print("✓ All tests completed!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Connection error. Is the server running at http://localhost:8000?")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
