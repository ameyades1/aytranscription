#!/usr/bin/env python3

import sys
import os
import google.generativeai as genai

def process_with_gemini(prompt_file, input_file, output_file):
    """Process input file with Gemini API using a custom prompt"""

    # Check if files exist
    if not os.path.exists(prompt_file):
        print(f"Error: Prompt file '{prompt_file}' not found")
        sys.exit(1)

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)

    # Read prompt and input
    with open(prompt_file, 'r') as f:
        prompt = f.read().strip()

    with open(input_file, 'r') as f:
        content = f.read()

    # Configure Gemini API
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        if os.path.exists('gemini_api_key.txt'):
            with open('gemini_api_key.txt', 'r') as f:
                api_key = f.read().strip()
        else:
            print("Error: GEMINI_API_KEY not found. Set GEMINI_API_KEY env var or create gemini_api_key.txt")
            sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3.8-flash')

    # Process with Gemini
    print(f"Processing with Gemini...")
    response = model.generate_content(prompt + "\n\n" + content)
    result = response.text

    # Save output
    with open(output_file, 'w') as f:
        f.write(result)

    print(f"Output saved to: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <prompt_file> <input_file> <output_file>")
        sys.exit(1)

    prompt_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    process_with_gemini(prompt_file, input_file, output_file)
