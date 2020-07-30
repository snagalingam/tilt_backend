import React, { useEffect, useRef, useState } from "react";
import anime from "animejs/lib/anime.es.js";

import "./animated-counter.scss";

const initialState = {
  "1": 0,
  "2": 0,
  "3": 0,
  "4": 0,
  "5": 0,
  "6": 0,
  "7": 0,
};

const AnimatedCounter = () => {
  const counterRef = useRef(null);
  const [isAnimated, setIsAnimated] = useState(false);

  function handleScroll() {
    console.log("handling");
    const numbers = document.querySelectorAll(".number");
    if (counterRef?.current && !isAnimated) {
      if (
        counterRef.current.getBoundingClientRect().top <
        (window.innerHeight * 2) / 3
      ) {
        setIsAnimated((prev) => {
          if (!prev) {
            anime({
              targets: initialState,
              delay: anime.stagger(100, { start: 500 }),
              "1": 2,
              "2": 6,
              "3": 1,
              "4": 0,
              "5": 9,
              "6": 0,
              "7": 5,
              round: 1,
              easing: "linear",
              update: function () {
                for (
                  let i = numbers.length - 1, delay = 0;
                  i >= 0;
                  i--, delay += 250
                ) {
                  numbers[i].innerHTML = initialState[i + 1];
                }
              },
            });
          }
          return true;
        });
      }
    }
  }

  useEffect(() => {
    if (counterRef?.current) {
      if (!isAnimated) {
        window.addEventListener("scroll", handleScroll);
      } else {
        window.removeEventListener("scroll", handleScroll);
      }
    }
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, [counterRef?.current, isAnimated]);

  return (
    <div className="animated-counter" ref={counterRef}>
      <div>$</div>
      <div className="number">0</div>
      <div>,</div>
      <div className="number">0</div>
      <div className="number">0</div>
      <div className="number">0</div>
      <div>,</div>
      <div className="number">0</div>
      <div className="number">0</div>
      <div className="number">0</div>
    </div>
  );
};

export default AnimatedCounter;
