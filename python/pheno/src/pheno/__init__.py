"""Phenotype framework glue layer for FastMCP.

This package hosts framework-only code that previously lived in the
deprecated ``McpKit`` and ``AgentMCP`` phenotype repos. It is the Python
counterpart to the ``rust/`` and ``go/`` subtrees referenced in
``FORK-NOTES.md`` and is consumed by deployable servers in
``PhenoMCPServers`` — it is **not** a deployable server itself.

The layer is intentionally thin: it re-exports the FastMCP surface and
provides phenotype-specific helpers (agent registration, kit adapters,
HexaKit-style layout templates) that used to live in legacy repos.

Server implementations belong in https://github.com/KooshaPari/PhenoMCPServers.
"""

from __future__ import annotations

from pheno.agents import Agent, AgentContext
from pheno.kit import Kit, KitRegistry

__all__ = [
    "Agent",
    "AgentContext",
    "Kit",
    "KitRegistry",
    "__version__",
]

__version__ = "0.1.0"
