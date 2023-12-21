import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";


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
    <form onSubmit={handleSubmit}>
      <label>Username: </label>
      <input type="text" name="username" onChange={handleChange} required />
      <br />
      <label>Email: </label>
      <input type="email" name="email" onChange={handleChange} required />
      <br />
      <label>Password: </label>
      <input type="password" name="password" onChange={handleChange} required />
      <br />
      <button type="submit">Register</button>
    </form>
  );
};
