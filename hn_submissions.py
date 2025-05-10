# Lab17_Angeerika-1.py
# author: Angeerika
# comment: This program catches errors made from retrieving data from the API
# date: 05/10/25

""" this program retrieves the top 30 articles from Hacker News and displays their titles, links, and number of comments.
    It uses the Hacker News API to get the data and handles errors that may occur during the process."""

    
from operator import itemgetter
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
     
    # Make a new API call for each submission.
     url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
     r = requests.get(url)
     print(f"id: {submission_id}\tstatus: {r.status_code}")

     response_dict = r.json()

    # Build a dictionary for each article.
     submission_dict = {
        'title': response_dict.get('title', 'No title'), #uses get() to avoid KeyError
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0), #use 0 if no comments
    }
     submission_dicts.append(submission_dict) #add to list

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), #sort by comments
                            reverse=True)
# Print the titles and comments of the articles.
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")