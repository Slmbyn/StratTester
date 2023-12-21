import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import { Form, Button } from 'react-bootstrap';

export default function Login ({ setUser }) {
    const navigate = useNavigate();
  const [userLogin, setUserLogin] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setUserLogin({ ...userLogin, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/login/', userLogin);
      console.log(response.data);
      // store token & redirect the user
      setUser(response.data.user_id)
      const token = response.data.token;
      localStorage.setItem('token', token)
      navigate('/')
    } catch (error) {
      console.error('Login error:', error);
    }
  };
  return (
    <div className="d-flex flex-column align-items-center justify-content-center vh-100">
      <h1 className="text-light mb-4">Log In</h1>
      <Form onSubmit={handleSubmit} className="text-light">
        <Form.Group controlId="formEmail">
          <Form.Label>Email:</Form.Label>
          <Form.Control
            type="text"
            name="email"
            onChange={handleChange}
            required
          />
        </Form.Group>

        <Form.Group controlId="formPassword">
          <Form.Label>Password:</Form.Label>
          <Form.Control
            type="password"
            name="password"
            onChange={handleChange}
            required
          />
        </Form.Group>

        <div className="mt-3 d-flex justify-content-center">
          <Button variant="primary" type="submit">
            Login
          </Button>
        </div>
      </Form>
    </div>
  );
};

