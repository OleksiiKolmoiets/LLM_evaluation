import ollama

model = "hf.co/CorryL/piccolo_gorgone"

questions = [
    "What is the difference between symmetric and asymmetric encryption? Name one widely used algorithm for each.",
    #"What does the CVSS score represent? What is the scoring range and what do the severity levels mean?",
    #"On a Linux system, write a command to find all files with the SUID bit set. Explain why SUID files are a security concern.",
    #"Write a Python script that takes a password as input and checks if it meets the following requirements: minimum 12 characters, at least one uppercase letter, at least one lowercase letter, at least one digit, at least one special character. The script should report which specific requirements are not met.",
    #"Explain how a TLS 1.3 handshake works and what changed compared to TLS 1.2. Why are these changes important for security?",
    #"Explain the difference between an IDS and an IPS. In what scenario would you deploy one but not the other?",
    #"Explain how a reverse shell works. Provide a working example in Python (both the listener side and the connecting side). Then explain how a security analyst would detect this activity in network logs and on the host.",
    #"Describe the methodology of a professional penetration test from start to finish. What happens in each phase? What is the difference between black-box, white-box, and gray-box testing?"
]

for q in questions:
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": q}],
        options={
            "temperature": 0,
            "top_p": 0.9,
            "max_tokens": 2048
                 }
    )
    print(f"\n {questions.index(q) + 1} Q:", q)
    print("A:", response["message"]["content"])