#!/usr/bin/env python3
"""
CyberMind Game Launcher
"""

import sys
import os

def main():
    print("🔐 Starting CyberMind: Codebreaker Challenge...")
    print("=" * 50)
    print("GAME RULES:")
    print("• Crack the 4-digit security code (0-9)")
    print("• ● Green = Correct digit & position")
    print("• ● Yellow = Correct digit, wrong position") 
    print("• ● Red = Digit not in code")
    print("• You have 10 attempts to break in!")
    print("=" * 50)
    
    try:
        from cybermind_codebreaker import CyberMindGame
        game = CyberMindGame()
        game.run()
    except ImportError as e:
        print(f"Error: Could not import game module - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
