from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import GenerateQuizRequest, GenerateQuizResponse, QuizHistorySchema
from services.wikipedia_scraper import extract_article_content, WikipediaScraperError
from services.quiz_generator import generate_quiz, QuizGeneratorError
from services.database_service import DatabaseService
from model import Quiz
from sqlalchemy import select

router = APIRouter()



@router.post("/generate-quiz", response_model=GenerateQuizResponse)
async def generate_quiz_endpoint(
    request: GenerateQuizRequest,
    db: Session = Depends(get_db)
):
    """Generate a quiz from a Wikipedia article URL"""
    try:
        # Extract article content
        article_data = extract_article_content(request.wikipedia_url)

        # Get or create article in database
        article = DatabaseService.get_or_create_article(
            db,
            article_data["url"],
            article_data["title"],
            article_data["content"]
        )

        # Generate quiz using LLM
        quiz_data = generate_quiz(article_data["content"], article_data["title"])

        # Save quiz to database
        quiz = DatabaseService.create_quiz(db, str(article.id), quiz_data)

        return GenerateQuizResponse(
            article={
                "id": str(article.id),
                "url": article.url,
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at
            },
            quiz={
                "id": str(quiz.id),
                "article_id": str(quiz.article_id),
                "generated_at": quiz.generated_at,
                "questions": [
                    {
                        "id": str(q.id),
                        "question_text": q.question_text,
                        "option_a": q.option_a,
                        "option_b": q.option_b,
                        "option_c": q.option_c,
                        "option_d": q.option_d,
                        "correct_answer": q.correct_answer,
                        "explanation": q.explanation,
                        "difficulty": q.difficulty,
                        "order": q.order
                    }
                    for q in sorted(quiz.questions, key=lambda x: x.order)
                ],
                "related_topics": [
                    {
                        "id": str(t.id),
                        "topic_title": t.topic_title,
                        "topic_url": t.topic_url
                    }
                    for t in quiz.related_topics
                ]
            },
            message="Quiz generated successfully"
        )

    except WikipediaScraperError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except QuizGeneratorError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get("/quiz-history")
async def get_quiz_history(db: Session = Depends(get_db)):
    """Get all previously generated quizzes"""
    try:
        quizzes = db.query(Quiz).all()
        result = []

        for quiz in quizzes:
            result.append({
                "id": str(quiz.id),
                "article": {
                    "id": str(quiz.article.id),
                    "url": quiz.article.url,
                    "title": quiz.article.title,
                    "content": quiz.article.content,
                    "created_at": quiz.article.created_at
                },
                "quiz": {
                    "id": str(quiz.id),
                    "article_id": str(quiz.article_id),
                    "generated_at": quiz.generated_at,
                    "questions": [
                        {
                            "id": str(q.id),
                            "question_text": q.question_text,
                            "option_a": q.option_a,
                            "option_b": q.option_b,
                            "option_c": q.option_c,
                            "option_d": q.option_d,
                            "correct_answer": q.correct_answer,
                            "explanation": q.explanation,
                            "difficulty": q.difficulty,
                            "order": q.order
                        }
                        for q in sorted(quiz.questions, key=lambda x: x.order)
                    ],
                    "related_topics": [
                        {
                            "id": str(t.id),
                            "topic_title": t.topic_title,
                            "topic_url": t.topic_url
                        }
                        for t in quiz.related_topics
                    ]
                }
            })

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id: str, db: Session = Depends(get_db)):
    """Get a specific quiz by ID"""
    try:
        quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")

        return {
            "id": str(quiz.id),
            "article": {
                "id": str(quiz.article.id),
                "url": quiz.article.url,
                "title": quiz.article.title,
                "content": quiz.article.content,
                "created_at": quiz.article.created_at
            },
            "quiz": {
                "id": str(quiz.id),
                "article_id": str(quiz.article_id),
                "generated_at": quiz.generated_at,
                "questions": [
                    {
                        "id": str(q.id),
                        "question_text": q.question_text,
                        "option_a": q.option_a,
                        "option_b": q.option_b,
                        "option_c": q.option_c,
                        "option_d": q.option_d,
                        "correct_answer": q.correct_answer,
                        "explanation": q.explanation,
                        "difficulty": q.difficulty,
                        "order": q.order
                    }
                    for q in sorted(quiz.questions, key=lambda x: x.order)
                ],
                "related_topics": [
                    {
                        "id": str(t.id),
                        "topic_title": t.topic_title,
                        "topic_url": t.topic_url
                    }
                    for t in quiz.related_topics
                ]
            }
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
