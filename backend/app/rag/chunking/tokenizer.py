import tiktoken


class Tokenizer:

    def __init__(self):

        self.encoding = tiktoken.get_encoding("cl100k_base")

    def encode(self, text: str):

        return self.encoding.encode(text)

    def decode(self, tokens):

        return self.encoding.decode(tokens)

    def count_tokens(self, text: str):

        return len(
            self.encode(text)
        )


tokenizer = Tokenizer()