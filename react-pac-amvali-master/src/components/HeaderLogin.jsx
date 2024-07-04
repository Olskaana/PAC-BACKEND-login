import React from "react";
import { Link } from "react-router-dom";
import white_logo from "./assets/Logo AMV White.png";

function HeaderLogin() {
  return (
    <div className="info-page">
      <div className="logo">
        <Link to="/">
          <img src={white_logo} alt="Amvali White Logo" />
        </Link>
      </div>
      <div className="logo-text">
        <Link to="/">
          <h2>PÁGINA INICIAL</h2>
        </Link>
      </div>
    </div>
  );
}

export default HeaderLogin;
