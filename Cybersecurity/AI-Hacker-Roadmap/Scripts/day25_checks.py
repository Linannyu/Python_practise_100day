# From the AI-Hacker-Roadmap root, run: python3 -m Scripts.day25_checks
from Labs.CodeReview.profile_app import (
    SAMPLE_PROFILES,
    build_product_query,
    get_profile,
    render_search,
)

print("H1 baseline:")
print(build_product_query("books"))

print("H1 changed:")
print(build_product_query("books'"))

print("H2 baseline:")
print(render_search("hello"))

print("H2 changed:")
print(render_search("<b>hello</b>"))

print("H3 baseline:")
print(get_profile("alice", "alice", SAMPLE_PROFILES))

print("H3 changed:")
print(get_profile("bob", "alice", SAMPLE_PROFILES))
