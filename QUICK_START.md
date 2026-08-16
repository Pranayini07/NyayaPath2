# 🚀 Quick Start Guide

## Step-by-Step Setup (5 Minutes)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Your API Key
1. Visit: https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy the key

### 3. Configure API Key

**Option A: Using .env file (Recommended)**
```bash
# Copy the example file
copy .env.example .env

# Edit .env and add your API key
# GOOGLE_AI_STUDIO_API_KEY=your_actual_key_here
```

**Option B: Using Environment Variable**
```powershell
# Windows PowerShell
$env:GOOGLE_AI_STUDIO_API_KEY="your_actual_key_here"

# Linux/Mac
export GOOGLE_AI_STUDIO_API_KEY="your_actual_key_here"
```

### 4. Run the Application
```bash
streamlit run app.py
```

### 5. Open in Browser
The app will automatically open at `http://localhost:8501`

## ✅ Verification Checklist

Before demo:
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] API key configured (`.env` file or environment variable)
- [ ] Application starts without errors
- [ ] Test query works: "What are the stages of a civil court case?"
- [ ] Safety guardrails work: Try "Should I file a lawsuit?" (should be blocked)

## 🎯 Demo Tips

1. **Start with allowed questions:**
   - "What does 'plaintiff' mean?"
   - "What are the stages of a court case?"
   - "How does the discovery process work?"

2. **Show safety features:**
   - Try: "Should I sue someone?" → Should be blocked
   - Try: "Will I win my case?" → Should be blocked
   - Try: "Draft a legal document" → Should be blocked

3. **Highlight key features:**
   - Educational-only scope
   - No legal advice
   - No data storage
   - Clear disclaimers

## 🐛 Troubleshooting

**Error: "GOOGLE_AI_STUDIO_API_KEY not found"**
- Check `.env` file exists and contains the key
- Or verify environment variable is set: `echo $env:GOOGLE_AI_STUDIO_API_KEY`

**Error: "API authentication error"**
- Verify your API key is correct
- Check if API key has proper permissions

**Error: "Module not found"**
- Run: `pip install -r requirements.txt`
- Ensure Python 3.8+ is being used

**App won't start**
- Check if port 8501 is available
- Try: `streamlit run app.py --server.port 8502`

