"""
Explanation of what Claude AI is
"""

from manim import *

class WhatIsClaude(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        # Title
        title = Text("What is Claude AI?", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        # Key points
        points = [
            "✓ An AI assistant created by Anthropic",
            "✓ Trained to be helpful, harmless, and honest",
            "✓ Can understand and generate text",
            "✓ Available for free and premium users",
            "✓ Accessible in Nigeria and worldwide"
        ]
        
        point_objects = []
        for i, point in enumerate(points):
            text = Text(point, color="#FFFFFF", font_size=28)
            text.move_to(UP * (2 - i * 0.8))
            point_objects.append(text)
        
        # Animate points one by one
        for point in point_objects:
            self.play(FadeIn(point), run_time=0.5)
            self.wait(0.5)
        
        self.wait(2)


class Features(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        # Title
        title = Text("Key Features", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        # Feature boxes
        features = ["Multi-Modal", "Fast", "Accurate", "Affordable"]
        
        for i, feature in enumerate(features):
            # Create box
            box = Rectangle(
                width=3,
                height=1.5,
                color="#00D9FF",
                stroke_width=2,
                fill_color="#2A2A2A",
                fill_opacity=0.8
            )
            
            # Position in grid
            x = -4.5 + (i % 2) * 4.5
            y = 1.5 - (i // 2) * 2.5
            box.move_to([x, y, 0])
            
            # Text
            text = Text(feature, color="#00D9FF", font_size=24, weight=BOLD)
            text.move_to(box.get_center())
            
            self.play(Create(box), Write(text), run_time=1)
        
        self.wait(2)
