# ⚡ Energy-Aware LLM Chaining Framework

A modular, energy-efficient framework for building plug-and-play LLM chains. Designed to support chaining LLMs into cost-effective, energy-conscious solutions.
---

## 🚀 Project Goals

- ⚡ **Energy-aware orchestration**: dynamically route tasks to appropriate models based on cost/performance tradeoffs.
- 🧱 **Plug-and-play chain design**: swap in/out models, preprocessors, and logic with minimal friction.
- 🔄 **Reproducibility & Portability**: clean environment setup with rebuild/startup tooling.
- 🌐 **Remote-first**: developed with containerized or hosted GPU environments in mind.

---

## Long-Term Vision

The idea for chaining LLMs came from observing how we, as humans, approach problems. Most of the time, we use just enough effort to function effectively—and only dive deep when necessary. This mirrors how we think about efficiency in everything from manufacturing to daily life.

With the growing variety of LLMs—older, smaller, cheaper models alongside newer, larger, more power-hungry ones—it can be confusing to decide which to use. My proposal is simple: start small and scale up only as needed. By using lightweight models first and escalating to more powerful ones when required, we can solve problems more efficiently, both in terms of cost and energy.
This project aims to evolve into:

- **An Open-Source Protocol for Model Chaining:**  
  Developing a standardized protocol, tentatively named *LLMCast* or *ChainML*, to facilitate seamless integration and communication between diverse language models.

- **A Standard Adapter Library Between Open Models:**  
  Creating a comprehensive adapter library that enables interoperability among various open-source models, enhancing flexibility and usability.

- **A Green AI Toolkit with Live Token Cost & Energy Estimation:**  
  Building a toolkit focused on sustainability, providing real-time insights into token costs and energy consumption to promote environmentally conscious AI development.

Achieving these objectives will contribute meaningfully to the AI community by emphasizing collaboration, standardization, and sustainability.

## 📁 Project Structure

```
energy_aware_models/
├── src/
│   └── energy_aware_models/
│       ├── __init__.py
│       ├── config.py
│       └── main.py
├── venv/ (created by rebuild script)
├── rebuild_project.sh
├── startup.sh
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🧰 Setup Instructions

### 🔄 One-Time Rebuild

Run this if you're starting fresh or need to clean and restore your project environment:

```bash
./rebuild_project.sh
```

What it does:

- Backs up your `.git` directory
- Wipes everything else
- Restores `rebuild_project.sh` from Git
- Reinstalls your project into a **virtual environment**
- Installs dependencies from `pyproject.toml`
- Leaves you with a clean, reproducible dev setup

---

### 🔁 Regular Startup

Once your environment is built, use this script to activate the virtual environment and start developing:

```bash
source startup.sh
```

What it does:

- Activates `./venv`
- Prints out your current Python path and installed packages
- Leaves you ready to run `python`, launch scripts, or work in a REPL

---

## 🧪 Development Notes

- This project installs itself as an **editable package**, so changes in `src/energy_aware_models/` reflect instantly.
- Ideal for containerized dev (e.g., RunPod, Docker).
- Designed for chaining LLM calls together using dynamic routing, caching, and cost-aware strategies (coming soon).

---

## 📌 Coming Soon

- Configurable chaining syntax (YAML/JSON-based?)
- Cost/log tracking
- Model marketplace integration
- More robust examples + CLI

---

## 📄 License

License: MIT
---

## 🤝 Contributing

PRs welcome once this hits v0.2! Feel free to file issues or feature requests.

