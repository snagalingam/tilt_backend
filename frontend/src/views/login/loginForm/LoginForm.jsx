import React, { useEffect, useState } from "react";
import { Formik, Form, Field } from "formik";
import { Link } from "react-router-dom";
import { useMutation, gql } from "@apollo/client";
import { Redirect } from "react-router-dom";

import * as yup from "yup";

import "./login-form.scss";

const LOGIN_MUTATION = gql`
  mutation LOGIN_USER($email: String!, $password: String!) {
    loginUser(email: $email, password: $password) {
      user {
        email
      }
    }
  }
`;

const signUpSchema = yup.object().shape({
  email: yup
    .string()
    .email("Invalid email")
    .required("Please enter your email"),
  password: yup.string().required("Password is required"),
});

const FieldSet = ({
  name,
  label,
  fieldType,
  children,
  type,
  errors,
  touched,
}) => (
  <fieldset>
    <label htmlFor={`login-${name}`}>
      {label}
      {name === "password" && (
        <Link to="/reset-password">Forgot Password?</Link>
      )}
    </label>
    <Field as={fieldType} name={name} type={type}>
      {children}
    </Field>
    {errors[name] && touched[name] && (
      <span className="form-error">{errors[name]}</span>
    )}
  </fieldset>
);

const LoginForm = () => {
  // Will move this to Index.js once I figure out how to use Apollo
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loginUser, response] = useMutation(LOGIN_MUTATION);

  function handleSubmit(values) {
    if (values) {
      loginUser({ variables: values });
    }
  }

  useEffect(() => {
    if (response?.data?.loginUser?.user?.email) {
      setIsAuthenticated(true);
    } else {
      // TODO: try again
    }
  }, [response]);

  return (
    <>
      {isAuthenticated ? (
        <Redirect to="/dashboard" />
      ) : (
        <Formik
          initialValues={{
            email: "",
            password: undefined,
          }}
          validationSchema={signUpSchema}
          onSubmit={handleSubmit}
        >
          {(state) => (
            <Form className="login-form">
              <FieldSet name="email" label="Email" {...state} />
              <FieldSet
                name="password"
                label="Password"
                type="password"
                {...state}
              />

              <button>Login</button>
            </Form>
          )}
        </Formik>
      )}
    </>
  );
};

export default LoginForm;
