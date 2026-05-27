"""
How Claude AI works explanation
"""

from manim import *

class HowItWorks(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        # Title
        title = Text("How Claude AI Works", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        # Step 1: Input
        step1_box = Rectangle(width=2.5, height=1, color="#00D9FF", stroke_width=2, fill_opacity=0)
        step1_text = Text("Input", color="#00D9FF", font_size=20, weight=BOLD)
        step1_box.move_to([-4, 1.5, 0])
        step1_text.move_to(step1_box.get_center())
        
        self.play(Create(step1_box), Write(step1_text))
        
        # Arrow 1
        arrow1 = Arrow([-2.75, 1.5, 0], [-0.75, 1.5, 0], color="#00D9FF", stroke_width=2)
        self.play(Create(arrow1))
        
        # Step 2: Processing
        step2_box = Rectangle(width=2.5, height=1, color="#FFD700", stroke_width=2, fill_opacity=0)
        step2_text = Text("Process", color="#FFD700", font_size=20, weight=BOLD)
        step2_box.move_to([0.5, 1.5, 0])
        step2_text.move_to(step2_box.get_center())
        
        self.play(Create(step2_box), Write(step2_text))
        
        # Arrow 2
        arrow2 = Arrow([1.75, 1.5, 0], [3.75, 1.5, 0], color="#00D9FF", stroke_width=2)
        self.play(Create(arrow2))
        
        # Step 3: Output
        step3_box = Rectangle(width=2.5, height=1, color="#00D9FF", stroke_width=2, fill_opacity=0)
        step3_text = Text("Output", color="#00D9FF", font_size=20, weight=BOLD)
        step3_box.move_to([5, 1.5, 0])
        step3_text.move_to(step3_box.get_center())
        
        self.play(Create(step3_box), Write(step3_text))
        
        # Description
        desc = Text(
            "Claude processes your input and\ngenerates intelligent responses",
            color="#FFFFFF",
            font_size=24
        )
        desc.move_to(DOWN * 2)
        self.play(FadeIn(desc))
        
        self.wait(2)


class ProcessingFlow(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        title = Text("Processing Pipeline", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        steps = [
            "1. Receive user input",
            "2. Tokenize text",
            "3. Process through neural network",
            "4. Generate response",
            "5. Return to user"
        ]
        
        for i, step in enumerate(steps):
            text = Text(step, color="#FFFFFF", font_size=24)
            text.move_to(UP * (2 - i * 0.7))
            self.play(FadeIn(text), run_time=0.5)
            self.wait(0.3)
        
        self.wait(2)
