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
> [!IMPORTANT]
> The implementation is in its initial stages. Source code and build scripts are yet to be added.

- **TODO:** Identify the implementation language (likely Node.js or Python) and add corresponding build/run instructions here once `package.json` or `pyproject.toml` is created.
- **Standard MCP Pattern:** Once implemented, the server will likely be run using a command like `npx mcp-ssh-client` or `python -m mcp_ssh_client`.

## Development Conventions
### Automation with Gemini CLI
The project is configured to use Gemini CLI for several automated tasks. Maintainers can interact with Gemini via GitHub issue comments using the following commands:
- `@gemini-cli /invoke [prompt]`: Runs a one-off task or query.
- `@gemini-cli /approve`: Approves a proposed plan for execution.
- `!gemini /triage`: (Internal) Used by workflows for issue labeling.

### Coding Standards
- **Wait for Implementation:** Standards for naming, typing, and testing will be established once the core source code is scaffolded.
- **Security First:** Given the project involves SSH and remote system access, security-centric coding (input validation, credential handling) is a top priority.

## Next Steps for the AI Assistant
1. **Scaffolding:** Help the user decide on a tech stack (e.g., TypeScript/Node.js or Python).
2. **Implementation:** Create the entry point for the MCP server and implement basic SSH connectivity.
3. **Validation:** Set up a testing environment (e.g., using a mock SSH server or a local Docker container) to verify connectivity.
