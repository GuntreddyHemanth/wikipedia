from sqlalchemy.orm import Session
from sqlalchemy import select
from model import Article, Quiz, Question, RelatedTopic
import uuid

class DatabaseService:
    @staticmethod
    def get_or_create_article(db: Session, url: str, title: str, content: str) -> Article:
        """Get existing article or create new one"""
        article = db.query(Article).filter(Article.url == url).first()
        if article:
            return article

        article = Article(
            id=uuid.uuid4(),
            url=url,
            title=title,
            content=content
        )
        db.add(article)
        db.commit()
        db.refresh(article)
        return article

    @staticmethod
    def create_quiz(db: Session, article_id: str, quiz_data: dict) -> Quiz:
        """Create quiz with questions and related topics"""
        quiz = Quiz(id=uuid.uuid4(), article_id=article_id)
        db.add(quiz)
        db.flush()

        # Add questions
        for idx, q in enumerate(quiz_data.get("questions", [])):
            question = Question(
                id=uuid.uuid4(),
                quiz_id=quiz.id,
                question_text=q["question_text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"],
                difficulty=q.get("difficulty", "medium"),
                order=idx + 1
            )
            db.add(question)

        # Add related topics
        for topic in quiz_data.get("related_topics", []):
            related = RelatedTopic(
                id=uuid.uuid4(),
                quiz_id=quiz.id,
                topic_title=topic["topic_title"],
                topic_url=topic["topic_url"]
            )
            db.add(related)

        db.commit()
        db.refresh(quiz)
        return quiz

    @staticmethod
    def get_quiz_history(db: Session) -> list:
        """Get all quizzes with their articles"""
        quizzes = db.query(Quiz).all()
        return quizzes
