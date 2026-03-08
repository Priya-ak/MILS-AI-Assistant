import cv2

from ai_assistant.qa_agent import QAAgent
from schedular.ai_scheduler import AIScheduler
from schedular.autonomous_scheduler import AutonomousScheduler

from camera_module.posture import PostureDetector
from camera_module.object_detector import ObjectDetector
from camera_module.activity import ActivityClassifier

from utils.motion_detector import MotionDetector
from utils.productivity_tracker import ProductivityTracker
from utils.work_classifier import WorkClassifier
from utils.habit_memory import HabitMemory

from utils.voice_response import VoiceResponse
from voice_agent.assistant import VoiceAssistant

from emotion_module.emotion import EmotionDetector
from prediction_engine.decision_model import DecisionModel

from planner.day_planner import DayPlanner


# -----------------------------
# Initialize Modules
# -----------------------------

scheduler = AIScheduler()
auto_scheduler = AutonomousScheduler()

qa_agent = QAAgent()

posture_detector = PostureDetector()
object_detector = ObjectDetector()
activity_classifier = ActivityClassifier()
motion_detector = MotionDetector()

emotion_detector = EmotionDetector()
decision_model = DecisionModel()

tracker = ProductivityTracker()
work_classifier = WorkClassifier()

voice = VoiceResponse()
assistant = VoiceAssistant()

planner = DayPlanner()
habit_memory = HabitMemory()


# -----------------------------
# Shared Context
# -----------------------------

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
    "next_task": None,
    "next_time": None,
    "habits": {}
}


# -----------------------------
# AI Chat
# -----------------------------

def ask_assistant():

    while True:

        question = input("\nAsk Assistant ➜ ").strip()

        if not question:
            continue

        if question.lower() in ["exit", "quit"]:
            break

        command_response = assistant.process_command(question)

        if command_response != "I did not understand that command.":

            voice.speak(command_response)

        else:

            answer = qa_agent.ask(question, context)

            voice.speak(answer)
# -----------------------------
# Start Camera
# -----------------------------

cap = cv2.VideoCapture(0)


# -----------------------------
# Main AI Loop
# -----------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break


    # Emotion
    emotion = emotion_detector.detect_emotion(frame)


    # Posture
    try:
        _, posture_label = posture_detector.detect_posture(frame)
        posture = posture_label.lower()
    except:
        posture = "unknown"


    # Objects
    try:
        objects = object_detector.detect(frame)
    except:
        objects = []


    # Motion
    motion = motion_detector.detect_motion(frame)


    # Activity
    activity = activity_classifier.classify(posture, objects, motion)

    print("Detected Objects:", objects)
    print("Activity:", activity)


    # Work type
    work_type = work_classifier.classify(activity)


    # Productivity
    tracker.update(activity, work_type)

    stats = tracker.get_stats()

    print("Focus Time:", stats["focus_time"])
    print("Break Time:", stats["break_time"])
    print("Distraction Time:", stats["distraction_time"])
    print("Productivity Score:", stats["productivity_score"], "%")


    # Autonomous Scheduler
    auto_decision = auto_scheduler.check(
        activity,
        stats["focus_time"],
        stats["break_time"]
    )


    # AI Decision
    decision = decision_model.decide(
        activity,
        emotion,
        work_type,
        habits=context["habits"],
        posture=posture,
        productivity_score=stats["productivity_score"],
        focus_time=stats["focus_time"],
        break_time=stats["break_time"],
        distraction_time=stats["distraction_time"]
    )

    if auto_decision:
        decision = auto_decision

    planner.plan(decision)

    voice.speak(decision)


    # Habit learning
    habit_memory.record_activity(activity)
    habit_memory.analyze_patterns()

    habits = habit_memory.get_habits()

    print("Learned Habits:", habits)


    # Scheduler
    schedule_info = scheduler.get_current_task()

    task = schedule_info["current_task"]
    next_task = schedule_info["next_task"]
    next_time = schedule_info["next_time"]

    if task:
        print("Current Task:", task)

    if next_task:
        print("Next Task:", next_task, "at", next_time)


    # Update context
    context["activity"] = activity
    context["emotion"] = emotion
    context["work_type"] = work_type
    context["decision"] = decision

    context["focus_time"] = stats["focus_time"]
    context["break_time"] = stats["break_time"]
    context["distraction_time"] = stats["distraction_time"]
    context["productivity_score"] = stats["productivity_score"]

    context["task"] = task
    context["next_task"] = next_task
    context["next_time"] = next_time
    context["habits"] = habits


    # Display
    cv2.putText(frame, f"Emotion: {emotion}", (30,50),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame, f"Activity: {activity}", (30,90),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.putText(frame, f"Work: {work_type}", (30,130),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

    cv2.putText(frame, f"Decision: {decision}", (30,170),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("MILS AI Assistant", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------

cap.release()
cv2.destroyAllWindows()


print("\n==============================")
print("Camera closed.")
print("Ask the AI assistant anything about your session.")
print("Type 'exit' or 'quit' to end.")
print("==============================\n")

ask_assistant()

print("\nGoodbye.")