# 📘 Flashy — French ↔ English Flashcards (Tkinter)

A clean and interactive flashcard learning app built with **Python**, **Tkinter**, and **Pandas**.
It helps you learn French vocabulary with automatic card flipping, progress saving, and a polished UI.

---

## 🎥 Demo

![Flashy Demo](./flashy_demo.gif)

---

## 🚀 Features

* ⏳ **Auto flip** from French → English after 3 seconds
* 🎴 Flashcard front/back design
* ✔️ Mark words as **Known**
* ❌ Mark words as **Unknown**
* 💾 Saves progress in `words_to_learn`
* 🔁 Continues from your last session
* 📊 Data handled through Pandas
* 🧠 Simple, clean vocabulary cycle

---

## 📂 Project Structure

```
Flashy/
│
├── main.py
├── data/
│   └── french_words.csv
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── flashy_demo.gif
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mrphoenix300/flashy.git
cd flashy
```

### 2️⃣ Install dependencies

```bash
pip install pandas
```

### 3️⃣ Run the app

```bash
python main.py
```

---

## 🎮 How It Works

1. Loads your saved progress from `words_to_learn` (if it exists).
2. Displays a **French word**.
3. After **3 seconds**, the card flips to show its **English translation**.
4. Press:

   * ❌ **Wrong** → add the word to your “unknown” list
   * ✔️ **Right** → remove it from the review list
5. Moves to the next word automatically.

---

## 📄 Learning Progress

Your progress is saved in:

```
words_to_learn
```

This file updates automatically based on your answers.

---

## 🧠 Built With

* Python
* Tkinter
* Pandas
* CSV data

---

## 📜 License

This project is licensed under the **MIT License**.
See the [`LICENSE`](./LICENSE) file for details.


