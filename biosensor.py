# Simulation of Physiological Signals by Wristband
import random


class BioSensor:
   # Simulated wristband data (heart rate, skin conductance)

    def read(self):
        return {
            # simulate heart rate fluctuations
            'heart_rate': random.randint(60, 140),
            # galvanic skin response
            'gsr': round(random.uniform(0.5, 5.0)),
            # action detection
            'motion': random.choice(['normal', 'repetitive'])
        }
