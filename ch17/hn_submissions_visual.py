from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make an api call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:15]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Create a dictionary for each submission.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

# Sort submissions by top comment in descending order.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
    reverse=True)

# Get information about submissions.
submission_links, comments, labels = [], [], []
for submission_dict in submission_dicts:
    submission_link = (f"<a href='{submission_dict['hn_link']}' "
        f"style='color:rgb(42,63,95);'>{submission_dict['title']}</a>")
    
    # Shorten the title if needed.
    if len(submission_dict['title']) > 24:
        shortened_title = submission_dict['title'][:24] + '...'
        shortened_link = (f"<a href='{submission_dict['hn_link']}' "
            f"style='color:rgb(42,63,95);'>{shortened_title}</a>")
        submission_links.append(shortened_link)
    else:
        submission_links.append(submission_link)
    
    comments.append(submission_dict['comments'])
    labels.append(submission_link)

# Plot data.
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': comments,
    'hoverinfo': 'text',
    'hovertext': labels,
    'marker': {'color': 'rgb(255, 102, 0)'},
    'opacity': 0.90
}]

my_layout = {
    'title': 'Most Active Discussions Currently on Hacker News',
    'title_x': 0.5,
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Submissions',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Commments',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14}
    },
    'plot_bgcolor': 'rgb(240, 240, 233)',
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')

