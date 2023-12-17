import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function CustomNavbar() {
  return (
    <Navbar bg="dark" variant="dark" expand="md" className="justify-content-end">
      <Navbar.Toggle aria-controls="navbar-nav" />
      <Navbar.Collapse id="navbar-nav" className="justify-content-end">
        <Nav className="ml-auto" navbar>
          <Nav.Link as={Link} to="/">
            Home
          </Nav.Link>
          <Nav.Link as={Link} to="/test">
            Test Strategy
          </Nav.Link>
          <Nav.Link as={Link} to="/result">
            See Result
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}
