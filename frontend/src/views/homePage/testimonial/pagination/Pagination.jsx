import React, { useEffect, useState } from "react";

import "./pagination.scss";

const Pagination = ({ total, perPage, next, previous, barColor }) => {
  const [currentPage, changePage] = useState(1);
  const [pages] = useState(Math.ceil(total / perPage));

  function createBars(numberOfPages) {
    const bars = [];
    for (let i = 1; i <= numberOfPages; i++) {
      bars.push(
        <div
          key={i}
          className={`page-bar${i === currentPage ? " selected" : ""}`}
        ></div>
      );
    }
    return bars;
  }

  function handlePrevious() {
    if (currentPage !== 1) {
      changePage((prev) => (prev -= 1));
      if (previous) {
        previous();
      }
    }
  }

  function handleNext() {
    if (currentPage !== pages) {
      changePage((prev) => (prev += 1));
      if (next) {
        next();
      }
    }
  }

  useEffect(() => {
    createBars(5);
  }, [pages]);

  return (
    <div className="Pagination">
      <div className="Pagination__pages">
        <div>
          <span>{currentPage}</span>
          <span>/</span>
          <span>{pages}</span>
        </div>
      </div>
      <div className={`pagination-bar${barColor ? ` ${barColor}` : ""}`}>
        {createBars(pages)}
      </div>
      <div className="Pagination__buttons">
        <button onClick={handlePrevious} disabled={currentPage === 1}>
          Previous
        </button>
        <button onClick={handleNext} disabled={currentPage === pages}>
          Next
        </button>
      </div>
    </div>
  );
};

export default Pagination;
