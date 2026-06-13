import time    # for time measurement
import random  # for random word selection

sentence = [
    "The quick brown fox jumps over the lazy dog",
    "Python programming is fun and rewarding",
    "Typing speed tests can improve your typing skills",
    "Practice makes perfect",
    "Stay focused and keep typing"
    "A journey of a thousand miles begins with a single step",
]

def typing_speed_test():
    test_sentence = random.choice(sentence) # randomly selects a sentence from the list
    print("Print the following as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    start_time = time.time()   #time.time() gives us the current time in seconds since the epoch
    user_input = input()   # takes the user's input
    end_time = time.time()   # captures the end time after the user has finished typing
    time_taken = end_time - start_time   # calculates the time taken by subtracting the start time from the end time
    words = len(test_sentence.split())   # counts the number of words in the test sentence
    wpm = (words / (time_taken / 60))   # calculates words per minute
    word_count = len(test_sentence.split(" "))   # counts the number of words in the test sentence
    print(f"Time taken: {time_taken / 60:.2f} minutes") 
    print(f"Words per minute: {wpm:.2f}")

    print("result of typing speed test")
    print(f"time taken: {time_taken / 60:.2f} minutes")
    print(f"words typed: {word_count}")
    print(f"typing speed : {word_count / (time_taken / 60):.2f} words per minute")

typing_speed_test()