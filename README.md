
# WikiQuiz - AI-Powered Wikipedia Quiz Generator

Transform any Wikipedia article into an interactive quiz with AI-generated questions!

## 🌟 Features

### Generate Quizzes
- 📝 Input any Wikipedia article URL
- 🤖 AI generates 5-8 multiple-choice questions using Google Gemini
- 🎯 Questions with difficulty levels (easy/medium/hard)
- 💡 Detailed explanations for each answer
- 🔗 Related Wikipedia topics for further learning

### Quiz Management
- 📚 View all previously generated quizzes
- 🔍 Browse quiz history with metadata
- 📋 Re-view past quizzes in modal popup
- ⏱️ Track when quizzes were generated

### Beautiful UI
- 🎨 Clean, modern design with Tailwind CSS
- 📱 Fully responsive layout
- ✨ Smooth animations and transitions
- 🎯 Intuitive user experience
- ⌨️ Keyboard and mouse navigation

---



### Backend Setup

See [BACKEND_README.md](./BACKEND_README.md) for complete Python FastAPI setup instructions.

### Full Setup

Follow [SETUP_GUIDE.md](./SETUP_GUIDE.md) for step-by-step instructions covering:
- Frontend setup
- Backend setup
- Database configuration
- API key setup
- Local testing
- Production deployment

### Quick Reference

See [QUICK_START.md](./QUICK_START.md) for a 5-minute setup cheat sheet.

---

## 📋 How It Works

```
1. User enters Wikipedia URL
   ↓
2. Backend scrapes article content
   ↓
3. Gemini API generates quiz questions
   ↓
4. Quiz stored in PostgreSQL database
   ↓
5. Frontend displays beautiful quiz interface
   ↓
6. User navigates through questions with explanations
   ↓
7. All quizzes saved in history for later review
```

---

## 💻 Technology Stack

### Backend
- **FastAPI** 0.104.1 - API framework
- **Python** 3.8+ - Language
- **SQLAlchemy** - ORM
- **BeautifulSoup** - Web scraping
- **LangChain** - LLM integration
- **Google Gemini** - AI quiz generation


## 📁 Project Structure

```
.
├── src/
│   ├── components/
│   │   ├── GenerateQuizTab.tsx      # Quiz generation interface
│   │   ├── HistoryTab.tsx            # Quiz history view
│   │   ├── QuizCard.tsx              # Question display
│   │   └── QuizModal.tsx             # Historical quiz modal
│   ├── types/
│   │   └── quiz.ts                   # TypeScript interfaces
│   ├── lib/
│   │   └── api.ts                    # Backend API client
│   ├── App.tsx                       # Main application
│   └── index.css                     # Global styles
├── dist/                             # Production build
├── SETUP_GUIDE.md                   # Detailed setup instructions
├── QUICK_START.md                   # 5-minute setup
├── BACKEND_README.md                # Backend implementation
├── API_INTEGRATION.md               # API documentation
├── PROJECT_SUMMARY.md               # Project overview
└── README.md                        # This file
```

---

## 🎯 Available Scripts

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint
npm run typecheck    # TypeScript type checking
```

---

## 🔌 API Endpoints

The backend provides these REST endpoints:

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/generate-quiz` | Generate new quiz from Wikipedia URL |
| GET | `/api/quiz-history` | Retrieve all generated quizzes |
| GET | `/api/quizzes/{id}` | Get specific quiz by ID |
| GET | `/health` | Health check |

See [API_INTEGRATION.md](./API_INTEGRATION.md) for detailed API documentation.

---

## 📦 Environment Variables

### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000
```

### Backend (.env) - See BACKEND_README.md
```env
DATABASE_URL=postgresql://...
GOOGLE_API_KEY=your_key_here
FRONTEND_URL=http://localhost:5173
```

---

## 🧪 Testing

```bash
# Generate a quiz from CLI
curl -X POST http://localhost:8000/api/generate-quiz \
  -H "Content-Type: application/json" \
  -d '{"wikipedia_url": "https://en.wikipedia.org/wiki/Albert_Einstein"}'

# Get quiz history
curl http://localhost:8000/api/quiz-history
```

---

## 🚢 Deployment

### Frontend
```bash
npm run build
# Deploy dist/ folder to Vercel, Netlify, Railway, etc.
```

### Backend
Deploy to Railway, Render, Heroku, AWS, or your own server.

See [SETUP_GUIDE.md](./SETUP_GUIDE.md) for production deployment details.

---

## 📚 Documentation

- **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - Complete setup with troubleshooting
- **[QUICK_START.md](./QUICK_START.md)** - 5-minute quick reference
- **[BACKEND_README.md](./BACKEND_README.md)** - Backend code and implementation
- **[API_INTEGRATION.md](./API_INTEGRATION.md)** - Frontend-backend integration
- **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Complete project overview

---

## 🐛 Troubleshooting

### Frontend won't connect to backend
- Check `VITE_API_URL` in `.env`
- Ensure backend is running: `http://localhost:8000`
- Check browser console for CORS errors

### CORS errors
- Verify backend `.env` has correct `FRONTEND_URL`
- Restart backend after changing `.env`

### Database connection fails
- Check PostgreSQL is running
- Verify `DATABASE_URL` is correct
- Check database exists

### Gemini API errors
- Verify API key is valid
- Check you have quota remaining
- Ensure internet connection works

**WikiQuiz** - Transform Wikipedia articles into interactive learning experiences with AI! 🎓








### SAMPLE DATE FROM BACKEND FASTAPI: http://localhost:8000/docs#/quize/generate_quiz_endpoint_api_generate_quiz_post

{
  "article": {
    "id": "bbf6d840-a414-4d70-8706-22d016b95ad4",
    "url": "https://en.wikipedia.org/wiki/Tiger",
    "title": "Tiger",
    "content": "Thetiger(Panthera tigris) is a largecatand a member of the genusPantheranative toAsia. It has a powerful, muscular body with a large head and paws, a long tail and orange fur with black, mostly vertical stripes. It is traditionally classified into ninerecentsubspecies, though some recognise only two subspecies, mainland Asian tigers and the island tigers of theSunda Islands.\n\nThroughout the tiger's range, it inhabits mainlyforests, fromconiferousandtemperate broadleaf and mixed forestsin theRussian Far EastandNortheast Chinatotropical and subtropical moist broadleaf forestson theIndian subcontinentandSoutheast Asia. The tiger is anapex predatorand preys mainly onungulates, which it takes by ambush. It lives a mostly solitary life and occupieshome ranges, defending these from individuals of the same sex. The range of a male tiger overlaps with that of multiple females with whom he mates. Females give birth to usually two or three cubs that stay with their mother for about two years. When becoming independent, they leave their mother's home range and establish their own.\n\nSince the early 20th century, tiger populations have lost at least 93% of their historic range and arelocally extinctinWestandCentral Asia, in large areas ofChinaand on the islands ofJavaandBali. Today, the tiger's range is severely fragmented. It is listed asEndangeredon theIUCN Red List of Threatened Species, as its range is thought to have declined by 53% to 68% since the late 1990s. Major threats to tigers arehabitat destructionandfragmentationdue todeforestation,poachingfor fur and the illegal trade of body parts for medicinal purposes. Tigers are also victims ofhuman–wildlife conflictas they attack and prey on livestock in areas where natural prey is scarce. The tiger is legally protected in all range countries. National conservation measures consist of action plans,anti-poachingpatrols and schemes for monitoring tiger populations. In several range countries,wildlife corridorshave been established and tiger reintroduction is planned.\n\nThe tiger is among the most popular of the world'scharismatic megafauna. It has been kept in captivity since ancient times and has been trained to perform incircusesand other entertainment shows. The tiger featured prominently in the ancientmythologyandfolkloreof cultures throughout its historic range and has continued toappear in cultureworldwide.",
    "created_at": "2025-11-17T00:43:37.606302"
  },
  "quiz": {
    "id": "2f676237-d286-46a4-82df-af94e537120b",
    "article_id": "bbf6d840-a414-4d70-8706-22d016b95ad4",
    "generated_at": "2025-11-17T00:48:23.929516",
    "questions": [
      {
        "id": "e8e41f2e-fbe6-40af-9e05-167e1b980dc1",
        "question_text": "What is the primary color of a tiger's fur, as described in the article?",
        "option_a": "Brown",
        "option_b": "Orange",
        "option_c": "Yellow",
        "option_d": "White",
        "correct_answer": "B",
        "explanation": "The article states, 'It has...orange fur with black, mostly vertical stripes.'",
        "difficulty": "easy",
        "order": 1
      },
      {
        "id": "6f54481b-0e7c-4b41-b6eb-bd9530dbf26d",
        "question_text": "Which of the following is NOT explicitly listed as a major threat to tiger populations in the article?",
        "option_a": "Habitat destruction and fragmentation",
        "option_b": "Poaching for fur and illegal trade of body parts",
        "option_c": "Natural predators competing for prey",
        "option_d": "Human–wildlife conflict when attacking livestock",
        "correct_answer": "C",
        "explanation": "The article lists habitat destruction, poaching, and human-wildlife conflict as major threats. It does not mention natural predators, as tigers are described as apex predators.",
        "difficulty": "medium",
        "order": 2
      },
      {
        "id": "7fb47b6b-59f3-4f82-af1b-79817279671e",
        "question_text": "How long do tiger cubs typically stay with their mother before becoming independent?",
        "option_a": "About six months",
        "option_b": "About one year",
        "option_c": "About two years",
        "option_d": "About five years",
        "correct_answer": "C",
        "explanation": "The article states: 'Females give birth to usually two or three cubs that stay with their mother for about two years.'",
        "difficulty": "medium",
        "order": 3
      },
      {
        "id": "030bddc5-5bba-498e-8b25-67f2190f27db",
        "question_text": "According to the article, by what percentage is the tiger's range thought to have declined since the late 1990s?",
        "option_a": "Less than 20%",
        "option_b": "25% to 50%",
        "option_c": "53% to 68%",
        "option_d": "Over 90%",
        "correct_answer": "C",
        "explanation": "The article states: 'It is listed as Endangered on the IUCN Red List of Threatened Species, as its range is thought to have declined by 53% to 68% since the late 1990s.' The 'over 90%' refers to the loss of historic range since the early 20th century.",
        "difficulty": "hard",
        "order": 4
      },
      {
        "id": "1ce0ef9c-e8c3-4f51-9dd2-f5c02ceffcfc",
        "question_text": "To which continent is the tiger native?",
        "option_a": "Africa",
        "option_b": "South America",
        "option_c": "Asia",
        "option_d": "North America",
        "correct_answer": "C",
        "explanation": "The first sentence states: 'The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia.'",
        "difficulty": "easy",
        "order": 5
      }
    ],
    "related_topics": [
      {
        "id": "af5f396d-d427-4aa9-85d0-6f8c5f6455f6",
        "topic_title": "Tiger",
        "topic_url": "https://en.wikipedia.org/wiki/Tiger"
      },
      {
        "id": "ded90297-026e-4efc-8191-e95e8f02a235",
        "topic_title": "Endangered Species",
        "topic_url": "https://en.wikipedia.org/wiki/Endangered_species"
      },
      {
        "id": "e8859f9a-93cb-498d-8591-08902c97704c",
        "topic_title": "Apex Predator",
        "topic_url": "https://en.wikipedia.org/wiki/Apex_predator"
      },
      {
        "id": "2578ec38-44e0-4ece-8410-d02c0fd045d0",
        "topic_title": "Habitat destruction",
        "topic_url": "https://en.wikipedia.org/wiki/Habitat_destruction"
      }
    ]
  },
  "message": "Quiz generated successfully"
}

IMAGES: 

<img width="1344" height="678" alt="Screenshot 2025-11-17 063100" src="https://github.com/user-attachments/assets/25c3c615-3c26-45a6-8ab0-df220b50e923" />
<img width="1828" height="820" alt="Screenshot 2025-11-17 062814" src="https://github.com/user-attachments/assets/cdac729b-9a59-451a-9258-e2b59f66c76d" />

