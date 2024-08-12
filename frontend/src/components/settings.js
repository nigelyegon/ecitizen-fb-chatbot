// fortheme changes and password reset

// Importing React and useState hook for managing state
import React, { useState } from 'react';
// Importing the CSS file for styling the Settings component
import './Settings.css';

const Settings = ({ currentTheme, onThemeChange }) => {  // Settings component accepting currentTheme and onThemeChange as props
  const [newPassword, setNewPassword] = useState('');  // State for managing the new password input, initialized to an empty string

  // Function to handle password change form submission
  const handlePasswordChange = (e) => {
    e.preventDefault();  // Prevents the default form submission behavior
    // Implement password change logic here
    console.log('Password changed to:', newPassword);  // For now, just log the new password to the console
    setNewPassword('');  // Clear the new password input field
  };

  return (  // JSX to render the Settings component
    <div className="settings">  // Main container div with class 'settings'
      <h2>Settings</h2>  // Heading for the Settings page
      <div className="theme-settings">  // Container div for theme settings
        <h3>Theme</h3>  // Subheading for theme settings
        <select value={currentTheme} onChange={(e) => onThemeChange(e.target.value)}>  // Dropdown to select the theme
          <option value="light">Light</option>  // Option for light theme
          <option value="dark-blue">Dark Blue</option>  // Option for dark blue theme
          <option value="dark-green">Dark Green</option>  // Option for dark green theme
          <option value="dark-purple">Dark Purple</option>  // Option for dark purple theme
        </select>
      </div>
      <div className="password-settings">  // Container div for password settings
        <h3>Change Password</h3>  // Subheading for password settings
        <form onSubmit={handlePasswordChange}>  // Form to handle password change
          <input
            type="password"  // Input field for new password
            value={newPassword}  // Controlled input value linked to newPassword state
            onChange={(e) => setNewPassword(e.target.value)}  // Update the newPassword state on input change
            placeholder="New Password"  // Placeholder text for the input field
            required  // Makes the input field required
          />
          <button type="submit">Change Password</button>  // Submit button to change the password
        </form>
      </div>
    </div>
  );
};

export default Settings;  // Exporting the Settings component as the default export
