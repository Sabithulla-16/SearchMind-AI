import asyncio

from app.pipeline.search_pipeline import search_pipeline


async def main():

    print("=" * 80)
    print("SearchMind AI")
    print("=" * 80)

    query = input("\nEnter your query: ").strip()

    if not query:
        print("Query cannot be empty.")
        return

    result = await search_pipeline.run(query)

    print("\n")
    print("=" * 80)
    print("FINAL ANSWER")
    print("=" * 80)

    print(result["answer"])

    print("\n")
    print("=" * 80)
    print("SOURCES")
    print("=" * 80)

    for i, source in enumerate(result["sources"], start=1):
        print(f"\n[{i}] {source['title']}")
        print(source["url"])


if __name__ == "__main__":
    asyncio.run(main())