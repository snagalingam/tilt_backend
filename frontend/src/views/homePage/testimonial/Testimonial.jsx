import React, { useState, useEffect } from "react";
import StarIcon from "@material-ui/icons/Star";

import Pagination from "./pagination/Pagination";

import "./testimonial.scss";
import { Star } from "react-feather";

const Testimonial = () => {
  const [currentPage, changePage] = useState(1);
  const [perPage, changePerPage] = useState(2);
  const [toBeDisplayed, changeToBeDisplayed] = useState([]);

  const items = [
    {
      rating: 5,
      user: "Student who chose Notre Dame University",
      testimonial:
        "The financial aid report that Tilt made and sent to me made it a lot easier for me to compare the different financial aid packages that I received from each college, by using one standard template that was easy to understand.",
    },
    {
      rating: 5,
      user: "Student who chose Ohio State University",
      testimonial:
        "It was really helpful in deciding what college fit me best.",
    },
    {
      rating: 5,
      user: "Student who chose Bradley University",
      testimonial:
        "It made it easier to see which college was financially better.",
    },
    {
      rating: 5,
      user: "Student who chose Bradley University",
      testimonial: "Very helpful when it came to explaining my financial aid.",
    },
    {
      rating: 5,
      user: "Student who chose Notre Dame University",
      testimonial:
        "I found it extremely helpful, and I think others that I know would as well.",
    },
    {
      rating: 5,
      user: "Student who chose Ohio State University",
      testimonial:
        "It was superrr useful and they listen to feedback or any concerns in a timely manner.",
    },
    {
      rating: 5,
      user: "Student who chose Bradley University",
      testimonial: "It was quick and easy to use and a very helpful tool.",
    },
    {
      rating: 5,
      user: "Student who chose Bradley University",
      testimonial: "They were very helpful.",
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
    <div className="tilt-testimonial">
      <div className="testimonials">
        {toBeDisplayed.map((item) => {
          const stars = [];
          for (let i = 0; i < item.rating; i++) {
            stars.push(<StarIcon className="star" />);
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
      <div className="pagination">
        <Pagination
          total={items.length}
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
