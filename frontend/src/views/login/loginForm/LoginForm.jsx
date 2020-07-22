import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import './login-form.scss';

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
    <label htmlFor={`login-${name}`}>{label}</label>
    <Field as={fieldType} name={name} type={type}>
      {children}
    </Field>
    {errors[name] && touched[name] && (
      <span className="form-error">{errors[name]}</span>
    )}
  </fieldset>
);

const LoginForm = () => {
  function handleSubmit(values) {
    console.log(values);
  }

  return (
    <Formik
      initialValues={{
        lastName: "",
        password: undefined,
      }}
      validationSchema={signUpSchema}
      onSubmit={handleSubmit}
    >
      {(state) => (
        <Form className="login-form form">
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
