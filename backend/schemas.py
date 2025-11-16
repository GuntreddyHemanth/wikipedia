from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List

class QuestionSchema(BaseModel):
    id: str
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    explanation: str
    difficulty: str
    order: int

    class Config:
        from_attributes = True

class RelatedTopicSchema(BaseModel):
    id: str
    topic_title: str
    topic_url: str

    class Config:
        from_attributes = True

class QuizSchema(BaseModel):
    id: str
    article_id: str
    generated_at: datetime
    questions: List[QuestionSchema]
    related_topics: List[RelatedTopicSchema]

    class Config:
        from_attributes = True

class ArticleSchema(BaseModel):
    id: str
    url: str
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

class QuizHistorySchema(BaseModel):
    id: str
    article: ArticleSchema
    quiz: QuizSchema

    class Config:
        from_attributes = True

class GenerateQuizRequest(BaseModel):
    wikipedia_url: str

class GenerateQuizResponse(BaseModel):
    article: ArticleSchema
    quiz: QuizSchema
    message: str