import re


class ResponseParser:

    def parse(
        self,
        response: str,
    ) -> str:
        """
        Clean and normalize LLM output.

        Future versions can also parse JSON responses.
        """

        if response is None:
            return ""

        response = response.strip()

        # Collapse multiple blank lines
        response = re.sub(r"\n{3,}", "\n\n", response)

        # Collapse multiple spaces
        response = re.sub(r"[ \t]+", " ", response)

        return response


response_parser = ResponseParser()