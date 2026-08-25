# ⚖️ NyayaPath – Judicial Court Process & Case Flow Explainer Bot

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-green)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)



A Generative AI-powered web application that explains judicial court procedures, case lifecycle stages, and legal terminology in simple, neutral language to improve public legal awareness and accessibility.

## 🎯 Project Goal

This system exists **ONLY** to explain procedures. It **MUST NEVER** influence legal decisions or outcomes.

## ⚠️ Important Disclaimer

This system is designed for **educational purposes only**. It explains general court procedures and terminology but does **NOT** provide:
- Legal advice
- Law interpretation
- Case outcome predictions
- Strategic recommendations
- Legal document generation

For legal guidance specific to your situation, please consult a qualified attorney.

## 🛡️ Safety Features

- **Strict System Prompt**: Enforces judicial neutrality and educational scope
- **Keyword-Based Guardrails**: Pre-checks queries before AI processing
- **Polite Refusals**: Clear explanations when requests exceed scope
- **No Data Storage**: User queries are not stored or tracked
- **No Personalization**: Responses are general and educational only

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google AI Studio API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone or download this project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_AI_STUDIO_API_KEY=your_api_key_here
   ```
   
   Or set it as an environment variable:
   ```bash
   # Windows PowerShell
   $env:GOOGLE_AI_STUDIO_API_KEY="your_api_key_here"
   
   # Linux/Mac
   export GOOGLE_AI_STUDIO_API_KEY="your_api_key_here"
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
judicial-explainer-bot/
├── app.py                 # Main Streamlit application
├── ai_handler.py          # Google AI Studio API integration
├── prompts.py             # System prompt and safety guardrails
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .env.example           # Example environment file
└── .gitignore             # Git ignore rules
```

## 🔧 Configuration

### Environment Variables

- `GOOGLE_AI_STUDIO_API_KEY`: Your Google AI Studio API key (required)

### Model Configuration

The system uses:
- **Model**: `gemini-1.5-flash`
- **Provider**: Google AI Studio
- **System Prompt**: Strict educational-only prompt (see `prompts.py`)

## 📝 Usage Examples

### ✅ Allowed Questions

- "What are the stages of a civil court case?"
- "What does 'plaintiff' mean?"
- "How does the discovery process work?"
- "What happens during an appeal?"

### ❌ Blocked Questions

- "Should I file a lawsuit?" (advice-seeking)
- "Will I win my case?" (prediction)
- "Draft a legal document for me" (document generation)
- "What should I do?" (strategy recommendation)
- "Interpret this law for me" (legal interpretation)

## 🏗️ Architecture

### Separation of Concerns

- **`app.py`**: User interface and interaction logic
- **`ai_handler.py`**: AI API integration and error handling
- **`prompts.py`**: System prompt and safety guardrails

### Safety Flow

1. User submits query
2. **Safety Pre-Check**: Keyword-based validation (`prompts.py`)
3. If unsafe → Block and show refusal message (no AI call)
4. If safe → Send to AI with system prompt injection
5. Display response with educational disclaimer

## 🎓 For Hackathon Juries

### Key Features Demonstrated

- ✅ Responsible GenAI usage with strict boundaries
- ✅ Ethical boundary enforcement (keyword + prompt-based)
- ✅ Clear public value (legal education and awareness)
- ✅ Technical correctness (clean code, proper error handling)
- ✅ Zero risky behavior (no advice, predictions, or document generation)

### Demo Checklist

- [ ] API key configured
- [ ] Dependencies installed
- [ ] Application runs without errors
- [ ] Test with allowed questions (procedures, terminology)
- [ ] Test with blocked questions (advice, predictions)
- [ ] Verify refusal messages are clear and polite
- [ ] Confirm disclaimer is visible

## 🔒 Security & Privacy

- **No Data Storage**: Queries are not saved or logged
- **No User Tracking**: No cookies or session data stored
- **API Key Security**: Loaded from environment variables only
- **No Personal Information**: System does not request or store PII

## 📄 License

This project is created for educational and hackathon purposes.

## 🤝 Contributing

This is a hackathon project. For improvements or suggestions, please ensure all changes maintain the strict safety boundaries outlined in the project constraints.

## 📞 Support

For issues or questions:
1. Check that your API key is correctly set
2. Verify all dependencies are installed
3. Ensure Python 3.8+ is being used
4. Review error messages for specific guidance

---

