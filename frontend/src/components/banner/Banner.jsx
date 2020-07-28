import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import TiltButton from "../tiltButton/TiltButton";

import banner1 from "../../img/banner1.png";
import "./banner.scss";
import { useEffect } from "react";

const emailSchema = yup.object().shape({
  email: yup.string().email().required("Please enter a valid email"),
});

const Banner = () => {
  function handleSubmit(values) {
    console.log(values);
  }

  return (
    <div className="tilt-banner tilt-couple">
      <div className="text">
        <h1>Find an affordable path to a college degree</h1>
        <p>
          We help you find and select colleges that will offer you the most
          money.
        </p>
        <div>
          <Formik
            initialValues={{
              email: "",
            }}
            validationSchema={emailSchema}
            onSubmit={handleSubmit}
          >
            {(state) => (
              <Form className="tilt-email-input">
                <Field name="email" placeholder="Enter your email"></Field>
                {/* {state.errors && state.touched && (
            <span className="custom-text-input-error">
              {state.errors[field]}
            </span>
          )} */}
                <TiltButton classes={["dark"]} type="submit">
                  Get Started
                </TiltButton>
              </Form>
            )}
          </Formik>
        </div>
      </div>
      <div className="image">
        <img src={banner1} alt="girl waiting" />
      </div>
    </div>
  );
};

export default Banner;
