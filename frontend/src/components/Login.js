import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";
import axios from "axios";
import bg from "../assets/login.png";
import logo from "../assets/logo.svg";
import facebookLogo from "../assets/Facebook_Logo_Primary.png";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState(null);
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const access_token = localStorage.getItem("access_token");
    if (access_token) {
      navigate("/home");
    } else {
      console.log("No access token found");
    } // Add your authentication logic here to check if user is already logged in and navigate to home page if true
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email && password) {
      axios
        .post(
          "http://127.0.0.1:5000/api/v1/chatbot/auth/login",
          { email, password },
          { Headers: { "Content-Type": "application/json" } }
        )
        .then((resp) => {
          const response = resp.data;
          console.log(response);
          const { access_token, refresh_token } = response;
          localStorage.setItem("access_token", access_token);
          localStorage.setItem("refresh_token", refresh_token);
          navigate("/home");
        })
        .catch((err) => {
          const error = err.response.data;
          console.log(error);
          setErrorMessage(error.message);
          setPassword("");
          setEmail("");
        });
    }
  };
  const toggleShowPassword = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="login-container">
      <div className="left">
        <img src={bg} alt="Background" />
      </div>
      <div className="right">
        <div className="login-form-wrapper">
        <div className="logo-container">
            <img src={logo} alt="Coat of Arms" className="coat-of-arms" />
            <img src={facebookLogo} alt="eCitizen Logo" className="ecitizen-logo" />
        </div>
          <h2>Admin Login</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <div className="password-input-container">
                <input
                  type={showPassword ? "text" : "password"}
                  id="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
                <button type="button" onClick={toggleShowPassword} className="show-password-btn">
                  {showPassword ? "Hide" : "Show"}
                </button>
              </div>
            </div>
            <button type="submit">Login</button>
          </form>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
        </div>
      </div>
    </div>
  );
};

export default Login;