import subprocess
from pathlib import Path

INPUT_VIDEO = "input.mp4"

output_video = Path(INPUT_VIDEO).with_name(
    Path(INPUT_VIDEO).stem + "_4K.mp4"
)

cmd = [
    "ffmpeg",
    "-i", INPUT_VIDEO,

    "-vf",
    "scale=3840:2160:flags=lanczos",

    "-c:v", "libx265",
    "-preset", "slow",
    "-crf", "18",

    "-pix_fmt", "yuv420p",

    "-c:a", "copy",

    str(output_video)
]

subprocess.run(cmd, check=True)

print(f"Done: {output_video}")