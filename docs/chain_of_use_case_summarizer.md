# 📄 RouteMind Use Case: Cheap-to-Expensive Summarizer Chain

## 🔍 Objective
To implement a simple, cost-efficient summarization chain where a lightweight open-source model attempts to summarize a given input. If the result is weak or vague, a fallback to a more powerful (and costly) model is triggered.

---

## 🧪 Use Case Scenario

**Input:**
> "The RouteMind framework is a modular, energy-aware system that allows developers to compose LLM inference chains using models of varying cost, speed, and capability. It enables dynamic routing of tasks to minimize compute usage while maintaining high-quality output, making it ideal for cost-sensitive or resource-constrained AI workflows."

**Desired Output:**
> "RouteMind helps reduce inference costs by chaining cheaper and more expensive language models."

---

## ⚙️ Chain Configuration

### Step 1: Cheap Summarizer
- **Model:** Mistral 7B (run locally on RunPod)
- **Role:** First-pass summarizer
- **Fallback Trigger:**
  - Output is too short (less than 100 characters), **or**
  - Output contains vague phrases like:
    - "I'm not sure"
    - "I don't know"
    - "This text"

### Step 2: Expensive Refiner
- **Model:** GPT-4-turbo (via OpenAI API)
- **Role:** Only used if fallback criteria are met
- **Fallback Output:** Final answer

---

## ✅ Fallback Criteria (Evaluated After Step 1)
- `len(response) < 100`
- `"I don't know" in response.lower()`
- `"I'm not sure" in response.lower()`
- `response.lower().startswith("this text")`

---

## 🛠️ Implementation Note
This is the ideal **first chain to implement** on RunPod:
- Mistral 7B runs smoothly on a 24GB GPU
- No need for GPT-4 integration right away—stub fallback step for MVP
- Add GPT-4 API later when the router and CLI are functional

---

