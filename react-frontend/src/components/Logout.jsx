import React from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";


export default function Logout () {
    const navigate = useNavigate();
    const handleLogout = async () => {
        try {
            await axios.post('http://localhost:8000/logout/', null, {
                headers: {
                Authorization: `Token ${localStorage.getItem('token')}`,
                },
            });
            // Clear token from local storage or state
            localStorage.removeItem('token');
            navigate('/')
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

  return (
    <div>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

