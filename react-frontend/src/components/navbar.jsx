import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const CustomNavbar = ({ authenticated, setUser, setAuthenticated }) => {
  const navigate = useNavigate();

  // const handleLogout = () => {
  //   localStorage.removeItem('token');
  //   navigate('/');
  // };

  const handleLogout = async () => {
    try {
      const token = localStorage.getItem('token');
      console.log('Authorization Header:', `Token ${token}`);
        await axios.get('http://localhost:8000/logout/', {
            headers: {
            Authorization: `Token ${token}`,
            },
        });
        // Clear token from local storage or state
        setUser(null)
        setAuthenticated(false)
        localStorage.removeItem('token');
        navigate('/')
    } catch (error) {
        console.error('Logout error:', error);
    }
};


  return (
    <Navbar bg="dark" variant="dark" expand="md" className="justify-content-between">
      {/* <Navbar.Brand as={Link} to="/">
        {authenticated ? `Hello, ${username}` : 'StratTester'}
      </Navbar.Brand> */}
      <Navbar.Toggle aria-controls="navbar-nav" />
      <Navbar.Collapse id="navbar-nav" className="justify-content-end">
        <Nav className="ml-auto" navbar>
          <Nav.Link as={Link} to="/">
            Home
          </Nav.Link>
          <Nav.Link as={Link} to="/test">
            Test Strategy
          </Nav.Link>
          {authenticated ? (
            <>
              <Nav.Link as={Link} to="/result">
                See Result
              </Nav.Link>
              <Nav.Link onClick={handleLogout} className="text-danger">
                Logout
              </Nav.Link>
            </>
          ) : (
            <>
              <Nav.Link as={Link} to="/login">
                Login
              </Nav.Link>
              <Nav.Link as={Link} to="/register">
                Register
              </Nav.Link>
            </>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default CustomNavbar;
