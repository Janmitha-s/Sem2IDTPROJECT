# LoRa Passive Radar Human Detection

This project simulates a bistatic passive radar system using LoRa communication signals.

## Project Overview

- Drone A transmits a LoRa-like signal.
- A human reflects the signal.
- Drone B receives the reflected signal.
- Signal processing extracts breathing and heartbeat frequencies.

## Files

- generate_signal.py
- simulate_human.py
- add_noise.py
- process_signal.py
- spectrogram.py

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python generate_signal.py
python simulate_human.py
python add_noise.py
python process_signal.py
python spectrogram.py
```

## Output

A spectrogram showing simulated breathing and heartbeat micro-Doppler signatures.