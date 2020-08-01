import React, { useState, useEffect } from "react";
import StarIcon from "@material-ui/icons/Star";

import Pagination from "./pagination/Pagination";
import { testimonials } from "./testimonials";

import "./testimonial.scss";

const Testimonial = () => {
  const [currentPage, changePage] = useState(1);
  const [perPage] = useState(2);
  const [toBeDisplayed, changeToBeDisplayed] = useState([]);

  function handleNext() {
    const totalPaginations = Math.ceil(testimonials.length / perPage);
    if (currentPage !== totalPaginations) {
      changePage((prev) => (prev += 1));
    }
  }

  function handlePrevious() {
    if (currentPage !== 1) {
      changePage((prev) => (prev -= 1));
    }
  }

  useEffect(() => {
    const lastIndex = perPage * currentPage - 1;
    const startingIndex = lastIndex - (perPage - 1);
    const itemsToBeDisplayed = testimonials.slice(startingIndex, lastIndex + 1);
    changeToBeDisplayed(itemsToBeDisplayed);
  }, [currentPage, perPage]);

  return (
    <div className="TiltTestimonial">
      <div className="TiltTestimonial__testimonials">
        {toBeDisplayed.map((item) => {
          const stars = [];
          for (let i = 0; i < item.rating; i++) {
            stars.push(
              <StarIcon
                key={`${item.testimonial}-${item.rating}-${i}`}
                className="star"
              />
            );
          }
          return (
            <div key={item.testimonial} className="testimonial">
              <div>{stars}</div>
              <p>{item.testimonial}</p>
              <span>- {item.user}</span>
            </div>
          );
        })}
      </div>
      <div className="TiltTestimonial__pagination">
        <Pagination
          total={testimonials.length}
          perPage={perPage}
          next={handleNext}
          previous={handlePrevious}
          barColor="purple"
        />
      </div>
    </div>
  );
};

export default Testimonial;
