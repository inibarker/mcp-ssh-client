import logging

import paramiko
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-ssh-client")

# Initialize FastMCP server
mcp = FastMCP("SSH Client")

@mcp.tool()
def execute_command(
    host: str, username: str, command: str, password: str | None = None, port: int = 22
) -> str:
    """
    Executes a command on a remote host via SSH.

    Args:
        host: The hostname or IP address of the remote server.
        username: The SSH username.
        command: The shell command to execute.
        password: The SSH password (optional if using keys).
        port: The SSH port (default 22).
    """
    logger.info(f"Executing command on {host}: {command}")
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname=host, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        
        if error:
            return f"Output:\n{output}\nErrors:\n{error}"
        return output
    except Exception as e:
        return f"Error connecting or executing command: {str(e)}"
    finally:
        client.close()

def main() -> None:
    mcp.run()

if __name__ == "__main__":
    main()
