# PhenoFastMCP

Phenotype-org hard fork of [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp).

This repository is the **MCP framework boundary** — server/client SDK, transports,
tool registration, and CLI. It is **not** a collection of deployable MCP servers;
those live in [PhenoMCPServers](https://github.com/KooshaPari/PhenoMCPServers).

## Upstream

| Field | Value |
|-------|-------|
| Upstream | `https://github.com/PrefectHQ/fastmcp` |
| Baseline tag | `v3.4.2` |
| Sync remote | `upstream` → PrefectHQ/fastmcp |
| Branches mirrored | **140** (all `refs/heads/*` at fork time) |
| Tags mirrored | **105** |
| PR refs | **not mirrored** (GitHub rejects `refs/pull/*` on forks) |

## Phenotype extensions (planned)

Language tier order for native work:

1. **Tier 0:** Go, Rust, Zig, Mojo — protocol core, codegen, perf paths
2. **Tier 1:** C#, TypeScript, Python 3.14+, Java — bindings
3. **Tier 2:** Shell, PowerShell — CLI wrappers and install scripts

Python (fastmcp) remains the primary binding today; tier-0 siblings land under
`go/`, `rust/`, etc. as forks of optimal upstream SDKs (see `FORK-NOTES.md`).

## Framework glue layer

Framework-only code absorbed from the deprecated `McpKit` and `AgentMCP`
phenotype repos lives under [`python/pheno/`](python/pheno/). It is the
Python counterpart to the planned `rust/` and `go/` subtrees, exposes a
thin `pheno.agents` / `pheno.kit` surface on top of FastMCP, and is
consumed by deployable servers in [PhenoMCPServers](https://github.com/KooshaPari/PhenoMCPServers).
See `FORK-NOTES.md` for the absorption status of each source repo.

## Consumption

```bash
pip install git+https://github.com/KooshaPari/PhenoFastMCP.git@v3.4.2
# or editable during dev:
pip install -e ".[dev]"
```

Deployable servers depend on this package; they do **not** vendor framework code.

## Governance

- `main` tracks upstream `main` plus phenotype merge commits
- `feat/phenotype-foundation` — docs, fork policy, first phenotype patches
- `phenotype/superset` — integration branch for merged useful upstream branches

See `FORK-NOTES.md` for branch merge inventory and sync commands.
