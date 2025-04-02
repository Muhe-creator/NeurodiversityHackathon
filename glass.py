# Intelligent Glasses Control


class ARGlasses:
    """Smart glasses control module"""

    def __init__(self):
        self.brightness = 100  # Initial brightness percentage

    def adjust_light(self, percent):
        """Adjust the transmittance"""
        self.brightness = percent
        print(f"[Glass] Adjust the Transmittance to{percent}%")

    def show_guide(self, text):
        """Display respiratory guidance"""
        print(f"[Glass] Display Hints: {text}")
