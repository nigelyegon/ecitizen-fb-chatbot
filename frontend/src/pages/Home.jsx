// src/pages/Home.js
import React, { useContext, useEffect, useState } from 'react'; // Importing React and the useState hook
import Sidebar from '../components/Sidebar'; // Importing the Sidebar component
import Header from '../components/navbar/Navbar'; // Importing the Header component
import Card from '../components/card/Card'; // Importing the Card component
import Footer from '../components/footer/Footer'; // Importing the Foot
import { useTheme } from '../contexts/ThemeContext'; // Importing the useTheme custom hook for theme management
import '../App.css'; // Importing the main application CSS
import '../Theme.css'; // Importing the theme-specific CSS
import { useNavigate } from 'react-router-dom';
import AuthContext from '../contexts/AuthContext';

const Home = () => {
  const { isAuth } = useContext(AuthContext);

  // Home component definition
  const [sidebarOpen, setSidebarOpen] = useState(false); // State for managing the sidebar's open/closed state
  const { theme, toggleTheme } = useTheme(); // Using the custom hook to get the current theme and the function to toggle it
  const navigate = useNavigate(); // Using the navigate hook to navigate between routes

  useEffect(() => {
    if (!isAuth) {
      navigate('/login');
    }
  }, [isAuth]);

  const toggleSidebar = () => {
    // Function to toggle the sidebar's open/closed state
    setSidebarOpen(!sidebarOpen); // Toggle the state value
  };

  return (
    // JSX to render the component
    <div className={`app app-${theme} ${sidebarOpen ? 'sidebar-open' : ''}`}>
      <Sidebar />
      <div className='main-content'>
        {/* // Container div for the main content */}
        <Header
          toggleSidebar={toggleSidebar}
          toggleTheme={toggleTheme}
          theme={theme}
        />
        {/* // Rendering the Header component with props for toggling sidebar and theme, and passing the current theme */}
        <section className='cards'>
          {/* // Section for the card components */}
          <Card
            title='Daily Users' // Title prop for the card
            description='Number of users that have interacted with system today.' // Description prop for the card
            type='counter'
            // Type prop to specify this card is a counter
          />
          <Card
            title='Message Hits' // Title prop for the card
            description="Today's Messages." // Description prop for the card
            type='counter' // Type prop to specify this card is a counter
          />
          <Card
            title='FAQs' // Title prop for the card
            description='Most frequently asked questions.' // Description prop for the card
            // No type prop, so this card will display the description
          />
          <Card
            title='Comment Chart' // Title prop for the card
            description='Satisfaction distribution' // Description prop for the card
            type='chart' // Type prop to specify this card is a chart
          />
        </section>
      </div>
      <Footer></Footer>
    </div>
  );
};

export default Home; // Exporting the Home component as the default export
