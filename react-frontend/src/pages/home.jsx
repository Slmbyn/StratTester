const ROOT_URL = 'https://newsapi.org/v2';
const newsAPIKey = process.env.REACT_APP_NEWS_API_KEY
console.log('api key', newsAPIKey)
const endpoint = 'top-headlines'

export default function Home(){
    const topNewsURL = `${ROOT_URL}/${endpoint}/sources?apiKey=${newsAPIKey}`
    return (
        <>
            <h1>Home Page</h1>
        </>
    )
}