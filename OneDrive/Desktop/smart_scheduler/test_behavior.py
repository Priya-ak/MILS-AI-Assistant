from behavior_engine.engine import BehaviorEngine

engine = BehaviorEngine()

activity = "Working"
emotion = "tired"
intent = "study"

decision = engine.decide(activity, emotion, intent)

print("Decision:", decision)