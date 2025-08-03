import ollama
import os
from datetime import datetime

# Get the image path
image_path = 'images/test.png'

# Check if image exists
if not os.path.exists(image_path):
    print(f"Error: Image file {image_path} not found!")
    exit(1)

# Create results folder if it doesn't exist
results_folder = 'results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
    print(f"Created results folder: {results_folder}")

# Use Qwen2.5VL model for better multilingual support
model_name = 'qwen2.5vl:7b'

response = ollama.chat(
    model=model_name,
    messages=[{
        'role': 'user',
        'content': 'Extract and transcribe all the text from this image. Provide the text exactly as it appears, maintaining the original formatting and structure. Pay special attention to Finnish text and ensure accurate character recognition.',
        'images': [image_path]
    }]
)

# Get the extracted text
extracted_text = response['message']['content']

# Create output filename with timestamp and model name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_short = model_name.replace(':', '_').replace('.', '')
output_filename = os.path.join(results_folder, f"extracted_text_{model_short}_{timestamp}.txt")

# Save the text to file
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(f"Text extracted using {model_name} and saved to: {output_filename}")
print(f"\nExtracted text preview:\n{'-' * 30}")
print(extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text)
