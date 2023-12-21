import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import { Form, Button } from 'react-bootstrap';


export default function RegisterUser({ setUser }) {
  const navigate = useNavigate();
  const [newUser, setNewUser] = useState({
    username: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setNewUser({ ...newUser, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Register the user
      const registerResponse = await axios.post('http://localhost:8000/register/', newUser);
      console.log('Registration response:', registerResponse.data);
      //Log in the user after registration
      const loginResponse = await axios.post('http://localhost:8000/login/', {
        email: newUser.email,
        password: newUser.password,
      });
      console.log('Login response.data:', loginResponse.data);
      console.log('Login response:', loginResponse);
      setUser(loginResponse.data.user_id)

      // Store the token in local storage
      localStorage.setItem('token', loginResponse.data.token);

      // Redirect to the home page
      navigate('/');
    } catch (error) {
      console.error('Registration or login error:', error);
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <Form onSubmit={handleSubmit} className="text-light">
        <h1 className="mb-4 ">Sign-Up</h1>
        <Form.Group controlId="formUsername">
          <Form.Label>Username:</Form.Label>
          <Form.Control
            type="text"
            name="username"
            onChange={handleChange}
            required
          />
        </Form.Group>

        <Form.Group controlId="formEmail">
          <Form.Label>Email:</Form.Label>
          <Form.Control
            type="email"
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
            Register
          </Button>
        </div>
      </Form>
    </div>
  );
};
