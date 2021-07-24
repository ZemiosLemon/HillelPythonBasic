import json
#import datetime


#
# def duration():
#     with open('acdc.json') as f:
#         file_dict = json.load(f)
#         summa = 0
#         for num in range(10):
#             summa += int(file_dict['album']['tracks']['track'][num]['duration'])
#         return summa
#
#
# def conversion_in_seconds(func):
#     size = datetime.timedelta(seconds=func)
#     return size
#
#
#
# print(conversion_in_seconds(duration()))
#(sum([track['duration'] for track in

#def ggggg():
with open('acdc.json') as f:
    file_dict = json.load(f)
#print(file_dict)
#gggg = file_dict['album']['tracks']['track']
for track in file_dict['album']['tracks']['track']:
    print(track['duration'])
    print(file_dict['album']['tracks']['track'])

