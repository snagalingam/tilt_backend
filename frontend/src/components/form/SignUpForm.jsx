import React, { useEffect } from "react";
import { Formik, Form } from "formik";
import * as yup from "yup";
import { useQuery, useMutation } from "@apollo/react-hooks";
import Cookies from "js-cookie";

import TiltButton from "../button/TiltButton";
import FieldSet from "./FieldSet";
import { GET_USERS } from "../../gqlQueries/user";
import { CREATE_USER } from "../../gqlQueries/authentication";

import "./form.scss";
import Axios from "axios";

const csrfToken = Cookies.get("csrftoken");
const headers = { "X-CSRFTOKEN": csrfToken };

const signUpSchema = yup.object().shape({
  firstName: yup.string().required("Please enter you first name"),
  lastName: yup.string().required("Please enter you last name"),
  email: yup
    .string()
    .email("Invalid email")
    .required("Please enter your email"),
  password: yup.string().required("Password is required"),
});

const SignUpForm = ({ setIsAuthenticated }) => {
  const { data, loading, error } = useQuery(GET_USERS);

  const [
    createUser,
    { data: createData, loading: isCreateLoading, error: createHasError },
  ] = useMutation(CREATE_USER, {
    onError: handleError,
  });

  function handleError(error) {
    console.log(error);
  }

  function handleSubmit(values) {
    console.log(values);
    createUser({
      variables: values,
    });
  }

  useEffect(() => {
    if (createData && !isCreateLoading && !createHasError) {
      setIsAuthenticated(true);
    }
  }, [createData]);

  useEffect(() => {
    console.log(`loading: ${loading}`);
    console.log(`error: ${!!error}`);
    console.log(data);
  }, [data]);

  return (
    <Formik
      initialValues={{
        email: "",
        firstName: "",
        lastName: "",
        password: undefined,
      }}
      validationSchema={signUpSchema}
      onSubmit={handleSubmit}
    >
      {({ errors, touched }) => (
        <Form className="sign-up-form form">
          <FieldSet name="email" label="Email" />
          {errors.email && touched.email && <span>{errors.email}</span>}
          <FieldSet name="firstName" label="First Name" />
          {errors.firstName && touched.firstName && (
            <span>{errors.firstName}</span>
          )}
          <FieldSet name="lastName" label="Last Name" />
          {errors.lastName && touched.lastName && (
            <span>{errors.lastName}</span>
          )}
          <FieldSet name="password" label="Password" type="password" />
          {errors.password && touched.password && (
            <span>{errors.password}</span>
          )}

          {/* <FieldSet fieldType="select" name="userType" label="User Type">
            <option value="Student">Student</option>
            <option value="Parent">Parent</option>
            <option value="Counselor">Counselor</option>
          </FieldSet> */}
          <TiltButton type="submit">Sign Up Now</TiltButton>
        </Form>
      )}
    </Formik>
  );
};

export default SignUpForm;
