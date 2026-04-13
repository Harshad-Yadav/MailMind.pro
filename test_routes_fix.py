#!/usr/bin/env python3
"""Quick local test of the fixed FastAPI routes"""
import sys
from pathlib import Path

# Add the project to path
sys.path.insert(0, str(Path(__file__).parent))

from fastapi.testclient import TestClient
from backend.main import app
import json

client = TestClient(app)

print("=" * 60)
print("Testing FastAPI Routes After Fix")
print("=" * 60)

# Test 1: /tasks endpoint (should work now)
print("\n✓ Testing /tasks endpoint...")
response = client.get("/tasks")
print(f"  Status Code: {response.status_code}")
if response.status_code == 200:
    tasks = response.json()
    print(f"  Tasks returned: {len(tasks)}")
    for i, task in enumerate(tasks, 1):
        print(f"    Task {i}: {task.get('task_id')} - Grader: {task.get('grader')}")
else:
    print(f"  Error: {response.text}")

# Test 2: /api/tasks endpoint (should also work)
print("\n✓ Testing /api/tasks endpoint...")
response = client.get("/api/tasks")
print(f"  Status Code: {response.status_code}")
if response.status_code == 200:
    tasks = response.json()
    print(f"  Tasks returned: {len(tasks)}")
else:
    print(f"  Error: {response.text}")

# Test 3: /health endpoint
print("\n✓ Testing /health endpoint...")
response = client.get("/health")
print(f"  Status Code: {response.status_code}")
if response.status_code == 200:
    print(f"  Response: {response.json()}")

# Test 4: /metadata endpoint
print("\n✓ Testing /metadata endpoint...")
response = client.get("/metadata")
print(f"  Status Code: {response.status_code}")
if response.status_code == 200:
    print(f"  Response: {json.dumps(response.json(), indent=2)}")

print("\n" + "=" * 60)
print("All local tests completed!")
print("=" * 60)
