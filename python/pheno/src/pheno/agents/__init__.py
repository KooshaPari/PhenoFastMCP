"""HexaKit-style agent adapters absorbed from the deprecated ``AgentMCP`` repo.

These helpers let phenotype servers register agents that follow the
HexaKit layout convention without pulling the legacy ``agentmcp`` wheel.
Server implementations stay in ``PhenoMCPServers``; this module is the
framework glue they import.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    """Per-request context shared with a registered agent.

    Wraps the FastMCP ``Context`` so that phenotype code does not need to
    import fastmcp directly; the underlying context is exposed via
    ``raw`` for advanced use.
    """

    name: str
    raw: Any = None
    state: dict[str, Any] = field(default_factory=dict)


@dataclass
class Agent:
    """A named agent definition absorbed from ``AgentMCP``.

    Agents are descriptors: they carry a name and a small registry of
    capabilities. The actual MCP tools/resources are registered on the
    FastMCP server in the consuming project; this object is the metadata
    layer that other phenotype tooling (CLI, observability) reads.
    """

    name: str
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def can(self, capability: str) -> bool:
        return capability in self.capabilities
