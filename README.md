# JARVIS Clone - Marvel's AI Assistant

![JARVIS](https://your-banner-url.com/banner.png) <!-- Replace with your own banner image URL -->

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

## Technologies Used

- **Programming Language:** Python
- **Libraries:** `pyttsx3`, `requests`, `SpeechRecognition`, `pyjokes`, `pywhatkit`, `pyaudio`, `matplotlib`, `cartopy`, `wikipedia`, `keyboard`, `mouse`, `pyautogui`, `Pillow`, `psutil`, `pywikihow`

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
