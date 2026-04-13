import requests
import json

# Test the deployed Space endpoint
url = "https://MidNightCoders01-MailMind.hf.space/tasks"

print(f"Testing endpoint: {url}\n")

try:
    response = requests.get(url, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Status: {'✅ SUCCESS' if response.status_code == 200 else '❌ FAILED'}\n")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Number of tasks: {len(data)}\n")
        
        for i, task in enumerate(data, 1):
            print(f"Task {i}:")
            print(f"  ID: {task.get('task_id', 'N/A')}")
            print(f"  Title: {task.get('title', 'N/A')}")
            print(f"  Grader: {task.get('grader', 'N/A')}")
            print(f"  Difficulty: {task.get('difficulty', 'N/A')}")
            print()
        
        # Full JSON dump
        print("Full Response:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Response text: {response.text}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTrying alternative URL...")
    
    url2 = "https://MidNightCoders01-MailMind.ai.hf.space/tasks"
    try:
        response = requests.get(url2, timeout=10)
        print(f"Alternative URL {url2} Status: {response.status_code}")
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
    except Exception as e2:
        print(f"Alternative also failed: {e2}")
