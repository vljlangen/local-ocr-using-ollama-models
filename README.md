# Local OCR using Ollama Models

A powerful local OCR (Optical Character Recognition) solution using Ollama's vision models. Extract text from images with excellent accuracy, especially for multilingual content including Finnish text with proper diacritic support.

## Features

- 🔍 **High-quality OCR** - Extract text from images with accuracy comparable to or better than Tesseract
- 🌍 **Multilingual support** - Excellent handling of English and Finnish text with proper character recognition (ä, ö, å)
- 🏠 **Completely local** - No cloud dependencies, runs entirely on your machine
- 📁 **Organized output** - Results saved to timestamped files in a `results/` folder
- 🎯 **Clean text output** - Pure extracted text without metadata headers
- ⚡ **Fast processing** - Optimized for quick text extraction

## Prerequisites

1. **Ollama** - Install and run Ollama locally
   ```bash
   # Install Ollama (if not already installed)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Start Ollama
   ollama serve
   ```

2. **Download Qwen2.5VL model** (recommended for best results)
   ```bash
   ollama pull qwen2.5vl:7b
   ```

3. **Python 3.8+** with pip

## Installation

1. **Clone or download the project**
   ```bash
   cd local-ocr-using-ollama-models
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

### Basic OCR Usage

1. **Place an image in the `images/` folder**
   ```bash
   # Copy your image to the images directory
   cp your_image.png images/test.png
   ```

2. **Run the OCR script**
   ```bash
   python simple_ollama.py
   ```

3. **Find your results**
   - Extracted text is saved to `results/extracted_text_qwen25vl_7b_YYYYMMDD_HHMMSS.txt`
   - Each extraction gets a unique timestamped filename

### Supported Models

The script currently uses **Qwen2.5VL:7b** for optimal results, especially for:
- Finnish text with diacritics (ä, ö, å)
- Multilingual content
- Complex document layouts

You can also use other vision models:
- `llama3.2-vision:11b` - Good for English text
- `qwen2.5vl:7b` - **Recommended** for multilingual content

### Customizing the Script

You can easily modify the script to:
- Use different models
- Change the OCR prompt
- Process different images
- Adjust output formatting

#### Example: Using a different model
```python
# Change the model name in simple_ollama.py
model_name = 'llama3.2-vision:11b'  # or 'qwen2.5vl:7b'
```

#### Example: Custom OCR prompt
```python
response = ollama.chat(
    model=model_name,
    messages=[{
        'role': 'user',
        'content': 'Extract and transcribe all the text from this image. Provide the text exactly as it appears, maintaining the original formatting and structure. Pay special attention to Finnish text and ensure accurate character recognition.',
        'images': [image_path]
    }]
)
```

## Project Structure

```
local-ocr-using-ollama-models/
├── images/                 # Place your images here (ignored by git)
├── results/                # Extracted text files (auto-created)
├── simple_ollama.py       # Main OCR script
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Performance Results

### Model Comparison

| Model | English Text | Finnish Text | Diacritics | Overall Accuracy |
|-------|-------------|--------------|------------|------------------|
| llama3.2-vision:11b | ✅ Excellent | ❌ Poor | ❌ Garbled | ⭐⭐⭐ |
| qwen2.5vl:7b | ✅ Excellent | ✅ Excellent | ✅ Perfect | ⭐⭐⭐⭐⭐ |

### Example Results

**Input Image**: Finnish text with diacritics

**Qwen2.5VL Output**:
```
Tämä teksti on tarkoitettu erilaisten OCR-ratkaisujen testaukseen.
Sen avulla voidaan arvioida, kuinka hyvin ohjelmisto tunnistaa 
suomenkielistä sisältöä, mukaan lukien ääkkiset: ä, ö, ja å.
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
   - Download the model: `ollama pull qwen2.5vl:7b`
   - Check available models: `ollama list`

3. **"Image not found"**
   - Ensure the image path in the script matches your actual image
   - Check that the image file exists in the `images/` directory

4. **Poor Finnish text recognition**
   - Use the Qwen2.5VL model for best results with Finnish text
   - Ensure the image quality is good (300+ DPI recommended)

### Performance Tips

- Use the Qwen2.5VL model for multilingual content
- Ensure good image quality for best OCR results
- Close other applications to free up memory
- The Qwen2.5VL model is smaller (6.0 GB) than Llama3.2 Vision (7.8 GB)

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing the local AI inference platform
- [Qwen2.5VL](https://ollama.ai/library/qwen2.5vl) for excellent multilingual OCR capabilities
- [Llama3.2 Vision](https://ollama.ai/library/llama3.2-vision) for vision model support
