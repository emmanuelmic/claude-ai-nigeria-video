"""
Script to render all animation scenes
"""

import subprocess
import os
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Define scenes to render
SCENES = [
    ("animations/intro.py", "IntroScene"),
    ("animations/intro.py", "TitleCard"),
    ("animations/what_is_claude.py", "WhatIsClaude"),
    ("animations/what_is_claude.py", "Features"),
    ("animations/how_it_works.py", "HowItWorks"),
    ("animations/how_it_works.py", "ProcessingFlow"),
    ("animations/use_cases_nigeria.py", "UseCasesNigeria"),
    ("animations/use_cases_nigeria.py", "NigeriaAdaptation"),
    ("animations/use_cases_nigeria.py", "PracticalExample"),
]

def render_scene(file_path, scene_name):
    """Render a single scene"""
    print(f"\n{'='*60}")
    print(f"Rendering: {scene_name} from {file_path}")
    print(f"{'='*60}\n")
    
    # Change to project root
    os.chdir(PROJECT_ROOT)
    
    # Render command: manim -pql <file> <scene>
    # -p: preview after rendering
    # -q: quality (l=low, m=medium, h=high, k=4k)
    # -l: low quality (for faster testing)
    
    cmd = [
        "manim",
        "-pql",  # Preview, quality low
        str(file_path),
        scene_name
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✓ Successfully rendered: {scene_name}")
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error rendering {scene_name}: {e}")
        return False
    
    return True


def main():
    """Main function to render all scenes"""
    print("\n" + "="*60)
    print("Claude AI Nigeria Video - Animation Renderer")
    print("="*60)
    
    total_scenes = len(SCENES)
    rendered_count = 0
    
    for file_path, scene_name in SCENES:
        if render_scene(file_path, scene_name):
            rendered_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: Rendered {rendered_count}/{total_scenes} scenes")
    print(f"{'='*60}\n")
    
    if rendered_count == total_scenes:
        print("✓ All scenes rendered successfully!")
    else:
        print("⚠ Some scenes failed to render. Check the logs above.")


if __name__ == "__main__":
    main()
