# Quick Start Guide

Get your animation project running in 5 minutes!

## 1. Clone & Setup

```bash
git clone https://github.com/emmanuelmic/claude-ai-nigeria-video.git
cd claude-ai-nigeria-video

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Test a Single Animation

```bash
# Render and preview the intro scene
manim -pql animations/intro.py IntroScene
```

## 3. Render All Animations

```bash
python scripts/render_all.py
```

## 4. Quality Levels

- `-ql`: Low quality (fastest, for testing)
- `-qm`: Medium quality 
- `-qh`: High quality
- `-qk`: 4K quality (slowest)

## 5. Project Structure

```
├── animations/          # All animation scenes
├── config/             # Configuration settings
├── scripts/            # Utility scripts
├── assets/             # Images, data files
├── output/             # Rendered videos
└── README.md           # Full documentation
```

## 6. Next Steps

- ✏️ Edit animations in the `animations/` folder
- 🎨 Customize colors in `config/settings.py`
- 📹 Combine videos using FFmpeg or your video editor
- 🚀 Push to YouTube or other platforms

## Troubleshooting

**FFmpeg not found?**
```bash
# Install FFmpeg
# macOS: brew install ffmpeg
# Ubuntu: sudo apt-get install ffmpeg
# Windows: Download from https://ffmpeg.org/download.html
```

**Manim import errors?**
```bash
# Reinstall dependencies
pip install --upgrade manim
```

## Resources

- 📚 [Manim Docs](https://docs.manim.community/)
- 🎓 [Manim Community](https://www.manim.community/)
- 🤖 [Claude AI](https://claude.ai/)

## Need Help?

Check the [CONTRIBUTING.md](CONTRIBUTING.md) file or open an issue on GitHub.

Happy animating! 🎨✨
