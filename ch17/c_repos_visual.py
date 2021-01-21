# Ex 17-1

import requests
from plotly.graph_objs import bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process the data.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    # Create link.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Create tooltip.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"Owner: {owner}<br />Description: {description}"
    labels.append(label)

# Plot data.
data = {
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}

my_layout = {
    'title': 'Most Starred C Projects on GitHub',
    'title_x': 0.5,
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 18},
        'tickfont': {'size': 16}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 18},
        'tickfont': {'size': 16}
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='c_repos.html')
