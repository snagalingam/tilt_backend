import React, { useEffect } from "react";
import { Formik, Form } from "formik";
import * as yup from "yup";
import { useQuery, useMutation } from "@apollo/react-hooks";

import TiltButton from "../button/TiltButton";
import FieldSet from "./FieldSet";
import { GET_USERS, CREATE_USER } from "../../gqlQueries/user";

import "./form.scss";

const signUpSchema = yup.object().shape({
  firstName: yup.string().required("Please enter you first name"),
  lastName: yup.string().required("Please enter your last name"),
  email: yup
    .string()
    .email("Invalid email")
    .required("Please enter your email"),
});

const SignUpForm = ({ setIsAuthenticated }) => {
  const { data, loading, error } = useQuery(GET_USERS);

  const handleError = (error) => {
    console.log(error);
  };

  const [
    createUser,
    { data: createData, loading: isCreateLoading, error: createHasError },
  ] = useMutation(CREATE_USER, {
    onError: handleError,
  });

  const handleSubmit = (values) => {
    console.log(values);
    createUser({
      variables: values,
    });
  };

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
        firstName: "",
        lastName: "",
        email: "",
        password: undefined,
      }}
      validationSchema={signUpSchema}
      onSubmit={handleSubmit}
    >
      {({ errors, touched }) => (
        <Form className="sign-up-form form">
          <FieldSet name="email" label="Email" />
          <FieldSet name="firstName" label="First Name" />
          <FieldSet name="lastName" label="Last Name" />
          <FieldSet name="password" label="Password" type="password" />
          {/* <FieldSet
            name="confirmPassword"
            label="Confirm Password"
            type="password"
          /> */}
          {/* <FieldSet fieldType="select" name="userType" label="User Type">
            <option value="Student">Student</option>
            <option value="Parent">Parent</option>
            <option value="Counselor">Counselor</option>
          </FieldSet> */}
          <TiltButton type="submit">Sign Up</TiltButton>
        </Form>
      )}
    </Formik>
  );
};

export default SignUpForm;
