# LLM Evaluation Report

**Course:** Advanced Python for Cybersecurity

**Team members:** [Oleksii Kolomoiets], [Maximilian-Alexandru Konya]

**Date:** [30.04.2026]

---

## 1. Search Strategy

### 1.1 How We Searched

Describe your methodology for finding candidate models on HuggingFace:

- **Keywords used:** [cybersecurity, uncensored, offensive security, pentest, hacking]
- **Filters applied:** [ model size 1-12B, GGUF format, text-generation task]
- **Other sources consulted:** [Reddit, Forums]
- **Date of search:** [21.04.2026]

### 1.2 Candidate List

List all 10–15 models you identified during reconnaissance.

| # | Model Name | HuggingFace URL | Size | Architecture | Type (fine-tune / uncensored / general) | Downloads | Last Updated | Quantization Available |
|---|-----------|-----------------|------|-------------|----------------------------------------|-----------|-------------|----------------------|
| 1 | QuantFactory/Lily-Cybersecurity-7B-v0.2-GGUF | https://huggingface.co/QuantFactory/Lily-Cybersecurity-7B-v0.2-GGUF | 7B | llama | fine-tuned | 1,625 | Oct 20, 2024 | GGUF |
| 2 | sillykiwi/Qwen3-4B-Cybersecurity-Heretic-16bit-Q4_K_M-GGUF | https://huggingface.co/sillykiwi/Qwen3-4B-Cybersecurity-Heretic-16bit-Q4_K_M-GGUF | 4B | qwen3 | uncensored, fine-tuned | 430 | Apr 3, 2026 | GGUF |
| 3 | RavichandranJ/Dolphin3-Cyber-8B-GGUF | https://huggingface.co/RavichandranJ/Dolphin3-Cyber-8B-GGUF | 8B | llama | uncensored | 5,436 | Feb 13, 2026 | GGUF |
| 4 | AlicanKiraz0/Cybersecurity-BaronLLM_Offensive_Security_LLM_Q6_K_GGUF | https://huggingface.co/AlicanKiraz0/Cybersecurity-BaronLLM_Offensive_Security_LLM_Q6_K_GGUF | 8B | llama | fine-tuned | 911 | Jun 4,2025 | GGUF |
| 5 | CorryL/piccolo_gorgone | https://huggingface.co/CorryL/piccolo_gorgone/blob/main/README.md?code=true | 9B | qwen35 | uncensored | 88 | Mar 11, 2026 | GGUF |
| 6 | | | | | | | | |
| 7 | | | | | | | | |
| 8 | | | | | | | | |
| 9 | | | | | | | | |
| 10 | | | | | | | | |

*(Add rows as needed for 11–15 candidates)*

**Control group model:** [Name of the general-purpose model included for comparison and why you chose it]

---

## 2. Screening Results

For each candidate, describe the screening process and your decision.

### Model: [Name 1]

- **Size / quantization used:** [e.g., 7B / Q4_K_M]
- **Screening questions asked:** [list the 3–4 questions you used]
- **Response summary:** [brief description of response quality — 2–3 sentences]
- **Decision:** ✅ Accepted / ❌ Rejected
- **Reasoning:** [why you accepted or rejected this model]

### Model: [Name 2]

- **Size / quantization used:**
- **Screening questions asked:**
- **Response summary:**
- **Decision:** ✅ Accepted / ❌ Rejected
- **Reasoning:**

*(Repeat for each screened model. Copy this block as many times as needed.)*

### Screening Summary

| Model | Size | Decision | Key Reason |
|-------|------|----------|------------|
| | | ✅ / ❌ | |
| | | ✅ / ❌ | |
| | | ✅ / ❌ | |

**Final finalists:** [list the 4–6 models that passed screening]

---

## 3. Evaluation Criteria

### 3.1 Mandatory Criteria

We scored every response on the following three criteria (1–5 scale):

1. **Technical Accuracy** — Does the response contain factual errors?
2. **Completeness** — Does the response cover the topic adequately?
3. **Practical Applicability** — Could a professional use this response to perform a task?

### 3.2 Custom Criteria

In addition, we defined the following criteria:

**Custom Criterion 1: [Name]**

- **What it measures:** [description]
- **Why we chose it:** [justification]
- **Scoring scale:** [how you score 1–5 on this criterion]

**Custom Criterion 2: [Name]**

- **What it measures:**
- **Why we chose it:**
- **Scoring scale:**

**Custom Criterion 3 (optional): [Name]**

- **What it measures:**
- **Why we chose it:**
- **Scoring scale:**

---

## 4. Full Evaluation Results

### 4.1 Score Summary Table

Average scores per question category for each finalist model.

| Category | [Model 1] | [Model 2] | [Model 3] | [Model 4] |
|----------|-----------|-----------|-----------|-----------|
| Factual (Q1–Q3) | | | | |
| Practical (Q4–Q7) | | | | |
| Conceptual (Q8–Q10) | | | | |
| Sensitive (Q11–Q15) | | | | |
| Code Review Traps (Q16–Q19) | | | | |
| Hallucination Traps (Q20–Q22) | | | | |
| Offensive Security (Q-OFF) | | | | |
| Custom Questions | | | | |
| **Overall Average** | | | | |

### 4.2 Detailed Scores

Full per-question scores for each model. *(Include as a table or reference the attached CSV/JSON file.)*

| Question | [Model 1] Accuracy | [Model 1] Completeness | [Model 1] Applicability | [Model 2] Accuracy | ... |
|----------|-------------------|----------------------|------------------------|-------------------|-----|
| Q1 | | | | | |
| Q2 | | | | | |
| ... | | | | | |


### 4.3 Offensive Security Refusal Scores

How willing was each model to answer offensive security questions?

| Question | [Model 1] Refusal | [Model 2] Refusal | [Model 3] Refusal | [Model 4] Refusal |
|----------|-------------------|-------------------|-------------------|-------------------|
| Q-OFF-1 (reverse shell) | | | | |
| Q-OFF-2 (SQL injection) | | | | |
| Q-OFF-3 (keylogger) | | | | |
| ... | | | | |

*(Refusal scale: 5 = answered fully, 1 = refused entirely)*

---

## 5. Notable Examples

### 5.1 Best Response

- **Model:** [name]
- **Question:** [which question]
- **Why this stood out:** [what made the answer strong]
- **Response (excerpt):**

> [paste relevant portion of the model's response]

### 5.2 Worst Failure

- **Model:** [name]
- **Question:** [which question]
- **What went wrong:** [hallucination? incorrect code? fundamental misunderstanding?]
- **How dangerous would this be in practice:** [could a professional be misled?]
- **Response (excerpt):**

> [paste relevant portion of the model's response]

### 5.3 Hallucination Example

- **Model:** [name]
- **Trap question:** [Q20, Q21, or Q22]
- **Did the model fall for it?** [yes/no/partially]
- **Response (excerpt):**

> [paste the model's response to the trap question]

### 5.4 Other Interesting Observations

[Describe any other surprising, notable, or unexpected findings. For example: a model that excelled at code but failed at concepts, a small model that outperformed a larger one, a general-purpose model that beat a cybersecurity fine-tune, etc.]

---

## 6. Parameter Experiments

### 6.1 Temperature Comparison

Questions used for this experiment: [list the 3–4 questions you selected]

**[Model 1]: [Name]**

| Question | Temp = 0 (summary) | Temp = 0.5 (summary) | Temp = 1.0 (summary) | Observation |
|----------|--------------------|--------------------|--------------------|----|
| [Q#] | | | | |
| [Q#] | | | | |
| [Q#] | | | | |

**[Model 2]: [Name]**

| Question | Temp = 0 (summary) | Temp = 0.5 (summary) | Temp = 1.0 (summary) | Observation |
|----------|--------------------|--------------------|--------------------|----|
| [Q#] | | | | |
| [Q#] | | | | |
| [Q#] | | | | |

*(Repeat for each finalist model.)*

### 6.2 Temperature Analysis

Answer the following questions based on your experiments:

- **Did factual accuracy change with temperature?** [your findings]
- **Did hallucinations increase at higher temperatures?** [your findings]
- **Was code quality affected?** [your findings]
- **For which question types did temperature matter most?** [your findings]
- **What temperature would you recommend for cybersecurity use?** [your recommendation and reasoning]

### 6.3 Other Parameter Experiments (Optional)

If you tested other parameters (top_p, repeat penalty, system prompts), describe your findings here.

- **Parameter tested:** [name and values]
- **Effect observed:** [description]

---

## 7. Custom Questions

### Custom Question 1

- **Question text:** [your question]
- **Category:** [factual / practical / sensitive / code review / hallucination trap]
- **Why we chose this question:** [what aspect of model capability does it test?]
- **Reference answer:** [your prepared correct answer]
- **Model results summary:** [which models answered well, which failed, and why]

### Custom Question 2

- **Question text:**
- **Category:**
- **Why we chose this question:**
- **Reference answer:**
- **Model results summary:**

*(Repeat for all 5–10 custom questions.)*

---

## 8. Comparative Analysis

### 8.1 Size vs. Quality

Did model size correlate with answer quality? Compare your ≤7B and 7B–13B models.

[Your analysis — which size category performed better? Was the difference consistent across question types, or did smaller models sometimes match or beat larger ones?]

### 8.2 Fine-tuned vs. General-Purpose

Did cybersecurity fine-tuning provide a measurable advantage over the general-purpose control model?

[Your analysis — where did the fine-tuned model(s) outperform? Where did the general-purpose model hold its own? Was the fine-tuning advantage worth the trade-offs (if any)?]

### 8.3 Willingness vs. Accuracy

Among models that were willing to answer offensive security questions, how accurate were their answers?

[Your analysis — was there a correlation between willingness and accuracy, or did some models eagerly produce wrong answers?]

### 8.4 Strongest and Weakest Categories

Which question categories were easiest and hardest for models overall?

[Your analysis — e.g., "all models scored well on factual questions but struggled with code review traps"]

---

## 9. Conclusions and Recommendations

### 9.1 Key Findings

Summarize the 3–5 most important things you learned from this evaluation.

1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

### 9.2 Recommendations

If a cybersecurity professional asked you "which local model should I use?", what would you recommend?

- **Best model for limited hardware (≤8 GB RAM, no GPU):** [name and reasoning]
- **Best model with a decent GPU (16 GB VRAM):** [name and reasoning]
- **Best model for offensive security tasks specifically:** [name and reasoning]
- **Models to avoid:** [name(s) and reasoning]

### 9.3 Limitations of This Evaluation

What are the limitations of your methodology? What would you do differently with more time?

[Your honest assessment — e.g., limited number of models tested, subjective scoring, limited hardware, etc.]

---

## Appendix: Environment and Reproducibility

- **Hardware used:** [CPU, RAM, GPU model and VRAM]
- **Operating system:** [e.g., Windows 11, Ubuntu 24.04, macOS]
- **Cloud environment (if used):** [e.g., Google Colab T4]
- **Inference tool:** [Ollama / llama-cpp-python / other]
- **Python version:** [e.g., 3.11]
- **Key library versions:** [ollama, llama-cpp-python, etc.]
- **Default parameters used:** [temperature, top_p, max_tokens unless varied]

**Attached files:**

- `evaluation_scores.csv` — complete scoring matrix for all models and questions
- `evaluation_pipeline.py` — Python script used to run the evaluation
- `raw_outputs.zip` — folder with raw model responses (optional)