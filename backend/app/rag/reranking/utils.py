def build_pairs(
    query: str,
    chunks,
):

    return [
        (
            query,
            chunk.text
        )
        for chunk in chunks
    ]