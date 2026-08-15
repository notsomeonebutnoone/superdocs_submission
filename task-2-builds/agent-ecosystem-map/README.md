# Agent ecosystem map

Research date: 2026-08-06. “Fit” means a plausible extension path, not a shipped marketplace listing. Revalidate marketplace rules before committing engineering time.

## Baseline

SuperDocs documents a REST API, a remote Streamable HTTP MCP endpoint, and a public plugin repository with Claude Code and Cursor assets. Sources: [docs](https://docs.superdocs.app), [MCP setup](https://docs.superdocs.app/mcp/setup), [plugin repository](https://github.com/superdocsapp/superdocs-plugin).

| Ecosystem | Extension mechanics | SuperDocs wedge | Distribution move | Constraint |
|---|---|---|---|---|
| Claude Code / Claude | Remote or local MCP; plugins can bundle MCP, skills, commands, prompts | Finish customer-facing docs from the coding workflow | Maintain plugin; separately evaluate Connectors Directory | Hosted directory authentication and review requirements differ from manual MCP setup |
| Cursor | `.cursor/mcp.json`; plugins with rules, skills, commands, hooks | Teach the agent when to move from Markdown to a reviewed document | Package the existing assets for Marketplace review | Marketplace review and per-user secrets |
| VS Code / Copilot | MCP gallery or workspace `mcp.json`; full extensions for richer UI | Direct document tools without a new editor extension | Make MCP metadata discoverable in `@mcp` search | Workspace secrets and local-server trust controls |
| ChatGPT / Codex | Streamable HTTP MCP in Codex; reviewed plugins for hosted ChatGPT | MCP-backed draft, edit, review, revert, and export tools | Direct Codex guide first; plugin submission second | Publisher verification, hosted auth, safety annotations, evaluations |
| Gemini CLI | Extensions bundle MCP, skills, prompts, hooks, subagents | Thin manifest around hosted MCP plus the SuperDocs skill | Public repository and extension discovery | CLI/platform transition risk; confirm current path before launch |
| Microsoft Copilot Studio | Agent-level MCP connections; certified connectors | Proposal and policy agents that hand document execution to SuperDocs | Validate direct connection, then assess certification | Certification is heavier and requirements can change |
| n8n | MCP Client and MCP Client Tool; community nodes | Brief-to-reviewed-export workflow templates | Publish one MCP-based template before a custom node | Weaker product discovery than a verified node |
| Zapier | Public API integrations with triggers, actions, searches | REST actions for create/upload, edit job, status, and export | Build only a narrow beta integration | Separate adapter; asynchronous jobs and files complicate UX |
| LangChain / LangGraph | Typed tools; `langchain-mcp-adapters` for HTTP MCP | Reference graph with a human approval pause before export | Publish tested recipe | Developer-led distribution and session handling |
| CrewAI | Custom tools or MCP via `mcps`, including Streamable HTTP | Research crew hands a document task to SuperDocs | Publish reference crew | Tool mapping, secret handling, and no clear public marketplace path |

## Priority

1. **Package what already works:** Claude Code, Cursor, VS Code, and direct Codex.
2. **Show a complete workflow:** one n8n template and one framework recipe.
3. **Earn hosted distribution:** ChatGPT and connector directories after authentication and review work is scoped.
4. **Build REST adapters only with evidence:** Zapier should follow demand, not precede it.

## Shared risks

- Bearer keys work for several direct clients, while hosted directories may require OAuth or platform credential flows.
- Write, revert, archive, and export tools need accurate safety annotations and human approval boundaries.
- Project-level MCP configuration can leak secrets if committed.
- Exposing every tool can reduce tool-selection accuracy; lead with a workflow-sized subset.
- A working endpoint is not an approved marketplace listing.
- Extension rules change quickly; verify sources again at launch.

## Sources

- [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [Anthropic connector submission](https://claude.com/docs/connectors/building/submission)
- [Cursor MCP and plugins](https://cursor.com/docs/context/mcp)
- [VS Code MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [Codex MCP](https://developers.openai.com/codex/mcp/)
- [OpenAI plugin submission](https://developers.openai.com/plugins/deploy/submission)
- [Gemini CLI extensions](https://geminicli.com/docs/extensions/)
- [Copilot Studio MCP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp)
- [n8n MCP Client](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient.md)
- [Zapier Developer Platform](https://docs.zapier.com/platform/home)
- [LangChain MCP adapter](https://docs.langchain.com/oss/python/langchain/mcp)
- [CrewAI MCP](https://docs.crewai.com/en/mcp/overview)

All sources accessed 2026-08-06.
