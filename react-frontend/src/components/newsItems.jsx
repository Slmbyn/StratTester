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





// import { Link } from "react-router-dom";

// export default function NewsItem({ article }){
//     const source = article.source.name;
//     const title = article.title;
//     const articleURL = article.url;
//     const content = article.content
//     return (
//         <div className="container">
//                 <div className="card"> 
//                     <Link to={articleURL}>
//                         <div className="card-body">
//                             <h4 className="card-header">{title}</h4>
//                             {/* <a href={articleURL} target="_blank" rel="noopener noreferrer">
//                             Read Full Article
//                             </a> */}
//                             <p className="card-text">{content}</p>
                            
//                         </div>
//                     </Link>
//                 </div>
//             </div>
//     )
// }