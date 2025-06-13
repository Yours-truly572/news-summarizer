# 📰 AI News Summarizer & Publisher

An AI-powered Flask web app that scrapes the latest Google News articles, summarizes them using GPT-4, and publishes the result directly to a Ghost CMS blog — all with one click.

---

## 🚀 Features

✅ **Google News Scraper**  
Scrapes top 10 articles related to a user-defined topic using Google search.

✅ **AI Summarization**  
Uses OpenAI GPT-4 to summarize each article into digestible, human-readable content.

✅ **Ghost CMS Integration**  
Automatically publishes the summarized content as a draft post in a connected Ghost blog.

✅ **Minimal UI**  
A clean, responsive interface to enter topics and view summaries.

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Flask** – lightweight web server
- **BeautifulSoup** – article parsing
- **OpenAI API (GPT-4)** – text summarization
- **Requests** – HTTP requests
- **Ghost Admin API** – publishing posts

---

## 💻 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/news-summarizer.git
   cd news-summarizer
