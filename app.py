from flask import Flask, request

app = Flask(__name__)

videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

def merge_sort(lst):
    if len(lst) > 1:
        midway = len(lst) // 2
        left_half = lst[:midway]
        right_half = lst[midway:]

        merge_sort(left_half)
        merge_sort(right_half)

        l = 0 
        r = 0 
        m = 0 

        while l < len(left_half) and r < len(right_half):
            if left_half[l]['title'] < right_half[r]['title']:
                lst[m] = left_half[l]
                l += 1
            else:
                lst[m] = right_half[r]
                r += 1
            m += 1

        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1
    return lst

merge_sort(videos)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]['title'] == target:
            return arr[mid]
        elif arr[mid]['title'] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


@app.route('/')
def index():
    return 'Welcome to my simple API video search app :)'

@app.route('/sorted-vids')
def soreted_vids():
    return videos

@app.route('/videos')
def search_videos():
    search = request.args.get('search')
    if not search:
        return {'error': "Must have the 'search' query param"}, 400
    video = binary_search(videos, search)
    if video:
        return video
    else:
        return {'error': f"No video with the title '{search}'"}, 404
