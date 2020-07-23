import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import "./reset-password-form.scss";

const signUpSchema = yup.object().shape({
  email: yup
    .string()
    .email("Invalid email")
    .required("Please enter your email"),
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
    <label htmlFor={`reset-password-${name}`}>{label}</label>
    <Field as={fieldType} name={name} type={type}>
      {children}
    </Field>
    {errors[name] && touched[name] && (
      <span className="form-error">{errors[name]}</span>
    )}
  </fieldset>
);

const ResetPasswordForm = ({ handleSubmit }) => {
  return (
    <Formik
      initialValues={{
        email: "",
      }}
      validationSchema={signUpSchema}
      onSubmit={handleSubmit}
    >
      {(state) => (
        <Form className="reset-password-form">
          <FieldSet name="email" label="Email" {...state} />

          <button>Reset Password</button>
        </Form>
      )}
    </Formik>
  );
};

export default ResetPasswordForm;
