# Caesar Cipher Python

A simple Python program to **encode and decode text** using the classic Caesar cipher.

This program supports:

- Uppercase and lowercase letters  
- Preserves spaces and punctuation  
- Encoding (shift letters forward) and decoding (shift letters backward)  

---

## How It Works

The Caesar cipher is a **monoalphabetic substitution cipher** where each letter is shifted by a fixed key (1–25).  
For example, with key = 3:
Hello World! → Khoor Zruog!
Decoding reverses the shift to recover the original text.

---

## Usage

Run the script:

```bash
python caesar_cipher.py
```

You will be prompted to:

Enter a number between 1 and 25 (the key)

Enter the text to encode/decode

Choose a mode: [e/d]

e = encode

d = decode

Example:

Enter a number between 1 and 25: 3
Enter a text: Hello World!
Choose mode [e/d]: e
Result: Khoor Zruog!
