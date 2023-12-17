import { Link } from 'react-router-dom';

export default function Navbar() {
    return(
        <nav className='navbar navbar-expand' style={{ backgroundColor: 'grey' }}>
            <div className="container">
                <ul className='navbar-nav'>
                    <li className="nav-item">
                        <a href="/">Home</a>
                    </li>
                    <li className="nav-item">
                        <a href="/test">Test Strategy</a>
                    </li>
                    <li className="nav-item">
                        <a href="result">See Result</a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}
