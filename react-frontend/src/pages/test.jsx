import { useState } from "react"
import {createTest, getAll, getOne} from "../services/test.service"
import { useNavigate } from "react-router-dom";

export default function Test(){
    const navigate = useNavigate();
    const [test, setTest] = useState({
        strategy: '',
        ticker: '',
        date: ''
    })

    const handleInputChange = (evt) => {
        setTest({...test, [evt.target.name]: evt.target.value})
    }
console.log('before handle submit:',test)
    async function handleSubmit (evt) {
        evt.preventDefault();
        try {
            console.log('what is happening?!')
            const data = {
                strategy: test.strategy,
                ticker: test.ticker,
                date: test.date
            }
            console.log('data is', data)
            const response = await createTest(data);
            console.log('Response is:',response)
            setTest({
                id: response.id,
                strategy: response.strategy,
                date: response.date
            })
            navigate('/result')
        } catch (err) {
            console.log('this isnt working')
            console.log(err)
        }
    }
    return (
        <>
        <h1>Test A Strategy!</h1>
        <form onSubmit={handleSubmit}>
            <select name="strategy" value={test.strategy} onChange={handleInputChange}>
                <option value="5min ORB">5min ORB</option>
                <option value="S/R Break">S/R Break</option>
                <option value="10/20 ema cross">10/20 ema cross</option>
            </select> <br />
            <input type="text" 
            placeholder="Enter Stock Ticker"
            name="ticker"
            value={test.ticker}
            onChange={handleInputChange}
            /><br />
            <input 
            type="date" 
            name="date"
            value={test.date}
            onChange={handleInputChange}/><br />
            <button type="submit"> Test Strategy </button>
        </form>
        </>
    )
}