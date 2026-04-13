import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from backend.schemas.env import AgentAction, TaskDefinition
from graders.email_grader import grade_action

def test_grader_range():
    # Mock task
    task = TaskDefinition(
        task_id="test",
        difficulty="easy",
        title="Test",
        description="Test",
        required_outputs=["category"],
        reward_weights={"category": 1.0},
        max_steps=1
    )
    
    # Case 1: Perfect match
    action_perfect = AgentAction(category="billing")
    expected_perfect = {"category": "billing"}
    result_perfect = grade_action(task, action_perfect, expected_perfect)
    print(f"Perfect Score: {result_perfect.score} (Expected 0.99)")
    assert 0.0 < result_perfect.score < 1.0
    
    # Case 2: Zero match
    action_fail = AgentAction(category="spam")
    expected_fail = {"category": "billing"}
    result_fail = grade_action(task, action_fail, expected_fail)
    print(f"Zero Score: {result_fail.score} (Expected 0.01)")
    assert 0.0 < result_fail.score < 1.0
    
    print("✓ Grader verification successful. All scores are strictly between 0 and 1.")

if __name__ == "__main__":
    try:
        test_grader_range()
    except Exception as e:
        print(f"Verification failed: {e}")
        sys.exit(1)
