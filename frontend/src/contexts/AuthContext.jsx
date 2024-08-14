import React, { createContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import useLocalStorage from '../hooks/useLocalStorage';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();
  const [isAuth, setIsAuth] = useState(false);
  const [token, setToken] = useLocalStorage('token');

  const login = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(
        'http://localhost:5000/api/v1/chatbot/auth/login',
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: e.target.email.value,
            password: e.target.password.value,
          }),
        }
      );
      if (res.status === 200) {
        const response = await res.json();
        setToken(response.access_token);
        setIsAuth(true);
        navigate('/');
      }
    } catch (error) {
      console.log(error);
    }
  };

  const logout = async () => {
    try {
      const res = await fetch(
        'http://localhost:5000/api/v1/chatbot/auth/logout',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + token,
          },
        }
      );

      if (res.status === 200) {
        setIsAuth(false);
        navigate('/login');
      } else {
        const result = await res.json();
        console.log(result);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const data = { login, logout, isAuth };
  return <AuthContext.Provider value={data}>{children}</AuthContext.Provider>;
};

export default AuthContext;
