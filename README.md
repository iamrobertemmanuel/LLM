# Local Multimodal AI Chat

A multimodal chat application that integrates various AI models to manage audio, images, and PDFs seamlessly within a single interface.

## Features

- **Local Model Processing with Ollama**: Run local instances of AI models
- **OpenAI API Integration**: Access to OpenAI's powerful models
- **Audio Processing**: Voice messages with Whisper AI
- **PDF Processing**: Chat with your PDFs using Chroma DB
- **Image Understanding**: Process and discuss images using LLaVA
- **Multi-Session Support**: Manage multiple chat sessions
- **Authentication System**: Secure user authentication

## Quick Start

### Local Setup

1. **Install Ollama**
   ```bash
   # Visit https://ollama.com/download and install
   ```

2. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Local-Multimodal-AI-Chat.git
   cd Local-Multimodal-AI-Chat
   ```

3. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

4. **Install Requirements**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Configure the Application**
   ```bash
   cp config.yaml.example config.yaml
   # Edit config.yaml with your settings
   ```

6. **Initialize Database**
   ```bash
   python database_operations.py
   ```

7. **Run the Application**
   ```bash
   streamlit run app.py
   ```

### Replit Setup

1. Fork this repository to your GitHub account
2. Create a new Repl on Replit
3. Import from your GitHub repository
4. The included `.replit` and `replit.nix` files will handle the setup
5. Add your configuration in Replit's Secrets:
   - Add `CONFIG_YAML` secret with your configuration

## Required Models

Visit https://ollama.com/library to choose your models. Required models:
- An embedding model (e.g., nomic-embed-text)
- An image-capable model (e.g., llava)

Pull models using the chat command: `/pull MODEL_NAME`

## Configuration

Create a `config.yaml` file based on `config.yaml.example`:
```yaml
openai:
  api_key: "your-api-key-here"
ollama:
  host: "http://localhost:11434"
chat_icons:
  user: "chat_icons/user_image.png"
  bot: "chat_icons/bot_image.png"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Contact

- Email: leonsander.consulting@gmail.com
- Twitter: [@leonsanderai](https://twitter.com/leonsanderai)
