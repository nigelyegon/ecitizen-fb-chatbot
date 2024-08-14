import React, { useContext, useState } from 'react';
import './Login.css';
import banner from '../../assets/banner.svg';
import AuthContext from '../../contexts/AuthContext';

const Login = () => {
  const [showPassword, setShowPassword] = useState(false);

  const { login } = useContext(AuthContext);
  const toggleShowPassword = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className='login-container'>
      <div className='login-form-wrapper'>
        <div className='banner-container'>
          <img src={banner} alt='eCitizen Banner' className='banner' />
        </div>
        <h2>Login</h2>
        <form onSubmit={login}>
          <div className='form-group'>
            <label htmlFor='email' style={{ fontWeight: 100 }}>
              Email Adress
            </label>
            <input type='email' name='email' id='email' required />
          </div>
          <div className='form-group'>
            <label htmlFor='password' style={{ fontWeight: 100 }}>
              Password
            </label>
            <div className='password-input-container'>
              <input
                type={showPassword ? 'text' : 'password'}
                name='password'
                id='password'
                required
              />
              <button
                type='button'
                onClick={toggleShowPassword}
                className='show-password-btn'
              >
                {showPassword ? 'Hide' : 'Show'}
              </button>
            </div>
          </div>
          <button type='submit'>Login</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
