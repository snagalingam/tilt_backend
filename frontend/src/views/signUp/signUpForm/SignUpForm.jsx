import React, { useEffect, useState } from "react";
import { Formik, Form, Field } from "formik";
import { Link } from "react-router-dom";
import * as yup from "yup";
import { useMutation } from "@apollo/react-hooks";
import { Redirect } from "react-router-dom";
import gql from "graphql-tag";

import "./sign-up-form.scss";

const SIGNUP_MUTATION = gql`
  mutation CREATE_USER(
    $email: String!
    $firstName: String
    $lastName: String
    $password: String!
  ) {
    createUser(
      email: $email
      firstName: $firstName
      lastName: $lastName
      password: $password
    ) {
      user {
        firstName
        lastName
        email
      }
    }
  }
`;

const signUpSchema = yup.object().shape({
  firstName: yup.string().required("Please enter your first name"),
  lastName: yup.string().required("Please enter your last name"),
  email: yup
    .string()
    .email("Invalid email")
    .required("Please enter your email"),
  password1: yup.string().required("Password is required"),
  password2: yup.string().required("Please confirm your password"),
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
    <label htmlFor={`signup-${name}`}>{label}</label>
    <Field as={fieldType} name={name} type={type}>
      {children}
    </Field>
    {errors[name] && touched[name] && (
      <span className="form-error">{errors[name]}</span>
    )}
  </fieldset>
);

const SignUpForm = () => {
  // Will move this to Index.js once I figure out how to use Apollo
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [createUser, response] = useMutation(SIGNUP_MUTATION);

  function handleSubmit(values) {
    console.log(values);
    createUser({
      variables: {
        firstName: values.firstName,
        lastName: values.lastName,
        email: values.email,
        password: values.password1,
      },
    });
  }

  useEffect(() => {
    if (response?.data?.createUser?.user?.email) {
      setIsAuthenticated(true);
    }
  }, [response]);

  return (
    <>
      {isAuthenticated ? (
        <Redirect to="/" />
      ) : (
        <Formik
          initialValues={{
            email: "",
            firstName: "",
            lastName: "",
            password1: undefined,
            password2: undefined,
          }}
          validationSchema={signUpSchema}
          onSubmit={handleSubmit}
        >
          {(state) => (
            <Form className="sign-up-form">
              <FieldSet name="email" label="Email" {...state} />
              <div className="form-name-fields">
                <FieldSet name="firstName" label="First Name" {...state} />
                <FieldSet name="lastName" label="Last Name" {...state} />
              </div>
              <FieldSet
                name="password1"
                label="Password"
                type="password"
                {...state}
              />
              <FieldSet
                name="password2"
                label="Confirm Password"
                type="password"
                {...state}
              />

              <div className="sign-up-form-footer">
                <p>
                  By signing up, you agree to our{" "}
                  <Link to="/terms-of-service">Terms of Service</Link> and{" "}
                  <Link to="/privacy-policy">Privacy Policy</Link>
                </p>
              </div>

              <button>Create Account</button>
            </Form>
          )}
        </Formik>
      )}
    </>
  );
};

export default SignUpForm;
