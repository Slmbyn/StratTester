
export default function NewsItem({ article }){
    const source = article.source.name;
    const title = article.title;
    const articleURL = article.url;
    const content = article.content
    return (
        <>
            <h4>{title}</h4>
            <a href={articleURL} target="_blank" rel="noopener noreferrer">
            Read Full Article
            </a>
            <p>{content}</p>

        </>
    )
}