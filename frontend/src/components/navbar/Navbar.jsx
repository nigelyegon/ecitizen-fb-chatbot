import React, { useContext } from 'react';
import './Navbar.css';
import profilePic from '../../assets/profileimage.png';
import { useTheme } from '../../contexts/ThemeContext';
import { FaMoon, FaSun } from 'react-icons/fa';
import AuthContext from '../../contexts/AuthContext';

const Navbar = ({ toggleSidebar }) => {
  const { theme, toggleTheme } = useTheme();

  const { logout } = useContext(AuthContext);

  return (
    <header className={`header header-${theme}`}>
      <button className='menu-toggle' onClick={toggleSidebar}>
        ☰
      </button>
      <h1 className={`header-txt header-text-${theme}`}>Dashboard</h1>
      <div className='user-info'>
        <span className={`header-text-${theme}`}>Welcome, Admin</span>
        <img src={profilePic} alt='Admin' className='profile-pic' />
        <button className='theme-toggle' onClick={toggleTheme}>
          {theme === 'light' ? <FaMoon /> : <FaSun />}
        </button>
        <button onClick={logout} type='button' className='logout-btn'>
          Logout
        </button>
      </div>
    </header>
  );
};

export default Navbar;
