import { useEffect, useState } from "react";
import axios from "axios";
import NewsItem from "../components/newsItems";
// import './home.css'

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
    <div className="container">
      <div className="vstack gap-3">
        {newsArticles.map((article, index) => (
          <NewsItem key={index} article={article} />
        ))}
      </div>
    </div>
  );
}


// import { useEffect } from "react";
// import axios from "axios";
// import NewsItem from "../components/newsItems";


// const ROOT_URL = 'https://newsapi.org/v2';
// const newsAPIKey = process.env.REACT_APP_NEWS_API_KEY
// const endpoint = 'top-headlines'

// export default function Home(){
//     const topNewsURL = `${ROOT_URL}/${endpoint}?country=us&apiKey=${newsAPIKey}`;
//     useEffect(() => {
//         async function getNews() {
//           try {
//             const { data } = await axios.get(
//               topNewsURL,
//               { headers: { 'Content-Type': 'application/json' } }
//             );
//             const newsArticles = data.articles;
//             const article = newsArticles.map((a) => (
//                 <NewsItem article={a}/>
//             ) )
//             console.log(newsArticles);
//           } catch (error) {
//             console.error('Error fetching news:', error);
//           }
//         }
//         getNews();
//       }, []);
//     return (
//         <>
//             <span>{article}</span>
//         </>
//     )
// }