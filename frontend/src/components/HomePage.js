import React, { useEffect } from 'react';
import { Check } from 'react-feather';
import { Link } from 'react-router-dom';

import Footer from './Footer';
import NavBar from './NavBar';

import butler from '../img/clients/butler.svg';
import chart from '../img/product/chart.jpg';
import hfs from '../img/clients/hfs.svg';
import illustration from '../img/illustrations/illustration-1.png';
import sample from '../pdf/Tilt_Sample.pdf';
import solorio from '../img/clients/solorio.svg';
import westinghouse from '../img/clients/westinghouse.svg';

const HomePage = () => {
  useEffect(() => {
    document.title = 'Financial aid help for high school students - Tilt';
  });

  return (
    <div>
      <NavBar classList=" navbar-light bg-white" type="boxed" />
      {/* WELCOME
      ================================================== */}
      <section className="pt-4 pt-md-11 pb-11">
        <div className="container">
          <div className="row align-items-center">
            <div className="col-12 col-md-5 col-lg-6 order-md-2">

              {/* Image */}
              <div className="img-skewed img-skewed-left mb-8 mb-md-0">
                <img src={chart} alt="..." className="screenshot img-fluid mw-md-130" data-aos="img-skewed-item-left" data-aos-delay="100" />
              </div>

            </div>
            <div className="col-12 col-md-7 col-lg-6 order-md-1" data-aos="fade-up">

              {/* Heading */}
              <h1 className="display-4 text-center text-md-left">
                Make <span className="text-primary">smart financial decisions</span> when choosing a college
              </h1>

              {/* Text */}
              <p className="lead text-center text-md-left text-muted mb-6 mb-lg-8">
                We provide friendly reports simplifying your financial aid packages and helping you compare across colleges
              </p>

            </div>
          </div>
        </div>
      </section>

      {/* STEPS
      ================================================== */}
      <section className="pt-8 pb-9 pt-md-11 pb-md-10 border-bottom">
        <div className="container">
          <div className="row">
            <div className="col-12 col-md-4">
              <div className="row">
                <div className="col-auto col-md-12">

                  {/* Step */}
                  <div className="row no-gutters align-items-center mb-md-5">
                    <div className="col-auto">

                      <a href="#!" className="btn btn-sm btn-rounded-circle btn-gray-400 disabled opacity-1">
                        <span>1</span>
                      </a>

                    </div>
                    <div className="col">

                      <hr className="d-none d-md-block w-130" />

                    </div>
                  </div>

                </div>
                <div className="col col-md-12 ml-n5 ml-md-0">

                  {/* Heading */}
                  <h3>
                    Sign Up.
                  </h3>

                  {/* Text */}
                  <p className="text-muted mb-6 mb-md-0">
                    Fill out a short survey where we will collect your information and financial aid award letters.
                  </p>

                </div>
              </div>
            </div>
            <div className="col-12 col-md-4">
              <div className="row">
                <div className="col-auto col-md-12">

                  {/* Step */}
                  <div className="row no-gutters align-items-center mb-md-5">
                    <div className="col-auto">

                      <a href="#!" className="btn btn-sm btn-rounded-circle btn-gray-400 disabled opacity-1">
                        <span>2</span>
                      </a>

                    </div>
                    <div className="col">

                      <hr className="d-none d-md-block w-130" />

                    </div>
                  </div>

                </div>
                <div className="col col-md-12 ml-n5 ml-md-0">

                  {/* Heading */}
                  <h3>
                    Receive your report.
                  </h3>

                  {/* Text */}
                  <p className="text-muted mb-6 mb-md-0">
                    We will send you report via email with a detailed breakdown of each college’s financial aid offer and a comparison across your options.
                  </p>

                </div>
              </div>
            </div>
            <div className="col-12 col-md-4">
              <div className="row">
                <div className="col-auto col-md-12">

                  {/* Step */}
                  <div className="row no-gutters align-items-center mb-md-5">
                    <div className="col-auto">

                      <a href="#!" className="btn btn-sm btn-rounded-circle btn-gray-400 disabled opacity-1">
                        <span>3</span>
                      </a>

                    </div>
                  </div>

                </div>
                <div className="col col-md-12 ml-n5 ml-md-0">

                  {/* Heading */}
                  <h3>
                    Send us more!
                  </h3>

                  {/* Text */}
                  <p className="text-muted mb-0">
                    As you receive more acceptances and award letters, continue to send them to us, and we will continue to update your report.
                  </p>

                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* BRANDS
      ================================================== */}
      <section className="py-6 py-md-8 border-bottom bg-light">
        <div className="container">
          <div className="row align-items-center justify-content-center">

            {/* Badge */}
            <span className="badge badge-pill badge-gray-700-soft mb-4">
              <span className="h6 font-weight-bold text-uppercase">Our Clients</span>
            </span>

          </div>
          <div className="row align-items-center justify-content-between">
            <div className="col-6 col-sm-4 col-md-2 mb-4 mb-md-0">

              {/* Brand */}
              <div className="img-fluid text-gray-600 mb-2 mb-md-0 svg-shim">
                <img src={westinghouse} alt="..." />
              </div>

            </div>
            <div className="col-6 col-sm-4 col-md-2 mb-4 mb-md-0">

              {/* Brand */}
              <div className="img-fluid text-gray-600 mb-2 mb-md-0 svg-shim">
                <img src={solorio} alt="..." />
              </div>

            </div>
            <div className="col-6 col-sm-4 col-md-2 mb-4 mb-md-0">

              {/* Brand */}
              <div className="img-fluid text-gray-600 mb-2 mb-md-0 svg-shim">
                <img src={butler} alt="..." />
              </div>

            </div>
            <div className="col-6 col-sm-4 col-md-2 mb-4 mb-md-0">

              {/* Brand */}
              <div className="img-fluid text-gray-600 mb-2 mb-md-0 svg-shim">
                <img src={hfs} alt="..." />
              </div>

            </div>

          </div>
        </div>
      </section>

      {/* ABOUT
      ================================================== */}
      <section className="pt-8 pt-md-11 bg-gradient-light">
        <div className="container">
          <div className="row align-items-center justify-content-between mb-8 mb-md-11">
            <div className="col-12 col-md-6 order-md-2" data-aos="fade-left">

              {/* Heading */}
              <h2>
                The most useful resource <br />
                <span className="text-success">ever created for <span data-toggle="typed" data-options='{"strings": ["high school seniors.", "parents.", "counselors."]}'></span></span>
              </h2>

              {/* Text */}
              <p className="font-size-lg text-muted mb-6">
                Using Tilt to analyze your financial aid packages means never being confused again about the loans, scholarships, and costs for each college you have been accepted into.
                Our reports will provide you true transparency into the cost of college.
              </p>

              {/* List */}
              <div className="row">
                <div className="col-12 col-lg-6">

                  {/* Item */}
                  <div className="d-flex">

                    {/* Check */}
                    <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                      <Check />
                    </div>
                    {/* Text */}
                    <p className="text-success">
                      Unlimited colleges
                    </p>

                  </div>

                  {/* Item */}
                  <div className="d-flex">

                    {/* Check */}
                    <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                      <Check />
                    </div>

                    <p className="text-success mb-lg-0">
                      Personalized advice
                    </p>

                  </div>

                </div>
                <div className="col-12 col-lg-6 mb-6 mb-md-0">

                  {/* Item */}
                  <div className="d-flex">

                    {/* Check */}
                    <span className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                      <Check />
                    </span>

                    {/* Text */}
                    <p className="text-success">
                      Financial aid experts
                    </p>

                  </div>

                  {/* Item */}
                  <div className="d-flex">

                    {/* Check */}
                    <div className="badge badge-icon badge-rounded-circle badge-success-soft mr-1 mr-4">
                      <Check />
                    </div>

                    {/* Text */}
                    <p className="text-success mb-0">
                      Video resources
                    </p>

                  </div>

                </div>
              </div>

            </div>
            <div className="col-12 col-md-6 col-lg-5 order-md-1" data-aos="fade-right">

              {/* Card */}
              <div className="card shadow-light-lg lift lift-lg">

                {/* Image */}
                <img src={illustration} alt="..." className="card-img-top" />

                {/* Body */}
                <div className="card-body">

                  {/* Form */}
                  <div className="mt-6">
                    <a className="btn btn-block btn-success lift" type="submit" href={sample} target="_blank" rel="noopener noreferrer">
                      Download a sample
                    </a>
                  </div>

                </div>

              </div>

            </div>
          </div>
        </div>
      </section>

      {/*  SHAPE
      ================================================== */}
      <div className="position-relative mt-n8">
          <div className="shape shape-bottom shape-fluid-x svg-shim text-gray-200">
            <svg viewBox="0 0 2880 480" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fillRule="evenodd" clipRule="evenodd" d="M2160 0C1440 240 720 240 720 240H0V480H2880V0H2160Z" fill="currentColor"/>
            </svg>
        </div>
      </div>

      {/* PRICING
      ================================================== */}
      <section className="pt-9 pt-md-12 bg-gray-200">
        <div className="container">
          <div className="row justify-content-center pb-5">
            <div className="col-12 col-md-10 col-lg-8 text-center">

              {/* Heading */}
              <h1>
                Simple pricing for all.
              </h1>

              {/* Text */}
              <p className="lead text-gray-700">
                We charge a one-time fee per admissions cycle.
              </p>

            </div>
          </div>
          <div className="row justify-content-center no-gutters">
            <div className="col-12 col-md-6">

              {/* Card */}
              <div className="card rounded-lg shadow-lg mb-6 mb-md-0" style={{zIndex: 1}} data-aos="fade-up">

                {/* Body */}
                <div className="card-body py-6 py-md-8">
                  <div className="row justify-content-center">
                    <div className="col-12 col-xl-9">

                      {/* Price */}
                      <div className="d-flex justify-content-center">
                        <span className="h2 mb-0 mt-2">$</span>
                        <span className="price display-2 mb-0">0</span>
                      </div>

                      {/* Text */}
                      <p className="text-center text-muted mb-6 mb-md-8">
                        for the first 100 users
                      </p>

                      {/* Features */}
                      <div className="d-flex">

                        {/* Check */}
                        <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                          <Check />
                        </div>

                        {/* Text */}
                        <p>
                          Breakdown for each college
                        </p>

                      </div>
                      <div className="d-flex">

                        {/* Check */}
                        <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                          <Check />
                        </div>

                        {/* Text */}
                        <p>
                          Comparison across colleges
                        </p>

                      </div>
                      <div className="d-flex">

                        {/* Check */}
                        <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                          <Check />
                        </div>

                        {/* Text */}
                        <p>
                          Access to financial aid experts
                        </p>

                      </div>
                      <div className="d-flex">

                        {/* Check */}
                        <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                          <Check />
                        </div>

                        {/* Text */}
                        <p>
                          All online
                        </p>

                      </div>
                      <div className="d-flex">

                        {/* Check */}
                        <div className="badge badge-icon badge-rounded-circle badge-success-soft mt-1 mr-4">
                          <Check />
                        </div>

                        {/* Text */}
                        <p className="mb-0">
                          Satisfaction guarantee
                        </p>

                      </div>

                    </div>
                  </div>
                </div>

                {/* Button */}
                <a href="https://kellogg.qualtrics.com/jfe/form/SV_578NDO4HdsYbd4h" className="card-btn btn btn-block btn-lg btn-primary" target="_blank" rel="noopener noreferrer">
                  Sign up now
                </a>

              </div>

            </div>
          </div>
        </div> {/* / .container */}
      </section>

      {/* SHAPE
      ================================================== */}
      <div className="position-relative mt-n15">
        <div className="shape shape-bottom shape-fluid-x svg-shim text-dark">
          <svg viewBox="0 0 2880 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 48H1437.5H2880V0H2160C1442.5 52 720 0 720 0H0V48Z" fill="currentColor"/>
          </svg>
        </div>
      </div>

      {/* FAQ
      ================================================== */}
      <section className="pt-15 bg-dark">
        <div className="container pt-8 pt-md-11">
          <div className="row">
            <div className="col-12 col-md-6">

              {/* Item */}
              <div className="d-flex">

                {/* Badge */}
                <div className="badge badge-lg badge-rounded-circle badge-success">
                  <span>?</span>
                </div>

                <div className="ml-5">

                  {/* Heading */}
                  <h4 className="text-white">
                    How many award letters can I send?
                  </h4>

                  {/* Text */}
                  <p className="text-muted mb-6 mb-md-8">
                    Send all the award letters you have received. That can be as few as 1 or more than 20.
                  </p>

                </div>

              </div>

              {/* Item */}
              <div className="d-flex">

                {/* Badge */}
                <div className="badge badge-lg badge-rounded-circle badge-success">
                  <span>?</span>
                </div>

                <div className="ml-5">

                  {/* Heading */}
                  <h4 className="text-white">
                    Do I need to be a senior in high school?
                  </h4>

                  {/* Text */}
                  <p className="text-muted mb-6 mb-md-0">
                    Yes. We help you once you have been accepted into colleges and receive your award letters.
                  </p>

                </div>

              </div>

            </div>
            <div className="col-12 col-md-6">

              {/* Item */}
              <div className="d-flex">

                {/* Badge */}
                <div className="badge badge-lg badge-rounded-circle badge-success">
                  <span>?</span>
                </div>

                <div className="ml-5">

                  {/* Heading */}
                  <h4 className="text-white">
                    Is there a money back guarantee?
                  </h4>

                  {/* Text */}
                  <p className="text-muted mb-6 mb-md-8">
                    Yes! Our product comes with a satisfaction guarantee. Submit a return and get your money back.
                  </p>

                </div>

              </div>

              {/* Item */}
              <div className="d-flex">

                {/* Badge */}
                <div className="badge badge-lg badge-rounded-circle badge-success">
                  <span>?</span>
                </div>

                <div className="ml-5">

                  {/* Heading */}
                  <h4 className="text-white">
                    Do I have to have all my award letters when I sign up?
                  </h4>

                  {/* Text */}
                  <p className="text-muted mb-6 mb-md-0">
                    No. Keep sending your award letters when you receive them, and we will update your report.
                  </p>

                </div>

              </div>

            </div>
          </div>
        </div>
      </section>

      {/* CTA
      ================================================== */}
      <section className="py-8 py-md-11 bg-dark">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-12 col-md-10 col-lg-8 text-center">

              {/* Heading */}
              <h1 className="display-4 text-white">
                Understand the true cost of college.
              </h1>

              {/* Text */}
              <p className="font-size-lg text-muted mb-6 mb-md-8">
                Stop wasting time trying to figure it out yourself.
                <br />Tilt is faster, easier, and built by experts.
              </p>

              {/* Button */}
              <Link to="/contact" className="btn btn-success lift">
                Contact Us <i className="fe fe-arrow-right"></i>
              </Link>

            </div>
          </div>
        </div>
      </section>

      {/* SHAPE
      ================================================== */}
      <div className="position-relative">
        <div className="shape shape-bottom shape-fluid-x svg-shim text-gray-200">
          <svg viewBox="0 0 2880 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 48H1437.5H2880V0H2160C1442.5 52 720 0 720 0H0V48Z" fill="currentColor"/>
          </svg>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default HomePage;
