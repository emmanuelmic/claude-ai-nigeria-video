"""
Use cases of Claude AI in Nigeria
"""

from manim import *

class UseCasesNigeria(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        # Title
        title = Text("Claude AI Use Cases in Nigeria", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        # Use cases
        use_cases = [
            "📚 Education & Learning",
            "💼 Business Automation",
            "💡 Content Creation",
            "🔧 Technical Support",
            "📊 Data Analysis"
        ]
        
        for i, case in enumerate(use_cases):
            # Create colored box
            colors = ["#00D9FF", "#FFD700", "#00FF88", "#FF6B6B", "#9B59B6"]
            box = Rectangle(
                width=8,
                height=0.8,
                color=colors[i],
                stroke_width=2,
                fill_color=colors[i],
                fill_opacity=0.2
            )
            
            text = Text(case, color=colors[i], font_size=28)
            box.move_to(UP * (2 - i * 1))
            text.move_to(box.get_center())
            
            self.play(Create(box), Write(text), run_time=0.7)
        
        self.wait(2)


class NigeriaAdaptation(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        title = Text("Why Claude AI for Nigeria?", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        benefits = [
            "✓ Accessible via internet",
            "✓ Supports multiple languages",
            "✓ Affordable pricing",
            "✓ No location restrictions",
            "✓ Growing developer community"
        ]
        
        for i, benefit in enumerate(benefits):
            text = Text(benefit, color="#FFFFFF", font_size=26)
            text.move_to(UP * (2.2 - i * 0.9))
            self.play(FadeIn(text), run_time=0.5)
            self.wait(0.3)
        
        self.wait(2)


class PracticalExample(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        title = Text("Practical Example", color="#00D9FF", font_size=56, weight=BOLD)
        title.move_to(UP * 3.5)
        self.play(Write(title))
        
        # Input example
        input_box = Rectangle(width=10, height=1.5, color="#00D9FF", stroke_width=2, fill_opacity=0.1)
        input_box.move_to(UP * 0.5)
        input_text = Text(
            "Input: Explain machine learning\nin simple Nigerian English",
            color="#00D9FF",
            font_size=20
        )
        input_text.move_to(input_box.get_center())
        
        self.play(Create(input_box), Write(input_text))
        self.wait(1)
        
        # Output example
        output_box = Rectangle(width=10, height=1.5, color="#FFD700", stroke_width=2, fill_opacity=0.1)
        output_box.move_to(DOWN * 1.5)
        output_text = Text(
            "Output: Claude provides clear,\ncontextual explanation",
            color="#FFD700",
            font_size=20
        )
        output_text.move_to(output_box.get_center())
        
        self.play(Create(output_box), Write(output_text))
        self.wait(2)
