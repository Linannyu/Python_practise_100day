"""Intentionally flawed local code-review sample for Days 23–25.

This file does not connect to a database, web server, or network.
"""


def build_product_query(category: str) -> str:
    """Return a query string without executing it."""
    return "SELECT name FROM products WHERE category = '" + category + "'"


def render_search(term: str) -> str:
    """Return a small HTML fragment."""
    return f"<p>You searched for: {term}</p>"


def get_profile(
    requested_user: str,
    current_user: str,
    profiles: dict[str, dict[str, str]],
) -> dict[str, str]:
    """Return a requested profile without an ownership check."""
    _ = current_user
    return profiles[requested_user]


SAMPLE_PROFILES = {
    "alice": {"display_name": "Alice", "plan": "student"},
    "bob": {"display_name": "Bob", "plan": "student"},
}

