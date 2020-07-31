import React, { useEffect } from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";
import CheckCircleIcon from "@material-ui/icons/CheckCircle";

import AnimatedCounter from "../../components/animatedCounter/AnimatedCounter";
import Banner from "../../components/banner/Banner";
import BrushedText from "../../components/brushedText/BrushedText";
import FaqSection from "../../components/faqSection/FaqSection";
import Footer from "../../components/footer/Footer";
import JoinTilt from "./joinTilt/JoinTilt";
import Testimonial from "./testimonial/Testimonial";
import TiltButton from "../../components/tiltButton/TiltButton";

import "./home-page.scss";
import dog from "../../img/dog.png";
import butler from "../../img/clients/butler.svg";
import hfs from "../../img/clients/hfs.svg";
import solorio from "../../img/clients/solorio.svg";
import westinghouse from "../../img/clients/westinghouse.svg";

const emailSchema = yup.object().shape({
  email: yup.string().email().required("Please enter a valid email"),
});

const HomePage = () => {
  function handleSubmit(values) {
    console.log(values);
  }

  useEffect(() => {
    document.title = "Financial aid help for high school students - Tilt";
  }, []);

  return (
    <div className="home-page-container view-container">
      <Banner />

      <div className="tilt-partners">
        <div className="tilt-partners-header">
          <h2>Our Partners</h2>
          <p>
            Not only do we support students directly, we also partner with high
            schools and community organizations to help their students.
          </p>
        </div>
        <div className="client-logos">
          <div className="butler-logo">
            <img src={butler} alt="butler logo" />
          </div>
          <div>
            <img src={hfs} className="hfs-logo" alt="hfs logo" />
          </div>
          <div>
            <img src={solorio} className="solorio-logo" alt="solorio logo" />
          </div>
          <div>
            <img
              src={westinghouse}
              className="westinghouse-logo"
              alt="westinghouse logo"
            />
          </div>
        </div>
      </div>

      <JoinTilt />

      <div className="tilt-couple" style={{ marginTop: "10rem" }}>
        <div className="text">
          <h2>
            Find &#38; select <BrushedText text="affordable" /> colleges
          </h2>
          <p>
            Based on your background, we can help you find colleges that will
            offer you the most amount of grants and scholarships.
          </p>
          <div className="get-started">
            <TiltButton classes={["purple", "secondary"]}>
              Get Started
            </TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
        <div className="image">
          <img src={dog} />
        </div>
      </div>
      <div className="tilt-couple" style={{ marginTop: "10rem" }}>
        <div className="image">
          <img src={dog} />
        </div>
        <div className="text">
          <h2>
            Get help applying to <BrushedText text="financial" /> aid
          </h2>
          <p>
            We will walk you through how to fill out financial aid forms and
            compare your financial aid packages once you have been accepted.
          </p>
          <div className="get-started">
            <TiltButton classes={["orange", "secondary"]}>
              Get Started
            </TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
      </div>

      <div className="tilt-couple" style={{ marginTop: "10rem" }}>
        <div className="text">
          <h2>
            On-demand <BrushedText text="advisors" /> to answer questions
          </h2>
          <p>
            We know that figuring out how to pay for college can be confusing
            and overwhelming—that's why you'll always have access to our
            advisors who are ready to answer your questions.
          </p>
          <div className="get-started">
            <TiltButton classes={["purple", "secondary"]}>
              Get Started
            </TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
        <div className="image">
          <img src={dog} />
        </div>
      </div>

      <div className="tilt-couple" style={{ marginTop: "10rem" }}>
        <div className="image">
          <img src={dog} />
        </div>
        <div className="text">
          <h2>
            Database of <BrushedText text="vetted" /> scholarships
          </h2>
          <p>
            We find and evaluate scholarships offered across the country, so you
            don't have to.
          </p>
          <div className="get-started">
            <TiltButton classes={["orange", "secondary"]}>
              Get Started
            </TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
      </div>

      <div
        className="tilt-couple tilt-financial-aid"
        style={{ marginTop: "10rem" }}
      >
        <div className="text">
          <h2>Financial aid for students</h2>
        </div>
        <div className="image">
          <AnimatedCounter />
          <p>Last year, we helped students get financial aid.</p>
        </div>
      </div>

      <Testimonial />

      <FaqSection />

      <div className="purple-box" style={{ marginTop: "10rem" }}>
        <div className="organization">
          <div className="text">
            <h2>Become a partner</h2>
            <p>
              Interested in bringing Tilt to your school or community
              organization?
            </p>
          </div>

          <div className="form">
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
                  <TiltButton classes={["white"]} type="submit">
                    Get Started
                  </TiltButton>
                </Form>
              )}
            </Formik>
          </div>
        </div>

        <div
          style={{
            margin: "2rem 0",
            width: "100%",
            border: "1px solid gray",
          }}
        />

        <div className="features">
          <span>
            <CheckCircleIcon /> Access to student accounts
          </span>
          <span>
            <CheckCircleIcon /> Customized reporting
          </span>
          <span>
            <CheckCircleIcon /> Satisfaction guarantee
          </span>
        </div>
      </div>

      <Footer />
    </div>
  );
};

export default HomePage;
