# Local Multimodal AI Chat

A versatile chat application that supports multiple AI models and multimodal interactions. This application allows you to chat with different AI models including Google's Gemini, OpenAI's models, and Ollama's local models.

## Features

- Support for multiple AI providers:
  - Google Gemini
  - OpenAI
  - Ollama (local models)
- Multimodal capabilities:
  - Text chat
  - Image understanding
  - PDF document analysis
- Modern Streamlit interface
- Chat history persistence
- Document similarity search using ChromaDB

## Requirements

- Python 3.11 or later
- Dependencies listed in requirements.txt
- Google Gemini API key

## Setup

1. Clone the repository:
```bash
git clone https://github.com/iamrobertemmanuel/LLM.git
cd LLM
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys:
   - Copy `config.yaml.example` to `config.yaml`
   - Add your API keys for the services you want to use

   For Replit deployment:
   - Add the following secrets in your Replit environment:
     ```
     GOOGLE_API_KEY=your_gemini_api_key_here
     CONFIG_YAML="""
     gemini:
       api_key: "${GOOGLE_API_KEY}"
       model: "gemini-2.0-flash"
       vision_model: "gemini-2.0-flash"

     chromadb:
       chromadb_path: "chroma_db"
       collection_name: "pdfs"

     chat_sessions_database_path: "./chat_sessions/chat_sessions.db"
     """
     ```

5. Run the application:
```bash
streamlit run app.py
```

## Configuration

The application uses a `config.yaml` file for configuration. Example structure:

```yaml
gemini:
  api_key: "your-gemini-api-key"
  model: "gemini-2.0-flash"
  vision_model: "gemini-2.0-flash"

ollama:
  embedding_model: "nomic-embed-text"
  base_url: http://localhost:11434

chromadb:
  chromadb_path: "chroma_db"
  collection_name: "pdfs"

chat_sessions_database_path: "./chat_sessions/chat_sessions.db"
```

## Usage

1. Start the application using `streamlit run app.py`
2. Select your preferred AI provider from the sidebar
3. Choose the appropriate model
4. Start chatting!

### Features:
- Text chat: Simply type your message and press enter
- Image analysis: Upload an image to discuss it with the AI
- PDF analysis: Upload PDF documents to chat about their contents

## License

MIT License
