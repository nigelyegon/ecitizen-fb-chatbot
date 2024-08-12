// src/ThemeContext.js
import React, { createContext, useState, useContext } from "react"; // Importing necessary functions from React

const ThemeContext = createContext(); // Creating a context for theme management

export const ThemeProvider = ({ children }) => {
  // ThemeProvider component to wrap the application and provide theme context
  const [theme, setTheme] = useState("dark"); // State for managing the current theme, initialized to 'light'
  const [darkMode, setDarkMode] = useState("blue"); // State for managing the dark mode color, initialized to 'blue'

  // Function to toggle between light and dark themes
  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light")); // Toggle theme state between 'light' and 'dark'
  };

  // Function to change the dark mode color
  const changeDarkMode = (color) => {
    setDarkMode(color); // Update the darkMode state with the selected color
  };

  // Combine theme and dark mode color for easier use in components
  const currentTheme = theme === "light" ? "light" : `dark-${darkMode}`; // Determine the current theme string

  return (
    // Providing the theme context to the children components
    <ThemeContext.Provider
      value={{ currentTheme, theme, darkMode, toggleTheme, changeDarkMode }}
    >
      {children}
    </ThemeContext.Provider>
  );
};

// Custom hook to use the theme context
export const useTheme = () => useContext(ThemeContext);
