import React, { useEffect } from "react";
import { Formik, Form, Field } from "formik";
import { Link } from "react-router-dom";
import { useMutation } from "@apollo/client";
import * as yup from "yup";

import { LOGIN } from "../../../apollo/mutations/account";
import { isLoggedInVar } from "../../../apollo/reactiveVariables/account";

import "./login-form.scss";

const loginSchema = yup.object().shape({
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
  const [loginUser, response] = useMutation(LOGIN);

  function handleSubmit(values) {
    if (values) {
      loginUser({ variables: values });
    }
  }

  useEffect(() => {
    if (response?.data?.loginUser?.user?.email) {
      isLoggedInVar(true);
    } else {
      // TODO: try again
    }
  }, [response]);

  return (
    <Formik
      initialValues={{
        email: "",
        password: undefined,
      }}
      validationSchema={loginSchema}
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
  );
};

export default LoginForm;
