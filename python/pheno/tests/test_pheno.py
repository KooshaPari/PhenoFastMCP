"""Smoke tests for the pheno framework layer."""

from __future__ import annotations

from pheno import Agent, Kit, KitRegistry


def test_agent_capability_lookup() -> None:
    agent = Agent(name="researcher", capabilities=["search", "summarize"])
    assert agent.can("search")
    assert not agent.can("deploy")


def test_kit_register_and_find() -> None:
    kit = Kit(name="research-kit")
    agent = Agent(name="researcher")
    kit.add(agent)

    assert kit.find("researcher") is agent
    assert kit.find("missing") is None


def test_kit_registry_roundtrip() -> None:
    registry = KitRegistry()
    kit = Kit(name="ops-kit")
    registry.register(kit)

    assert registry.get("ops-kit") is kit
    assert "ops-kit" in registry.names()
    assert registry.get("missing") is None
