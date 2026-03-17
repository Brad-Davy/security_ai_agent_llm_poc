def build_prompt(query: str, context: str | None = None) -> str:
    base_system = (
        "You are a helpful, concise assistant. "
        "Answer clearly and technically where appropriate."
    )

    if context:
        return f"{base_system}\n\nContext:\n{context}\n\nUser:\n{query}"

    return f"{base_system}\n\nUser:\n{query}"
