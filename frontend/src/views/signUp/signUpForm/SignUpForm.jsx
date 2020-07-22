import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import "./sign-up-form.scss";

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
  function handleSubmit(values) {
    console.log(values);
  }

  return (
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
      {({ errors, touched }) => (
        <Form className="sign-up-form form">
          <FieldSet
            name="email"
            label="Email"
            errors={errors}
            touched={touched}
          />
          <div className="form-name-fields">
            <FieldSet
              name="firstName"
              label="First Name"
              errors={errors}
              touched={touched}
            />
            <FieldSet
              name="lastName"
              label="Last Name"
              errors={errors}
              touched={touched}
            />
          </div>
          <FieldSet
            name="password1"
            label="Password"
            type="password"
            errors={errors}
            touched={touched}
          />
          <FieldSet
            name="password2"
            label="Confirm Password"
            type="password"
            errors={errors}
            touched={touched}
          />

          <div className="sign-up-terms-of-service">
            <p>
              By signing up, you agree to our Terms of Service and Privacy
              Policy
            </p>
          </div>

          <button>Create Account</button>
        </Form>
      )}
    </Formik>
  );
};

export default SignUpForm;
