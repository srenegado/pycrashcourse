import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    # Create link.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = (f"<a href='{repo_url}' style='color:rgb(84,177,239)'>"
        f"{repo_name}</a>")
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Create tooltip.
    owner = repo_dict['owner']['login']
    # Shortened description if needed.
    if len(str(repo_dict['description'])) > 99:
        repo_dict['description'] = repo_dict['description'][:99] + '...'
    description = repo_dict['description']
    label = f'Owner: {owner}<br />Description: {description}'
    labels.append(label)

# Plot data.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(3, 102, 214)',
        'line': {'width': 1.5, 'color': 'rgb(225, 228, 232)'}
    },
    'opacity': 0.75
}]

my_layout = {
    'title': 'Most Starred Python Projects on GitHub',
    'title_x': 0.5,
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14}
    },
    'plot_bgcolor': 'rgb(235, 237, 240)'
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')