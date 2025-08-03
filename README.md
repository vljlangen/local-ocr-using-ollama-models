# Simple Ollama Vision

A minimal Python script for analyzing images using Ollama's vision models locally.

## Features

- 🔍 Analyze images using Ollama's vision models
- 🏠 Run completely locally - no cloud dependencies
- 🎯 Simple and straightforward API
- 📝 Easy to customize prompts

## Prerequisites

1. **Ollama** - Install and run Ollama locally
   ```bash
   # Install Ollama (if not already installed)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Start Ollama
   ollama serve
   ```

2. **Download Llama3.2 Vision model**
   ```bash
   ollama pull llama3.2-vision:11b
   ```

3. **Python 3.8+** with pip

## Installation

1. **Clone or download the project**
   ```bash
   cd simple-ollama-vision
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

1. **Place an image in the `images/` folder**
   ```bash
   # Copy your image to the images directory
   cp your_image.png images/test.png
   ```

2. **Run the script**
   ```bash
   python simple_ollama.py
   ```

### Customizing the Script

You can easily modify the script to:
- Use different models
- Change the prompt
- Analyze different images
- Add more complex interactions

#### Example: Using a different model
```python
response = ollama.chat(
    model='qwen2.5vl:7b',  # Different model
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['images/test.png']
    }]
)
```

#### Example: Custom prompt
```python
response = ollama.chat(
    model='llama3.2-vision:11b',
    messages=[{
        'role': 'user',
        'content': 'Describe this image in detail and identify any text you can see.',
        'images': ['images/test.png']
    }]
)
```

## Project Structure

```
simple-ollama-vision/
├── images/                 # Place your images here (ignored by git)
├── simple_ollama.py       # Main script
├── example.py             # Advanced usage examples
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Troubleshooting

### Common Issues

1. **"Error connecting to Ollama"**
   - Make sure Ollama is running: `ollama serve`
   - Check if Ollama is accessible at http://localhost:11434

2. **"Model not available"**
   - Download the model: `ollama pull llama3.2-vision:11b`
   - Check available models: `ollama list`

3. **"Image not found"**
   - Ensure the image path in the script matches your actual image
   - Check that the image file exists in the `images/` directory

### Performance Tips

- Use smaller images for faster processing
- Close other applications to free up memory
- Consider using a smaller model variant if available

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing the local AI inference platform
- [Llama3.2 Vision](https://ollama.ai/library/llama3.2-vision) for the vision model
