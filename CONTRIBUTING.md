# Contributing to Claude AI Nigeria Video

Welcome! We'd love your contributions. Here's how to get started:

## Getting Started

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes by rendering the animations
5. Commit with clear messages: `git commit -m "Add: Description of changes"`
6. Push to your branch: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Adding New Animations

1. Create a new file in the `animations/` directory
2. Follow the existing code structure and style
3. Use the color scheme from `config/settings.py`
4. Add the new scenes to `scripts/render_all.py`
5. Test by running: `manim -pql animations/your_file.py YourScene`

## Code Style

- Use clear, descriptive variable names
- Add comments for complex animations
- Follow the existing naming conventions (PascalCase for classes, snake_case for functions)

## Testing

Before submitting a PR:
- Render your animations to ensure they work
- Test with different quality levels (`-ql`, `-qm`, `-qh`)
- Check the output for visual issues

## Need Help?

- Check the [Manim Documentation](https://docs.manim.community/)
- Review existing animation files for examples
- Open an issue to discuss major changes first

Thank you for contributing! 🎨
