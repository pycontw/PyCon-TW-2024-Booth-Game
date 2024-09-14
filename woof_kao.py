import os
import random
import pouchy
from home import your_puzzle


def personal_task():
    with open("graffiti_wall.txt", "w") as f:
        message = "Anything you want to say about PyCon TW."
        f.write(message)

    with open("graffiti_wall.txt", "r") as f:
        photo = f.read()

    with open("social_media.txt", "w") as f:
        f.write(photo)
        f.write("@pycon.tw")

    if os.path.isfile("social_media.txt"):
        return True
    else:
        return False


def team_task(your_puzzle):
    members = ["PY", "TH", "ON"]
    your_teammates = [m for m in members if m != your_puzzle]
    photo_content = {}
    if len([your_puzzle] + your_teammates) == 3:
        photo_content["puzzle_image"] = "".join(members)
        photo_content["people"] = len(members)
        photo_content["background"] = "graffiti_wall"

    for _, value in photo_content.items():
        if value is None:
            return False

    return True


def booth_task():
    sponsor_booths = ["PSF", "E.SUN Bank", "REUVEN LERNER", "Tenlong bookstore"]
    community_booths = ["OCF", "COSCUP", "MOPCON", "Good Ideas Studio"]
    unfinished_booths = sponsor_booths + community_booths

    while len(unfinished_booths) > 0:
        booth = random.choice(unfinished_booths)
        if pouchy.visit(booth):
            unfinished_booths.remove(booth)

    if len(unfinished_booths) == 0:
        return True
    else:
        return False


def task():
    passed_count = 0
    if personal_task():
        passed_count += 1
    if team_task(your_puzzle):
        passed_count += 1
    if booth_task():
        passed_count += 1

    if passed_count == 3:
        return "Congratulations, you’ve qualified for the Grand Prize raffle!"


if __name__ == "_main_":
    task()
