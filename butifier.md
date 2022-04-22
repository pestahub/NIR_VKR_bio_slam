To ensure high performance in real-time, we marginalize old
lidar scans for pose optimization, rather than matching lidar
scans to a global map. Scan-matching at a local scale instead of
a global scale significantly improves the real-time performance
of the system, as does the selective introduction of keyframes,
and an efficient sliding window approach that registers a new
keyframe to a fixed-size set of prior “sub-keyframes.” The
proposed method is extensively evaluated on datasets gathered
from three platforms over various scales and environments.