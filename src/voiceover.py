from elevenlabs import generate, save, set_api_key
import os

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def generate_voiceover(text: str, output_path="output.mp3"):
    audio=generate(text=text, voice="Josh", model="eleven_multilingual_v2")

    with open(output_path, "wb") as f:
        f.write(audio)

    return output_path