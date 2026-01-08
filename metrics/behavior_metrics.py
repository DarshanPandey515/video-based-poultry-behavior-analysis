import numpy as np


def relative_movement_index(tracks):
    total_dist = 0
    count = 0

    for track in tracks.values():
        boxes = track["bbox"]
        for i in range(1, len(boxes)):
            x1 = (boxes[i-1][0] + boxes[i-1][2]) / 2
            y1 = (boxes[i-1][1] + boxes[i-1][3]) / 2
            x2 = (boxes[i][0] + boxes[i][2]) / 2
            y2 = (boxes[i][1] + boxes[i][3]) / 2
            total_dist += np.sqrt((x2-x1)**2 + (y2-y1)**2)
            count += 1

    return total_dist / max(count, 1)


def high_density_events(tracks, threshold=50):
    events = 0
    positions = []

    for track in tracks.values():
        if track["bbox"]:
            b = track["bbox"][-1]
            positions.append(((b[0]+b[2])/2, (b[1]+b[3])/2))

    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            dx = positions[i][0] - positions[j][0]
            dy = positions[i][1] - positions[j][1]
            if np.sqrt(dx*dx + dy*dy) < threshold:
                events += 1

    return events
