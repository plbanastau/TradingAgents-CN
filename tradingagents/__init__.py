"""TradingAgents-CN: A multi-agent trading framework for Chinese markets.

This package provides AI-powered trading agents that analyze financial data,
news, and market signals to support investment decision-making for A-shares
and other Chinese financial instruments.
"""

__version__ = "0.1.0"
__author__ = "TradingAgents-CN Contributors"
__license__ = "MIT"

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

__all__ = [
    "TradingAgentsGraph",
    "DEFAULT_CONFIG",
    "__version__",
]
