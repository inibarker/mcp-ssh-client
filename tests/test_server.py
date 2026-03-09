import unittest
from unittest.mock import MagicMock, patch

from mcp_ssh_client.server import execute_command


class TestSSHServer(unittest.TestCase):

    @patch("paramiko.SSHClient")
    def test_execute_command_success(self, mock_ssh_client: MagicMock) -> None:
        # Setup mock
        mock_client_instance = mock_ssh_client.return_value
        mock_stdout = MagicMock()
        mock_stdout.read.return_value = b"Hello from remote server"
        mock_stderr = MagicMock()
        mock_stderr.read.return_value = b""

        mock_client_instance.exec_command.return_value = (None, mock_stdout, mock_stderr)

        # Call the tool
        result = execute_command(
            host="example.com",
            username="testuser",
            command="echo 'Hello from remote server'",
            password="password",
        )

        # Assertions
        self.assertEqual(result, "Hello from remote server")
        mock_client_instance.connect.assert_called_with(
            hostname="example.com", port=22, username="testuser", password="password"
        )
        mock_client_instance.exec_command.assert_called_with("echo 'Hello from remote server'")

    @patch("paramiko.SSHClient")
    def test_execute_command_error(self, mock_ssh_client: MagicMock) -> None:
        # Setup mock
        mock_client_instance = mock_ssh_client.return_value
        mock_stdout = MagicMock()
        mock_stdout.read.return_value = b""
        mock_stderr = MagicMock()
        mock_stderr.read.return_value = b"Command not found"

        mock_client_instance.exec_command.return_value = (None, mock_stdout, mock_stderr)

        # Call the tool
        result = execute_command(
            host="example.com",
            username="testuser",
            command="invalid_command",
            password="password",
        )

        # Assertions
        self.assertIn("Errors:\nCommand not found", result)

    @patch("paramiko.SSHClient")
    def test_connection_failure(self, mock_ssh_client: MagicMock) -> None:
        # Setup mock to raise an exception on connect
        mock_client_instance = mock_ssh_client.return_value
        mock_client_instance.connect.side_effect = Exception("Connection refused")

        # Call the tool
        result = execute_command(
            host="example.com", username="testuser", command="ls", password="password"
        )

        # Assertions
        self.assertIn("Error connecting or executing command: Connection refused", result)

if __name__ == '__main__':
    unittest.main()
