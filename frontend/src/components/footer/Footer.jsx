import React from "react";
import Link from "react-router-dom/Link";
import CopyrightIcon from "@material-ui/icons/Copyright";
import FacebookIcon from "@material-ui/icons/Facebook";
import InstagramIcon from "@material-ui/icons/Instagram";
import SendIcon from "@material-ui/icons/Send";
import YouTubeIcon from "@material-ui/icons/YouTube";

import "./footer.scss";
import tiltLogo from "../../img/tilt_logo.png";

const Footer = () => {
  return (
    <div className="tilt-footer">
      <div className="company-info">
        <img src={tiltLogo} alt="tilt-logo" />
        <div>
          <p>
            <CopyrightIcon /> Tilt 2020
          </p>
          <p>Your financial aid expert</p>
        </div>
      </div>
      <div className="links">
        <nav>
          <ul>
            <li>
              <Link to="/blog">Blog</Link>
            </li>
            <li>
              <Link to="/faq">FAQ</Link>
            </li>
            <li>
              <Link to="/contact">Contact</Link>
            </li>
          </ul>
          <ul>
            <li>
              <Link to="/privacy-policy">Privacy Policy</Link>
            </li>
            <li>
              <Link to="/terms-of-service">Terms of Service</Link>
            </li>
          </ul>
        </nav>
        <div className="social-media">
          <a href="https://www.facebook.com">
            <FacebookIcon color="gray" />
          </a>
          <a href="https://instagram.com">
            <InstagramIcon />
          </a>
          <a href="https://youtube.com">
            <YouTubeIcon />
          </a>
          <a href="https://gmail.com">
            <SendIcon />
          </a>
        </div>
      </div>
    </div>
  );
};

export default Footer;
