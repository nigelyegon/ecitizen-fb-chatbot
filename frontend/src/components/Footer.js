// src/Footer.js

import React from "react";
import "./Footer.css"; // optional: for styling your footer

const Footer = () => {
  return (
    <footer className="footer">
      <p>&copy; 2024 My Website. All rights reserved.</p>
      <nav>
        <ul>
          <li>
            <a href="#privacy">Privacy Policy</a>
          </li>
          <li>
            <a href="#terms">Terms of Service</a>
          </li>
          <li>
            <a href="#contact">Contact</a>
          </li>
        </ul>
      </nav>
    </footer>
  );
};

export default Footer;
