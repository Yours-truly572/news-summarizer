# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_news(topic):
    query = topic.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}+site:news.google.com&hl=en"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for g in soup.find_all('a'):
        href = g.get('href')
        if href and "/articles/" in href:
            full_link = "https://news.google.com" + href[1:] if href.startswith("/") else href
            if full_link not in links:
                links.append(full_link)
        if len(links) >= 10:
            break
    return links

# summarizer.py
import openai
openai.api_key = 'YOUR_OPENAI_API_KEY'

def summarize_articles(articles):
    summaries = []
    for url in articles:
        try:
            res = requests.get(url, timeout=5)
            text = BeautifulSoup(res.text, 'html.parser').get_text()
            prompt = f"Summarize this article:\n{text[:3000]}"
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            summaries.append(response['choices'][0]['message']['content'])
        except Exception as e:
            continue
    return "\n\n".join(summaries)

# publisher.py
import requests

def publish_to_ghost(title, content):
    GHOST_API_URL = 'https://your-ghost-blog.ghost.io/ghost/api/admin/posts/?source=html'
    GHOST_ADMIN_API_KEY = 'YOUR_ADMIN_API_KEY'
    headers = {
        'Authorization': f'Ghost {GHOST_ADMIN_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "posts": [{
            "title": title,
            "html": f"<p>{content}</p>",
            "status": "draft"
        }]
    }
    requests.post(GHOST_API_URL, json=payload, headers=headers)

# templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>AI News Summarizer</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>📰 AI News Summarizer</h1>
    <form method="POST">
        <input type="text" name="topic" placeholder="Enter a topic...">
        <button type="submit">Summarize</button>
    </form>
    {% if summary %}
    <h2>Summary for: {{ topic }}</h2>
    <pre>{{ summary }}</pre>
    {% endif %}
</body>
</html>

# static/style.css
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    background: #f4f4f4;
    color: #333;
}
form {
    margin-bottom: 20px;
}
input {
    padding: 10px;
    font-size: 1em;
}
button {
    padding: 10px 15px;
    font-size: 1em;
    background: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}
button:hover {
    background: #0056b3;
}
