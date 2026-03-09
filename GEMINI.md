# GEMINI.md - Instructional Context for mcp-ssh-client

This document provides context and guidelines for interacting with the `mcp-ssh-client` project.

## Project Overview
`mcp-ssh-client` is a **Model Context Protocol (MCP)** server designed to empower AI agents with the ability to interact as SSH clients. This allows agents to securely and remotely manipulate systems, execute commands, and manage files on remote servers as part of a broader workflow.

- **Current Status:** Infrastructure and automation setup phase.
- **Core Technology:** Model Context Protocol (MCP).
- **Automation:** Integrated with Gemini CLI for issue triaging, pull request reviews, and autonomous plan execution via GitHub Actions.

## Project Structure
- `.github/`: Contains GitHub Action workflows and Gemini CLI command configurations.
- `LICENSE`: Project is licensed under the GNU General Public License v3.0 (GPLv3).
- `README.md`: Basic project introduction.
- `GEMINI.md`: This file, providing instructions and project context.

## Building and Running
The implementation uses **Python 3.10+** with the **Model Context Protocol (MCP) Python SDK** and `FastMCP`.

### Setup
Ensure you have Python installed. You can install the dependencies using:
```bash
pip install .
```

### Running the Server
To run the server locally:
```bash
python -m mcp_ssh_client.server
```

### Configuration for Claude Desktop
Add the following to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "mcp-ssh-client": {
      "command": "python",
      "args": ["-m", "mcp_ssh_client.server"]
    }
  }
}
```

## Development Conventions
### Automation with Gemini CLI
The project is configured to use Gemini CLI for several automated tasks. Maintainers can interact with Gemini via GitHub issue comments using the following commands:
- `@gemini-cli /invoke [prompt]`: Runs a one-off task or query.
- `@gemini-cli /approve`: Approves a proposed plan for execution.
- `!gemini /triage`: (Internal) Used by workflows for issue labeling.

### Coding Standards
- **Implementation Language:** Python 3.10+
- **MCP Framework:** `mcp-sdk-python` (FastMCP)
- **SSH Library:** `paramiko`
- **Security First:** Given the project involves SSH and remote system access, security-centric coding (input validation, credential handling) is a top priority.
- **Tools over Scripts:** Prefer defining tools via `@mcp.tool()` for AI interaction.

## Next Steps for the AI Assistant
1. **Refinement:** Add support for SSH key authentication in addition to passwords.
2. **Features:** Implement more tools (e.g., file upload/download via SCP/SFTP).
3. **Validation:** Set up a testing environment (e.g., using a local Docker container) to verify connectivity.
