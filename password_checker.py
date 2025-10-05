import re
import tkinter as tk
from tkinter import ttk

# ---------- UI & logic ----------
def evaluate_password(event=None):
    pwd = pw_var.get()

    has_lower = bool(re.search(r"[a-z]", pwd))
    has_upper = bool(re.search(r"[A-Z]", pwd))
    has_digit = bool(re.search(r"\d", pwd))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>\\[\\]\\/\\\\;:'`~+=-_]", pwd))
    long_enough = len(pwd) >= 8

    score = sum([has_lower, has_upper, has_digit, has_special, long_enough])

    # Update checklist visuals
    update_check(lbl_length, long_enough)
    update_check(lbl_lower, has_lower)
    update_check(lbl_upper, has_upper)
    update_check(lbl_digit, has_digit)
    update_check(lbl_special, has_special)

    # Update progress and text
    if score == 0:
        progress['value'] = 0
        strength_lbl.config(text="Empty", foreground="gray")
    elif score <= 2:
        progress['value'] = 25
        strength_lbl.config(text="Weak 🔓❌", foreground="#ff4d6d")
    elif score == 3:
        progress['value'] = 55
        strength_lbl.config(text="Medium 🔒⚠️", foreground="#ffb86b")
    elif score == 4:
        progress['value'] = 80
        strength_lbl.config(text="Strong ✅", foreground="#4de89a")
    else:  # 5
        progress['value'] = 100
        strength_lbl.config(text="Very Strong 🔐", foreground="#00ff7a")

def update_check(label_widget, ok):
    # label_widget is a Label; we show ✓ or • and color change
    if ok:
        label_widget.config(text="✓  " + label_widget._base_text, foreground="#4de89a")
    else:
        label_widget.config(text="•  " + label_widget._base_text, foreground="#9aa7b2")

def toggle_show():
    # Toggle show/hide password
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        entry.config(show='')
        toggle_btn.config(text='Hide')
    entry.focus_set()

# ---------- Build GUI ----------
root = tk.Tk()
root.title("CyberSecure — Password Checker (Tkinter)")
root.geometry("480x380")
root.configure(bg="#071026")

# Header
header = tk.Label(root, text="🔐 CyberSecure — Password Strength Checker", font=("Helvetica", 14, "bold"),
                  fg="#66ffb2", bg="#071026")
header.pack(pady=(14, 6))

sub = tk.Label(root, text="Type a password to analyze its strength (live).", fg="#9aa7b2", bg="#071026")
sub.pack()

frame = tk.Frame(root, bg="#071026")
frame.pack(pady=12, padx=12, fill="x")

# Password entry + toggle
pw_var = tk.StringVar()
entry = tk.Entry(frame, textvariable=pw_var, font=("Courier New", 14), show="*", width=28,
                 bg="#0a1620", fg="#e6f1f5", insertbackground="#e6f1f5", relief="flat")
entry.grid(row=0, column=0, padx=(2,6), pady=6, sticky="w")

toggle_btn = tk.Button(frame, text="Show", command=toggle_show, bg="#001a13", fg="#00ff7a", relief="raised")
toggle_btn.grid(row=0, column=1, padx=(0,2), pady=6, sticky="e")

# Progress bar and strength label
progress_style = ttk.Style()
progress_style.theme_use('default')
progress_style.configure("green.Horizontal.TProgressbar", troughcolor="#0a1620", background="#00ff7a",
                         thickness=14, bordercolor="#071026")

progress = ttk.Progressbar(root, style="green.Horizontal.TProgressbar", orient="horizontal", length=400, mode="determinate")
progress.pack(pady=(6,4))

strength_frame = tk.Frame(root, bg="#071026")
strength_frame.pack(fill="x", padx=12)
strength_lbl = tk.Label(strength_frame, text="Strength: —", font=("Helvetica", 12, "bold"), bg="#071026", fg="#e6f1f5")
strength_lbl.pack(anchor="w")

# Checklist
checks_frame = tk.Frame(root, bg="#071026")
checks_frame.pack(pady=12, padx=12, fill="x")

lbl_length = tk.Label(checks_frame, text="•  At least 8 characters", anchor="w", bg="#071026", font=("Arial", 11))
lbl_lower = tk.Label(checks_frame, text="•  Contains lowercase letter", anchor="w", bg="#071026", font=("Arial", 11))
lbl_upper = tk.Label(checks_frame, text="•  Contains uppercase letter", anchor="w", bg="#071026", font=("Arial", 11))
lbl_digit = tk.Label(checks_frame, text="•  Contains a number", anchor="w", bg="#071026", font=("Arial", 11))
lbl_special = tk.Label(checks_frame, text="•  Contains a special character (e.g. !@#%)", anchor="w", bg="#071026", font=("Arial", 11))

# store base text so update_check can reuse it
for lbl in (lbl_length, lbl_lower, lbl_upper, lbl_digit, lbl_special):
    lbl._base_text = lbl.cget("text")[3:]  # remove "•  " prefix from stored base text
    lbl.pack(anchor="w", pady=2)

# Bind key updates
entry.bind("<KeyRelease>", evaluate_password)
# Also link variable changes (in case of paste)
pw_var.trace_add("write", lambda *args: evaluate_password())

# initial state
evaluate_password()

# Footer / instructions
footer = tk.Label(root, text="Tip: Use a passphrase (3+ random words) or a password manager.", fg="#9aa7b2", bg="#071026")
footer.pack(side="bottom", pady=10)

root.mainloop()
