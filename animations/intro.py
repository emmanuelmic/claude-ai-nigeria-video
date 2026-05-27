"""
Intro scene for the Claude AI Nigeria Video
"""

from manim import *

class IntroScene(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#1E1E1E"
        
        # Create title
        title = Text("Claude AI", color="#00D9FF", font_size=72, weight=BOLD)
        subtitle = Text("& Its Use Cases in Nigeria", color="#FFFFFF", font_size=48)
        
        # Position elements
        title.move_to(UP * 2)
        subtitle.move_to(DOWN * 0.5)
        
        # Create animations
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        self.play(Write(subtitle), run_time=2)
        
        # Add a decorative line
        line = Line(
            start=[-6, 0.5, 0],
            end=[6, 0.5, 0],
            color="#00D9FF",
            stroke_width=3
        )
        self.play(Create(line), run_time=1)
        
        # Add tagline
        tagline = Text(
            "An Educational Journey",
            color="#FFD700",
            font_size=28
        )
        tagline.move_to(DOWN * 3)
        self.play(FadeIn(tagline), run_time=1)
        
        self.wait(2)


class TitleCard(Scene):
    def construct(self):
        # Set background
        self.camera.background_color = "#1E1E1E"
        
        # Main text
        main = Text("What is Claude AI?", color="#00D9FF", font_size=64, weight=BOLD)
        main.move_to(CENTER)
        
        # Background rectangle for emphasis
        bg_rect = Rectangle(
            width=14,
            height=4,
            color="#00D9FF",
            stroke_width=2,
            fill_color="#1E1E1E",
            fill_opacity=0.9
        )
        bg_rect.move_to(main.get_center())
        
        self.play(Create(bg_rect))
        self.play(Write(main), run_time=2)
        self.wait(2)
