import { useState, useEffect } from 'react'
import axios from 'axios';

export default function Result(){
    const [test, setTest] = useState([])
    const [result, setResult] = useState([])
  
    useEffect(() => {
      axios.get("http://localhost:8000/api/tests/")
      .then((res) => {
        console.log(res.data)
        setTest(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
      
      axios.get("http://localhost:8000/api/results/")
      .then((res) => {
        console.log(res.data)
        setResult(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }, [])
    return(
        <>
        <h1>Tests:</h1>
        <p>
            {test.map((e) => {
                return(
                    <div>
                        <p> Strategy Name: {e.strategy} </p>
                        <p> Ticker: {e.ticker} </p>
                        <p> Date Tested: {e.date} </p>
                    </div>
                )
            })}
        </p>
        <h1>Results:</h1>
        <p>
            {result.map((e) => {
                return(
                    <div>
                        <p> %P/L: {e.PL_percent}% </p>
                        <p> $P/L: ${e.PL_abs} </p>
                        <p> Volume: {e.volume} </p>
                        <p> Entry Price: {e.entry_price} </p>
                        <p> Exit Price: {e.exit_price} </p>
                        <p> Test_id: {e.test} </p>
                    </div>
                )
            })}
        </p>
        </>
    )
}