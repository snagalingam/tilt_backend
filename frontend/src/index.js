import React, { useEffect, lazy, Suspense } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route } from "react-router-dom";
import { loadReCaptcha } from "react-recaptcha-google";
import { useQuery } from "@apollo/client";

import Apollo from "./apollo/ApolloProvider/Apollo";
import CreateScholarship from "./components/resources/scholarships/CreateScholarship";
import ContactUs from "./components/ContactUs";
import PrivacyPolicy from "./components/PrivacyPolicy";
import ResourcesFAQs from "./components/resources/ResourcesFAQs";
import ResourcesIntro from "./components/resources/ResourcesIntro";
import Scholarships from "./components/resources/scholarships/Scholarships";
import ScrollToTop from "./components/ScrollToTop";
import Sitemap from "./components/Sitemap";
import SignupSurvey from "./components/signup/SignupSurvey";
import SignupThankYou from "./components/signup/SignupThankYou";
import Terminology from "./components/resources/Terminology";
import TermsOfService from "./components/TermsOfService";
import Navbar from "./components/navBar/NavBar";

import {
  initializeAOS,
  initializeSmoothScroll,
  initializeTyped,
} from "./js/helpers";
import { GET_ME } from "./apollo/queries/account";
import { isLoggedInVar } from "./apollo/reactiveVariables/account";

import "./scss/main.scss";
import "aos/dist/aos.css";
import "./fonts/Feather/feather.css";
import "./scss/theme.scss";
import "cross-fetch/polyfill";

const Dashboard = lazy(() => import("./views/dashboard/Dashboard"));
const FaqPage = lazy(() => import("./views/faqPage/FaqPage"));
const HomePage = lazy(() => import("./views/homePage/HomePage"));
const Login = lazy(() => import("./views/login/Login"));
const Onboarding = lazy(() => import("./views/onboarding/Onboarding"));
const ResetPassword = lazy(() => import("./views/resetPassword/ResetPassword"));
const SignUp = lazy(() => import("./views/signUp/SignUp"));

const App = () => {
  const { data, loading, error } = useQuery(GET_ME);

  useEffect(() => {
    if (data) {
      isLoggedInVar(true);
    }
    if (error) {
      isLoggedInVar(false);
    }
  }, [data, loading, error]);

  useEffect(() => {
    loadReCaptcha();
    document.title = "Financial aid help for high school students - Tilt";
    initializeAOS();
    initializeSmoothScroll();
    initializeTyped();
  }, []);

  return (
    <BrowserRouter>
      <ScrollToTop>
        <Navbar />
        <Suspense fallback={<div />}>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/faq" component={FaqPage} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/reset-password" component={ResetPassword} />
          <Route exact path="/signup" component={SignUp} />
          {/* protected routes */}
          <Route exact path="/dashboard" component={Dashboard} />
          <Route exact path="/onboarding" component={Onboarding} />
        </Suspense>
        <Route exact path="/contact" component={ContactUs} />
        <Route exact path="/privacy-policy" component={PrivacyPolicy} />
        <Route exact path="/terms-of-service" component={TermsOfService} />
        <Route exact path="/resources" component={ResourcesIntro} />
        <Route exact path="/resources/faqs" component={ResourcesFAQs} />
        <Route exact path="/resources/scholarships" component={Scholarships} />
        <Route
          exact
          path="/resources/scholarships/create"
          component={CreateScholarship}
        />
        <Route exact path="/resources/terminology" component={Terminology} />
        <Route exact path="/signup-survey" component={SignupSurvey} />
        <Route exact path="/signup-thank-you" component={SignupThankYou} />
        <Route exact path="/sitemap" component={Sitemap} />
      </ScrollToTop>
    </BrowserRouter>
  );
};

ReactDOM.render(
  <Apollo>
    <App />
  </Apollo>,
  document.querySelector("#root")
);
