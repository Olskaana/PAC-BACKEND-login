import React from "react";
import { Link } from "react-router-dom";
import white_logo from "./assets/Logo AMV White.png";
import avatar_login from "./assets/AvatarWhite.png";

function HeaderWhite() {
  return (
    <nav className="navbar">
      <div className="content-nav">
        <div className="logo-dash">
          <a
            href="https://amvali.org.br/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img id="white-logo" src={white_logo} alt="White logo Amvali" />
          </a>
        </div>
        <div className="identity">
          <h1>
            <a
              href="https://amvali.org.br/"
              target="_blank"
              rel="noopener noreferrer"
            >
              AMVALI
            </a>
          </h1>
        </div>
        <div>
          <Link to="login">
            <img id="login" src={avatar_login} alt="Login Avatar" />
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default HeaderWhite;
