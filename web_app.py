"""
Web deployment for MILS AI Assistant.
Uses the same backend pipeline as main.py; does not modify existing modules.
"""

import base64
import os
import subprocess
import requests
import time

import cv2
import numpy as np
from flask import Flask, request, jsonify, send_from_directory

# Reuse exact same backend as main.py
from ai_assistant.qa_agent import QAAgent
from camera_module.posture import PostureDetector
from camera_module.object_detector import ObjectDetector
from camera_module.activity import ActivityClassifier
from utils.motion_detector import MotionDetector
from utils.productivity_tracker import ProductivityTracker
from utils.work_classifier import WorkClassifier
from utils.habit_memory import HabitMemory
from emotion_module.emotion import EmotionDetector
from prediction_engine.decision_model import DecisionModel


# ---------------------------
# AUTO START OLLAMA
# ---------------------------
def ensure_ollama_running():
    try:
        requests.get("http://localhost:11434", timeout=2)
        print("✅ Ollama already running")
    except:
        print("⚠ Ollama not running. Starting Ollama...")
        subprocess.Popen(["ollama", "serve"])
        time.sleep(5)


app = Flask(__name__, static_folder="web/static", template_folder="web/templates")

# One-time init (same as main.py)
posture_detector = PostureDetector()
object_detector = ObjectDetector()
activity_classifier = ActivityClassifier()
motion_detector = MotionDetector()
emotion_detector = EmotionDetector()
decision_model = DecisionModel()
tracker = ProductivityTracker()
work_classifier = WorkClassifier()
habit_memory = HabitMemory()
qa_agent = QAAgent()

context = {
    "activity": None,
    "emotion": None,
    "work_type": None,
    "decision": None,
    "focus_time": 0,
    "break_time": 0,
    "distraction_time": 0,
    "productivity_score": 0,
    "task": None,
    "habits": {},
}


def run_pipeline(frame_bgr):

    emotion = emotion_detector.detect_emotion(frame_bgr)

    try:
        _, posture_label = posture_detector.detect_posture(frame_bgr)
        posture = posture_label.lower() if isinstance(posture_label, str) else "unknown"
    except:
        posture = "unknown"

    try:
        objects = object_detector.detect(frame_bgr)
    except:
        objects = []

    motion = motion_detector.detect_motion(frame_bgr)

    activity = activity_classifier.classify(posture, objects, motion)

    work_type = work_classifier.classify(activity)

    tracker.update(activity, work_type)

    stats = tracker.get_stats()

    decision = decision_model.decide(
        activity,
        emotion,
        work_type,
        habits=context.get("habits") or {},
        posture=posture,
        productivity_score=stats.get("productivity_score"),
        focus_time=stats.get("focus_time", 0),
        break_time=stats.get("break_time", 0),
        distraction_time=stats.get("distraction_time", 0),
    )

    habit_memory.record_activity(activity)
    habit_memory.analyze_patterns()
    habits = habit_memory.get_habits()

    context["activity"] = activity
    context["emotion"] = emotion
    context["work_type"] = work_type
    context["decision"] = decision
    context["focus_time"] = stats["focus_time"]
    context["break_time"] = stats["break_time"]
    context["distraction_time"] = stats["distraction_time"]
    context["productivity_score"] = stats["productivity_score"]
    context["task"] = None
    context["habits"] = habits

    return {
        "emotion": emotion,
        "posture": posture,
        "objects": objects,
        "activity": activity,
        "work_type": work_type,
        "decision": decision,
        "focus_time": round(stats["focus_time"], 1),
        "break_time": round(stats["break_time"], 1),
        "distraction_time": round(stats["distraction_time"], 1),
        "productivity_score": stats["productivity_score"],
        "habits": habits,
    }


@app.route("/")
def index():
    return send_from_directory(app.template_folder, "index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.get_json() or {}
    image_b64 = data.get("image")

    if not image_b64:
        return jsonify({"error": "Missing image"}), 400

    try:
        raw = base64.b64decode(
            image_b64.split(",")[-1] if "," in image_b64 else image_b64
        )

        arr = np.frombuffer(raw, dtype=np.uint8)

        frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({"error": "Invalid image"}), 400

        result = run_pipeline(frame)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/ask", methods=["POST"])
def ask():

    ensure_ollama_running()

    data = request.get_json() or {}
    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({"error": "Missing question"}), 400

    try:
        answer = qa_agent.ask(question, context)
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e), "answer": None}), 500


@app.route("/api/context", methods=["GET"])
def get_context():
    return jsonify(context)


if __name__ == "__main__":

    ensure_ollama_running()

    os.makedirs(app.template_folder, exist_ok=True)

    print("🚀 Starting MILS AI Assistant Server")

    app.run(host="0.0.0.0", port=5000, debug=False)