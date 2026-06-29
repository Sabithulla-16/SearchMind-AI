import asyncio

from app.pipeline.search_pipeline import search_pipeline


async def main():

    result = await search_pipeline.run(

        "What is Python used for?"

    )

    print()

    print("=" * 80)

    print("Planner")

    print(result.plan)

    print()

    print("=" * 80)

    print("Retrieved Documents:", len(result.documents))

    print("Chunks:", len(result.chunks))

    print("Embedded:", len(result.embedded_chunks))

    print()

    print("=" * 80)

    print("Top Semantic Results")

    for hit in result.semantic_results:

        print()

        print(hit.title)

        print(hit.score)

        print(hit.url)

        print(hit.text[:250])

        print("-" * 60)


asyncio.run(main())