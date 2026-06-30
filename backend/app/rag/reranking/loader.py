from sentence_transformers import CrossEncoder

from app.rag.reranking.config import MODEL_NAME


class CrossEncoderLoader:

    def __init__(self):

        self.model = CrossEncoder(
            MODEL_NAME
        )


cross_encoder = CrossEncoderLoader().model