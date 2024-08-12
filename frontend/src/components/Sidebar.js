// src/components/Sidebar.js
import React from "react";
import "./Sidebar.css";
import logo from "../assets/ecitizen.png"; // Add the logo file

const Sidebar = () => {
  return (
    <div className="sidebar">
      <img src={logo} alt="Logo" className="logo" />
      <ul>
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">Users</a>
        </li>
        <li>
          <a href="#">Settings</a>
        </li>
        <li>
          <a href="#">Change Password</a>
        </li>
        <li>
          <a href="#">Logout</a>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
