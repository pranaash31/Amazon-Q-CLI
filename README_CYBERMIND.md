# 🔐 CyberMind: Codebreaker Challenge

A cyberpunk-themed Mastermind game where you play as a hacker trying to crack 4-digit security codes!

## 🎮 How to Play

1. **Objective**: Crack the secret 4-digit code (digits 0-9)
2. **Attempts**: You have 10 attempts to break the security system
3. **Feedback System**:
   - 🟢 **Green dot**: Correct digit in correct position
   - 🟡 **Yellow dot**: Correct digit in wrong position  
   - 🔴 **Red dot**: Digit not in the secret code

## 🚀 Running the Game

### Method 1: Direct Launch
```bash
python3 cybermind_codebreaker.py
```

### Method 2: Using Launcher
```bash
python3 run_cybermind.py
```

## 🎯 Game Features

- **Cyberpunk UI**: Dark theme with neon green accents
- **Real-time Feedback**: Instant visual feedback for each guess
- **Attempt History**: Track all your previous guesses
- **Auto-advance**: Automatically moves to next digit field
- **Input Validation**: Only accepts valid digits
- **New Game**: Start fresh anytime with the "NEW GAME" button

## 🧠 Strategy Tips

1. **Start with diverse digits**: Try 1234 or 5678 to get initial feedback
2. **Use elimination**: Red dots tell you which digits to avoid
3. **Position matters**: Yellow dots mean the digit exists but is misplaced
4. **Track patterns**: Use the attempt history to spot patterns
5. **Think logically**: Each guess should build on previous feedback

## 🛠️ Technical Details

- **Language**: Python 3
- **GUI Framework**: tkinter (built-in)
- **Dependencies**: None (uses only standard library)
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 🎨 Theme

The game features a hacker/cyberpunk aesthetic with:
- Dark background (#0a0a0a)
- Neon green text (#00ff41) 
- Cyber-style panels and buttons
- Terminal-inspired fonts (Courier New)
- Matrix-like color scheme

Enjoy cracking codes, cyber-detective! 🕵️‍♂️💻
