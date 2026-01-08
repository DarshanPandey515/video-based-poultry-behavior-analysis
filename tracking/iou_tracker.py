def iou(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    inter_area = max(0, x2-x1) * max(0, y2-y1)
    area1 = (box1[2]-box1[0])*(box1[3]-box1[1])
    area2 = (box2[2]-box2[0])*(box2[3]-box2[1])

    return inter_area / (area1 + area2 - inter_area + 1e-6)


class SimpleTracker:
    def __init__(self, iou_threshold=0.3):
        self.tracks = {}
        self.next_id = 0
        self.iou_thresh = iou_threshold

    def update(self, detections):
        updated_tracks = {}
        used_ids = set()

        for det in detections:
            matched = False
            for tid, track in self.tracks.items():
                if tid in used_ids:
                    continue
                if iou(det, track["bbox"][-1]) > self.iou_thresh:
                    track["bbox"].append(det)
                    updated_tracks[tid] = track
                    used_ids.add(tid)
                    matched = True
                    break

            if not matched:
                updated_tracks[self.next_id] = {"bbox": [det]}
                self.next_id += 1

        self.tracks = updated_tracks
        return self.tracks
