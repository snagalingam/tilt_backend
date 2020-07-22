import React, { useState, useEffect } from "react";

import "./login-carousel.scss";

const messages = [
  {
    primary:
      "We provide friendly reports simplifying your financial aid package and helping you compare across colleges",
    secondary: "Jane Cooper - Director Butler College Prep",
    image:
      "https://res.cloudinary.com/dgbm9hshy/image/upload/v1564596730/LRM_EXPORT_177119709472004_20190731_110718849_jlfv22.jpg",
  },
  {
    primary: "I enjoy building interactive and intuitive user interfaces",
    secondary: "Tony Yu, Software Engineer",
    image:
      "https://res.cloudinary.com/dgbm9hshy/image/upload/v1566720969/IMG_20190310_152414_807_acakcz.jpg",
  },
  {
    primary: "Don't give me any devops tasks",
    secondary: "Johnny Siu, Javascript Engineer",
    image:
      "https://scontent-sjc3-1.xx.fbcdn.net/v/t31.0-8/22095808_10154654866856650_6342051792776742728_o.jpg?_nc_cat=111&_nc_sid=09cbfe&_nc_ohc=XjSk7v3XQP8AX_CwtWQ&_nc_ht=scontent-sjc3-1.xx&oh=5dd522aea204cec8285241f4d4dae1e7&oe=5F3EE16B",
  },
];

const LoginCarousel = () => {
  const [numberOfItems] = useState(messages.length);
  const [selectedIndex, selectIndex] = useState(0);

  function handleLeft() {
    if (selectedIndex - 1 >= 0) {
      selectIndex((prevIndex) => (prevIndex -= 1));
    }
  }

  function handleRight() {
    if (selectedIndex + 1 <= numberOfItems - 1) {
      selectIndex((prevIndex) => (prevIndex += 1));
    }
  }

  function handleInterval() {
    selectIndex((prevIndex) => {
      if (prevIndex + 1 > numberOfItems - 1) {
        return 0;
      } else {
        return (prevIndex += 1);
      }
    });
  }

  useEffect(() => {
    setInterval(handleInterval, 10000);
    return () => {
      clearInterval(handleInterval);
    };
  }, []);

  return (
    <div className="login-carousel">
      <div className="login-carousel-controls">
        <div
          onClick={handleLeft}
          className={`${selectedIndex - 1 < 0 ? "disabled" : ""}`}
          role="button"
        >
          &#60;
        </div>
        <div
          onClick={handleRight}
          className={`${
            selectedIndex + 1 > numberOfItems - 1 ? "disabled" : ""
          }`}
          role="button"
        >
          &#62;
        </div>
      </div>

      <div className="tilt-messages">
        {messages.map((message, index) => {
          return (
            <div
              key={message.secondary}
              className={`tilt-message-container${
                index === selectedIndex ? " visible" : ""
              }`}
              style={{
                backgroundImage: `linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.5)), url(${message.image})`,
                backgroundPosition: "center",
                backgroundRepeat: "no-repeat",
                backgroundSize: "cover",
              }}
            >
              <p className="tilt-message-primary">{message.primary}</p>
              <p className="tilt-message-secondary">{message.secondary}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default LoginCarousel;
