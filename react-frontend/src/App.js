import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/home';
import Test from './pages/test';
import Navbar from './components/navbar';
import Result from './pages/result';

function App() {
  

  return (
    <div className="App">
      <BrowserRouter>
      {<Navbar />}
        <Routes>
          <Route path='/' element={ <Home />} />
          <Route path='/test' element={ <Test />} />
          <Route path='/result' element={ <Result />} />
        </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
