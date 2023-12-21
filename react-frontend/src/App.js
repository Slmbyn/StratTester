import React, { useState, useEffect } from 'react';
import './App.css';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/home';
import Test from './pages/test';
import Navbar from './components/navbar';
import Result from './pages/result';
import Register from './components/Register';
import Login from './components/Login';
import Logout from './components/Logout';
import { getUser, getToken } from './services/user.service';

function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [user, setUser] = useState(null)

  // Check if the user is authenticated on component mount
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setAuthenticated(true);
    }
  }, [user]);

  return (
    <div className="App">
      <BrowserRouter>
        <Navbar authenticated={authenticated} setAuthenticated={setAuthenticated} setUser={setUser} />
        <Routes>
          <Route path='/' element={ <Home />} />
          <Route path='/test' element={ <Test user={ user } />} />
          <Route path="/result" element={authenticated ? <Result user={user} /> : <Navigate to="/login" />} />
          <Route path="/register" element={<Register setUser={setUser}/>} />
          <Route path="/login" element={<Login setUser={setUser}/>} />
          {/* <Route path="/logout" element={<Logout />} /> */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;




// import './App.css';
// import { BrowserRouter, Routes, Route } from 'react-router-dom'
// import Home from './pages/home';
// import Test from './pages/test';
// import Navbar from './components/navbar';
// import Result from './pages/result';

// function App() {
  

//   return (
//     <div className="App">
//       <BrowserRouter>
//       {<Navbar />}
//         <Routes>
//           <Route path='/' element={ <Home />} />
//           <Route path='/test' element={ <Test />} />
//           <Route path='/result' element={ <Result />} />
//         </Routes>
//       </BrowserRouter>
      
//     </div>
//   );
// }

// export default App;
