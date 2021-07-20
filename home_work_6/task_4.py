import json
import datetime


def duration():
    with open('acdc (3).json') as f:
        file_dict = json.load(f)
        seconds = 0
        for track in file_dict['album']['tracks']['track']:
            seconds += int(track['duration'])
        return datetime.timedelta(seconds=seconds)


print(duration())
