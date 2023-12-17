import { Link } from "react-router-dom";
import './newsItems.css';

export default function NewsItem({ article }) {
  const source = article.source.name;
  const title = article.title;
  const articleURL = article.url;
  const content = article.content;

  return (
    <div className="container dark-bg">
      <div className="card">
        <a href={articleURL} target="_blank" rel="noopener noreferrer">
          <div className="card-body">
            <h4 className="card-header">{title}</h4>
            <p className="card-text">{content}</p>
          </div>
        </a>
      </div>
    </div>
  );
}