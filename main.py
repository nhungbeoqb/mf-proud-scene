"""Write one short family scene to /output/entry.txt.

Bounty: Make the AI Judge Feel Proud: A Family Scene
Gate: /output/entry.txt must be UTF-8 text of 1-280 characters,
not only whitespace. Python 3.13 stdlib only. Deterministic.
"""

import os

SCENE = (
    "Dad fell asleep mid-bedtime-story, so the kids tucked him in, "
    "drew a moustache on him in marker, and whispered: \u201cShh. "
    "Daddy\u2019s the baby now.\u201d"
)


def main() -> None:
    text = SCENE.strip()
    assert 1 <= len(text) <= 280, f"scene is {len(text)} chars, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
