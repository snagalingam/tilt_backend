import React, { useState, useEffect } from "react";

import Pagination from "./pagination/Pagination";

import "./testimonial.scss";

const Testimonial = () => {
  const [currentPage, changePage] = useState(1);
  const [perPage, changePerPage] = useState(2);
  const [toBeDisplayed, changeToBeDisplayed] = useState([]);

  const items = [
    {
      user: "Tony",
      testimonial:
        "It made it easier to see which college was financially better",
    },
    {
      user: "Johnny",
      testimonial: "I found the right school for me.",
    },
    {
      user: "Ariel",
      testimonial: "This is such an amazin tool!",
    },
  ];

  useEffect(() => {
    const lastIndex = perPage * currentPage - 1;
    const startingIndex = lastIndex - (perPage - 1);
    const itemsToBeDisplayed = items.slice(startingIndex, lastIndex + 1);
    changeToBeDisplayed(itemsToBeDisplayed);
  }, [currentPage]);

  function handleNext() {
    const totalPaginations = Math.ceil(items.length / perPage);
    if (currentPage !== totalPaginations) {
      changePage((prev) => (prev += 1));
    }
  }

  function handlePrevious() {
    if (currentPage !== 1) {
      changePage((prev) => (prev -= 1));
    }
  }

  return (
    <div className="testimonials-container">
      <div className="testimonials">
        {toBeDisplayed.map((item) => {
          return (
            <div className="testimonial">
              <p>{item.testimonial}</p>
              <span>- {item.user}</span>
            </div>
          );
        })}
      </div>
      <div className="pagination">
        <Pagination
          total={items.length}
          perPage={perPage}
          next={handleNext}
          previous={handlePrevious}
        />
      </div>
    </div>
  );
};

export default Testimonial;
