from pathlib import Path
import anthropic
import base64

# File path definition using Path
file_path = Path('')
# Alternative using home directory
# file_path = Path.home() / 'path' / 'to' / 'temp.txt'

# Read text content from file
text_content = file_path.read_text()

def safe_encode(text):
    try:
        # Convert text to bytes if it's a string
        if isinstance(text, str):
            text = text.encode('utf-8')
        # Encode to base64
        encoded = base64.b64encode(text)
        return encoded.decode('utf-8')
    except Exception as e:
        print(f"Encoding error: {e}")
        return None

# Configure Anthropic client
client = anthropic.Anthropic(api_key='your_api_key_here')  # Replace with your actual API key or import from credentials

def summarized():
    prompt = "Summarize this content: " + text_content
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text)
    return response.content[0].text

def detailed():
    prompt = "Expand this content and provide enough details to generate a lecture: " + text_content
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=2048,  # Increased token limit for detailed response
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text)
    return response.content[0].text

def get_bullet_points():
    prompt = "Extract main bullet points from this content: " + text_content
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text)
    return response.content[0].text

# Add a main function to demonstrate usage
if __name__ == "__main__":
    print("1. Summarize")
    print("2. Detailed expansion")
    print("3. Bullet points")
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        summarized()
    elif choice == "2":
        detailed()
    elif choice == "3":
        get_bullet_points()
    else:
        print("Invalid choice")