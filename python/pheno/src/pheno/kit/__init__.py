"""Kit abstractions absorbed from the deprecated ``McpKit`` framework.

``Kit`` is a thin grouping primitive for related agents, tools, and
resources. The full ``McpKit`` server scaffolding (CLI, lifecycle, LSP
shim) is intentionally **not** re-implemented here — servers use
FastMCP directly. This module only preserves the layout vocabulary that
``AgentMCP`` hex adapters depended on.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pheno.agents import Agent


@dataclass
class Kit:
    """A named collection of agents.

    Mirrors the ``HexaKit`` template layout used by ``AgentMCP`` so
    existing server repos can drop the legacy import and pull from
    ``pheno.kit`` instead.
    """

    name: str
    agents: list["Agent"] = field(default_factory=list)

    def add(self, agent: "Agent") -> None:
        self.agents.append(agent)

    def find(self, name: str) -> "Agent | None":
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None


class KitRegistry:
    """Process-wide registry of named kits.

    Replaces the ad-hoc module-level dict that ``McpKit`` exposed; keeps
    the same ``register``/``get`` shape so migration is a one-line
    import change.
    """

    def __init__(self) -> None:
        self._kits: dict[str, Kit] = {}

    def register(self, kit: Kit) -> None:
        self._kits[kit.name] = kit

    def get(self, name: str) -> Kit | None:
        return self._kits.get(name)

    def names(self) -> list[str]:
        return sorted(self._kits)
