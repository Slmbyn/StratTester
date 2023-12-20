import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

export default function Login () {
    const navigate = useNavigate();
  const [user, setuser] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setuser({ ...user, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/login/', user);
      console.log(response.data);
      // store token & redirect the user
      const token = response.data.token;
      localStorage.setItem('token', token)
      navigate('/')
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Email: </label>
      <input type="text" name="email" onChange={handleChange} required />
      <br />
      <label>Password: </label>
      <input type="password" name="password" onChange={handleChange} required />
      <br />
      <button type="submit">Login</button>
    </form>
  );
};

