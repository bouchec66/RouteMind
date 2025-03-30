© 2025 RouteMind Project. Released under the MIT License.

# RouteMind – Energy-Aware LLM Chaining Framework
![image](https://github.com/user-attachments/assets/d7a59dbe-dbc6-4e2a-bcf0-646a450498bc)
RouteMind is a modular, energy-aware framework for building plug-and-play LLM chains. It supports chaining LLMs into cost-effective, energy-conscious solutions across providers and model generations.
---

## 🚀 Project Goals

- ⚡ **Energy-aware orchestration**: dynamically route tasks to appropriate models based on cost/performance tradeoffs.
- 🧱 **Plug-and-play chain design**: swap in/out models, preprocessors, and logic with minimal friction.
- 🔄 **Reproducibility & Portability**: clean environment setup with rebuild/startup tooling.
- 🌐 **Remote-first**: developed with containerized or hosted GPU environments in mind.

---

https://github.com/bouchec66/RouteMind/wiki

## 📁 Project Structure

```
RouteMind/
├── README.md                # Project overview and setup instructions
├── LICENSE                  # License info (MIT)
├── docs/
│   └── wbs.md               # Work Breakdown Structure
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # Optional: static dependency pinning
├── rebuild_project.sh       # One-time environment reset script
├── startup.sh               # Regular dev session startup script
├── src/
│   └── RouteMind/           # Core logic and configuration
├── tests/                   # Test cases for critical modules
├── utils/                   # Utility scripts (e.g., chatbot, Gradio runner)
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

- This project installs itself as an **editable package**, so changes in `src/RouteMind/` reflect instantly.
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

