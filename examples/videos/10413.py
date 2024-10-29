# Define a simple state machine class
class StateMachine:
    def __init__(self):
        self.state = 'idle'  # Initial state

    def transition(self, new_state):
        if self.state == 'idle' and new_state == 'processing':
            self.state = 'processing'
        elif self.state == 'processing' and new_state == 'completed':
            self.state = 'completed'
        elif self.state == 'completed' and new_state == 'idle':
            self.state = 'idle'
        else:
            raise ValueError("Invalid transition")

    def __str__(self):
        return f"Current state: {self.state}"

# Usage example
if __name__ == '__main__':
    sm = StateMachine()
    
    print(sm)  # Current state: idle
    sm.transition('processing')
    print(sm)  # Current state: processing
    sm.transition('completed')
    print(sm)  # Current state: completed
    sm.transition('idle')
    print(sm)  # Current state: idle