# Medicare-Alarm

A smart Python medicine reminder app that uses **API** to understand voice and text commands (in any language) and schedule medicine 
alarms with popup notifications.

🎙️ Voice input  
⌨️ Text input  
🌍 Multilingual support  
⏰ Automatic medicine reminders

---

## 🔍 Features

- Natural language understanding with GPT  
- Supports voice and text commands  
- Set alarms in any language  
- Popup reminders for medicine time  
- CSV-based medicine list support

---

## 🧠 How It Works

1. User gives a command (text or voice).  
2. The app sends input to GPT API for understanding.  
3. It extracts the medicine name and reminder time.  
4. A scheduled alarm triggers a popup when time arrives.

Example commands:

- “Remind me in 2 hours to take my medicine.”
- “याद दिलाओ कि मैं 7 बजे दवा लूँ।”

---

## 🧾 Setup

1. Clone the repo:
   
       git clone https://github.com/aanvee/Medicare-Alarm.git
       cd Medicare-Alarm
   
2.Create and activate a virtual environment:
   
    python -m venv venv
    source venv/bin/activate  # (Linux / Mac)
    venv\Scripts\activate     # (Windows)

3.Install dependencies:

    pip install -r requirements.txt

4.Create a .env :

    cp .env.example .env
    Add:
    OPENAI_API_KEY=your_openai_api_key_here

5.Run the app:

python main.py
🗂️ File Structure
Medicare-Alarm/
├── ai_assistant.py
├── code.py
├── python_test.py
├── users.csv
├── .env.example
├── requirements.txt
└── README.md

<img width="1903" height="837" alt="image" src="https://github.com/user-attachments/assets/54767c28-bb30-4a7b-8ebd-639fda474a99" />
<img width="1106" height="750" alt="image" src="https://github.com/user-attachments/assets/99d8e61b-38ec-46b9-90a5-0883954541e7" />
