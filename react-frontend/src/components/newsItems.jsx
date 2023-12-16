
export default function NewsItem({ article }){
    const source = article.source.name;
    const title = article.title;
    const articleURL = article.url;
    const content = article.content
    return (
        <>
            <h4>Title: {title}</h4>
            <h5>{source}</h5>
            <a href={articleURL}> Read More</a>
            <p>{content}</p>

        </>
    )
}