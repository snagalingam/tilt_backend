import React, { useEffect } from "react";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { Link, Redirect } from "react-router-dom";
import { useMutation, gql } from "@apollo/client";
import * as Yup from "yup";

import logo from "../../img/tilt_logo.png";

const LOGIN_MUTATION = gql`
  mutation LOGIN_MUTATION($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
    }
  }
`;

const Login = () => {
  const BG_LIGHT = "bg-light";

  useEffect(() => {
    document.title = "Tilt: Login";
    document.body.classList.add(BG_LIGHT);

    return () => {
      document.body.classList.remove(BG_LIGHT);
    };
  });

  const [loginMutation, { error: mutationError, data: token }] = useMutation(
    LOGIN_MUTATION
  );
  if (mutationError) {
    console.log(JSON.stringify(mutationError));
  }
  if (token) {
    document.cookie = "token=" + token.tokenAuth.token;
    return <Redirect to="/" />;
  }

  return (
    <div>
      <section>
        <div className="container d-flex flex-column">
          <div className="row align-items-center justify-content-center no-gutters min-vh-100">
            <div className="col-12 col-md-6 col-lg-5 py-8 py-md-11">
              {/* Brand */}
              <div className="row align-items-center justify-content-center mb-2">
                <Link className="mb-5" to="/">
                  <img src={logo} className="navbar-brand-img" alt="..." />
                </Link>
              </div>

              <div className="card card-row shadow-light">
                <div className="row no-gutters">
                  <div className="col-12">
                    <div className="card-body">
                      {/* Heading */}
                      <h3 className="mb-5">Sign in to your account</h3>

                      {/* Form */}
                      <Formik
                        initialValues={{
                          username: "",
                          password: "",
                        }}
                        validationSchema={Yup.object().shape({
                          username: Yup.string().required(
                            "Username is required"
                          ),
                          password: Yup.string()
                            .min(6, "Password must be at least 6 characters")
                            .required("Password is required"),
                        })}
                        onSubmit={(values, { setSubmitting, resetForm }) => {
                          setTimeout(() => {
                            alert(JSON.stringify(values, null, 2));
                            console.log(values);
                            loginMutation({ variables: values });
                            setSubmitting(false);
                            resetForm();
                          }, 400);
                        }}
                      >
                        {({ errors, status, touched }) => (
                          <Form>
                            {/* Email */}
                            <div className="form-group">
                              <label htmlFor="username">Username</label>
                              <Field
                                name="username"
                                type="text"
                                className={
                                  "form-control" +
                                  (errors.username && touched.username
                                    ? " is-invalid"
                                    : "")
                                }
                              />
                              <ErrorMessage
                                name="username"
                                component="div"
                                className="invalid-feedback"
                              />
                            </div>

                            {/* Password */}
                            <div className="form-group">
                              <label htmlFor="password">Password</label>
                              <Field
                                name="password"
                                type="password"
                                className={
                                  "form-control" +
                                  (errors.password && touched.password
                                    ? " is-invalid"
                                    : "")
                                }
                              />
                              <ErrorMessage
                                name="password"
                                component="div"
                                className="invalid-feedback"
                              />
                            </div>

                            {/* Submit */}
                            <button
                              className="btn btn-block btn-primary"
                              type="submit"
                            >
                              Continue
                            </button>
                          </Form>
                        )}
                      </Formik>
                    </div>
                  </div>
                </div>
              </div>

              {/* Text */}
              <p className="mt-5 mb-5 font-size-sm text-center text-muted">
                Don't have an account?{" "}
                <a href="{% url 'account_signup' %}">Sign up</a>.
              </p>

              {/* Text */}
              <div className="col-10 offset-1">
                <div className="container d-flex flex-column">
                  <div className="row align-items-center justify-content-between no-gutters mt-3">
                    <div className="col-4 text-center">
                      <p>
                        <a
                          className="font-size-sm text-center text-muted"
                          href="{% url 'home' %}"
                        >
                          © Tilt
                        </a>
                      </p>
                    </div>
                    <div className="col-4 text-center">
                      <p>
                        <a
                          className="font-size-sm text-center text-muted"
                          href="{% url 'contact' %}"
                        >
                          Contact
                        </a>
                      </p>
                    </div>
                    <div className="col-4 text-center">
                      <p className="font-size-sm text-center text-muted">
                        <a
                          className="font-size-sm text-center text-muted"
                          href="{% url 'privacy-policy' %}"
                        >
                          Privacy
                        </a>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Login;
