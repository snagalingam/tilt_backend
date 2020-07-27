import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import TiltButton from "../tiltButton/TiltButton";

import banner1 from "../../img/banner1.png";
import "./banner.scss";

const emailSchema = yup.object().shape({
  email: yup.string().email().required("Please enter a valid email"),
});

const Banner = () => {
  function handleSubmit(values) {
    console.log(values);
  }

  return (
    <div className="tilt-banner-container">
      <div className="left">
        <h1>Make smart financial decisions when choosing a college</h1>
        <p>
          We provide friendly reports simplifying your financial aid packages
          and helping you compare across colleges
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
      <div className="right">
        <img src={banner1} alt="girl waiting" />
      </div>
    </div>
  );
};

export default Banner;
