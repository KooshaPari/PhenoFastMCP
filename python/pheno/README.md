# pheno

Phenotype framework glue layer for [PhenoFastMCP](https://github.com/KooshaPari/PhenoFastMCP).

This package is the **framework layer** absorbed from the deprecated
`McpKit` and `AgentMCP` phenotype repos. It re-exports the FastMCP
surface and provides phenotype-specific helpers (agent registration,
kit adapters, HexaKit-style layout templates) for downstream servers.

It is **not** a deployable MCP server. Deployable servers live in
[PhenoMCPServers](https://github.com/KooshaPari/PhenoMCPServers); they
depend on this package and on PhenoFastMCP — they do **not** vendor
framework code.

## What's absorbed

| Source (deprecated)              | Lands in           | Status   |
| -------------------------------- | ------------------ | -------- |
| `McpKit` framework crates        | `rust/`, `go/`     | planned  |
| `AgentMCP` hex adapters          | `pheno.agents`     | absorbed |
| `McpKit` kit/registry primitives | `pheno.kit`        | absorbed |
| `PhenoMCP` hand-rolled server    | (delete, use FastMCP) | done  |
| `phenotype-python-sdk` mcp-kit   | (remove package)   | done     |

## Install

```bash
pip install git+https://github.com/KooshaPari/PhenoFastMCP.git#subdirectory=python/pheno
```

## Usage

```python
from pheno import Agent, Kit, KitRegistry

agent = Agent(name="researcher", capabilities=["search", "summarize"])
kit = Kit(name="research-kit")
kit.add(agent)

registry = KitRegistry()
registry.register(kit)
```

See [PhenoMCPServers](https://github.com/KooshaPari/PhenoMCPServers) for
deployable server examples that consume this layer.
