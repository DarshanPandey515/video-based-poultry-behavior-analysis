from metrics.behavior_metrics import relative_movement_index, high_density_events
from data.video_reader import read_video
from detection.detector import BirdDetector
from tracking.iou_tracker import SimpleTracker

frames = read_video("data/sample.mp4")
detector = BirdDetector()
tracker = SimpleTracker()

for i, frame in enumerate(frames[:5]):
    birds = detector.detect(frame)
    tracks = tracker.update(birds)
    print(f"Frame {i}: {len(birds)} birds detected, {len(tracks)} tracks")

rmi = relative_movement_index(tracks)
hd_events = high_density_events(tracks)

print("Relative Movement Index:", rmi)
print("High-Density Interaction Events:", hd_events)
