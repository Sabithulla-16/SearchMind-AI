import uuid

from pydantic import BaseModel

from fastapi import Request

from app.observability.models import (
    StageMetric,
)

from app.observability.service import (
    observability_service,
)


# ----------------------------------
# Source
# ----------------------------------

class SourceResponse(BaseModel):

    title: str

    url: str


# ----------------------------------
# Metrics
# ----------------------------------

class MetricsResponse(BaseModel):

    retrieved_documents: int

    chunks: int

    embedded_chunks: int

    hybrid_results: int

    candidates: int

    reranked_results: int


# ----------------------------------
# Timings
# ----------------------------------

class TimingsResponse(BaseModel):

    sources_ms: float

    chunking_ms: float

    embedding_ms: float

    indexing_ms: float

    hybrid_search_ms: float

    candidate_selection_ms: float

    cross_encoder_ms: float

    generation_ms: float

    total_ms: float


# ----------------------------------
# Pipeline
# ----------------------------------

class PipelineResponse(BaseModel):

    type: str

    query: str


# ----------------------------------
# Error
# ----------------------------------

class ErrorResponse(BaseModel):

    type: str

    message: str


# ----------------------------------
# Success Response
# ----------------------------------

class SearchResponse(BaseModel):

    request_id: str

    success: bool

    pipeline: PipelineResponse

    answer: str

    sources: list[SourceResponse]

    metrics: MetricsResponse

    timings: TimingsResponse


# ----------------------------------
# Failed Response
# ----------------------------------

class SearchErrorResponse(BaseModel):

    request_id: str

    success: bool

    error: ErrorResponse


# ----------------------------------
# Builder
# ----------------------------------

class ResponseBuilder:

    def success(
        self,
        request: Request,
        pipeline_type: str,
        query: str,
        result,
    ):

        generation = result["generation"]

        metrics = observability_service.metrics()

        stages = metrics.stages

        counters = metrics.counters

        total = sum(

            stage.duration_ms

            for stage in stages.values()

        )

        return SearchResponse(

            request_id=request.state.request_id,

            success=True,

            pipeline=PipelineResponse(

                type=pipeline_type,

                query=query,

            ),

            answer=generation.answer,

            sources=[

                SourceResponse(

                    title=source.title,

                    url=source.url,

                )

                for source in generation.sources

            ],

            metrics=MetricsResponse(

                retrieved_documents=counters.get(
                    "Retrieved Documents",
                    0,
                ),

                chunks=counters.get(
                    "Chunks",
                    0,
                ),

                embedded_chunks=counters.get(
                    "Embedded Chunks",
                    0,
                ),

                hybrid_results=counters.get(
                    "Hybrid Results",
                    0,
                ),

                candidates=counters.get(
                    "Candidates",
                    0,
                ),

                reranked_results=counters.get(
                    "Reranked Results",
                    0,
                ),

            ),

            timings=TimingsResponse(

                sources_ms=stages.get(
                    "Sources",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                chunking_ms=stages.get(
                    "Chunking",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                embedding_ms=stages.get(
                    "Embedding",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                indexing_ms=stages.get(
                    "Indexing",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                hybrid_search_ms=stages.get(
                    "Hybrid Search",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                candidate_selection_ms=stages.get(
                    "Candidate Selector",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                cross_encoder_ms=stages.get(
                    "Cross Encoder",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                generation_ms=stages.get(
                    "Generation",
                    StageMetric(
                        name="",
                        duration_ms=0,
                    ),
                ).duration_ms,

                total_ms=total,

            ),

        )

    def error(
        self,
        request: Request,
        error: Exception,
    ):

        return SearchErrorResponse(

            request_id=request.state.request_id,

            success=False,

            error=ErrorResponse(

                type=type(error).__name__,

                message=str(error),

            ),

        )


response_builder = ResponseBuilder()