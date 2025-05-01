import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nIs it all inside of my head?", 0.12),
        ("Maybe you still think I don't care", 0.1),
        ("But all I need is you", 0.1),
        ("Yeah, you know it's true", 0.08),
        ("Yeah, you know it's true\n", 0.08),
        
        ("Forget about where we are", 0.1),
        ("And let go, we're so close", 0.09),
        ("If you don't know where to start", 0.08),
        ("Just hold on and don't run", 0.12),
        ("No...\n", 0.14),
        
        ("We're looking back", 0.09),
        ("We're messing around", 0.08),
        ("But that was then", 0.09),
        ("And this is now", 0.06),
        ("All we need is enough love", 0.14),
        ("To hold us", 0.1),
        ("Where we are", 0.09)
    ]
    
    delays = [0.4, 4.66, 8.7, 11, 13, 15.33, 18.33, 22.33, 26, 31, 32, 34, 35.7, 37.7, 39, 43.7, 46]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
    
    
