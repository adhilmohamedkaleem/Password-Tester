# Password Strength Tester 🔐

A modern **dark mode password strength checker** built using **Python** and **Tkinter**.

This application analyzes passwords in **real time** and estimates how long it would take to crack them — similar to tools like:

* Bitwarden Password Strength Tester
* Dropbox zxcvbn

---

## ✨ Features

* 🌙 Dark Mode UI
* ⚡ Real-Time Password Analysis
* 📊 Password Strength Meter
* 🔓 Estimated Crack Time
* 👁️ Show / Hide Password
* 💡 Password Improvement Suggestions
* 🛡️ Detects:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
  * Password length

---

## 🛠️ Technologies Used

* Python
* Tkinter
* Regex (`re` module)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/password-strength-tester.git
```

### 2. Navigate to Project Folder

```bash
cd password-strength-tester
```

### 3. Run the Application

```bash
python password_checker.py
```

---

## 📁 Project Structure

```text
password-strength-tester/
│
├── password_checker.py
├── README.md
└── assets/
```

---

## 🧠 How It Works

The application calculates password strength using:

* Password length
* Character diversity
* Estimated possible combinations
* Brute-force crack time estimation

### Strength Levels

| Score | Strength  |
| ----- | --------- |
| 0 - 2 | Weak 🔴   |
| 3 - 4 | Medium 🟡 |
| 5     | Strong 🟢 |

---

## 🔐 Crack Time Estimation

The app estimates crack time using:

```text
Possible Combinations = Character Set ^ Password Length
```

Then compares it against:

```text
1 Billion guesses per second
```

---

## 🚀 Future Improvements

* CustomTkinter modern UI
* Password entropy graph
* Breached password detection
* Save analysis report
* Web version using Flask or React
* AI-based password suggestions

---

## 🤝 Contributing

Pull requests are welcome.

If you'd like to improve the UI or security calculations, feel free to fork the project and submit a PR.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Made with ❤️ by Adhil Kaleem
