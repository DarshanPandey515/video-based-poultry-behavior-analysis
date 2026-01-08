# Video-Based Poultry Behavior Analysis

## Overview
This project uses computer vision to extract **behavioral proxies** from poultry videos.  
It tracks individual birds across frames and computes movement and interaction metrics.

## Features
- Detect chickens in videos using YOLOv8
- Track individual birds across frames
- Calculate Relative Movement Index (RMI)
- Count High-Density Interaction Events (HDIE)

## Motivation
Supports research in **precision livestock monitoring**, providing non-invasive indicators of bird activity and spatial interactions.

## How to Run
1. Activate virtual environment:
```
venv\Scripts\activate
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run analysis on a sample video:
```
python analysis\run_analysis.py
```


## Assumptions & Limitations
- RMI and HDIE are **proxy metrics**, not direct health or welfare measurements.
- Detection is based on **pretrained YOLOv8 ‘bird’ class**, may misclassify other birds.
- High-density events are only based on proximity, not aggression.

## Future Work
- Integrate custom-trained chicken detector
- Add more complex tracking (e.g., DeepSORT)
- Include multiple camera angles for 3D behavior estimation

