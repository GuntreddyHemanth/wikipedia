import json
from typing import List, Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from config import settings

class QuizGeneratorError(Exception):
    pass

def generate_quiz(article_content: str, article_title: str) -> Dict[str, Any]:
    """Generate quiz questions using Gemini API"""
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.7
        )

        prompt_template = ChatPromptTemplate.from_template("""
Based on the following article excerpt, generate exactly 4-5 multiple choice questions for a quiz.

Article Title: {title}
Article Content: {content}

Return ONLY a valid JSON object (no markdown, no code blocks) with this structure:
{{
  "questions": [
    {{
      "question_text": "Question here?",
      "option_a": "Option A",
      "option_b": "Option B",
      "option_c": "Option C",
      "option_d": "Option D",
      "correct_answer": "A",
      "explanation": "Brief explanation of the correct answer",
      "difficulty": "easy"
    }}
  ],
  "related_topics": [
    {{"topic_title": "Topic Name", "topic_url": "https://en.wikipedia.org/wiki/Topic_Name"}}
  ]
}}

Ensure:
- Each question tests understanding of key concepts from the article
- Difficulty levels are mixed (easy, medium, hard)
- Related topics are real Wikipedia articles related to the content
- Explanations are clear and educational
- All options are plausible but only one is correct
""")

        chain = prompt_template | llm

        response = chain.invoke({
            "title": article_title,
            "content": article_content
        })

        # Parse response
        response_text = response.content

        # Try to find JSON in the response
        try:
            quiz_data = json.loads(response_text)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown code blocks
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0]
                quiz_data = json.loads(json_str)
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0]
                quiz_data = json.loads(json_str)
            else:
                raise QuizGeneratorError("Could not parse LLM response as JSON")

        return quiz_data

    except Exception as e:
        raise QuizGeneratorError(f"Error generating quiz: {str(e)}")
