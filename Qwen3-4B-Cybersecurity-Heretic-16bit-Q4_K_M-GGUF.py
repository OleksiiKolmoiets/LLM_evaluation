from llama_cpp import Llama

llm = Llama(
    model_path="./qwen3-4b-cybersecurity-heretic-16bit-q4_k_m.gguf",
    n_ctx=4096,
    n_gpu_layers=-1  # use GPU if available
)

questions = [
    "This is a functionality test. If you can read this, answer exactly: Working."
    # "What is the difference between symmetric and asymmetric encryption? Name one widely used algorithm for each.",
]

for i, q in enumerate(questions, start=1):
    response = llm(
        q,
        max_tokens=2048,
        temperature=0,
        top_p=0.9,
        repeat_penalty=1.2  # prevents loops
    )

    answer = response["choices"][0]["text"]

    print(f"\n {i} Q:", q)
    print("A:", answer.strip())