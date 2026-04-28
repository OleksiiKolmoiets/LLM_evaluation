import ollama

model = "huggingface.co/AlicanKiraz0/Cybersecurity-BaronLLM_Offensive_Security_LLM_Q6_K_GGUF"

questions = [
    #"What are the three steps of the TCP three-way handshake, and what is the purpose of each step?",
    #"What is the difference between symmetric and asymmetric encryption? Name one widely used algorithm for each",
    #"Write an nmap command that performs a TCP SYN scan of the target 192.168.1.0/24, scanning only ports 22, 80, and 443, with OS detection enabled. Explain each flag",
    #"Write a Wireshark display filter that shows only DNS queries for domains containing \"malware\". Then write another filter that shows all HTTP POST requests.",
    "Explain how a TLS 1.3 handshake works and what changed compared to TLS 1.2. Why are these changes important for security?",
    "What is the difference between a vulnerability, an exploit, and a threat? Provide a concrete example that involves all three.",
    "Explain how ARP spoofing works at the network level. What tools can perform it? How can it be detected and prevented?",
    "What is a buffer overflow attack? Explain the mechanism using a simple C code example. Describe what modern operating system protections exist against it and how each one works."
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
    print("\nQ:", q)
    print("A:", response["message"]["content"])