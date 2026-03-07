# 🤖 MILS AI Assistant
### Intelligent Productivity Monitoring & Scheduling System

An AI-powered assistant that monitors user activity using **computer vision**, analyzes **productivity patterns**, and provides **smart task recommendations** in real time.

---

## 📌 Project Overview

MILS AI Assistant observes the user's working behavior through a webcam and analyzes:

- 🧠 Work activities  
- 🙂 Emotional state  
- ⏱ Focus time  
- ☕ Break time  
- 📱 Distraction patterns  

Using this information, the system generates **AI-driven productivity insights and recommendations**.

---

## 🚀 Key Features

| Feature | Description |
|--------|-------------|
| 🎥 Computer Vision Monitoring | Detects posture, motion, and activities using webcam |
| 🙂 Emotion Detection | Analyzes user emotional state |
| 📊 Productivity Tracking | Tracks focus, break, and distraction time |
| 🧠 AI Decision Engine | Generates intelligent productivity suggestions |
| 📅 Smart Task Scheduler | Manages daily tasks and workflow |
| 🤖 AI Assistant | Answers questions about productivity and tasks |
| 🌐 Web Dashboard | Interactive UI for monitoring and AI interaction |

---

## 🖥 Dashboard Preview

### Main Dashboard

<img width="959" height="524" alt="image" src="https://github.com/user-attachments/assets/4244fe32-bd32-49c0-9033-81c7a49f6748" />


---

### AI Assistant Interface

<img width="528" height="163" alt="image" src="https://github.com/user-attachments/assets/8be56fe2-8f6c-491c-9f65-14df0a3cbc59" />



Users can ask questions such as:

```
What is my current task?
How productive was I?
What should I do next?
```

---

### Activity Detection

<img width="949" height="504" alt="image" src="https://github.com/user-attachments/assets/ea0723cf-181c-4dc9-9d4c-dc7f63fdddca" />


The system detects:

- posture
- motion
- activity
- emotional signals

---

## 🧠 System Architecture

```
Camera Input
     │
     ▼
Computer Vision Modules
     │
     ├── Emotion Detection
     ├── Activity Recognition
     ├── Posture Detection
     │
     ▼
Behavior Analysis Engine
     │
     ▼
Productivity Tracker
     │
     ▼
AI Decision Model
     │
     ▼
Task Scheduler
     │
     ▼
AI Assistant Interface
```

---

## 📂 Project Structure

```
mils-ai-assistant
│
├── ai_assistant
├── ai_brain
├── behavior_engine
├── camera_module
├── emotion_module
├── planner
├── prediction_engine
├── schedular
├── utils
├── vision
├── web
│
├── screenshots
│   ├── dashboard.png
│   ├── assistant.png
│   └── camera.png
│
├── main.py
├── web_app.py
├── run.bat
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Priya-ak/mils-ai-assistant.git
cd mils-ai-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama from:

https://ollama.com

Then install the AI model:

```bash
ollama pull llama3
```

---

## ▶ Run the System

Start the assistant:

```bash
run.bat
```

The dashboard will open automatically at:

```
http://127.0.0.1:5000
```

---

## 💬 Example AI Interaction

```
User: What is my current task?
AI: Your current task is Deep Work Session.

User: How productive was I?
AI: Your productivity score is 82%.

User: What should I do next?
AI: Continue your focus session or take a short break.
```

---

## 🛠 Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Core programming |
| OpenCV | Computer vision |
| MediaPipe | Human pose & activity detection |
| Flask | Web dashboard |
| Ollama | Local AI model inference |
| LLaMA | AI reasoning |

---

## 🔮 Future Improvements

- 📊 Productivity analytics dashboard  
- 🧠 AI-based schedule optimization  
- ☁ Cloud deployment  
- 📱 Mobile interface  
- 👥 Multi-user support  

---

## 👩‍💻 Author

**Priyadharshini**

AI Systems • Computer Vision • Intelligent Productivity Tools

---

⭐ If you find this project interesting, consider giving it a star on GitHub.
