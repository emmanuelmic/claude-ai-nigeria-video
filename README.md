# Claude AI Nigeria Video - Educational Animation Project

An educational video project with animations explaining Claude AI and its use cases in Nigeria.

## 📚 Project Overview

This project creates animated educational content about:
- What is Claude AI?
- How Claude AI works
- Use cases and applications in Nigeria
- Practical demonstrations and examples

## 🛠️ Tech Stack

- **Manim**: Mathematical animation engine for creating animated explanations
- **Matplotlib**: For data visualizations and charts
- **Python 3.10+**: Programming language
- **FFmpeg**: For video processing (installed via Manim)

## 📁 Project Structure

```
claude-ai-nigeria-video/
├── README.md
├── requirements.txt
├── .gitignore
├── animations/
│   ├── __init__.py
│   ├── intro.py
│   ├── what_is_claude.py
│   ├── how_it_works.py
│   └── use_cases_nigeria.py
├── assets/
│   ├── images/
│   ├── data/
│   └── fonts/
├── output/
│   ├── videos/
│   └── previews/
├── config/
│   └── settings.py
└── scripts/
    └── render_all.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- FFmpeg (required for Manim)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/emmanuelmic/claude-ai-nigeria-video.git
   cd claude-ai-nigeria-video
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Rendering Animations

**Render a single animation:**
```bash
manim -pql animations/intro.py IntroScene
```

**Render all animations:**
```bash
python scripts/render_all.py
```

**Flags explanation:**
- `-p`: Play the animation after rendering
- `-q`: Quality (l=low, m=medium, h=high, k=4k)
- `-l`: Low quality (faster rendering)

## 📝 Animation Scripts

### Current Scenes:

- **intro.py**: Title and introduction animations
- **what_is_claude.py**: Explanation of Claude AI
- **how_it_works.py**: How Claude AI processes information
- **use_cases_nigeria.py**: Use cases specific to Nigeria

## 📊 Adding Custom Animations

Each animation file should follow this structure:

```python
from manim import *

class YourSceneName(Scene):
    def construct(self):
        # Your animation code here
        pass
```

## 🎬 Video Editing

Combine all rendered videos using FFmpeg or your preferred video editor.

## 📚 Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim Community](https://www.manim.community/)
- [Claude AI Official Docs](https://claude.ai/docs)

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

MIT License - feel free to use and distribute

## 📧 Contact

For questions or suggestions, reach out to emmanuelmic

---

**Happy animating! 🎨✨**
