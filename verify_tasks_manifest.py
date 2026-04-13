import yaml
from pathlib import Path
from backend.main import app
from fastapi.testclient import TestClient

print('Openenv manifest:')
text = Path('openenv.yaml').read_text()
print(text)

data = yaml.safe_load(text)
print('\nManifest tasks:')
for t in data.get('tasks', []):
    print(t)

print('\nAPI /tasks response:')
client = TestClient(app)
resp = client.get('/tasks')
print(resp.status_code)
print(resp.json())
