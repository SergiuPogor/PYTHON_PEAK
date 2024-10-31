# Use case: Collecting user feedback scores for multiple topics and ensuring all topics have default list values

feedback = {}

def add_feedback(user, topic, score):
    # Set default list for each topic, then append new score
    feedback.setdefault(user, {}).setdefault(topic, []).append(score)

# Add feedback entries
add_feedback("Alice", "usability", 8)
add_feedback("Alice", "features", 7)
add_feedback("Bob", "usability", 6)
add_feedback("Alice", "usability", 9)  # Adding another score for Alice on usability
add_feedback("Bob", "performance", 8)

print("Feedback Scores by User:")
for user, topics in feedback.items():
    print(f"\n{user}:")
    for topic, scores in topics.items():
        print(f"  {topic}: {scores}")