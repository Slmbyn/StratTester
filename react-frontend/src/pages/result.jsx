import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

const darkTheme = {
  backgroundColor: '#343a40', // Dark background color
  color: 'white',            // White text color
};

export default function Result({ user }) {
  const [test, setTest] = useState([]);
  const [result, setResult] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/tests/")
      .then((res) => {
        setTest(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    axios.get("http://localhost:8000/api/results/")
      .then((res) => {
        setResult(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    // checking if this component already has the strat name & ticker in it. if so, render them on Results page
    console.log(`test in result.jsx ${test}`)
    console.log(`result in result.jsx ${result}`)

  }, []);

  return (
    <>
      <h1 style={{ ...darkTheme, textAlign: 'center' }}>Results</h1>
      <Table striped bordered hover variant="dark" style={darkTheme}>
        <thead>
          <tr>
            <th>% Profit / Loss</th>
            <th>$ Profit / Loss</th>
            <th>Volume</th>
            <th>Entry Price</th>
            <th>Exit Price</th>
            <th>Test_id</th>
          </tr>
        </thead>
        <tbody>
          {result.map((e, index) => (
            <tr key={e.id} style={index % 2 === 0 ? { backgroundColor: '#2c3036' } : { backgroundColor: '#343a40' }}>
              <td>{e.PL_percent}%</td>
              <td>${e.PL_abs}</td>
              <td>{e.volume}</td>
              <td>{e.entry_price}</td>
              <td>{e.exit_price}</td>
              <td>{e.test}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </>
  );
}






// import { useState, useEffect } from 'react'
// import axios from 'axios';
// import { Table } from 'react-bootstrap';


// export default function Result({ user }){
//     const [test, setTest] = useState([])
//     const [result, setResult] = useState([])
  
//     useEffect(() => {
//       axios.get("http://localhost:8000/api/tests/")
//       .then((res) => {
//         console.log(res.data)
//         setTest(res.data)
//       })
//       .catch((err) => {
//         console.log(err)
//       })
      
//       axios.get("http://localhost:8000/api/results/")
//       .then((res) => {
//         console.log(res.data)
//         setResult(res.data)
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     }, [])
//     return(
//         <>
//         <h1>Results:</h1>
//         <div>
//             {result.map((e) => {
//                 return(
//                     <div>
//                         <p> %P/L: {e.PL_percent}% </p>
//                         <p> $P/L: ${e.PL_abs} </p>
//                         <p> Volume: {e.volume} </p>
//                         <p> Entry Price: {e.entry_price} </p>
//                         <p> Exit Price: {e.exit_price} </p>
//                         <p> Test_id: {e.test} </p>
//                     </div>
//                 )
//             })}
//         </div>
//         </>
//     )
// }