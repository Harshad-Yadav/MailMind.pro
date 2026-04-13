import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add current directory to path
sys.path.append(os.getcwd())

class TestInferenceProxyLogic(unittest.TestCase):
    @patch('os.environ', {})
    def test_strict_env_failure(self):
        """Verify that the script exits if environment variables are missing."""
        import inference
        with patch('sys.exit') as mock_exit:
            import asyncio
            try:
                asyncio.run(inference.main())
            except SystemExit:
                pass
            mock_exit.assert_called_with(1)
            print("✓ Verified strict environment variable enforcement.")

    @patch.dict('os.environ', {
        'API_BASE_URL': 'https://proxy.scaler.com',
        'API_KEY': 'sk-test-key'
    })
    def test_url_normalization(self):
        """Verify that the base_url is correctly normalized with /v1."""
        import inference
        with patch('inference.OpenAI') as mock_openai:
            with patch('inference.wait_for_env', return_value=True):
                # Mock the pre-flight check to pass
                mock_openai.return_value.chat.completions.create.return_value = MagicMock()
                # Mock the HTTP client to fail early so we don't run the whole loop
                with patch('httpx.AsyncClient') as mock_http:
                    mock_http.return_value.__aenter__.side_effect = Exception("Stop early")
                    
                    import asyncio
                    try:
                        asyncio.run(inference.main())
                    except:
                        pass
                    
                    # Check first OpenAI call (constructor)
                    mock_openai.assert_called()
                    args, kwargs = mock_openai.call_args
                    self.assertEqual(kwargs['base_url'], 'https://proxy.scaler.com/v1')
                    print("✓ Verified URL normalization (appended /v1).")

if __name__ == "__main__":
    unittest.main()
