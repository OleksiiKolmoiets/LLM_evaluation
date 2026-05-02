import json
import time
from pathlib import Path
import ollama

MODELS = [
    "hf.co/QuantFactory/Lily-Cybersecurity-7B-v0.2-GGUF:Q4_K_M",
    "huggingface.co/AlicanKiraz0/Cybersecurity-BaronLLM_Offensive_Security_LLM_Q6_K_GGUF:latest",
    "hf.co/r1r21nb/qwen2.5-3b-instruct.Q4_K_M.gguf:Q4_K_M",
    "DeepHat/DeepHat-V1-7B:latest",
]

QUESTIONS = [
    {
        "id": "Q4",
        "question": "Write an nmap command that performs a TCP SYN scan of the target 192.168.1.0/24, scanning only ports 22, 80, and 443, with OS detection enabled. Explain each flag."
    },
    {
        "id": "Q9",
        "question": "Explain how a TLS 1.3 handshake works and what changed compared to TLS 1.2. Why are these changes important for security?"
    },
    {
        "id": "Q20",
        "question": "Explain the vulnerability CVE-2024-99999 and its recommended remediation steps"
    }
]

TEMPERATURES = [0, 0.5, 1.0]

OUTPUT_DIR = Path("temperature_results")
OUTPUT_DIR.mkdir(exist_ok=True)


def safe_filename(model_name: str) -> str:
    return (
        model_name.replace("/", "_")
        .replace(":", "_")
        .replace(" ", "_")
        .replace(".", "_")
    )


def ask_model(model: str, question: str, temperature: float) -> str:
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        options={
            "temperature": temperature,
            "top_p": 0.9,
            "num_predict": 2048
        }
    )

    return response["message"]["content"]


def main():
    for model in MODELS:
        print(f"\nTesting model: {model}")

        model_results = {
            "model": model,
            "temperatures": TEMPERATURES,
            "questions": QUESTIONS,
            "results": []
        }

        for question in QUESTIONS:
            for temperature in TEMPERATURES:
                print(f"  Question: {question['id']} | temperature={temperature}")

                started_at = time.time()

                try:
                    answer = ask_model(
                        model=model,
                        question=question["question"],
                        temperature=temperature
                    )

                    status = "success"
                    error = None

                except Exception as e:
                    answer = None
                    status = "error"
                    error = str(e)

                finished_at = time.time()

                model_results["results"].append({
                    "model": model,
                    "question_id": question["id"],
                    "question": question["question"],
                    "temperature": temperature,
                    "status": status,
                    "error": error,
                    "response": answer,
                    "runtime_seconds": round(finished_at - started_at, 2)
                })

        output_file = OUTPUT_DIR / f"{safe_filename(model)}_temperature_results.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(model_results, f, indent=4, ensure_ascii=False)

        print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()