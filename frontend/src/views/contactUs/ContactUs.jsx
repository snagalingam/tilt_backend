import React from "react";
import LocationOnIcon from "@material-ui/icons/LocationOn";
import HeadsetIcon from "@material-ui/icons/Headset";

import BrushedText from "../../components/brushedText/BrushedText";
import ContactUsForm from "./contactUsForm/ContactUsForm";
import FaqSection from "../../components/faqSection/FaqSection";
import Footer from "../../components/footer/Footer";

import "./contact-us.scss";

function ContactUs() {
  return (
    <div className="ContactUs view-container">
      <div className="ContactUs__contacts">
        <div className="left">
          <h2>
            Let us <BrushedText text="hear" /> from you directly!
          </h2>
          <p>
            We always want to hear from you! Let us know how we can best help
            you and we'll do our very best.
          </p>
          <div className="ContactUs__contact-information">
            <div className="ContactUs__contact-information-address">
              <div className="ContactUs__contact-information-icon">
                <LocationOnIcon />
              </div>

              <address>
                <p style={{ marginBottom: "1rem" }}>
                  <strong>Tilt HQ Address</strong>
                </p>
                <p>
                  120 N Racine Ave. Suite 100
                  <br />
                  Chicago, IL 60607
                </p>
              </address>
            </div>
            <div className="ContactUs__contact-information-number">
              <div className="ContactUs__contact-information-icon">
                <HeadsetIcon />
              </div>
              <p style={{ marginBottom: "1rem" }}>
                <strong>Customer Support</strong>
              </p>
              <p>Need help with anything?</p>
              <ul>
                <li>Call 1-312-313-1104</li>
                <li>Go to live chat</li>
              </ul>
            </div>
          </div>
        </div>
        <div className="right">
          <h3>Fill out the form</h3>
          <p>
            or drop us a message to{" "}
            <a href="mailto: hello@tilt.com">hello@tilt.com</a>
          </p>
          <ContactUsForm />
        </div>
      </div>
      <FaqSection />
      <Footer />
    </div>
  );
}

export default ContactUs;
