// fortheme changes and password reset

// Importing React and useState hook for managing state
import React, { useState } from 'react';
// Importing the CSS file for styling the Settings component
import './Settings.css';

const Settings = ({ currentTheme, onThemeChange }) => {
  // Settings component accepting currentTheme and onThemeChange as props
  const [newPassword, setNewPassword] = useState(''); // State for managing the new password input, initialized to an empty string

  // Function to handle password change form submission
  const handlePasswordChange = (e) => {
    e.preventDefault(); // Prevents the default form submission behavior
    // Implement password change logic here
    console.log('Password changed to:', newPassword); // For now, just log the new password to the console
    setNewPassword(''); // Clear the new password input field
  };

  return (
    // JSX to render the Settings component
    <div className='settings'>
      <h2>Settings</h2>
      <div className='theme-settings'>
        <h3>Theme</h3>
        <select
          value={currentTheme}
          onChange={(e) => onThemeChange(e.target.value)}
        >
          <option value='light'>Light</option>
          <option value='dark-blue'>Dark Blue</option>
          <option value='dark-green'>Dark Green</option>
          <option value='dark-purple'>Dark Purple</option>
        </select>
      </div>
      <div className='password-settings'>
        <h3>Change Password</h3>
        <form onSubmit={handlePasswordChange}>
          <input
            type='password' // Input field for new password
            value={newPassword} // Controlled input value linked to newPassword state
            onChange={(e) => setNewPassword(e.target.value)} // Update the newPassword state on input change
            placeholder='New Password' // Placeholder text for the input field
            required // Makes the input field required
          />
          <button type='submit'>Change Password</button>
        </form>
      </div>
    </div>
  );
};

export default Settings; // Exporting the Settings component as the default export
