import React from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import TiltButton from "../../../components/tiltButton/TiltButton";

import "./contact-us-form.scss";

const contactUsSchema = yup.object().shape({
  firstName: yup.string().required("Please enter your first name"),
  lastName: yup.string().required("Please enter your last name"),
  email: yup
    .string()
    .email("Invalid email")
    .required("Please enter your email"),
  message: yup.string().required("Please enter a message"),
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
    <label htmlFor={`ContactUsForm__${name}`}>{label}</label>
    <Field as={fieldType} name={name} type={type}>
      {children}
    </Field>
    {/* {errors[name] && touched[name] && (
      <span className="form-error">{errors[name]}</span>
    )} */}
  </fieldset>
);

function ContactUsForm() {
  const handleSubmit = (values) => {
    console.log(values);
  };

  return (
    <Formik
      initialValues={{
        email: "",
        firstName: "",
        lastName: "",
        message: "",
      }}
      validationSchema={contactUsSchema}
      onSubmit={handleSubmit}
    >
      {(state) => (
        <Form className="ContactUsForm">
          <div className="ContactUsForm__name-fields">
            <FieldSet name="firstName" label="First Name" {...state} />
            <FieldSet name="lastName" label="Last Name" {...state} />
          </div>
          <FieldSet name="email" label="Email" {...state} />
          <FieldSet
            name="message"
            label="Message"
            {...state}
            fieldType="textarea"
          />

          <TiltButton classes={["purple", "primary"]}>Send</TiltButton>
        </Form>
      )}
    </Formik>
  );
}

export default ContactUsForm;
