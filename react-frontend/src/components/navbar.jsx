import { Link } from 'react-router-dom';

export default function Navbar() {
    return(
        <div>
            <Link to="/">Home</Link>
            &nbsp; | &nbsp;
            <Link to="/test">Test Strategy</Link>
            &nbsp; | &nbsp;
            <Link to="/result">Test Result</Link>
        </div>
    )
}