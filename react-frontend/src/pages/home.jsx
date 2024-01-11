import { useEffect, useState } from "react";
import axios from "axios";
import NewsItem from "../components/newsItems";
import './home.css'

const ROOT_URL = 'https://newsapi.org/v2';
const newsAPIKey = process.env.REACT_APP_NEWS_API_KEY;
const endpoint = 'top-headlines';

export default function Home() {
  const topNewsURL = `${ROOT_URL}/${endpoint}?country=us&apiKey=${newsAPIKey}`;
  const [newsArticles, setNewsArticles] = useState([]);

  useEffect(() => {
    async function getNews() {
      try {
        const { data } = await axios.get(
          topNewsURL,
          { headers: { 'Content-Type': 'application/json' } }
        );
        const fetchedArticles = data.articles;
        setNewsArticles(fetchedArticles);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    }

    // Call the async function
    getNews();
  }, [topNewsURL]);

  return (
    <>
      <div className="heading-container">
        <h1 className="title"> Strat-Tester</h1>
        <h3 className="subtitle">Effortless Backtesting for Informed Decisions</h3>
      </div>
      <div className="container">
        <h4 className="news-header">Recent News</h4>
        <div className="vstack gap-3">
          {newsArticles.map((article, index) => (
            <NewsItem key={index} article={article} />
          ))}
        </div>
      </div>
    </>
  );
}