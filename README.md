# 🤖 MILS AI Assistant

### Intelligent Productivity Monitoring & Scheduling System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-OpenCV-green)
![AI](https://img.shields.io/badge/AI-TensorFlow%20%7C%20PyTorch-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

MILS AI Assistant is an **AI-powered productivity monitoring system** that uses **computer vision, emotion detection, and behavioral analysis** to understand user work patterns and provide **real-time productivity insights and intelligent task recommendations**.

The system observes the user's activity using a webcam, analyzes behavior patterns, detects emotional state, and provides **AI-driven suggestions for focus improvement, break management, and task scheduling.**

---

# 📌 Project Overview

MILS AI Assistant monitors multiple productivity signals:

* 🧠 **Work Activities** – Detects whether the user is working or distracted
* 🙂 **Emotion Detection** – Identifies emotional state
* ⏱ **Focus Duration** – Tracks productive work sessions
* ☕ **Break Monitoring** – Detects break intervals
* 📱 **Distraction Detection** – Identifies interruptions

Using these signals, the system generates **intelligent productivity insights and recommendations.**

---

# 🚀 Key Features

| Feature                       | Description                                     |
| ----------------------------- | ----------------------------------------------- |
| 🎥 Computer Vision Monitoring | Detects posture, motion, and activities         |
| 🙂 Emotion Detection          | Identifies emotional state                      |
| 📊 Productivity Tracking      | Tracks focus, break, and distraction time       |
| 🧠 AI Decision Engine         | Generates productivity recommendations          |
| 📅 Smart Task Scheduler       | Organizes and manages tasks                     |
| 🤖 AI Assistant               | Conversational AI for productivity guidance     |
| 🌐 Web Dashboard              | Visual interface for monitoring and interaction |

---

# 🖥 Dashboard Preview

## Main Dashboard
<img width="959" height="530" alt="image" src="https://github.com/user-attachments/assets/bdbd4c8f-a65e-4724-9236-4f7ef8c30fd0" />


---

## AI Assistant Interface

<img width="563" height="152" alt="image" src="https://github.com/user-attachments/assets/86847846-e7c6-412e-b456-205460452ea7" />

Example interaction:

```
What is my current task?
How productive was I today?
What should I do next?
```

---

## Activity Detection

<img width="521" height="266" alt="image" src="https://github.com/user-attachments/assets/24b7d188-e980-4275-8cf1-af9013fb02d3" />


The system detects:

* posture
* activity
* motion
* emotional signals

---

# 🧠 System Architecture

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

# 📂 Project Structure

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
├── scheduler
├── utils
├── vision
├── voice_agent
├── web
│
├── main.py
├── web_app.py
├── requirements.txt
├── README.md
```

---

# ⚙ Installation Guide

## 1️⃣ Clone the Repository

```
git clone https://github.com/Priya-ak/mils-ai-assistant.git
cd mils-ai-assistant
```

---

## 2️⃣ Create Virtual Environment

Windows

```
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Upgrade pip

```
python -m pip install --upgrade pip
```

---

# ⚠ Dependency Conflict Note

Some libraries such as **TensorFlow, MediaPipe, and DeepFace** require compatible versions of **protobuf and numpy**.

For example:

```
TensorFlow 2.10 requires protobuf < 3.20
MediaPipe requires protobuf >= 3.11
```

The compatible version range is:

```
protobuf >=3.11 and <3.20
```

Recommended version:

```
protobuf==3.19.6
```

---

## Recommended Installation Order

Install core dependencies first:

```
pip install protobuf==3.19.6 numpy==1.23.5
pip install tensorflow==2.10.0 keras==2.10.0
```

Then install remaining dependencies:

```
pip install -r requirements.txt
```

---

# ⚡ Generating a Conflict-Free requirements.txt (Recommended)

To ensure all dependencies work correctly, generate the requirements file from a working environment.

### Step 1 — Activate environment

```
venv\Scripts\activate
```

### Step 2 — Check installed packages

```
pip list
```

If everything works without errors, freeze the environment.

### Step 3 — Generate requirements.txt

```
pip freeze > requirements.txt
```

This command:

* Reads all installed packages
* Saves exact working versions
* Writes them into `requirements.txt`

Example output:

```
deepface==0.0.79
flask==2.3.3
keras==2.10.0
mediapipe==0.10.7
numpy==1.23.5
opencv-python==4.8.1.78
protobuf==3.19.6
requests==2.31.0
torch==2.1.2
torchvision==0.16.2
tqdm==4.66.1
ultralytics==8.0.196
```

These versions are guaranteed to work together because they were installed in the same environment.

---

# ▶ Running the System

Start the AI assistant:

```
python main.py
```

Start the dashboard:

```
python web_app.py
```

Open the browser:

```
http://127.0.0.1:5000
```

---

# 💬 Example AI Interaction

```
User: What is my current task?

AI: Your current task is Deep Work Session.

User: How productive was I?

AI: Your productivity score today is 82%.

User: What should I do next?

AI: Continue your focus session or take a short break.
```

---

# 🛠 Technologies Used

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Core programming    |
| OpenCV     | Computer vision     |
| MediaPipe  | Pose detection      |
| DeepFace   | Emotion recognition |
| TensorFlow | Emotion model       |
| PyTorch    | Vision models       |
| Flask      | Web dashboard       |
| Ollama     | Local LLM inference |
| LLaMA      | AI reasoning        |

---

# 🔮 Future Improvements

* 📊 Productivity analytics dashboard
* 🧠 AI-based schedule optimization
* ☁ Cloud deployment
* 📱 Mobile interface
* 👥 Multi-user support

---

# 👩‍💻 Author

**Priyadharshini**

AI Systems • Computer Vision • Intelligent Productivity Tools

---

# ⭐ Support

If you find this project interesting:

⭐ Star the repository
🍴 Fork the project
🚀 Contribute improvements
