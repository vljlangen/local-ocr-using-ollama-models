import ollama
import os

def analyze_image(image_path, prompt="What is in this image?"):
    """
    Analyze an image using Ollama's vision model.
    
    Args:
        image_path (str): Path to the image file
        prompt (str): The prompt to send with the image
    
    Returns:
        str: The model's response
    """
    if not os.path.exists(image_path):
        return f"Error: Image file '{image_path}' not found."
    
    try:
        response = ollama.chat(
            model='llama3.2-vision:11b',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Example usage of the image analysis function."""
    
    # Example 1: Basic image analysis
    print("=== Basic Image Analysis ===")
    result = analyze_image('images/test.png')
    print(result)
    print()
    
    # Example 2: Custom prompt for text extraction
    print("=== Text Extraction ===")
    text_prompt = "Extract all the text you can see in this image. If there's no text, say 'No text found'."
    result = analyze_image('images/test.png', text_prompt)
    print(result)
    print()
    
    # Example 3: Detailed description
    print("=== Detailed Description ===")
    detail_prompt = "Describe this image in detail. Include colors, objects, people, text, and any other relevant information."
    result = analyze_image('images/test.png', detail_prompt)
    print(result)

if __name__ == "__main__":
    main()
