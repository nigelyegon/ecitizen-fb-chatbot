// src/components/Header.js
import React from "react";
import "./Header.css";
import profilePic from "../assets/profileimage.png";
import { useTheme } from "../ThemeContext";
import { FaMoon, FaSun } from "react-icons/fa";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Header = ({ toggleSidebar }) => {
  const { theme, toggleTheme } = useTheme();
  const navigate = useNavigate();

  const handleLogout = () => {
    if (window.confirm("Are you sure you want to logout")) {
      const access_token = localStorage.getItem("access_token");
      axios
        .post(
          `http://127.0.0.1:5000/api/v1/chatbot/auth/logout`,
          {},
          {
            headers: {
              Authorization: `Bearer ${access_token}`,
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          localStorage.removeItem("access_token");
          navigate("/login");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  };

  return (
    <header className={`header header-${theme}`}>
      <button className="menu-toggle" onClick={toggleSidebar}>
        ☰
      </button>
      <h1 className={`header-txt header-text-${theme}`}>Dashboard</h1>
      <div className="user-info">
        <span className={`header-text-${theme}`}>Welcome, Admin</span>
        <img src={profilePic} alt="Admin" className="profile-pic" />
        <button className="theme-toggle" onClick={toggleTheme}>
          {theme === "light" ? <FaMoon /> : <FaSun />}
        </button>
        <button onClick={handleLogout} type="button" className="logout-btn">
          Logout
        </button>
      </div>
    </header>
  );
};

export default Header;
