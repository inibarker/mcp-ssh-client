import unittest
import time
import socket
from mcp_ssh_client.server import execute_command

class TestSSHIntegration(unittest.TestCase):
    HOST = "127.0.0.1"
    PORT = 2222
    USER = "testuser"
    PASS = "testpass"

    @classmethod
    def setUpClass(cls):
        """Wait for the SSH server to be ready."""
        max_retries = 10
        for i in range(max_retries):
            try:
                with socket.create_connection((cls.HOST, cls.PORT), timeout=2):
                    print("\nSSH server is ready!")
                    return
            except (ConnectionRefusedError, socket.timeout):
                print(f"Waiting for SSH server... (retry {i+1}/{max_retries})")
                time.sleep(2)
        raise RuntimeError("SSH server did not become ready in time.")

    def test_real_ssh_command(self):
        """Test executing a command on a real SSH server (Docker)."""
        result = execute_command(
            host=self.HOST,
            port=self.PORT,
            username=self.USER,
            password=self.PASS,
            command="whoami"
        )
        self.assertEqual(result.strip(), "testuser")

    def test_hostname_command(self):
        """Test another command."""
        result = execute_command(
            host=self.HOST,
            port=self.PORT,
            username=self.USER,
            password=self.PASS,
            command="hostname"
        )
        # In Docker it will return the container ID, but it shouldn't be empty
        self.assertTrue(len(result.strip()) > 0)

if __name__ == "__main__":
    unittest.main()
