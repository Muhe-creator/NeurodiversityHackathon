from biosensor import BioSensor
from glass import ARGlasses
import time
# Import the visualization library. Realize visualization of heart rate data
import matplotlib.pyplot as plt


class AutismAssistant:
    def __init__(self):
        self.bracelet = BioSensor()
        self.glasses = ARGlasses()
        self.heart_rates = []  # Store the latest 10 sets of heart rate data

    def _update_plot(self):
        """Update the heart rate curve chart"""
        plt.clf()  # Clear the previous frame
        plt.plot(self.heart_rates, 'b-')  # Blue line segment
        plt.title('Real-time heart rate monitoring')
        plt.ylim(60, 140)  # Fix the range of the Y-axis
        plt.xlabel('time (s)')
        plt.ylabel('heart rate (BPM)')
        plt.pause(0.01)  # Take a brief pause to update the chart.
        plt.axhline(120, color='orange', linestyle='--', label='warning line')
        plt.legend()  # Display legend

    def run(self):
        """main loop"""
        plt.ion()  # Enable interactive mode

        while True:
            data = self.bracelet.read()

            # Store the latest 10 sets of heart rate data
            self.heart_rates.append(data['heart_rate'])
            if len(self.heart_rates) > 10:
                self.heart_rates = self.heart_rates[-10:]

            # Scenario 1: Light-sensitive treatment
            if data['heart_rate'] > 120 or data['gsr'] > 3.5:
                print("\n⚠️Detected stress response!")
                self.glasses.adjust_light(70)
                self.glasses.show_guide(
                    "Deep breathing: Inhale for 4 seconds → Hold breath for 4 seconds → Exhale for 6 seconds")

                # Display real-time heart rate curve
                self._update_plot()

            time.sleep(1)


if __name__ == "__main__":
    print("Activate the AutismCompanion System...")
    system = AutismAssistant()
    system.run()
