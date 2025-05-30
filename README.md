# JARVIS Clone - Marvel's AI Assistant

![JARVIS](/database/image.png)

This repository contains a Python-based clone of JARVIS, the AI assistant from the Marvel movies. Inspired by Tony Stark's iconic virtual assistant, this project aims to recreate some of the advanced functionalities and interactions seen in the films.

## Features

- **Whole PC Automation:** Control various aspects of your computer, such as opening applications and managing files.
- **YouTube Automation:** Search for and play videos on YouTube.
- **Browser Automation:** Automate web browsing tasks.
- **WhatsApp Automation:** Send messages via WhatsApp Web.
- **Weather Forecast:** Get the current weather and forecast information.
- **Space Info:** Retrieve information about space and astronomy.
- **Music and Spotify Automation:** Control music playback and manage Spotify.
- **Discord Automation:** Automate tasks on Discord.
- **AI Chatbot (Google Gemini):** Natural conversation and question answering using Google Gemini 2.0 Flash model.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** `pyttsx3`, `requests`, `SpeechRecognition`, `pyjokes`, `pywhatkit`, `pyaudio`, `matplotlib`, `cartopy`, `wikipedia`, `keyboard`, `mouse`, `pyautogui`, `Pillow`, `psutil`, `pywikihow`, `google-generativeai`

## Google Gemini AI Integration

JARVIS now features seamless integration with Google Gemini (2.0 Flash model), enabling advanced AI-powered conversation and question answering. If a command is not recognized as a script or automation, JARVIS will automatically use Gemini to respond as a chatbot.

### Gemini Setup

1. **Get a Google Gemini API Key:**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and generate an API key.
2. **Set the API Key:**
   - In `jarvis.py`, set your API key in the `GOOGLE_API_KEY` variable:
     ```python
     GOOGLE_API_KEY = 'your_api_key_here'
     ```
3. **Install Dependencies:**
   ```bash
   pip install google-generativeai
   ```

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/JARVIS-Clone.git
    ```
2. **Navigate to the Project Directory:**
    ```bash
    cd JARVIS-Clone
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### How to Use

1. **Run the Application:**
    ```bash
    python jarvis.py
    ```

2. **Mouse Click Coordinates Tool:**
    - Use the provided tool to find the coordinates of a mouse click:
      ```bash
      python find_coordinates.py
      ```
    - Replace the default coordinates in the automation scripts with the coordinates you receive using the tool.

3. **Voice Commands in `jarvis.py`:**
    - **PC Automation:** 
        - "Open [application]"
        - "Create a file named [file name]"
    - **YouTube Automation:** 
        - "Play [video name] on YouTube"
    - **Browser Automation:** 
        - "Open [website name]"
    - **WhatsApp Automation:** 
        - "Send [message] to [contact name] on WhatsApp"
    - **Weather Forecast:** 
        - "What is the weather in [city name]?"
    - **Space Info:** 
        - "Tell me about [space topic]"
    - **Music and Spotify Automation:** 
        - "Play [song name] on Spotify"
    - **Discord Automation:** 
        - "Send [message] to [channel name] on Discord"
    - **AI Chatbot:**
        - Ask any general question or have a conversation. If JARVIS doesn't recognize a command, it will respond using Google Gemini AI.

## Mouse Click Coordinates Tool

To run some automations, you may need to find the coordinates of mouse clicks. This repository includes a tool to help with this.

1. **Run the Coordinates Tool:**
    ```bash
    python find_coordinates.py
    ```
2. **Follow the on-screen instructions to find and record the coordinates.**

3. **Update the Automation Scripts:**
    - Replace the default coordinates in the scripts with the coordinates obtained from the tool.

## Contributing

We welcome contributions to make JARVIS even more powerful! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for visiting our repository! Feel free to reach out and connect. Let's build and innovate together! 🚀
