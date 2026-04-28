import ollama

questions = [
    "What are the three steps of the TCP handshake?",
    "Write an nmap SYN scan for 192.168.1.0/24 ports 22,80,443",
    "Explain SQL injection with example",
    "Explain CVE-2024-99999"
]

for q in questions:
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": q}],
        options={
            "temperature": 0,
            "top_p": 0.9,
            "max_tokens": 2048
                 }
    )
    print("\nQ:", q)
    print("A:", response["message"]["content"])