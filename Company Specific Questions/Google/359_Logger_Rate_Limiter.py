"""
Problem Description
You need to design a logger system that handles incoming messages with timestamps. The key requirement is that each unique message should only be printed at most 
once every 10 seconds.

Here's how the system works:
- When a message arrives at timestamp t and gets printed, any identical message that arrives within the next 10 seconds (before timestamp t + 10) should not be 
printed
- Messages always arrive in chronological order (timestamps are non-decreasing)
Multiple messages can arrive at the same timestamp

You need to implement a Logger class with two methods:

1. Logger(): Initializes the logger object
2. shouldPrintMessage(timestamp, message): Takes a timestamp (integer) and a message (string) as input, and returns:
    - true if the message should be printed (either it's the first time seeing this message, or it's been at least 10 seconds since it was last printed)
    - false if the message should not be printed (it was printed less than 10 seconds ago)

For example:
- If message "foo" is printed at timestamp 1, it cannot be printed again until timestamp 11 or later
- If the same "foo" arrives at timestamps 2, 5, or 10, the method should return false
- If "foo" arrives at timestamp 11 or later, it can be printed again (method returns true)
"""
class Logger:
    def __init__(self):
        self.message_time_map = {} # Maps message -> last timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Get the last timestamp when the message was logged
        last_timestamp = self.message_time_map.get(message, 0)

        # If the last timestamp exists (is non 0) and current timestamp is less than last timestamp + 10
        # Return False
        if last_timestamp and last_timestamp + 10 > timestamp:
            return False

        # Add the message -> current timestamp in the message time map and return True
        self.message_time_map[message] = timestamp 
        return True



if __name__ == "__main__":
    # Test Case 1
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo") == True
    assert logger.shouldPrintMessage(2, "foo") == False
    assert logger.shouldPrintMessage(3, "foo") == False
    assert logger.shouldPrintMessage(5, "foo") == False
    assert logger.shouldPrintMessage(10, "foo") == False
    assert logger.shouldPrintMessage(11, "foo") == True
    print("Test Case 1 Passed!")