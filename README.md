# SCT_CS_3(Password_Strength_Checker)
# 🔐 CyberSecure Password Strength Checker (Python + TKinter)

A **cybersecurity-themed Password Strength Checker** built using **Python** and **Tkinter GUI**.  
This project analyzes password strength in real time and gives visual feedback using colors, emojis, and a hacker-style interface.

---

## 🔍 Overview

---
The tool helps users evaluate their password security level based on:
- Password length  
- Use of uppercase & lowercase letters  
- Inclusion of numbers and special characters  

It displays the strength level (**Weak**, **Medium**, **Strong**, **Very Strong**) and highlights which rules are satisfied — perfect for **ethical hacking**, **cyber awareness**, and **beginner cybersecurity projects**.

## 🛡️ Features
- ✅ Checks for **length** (≥8 characters)  
- ✅ Validates **lowercase, uppercase, numbers, and special characters**  
- ✅ Emoji-based feedback (🔓 Weak ❌, 🔒 Medium ⚠️, 🔐 Strong ✅)  
- ✅ Beginner-friendly Python script  
- ✅ Can be extended into GUI or web tools  

---

| Technology | Purpose |
|-------------|----------|
| **Python 3.x** | Main programming language |
| **Tkinter** | GUI framework for interface |
| **Regex (re module)** | Password pattern validation |

---

## ⚙️ How It Works

1. The user enters a password in the GUI.  
2. The program checks for:
   - Length ≥ 8  
   - At least one uppercase letter  
   - At least one lowercase letter  
   - At least one number  
   - At least one special character  
3. Based on these checks, it assigns a **score** (0–5).  
4. The result is displayed as:
   - **Weak 🔓❌** (Red)  
   - **Medium 🔒⚠️** (Orange)  
   - **Strong ✅** (Light Green)  
   - **Very Strong 🔐** (Neon Green)  

---

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/password-strength-checker-python.git

