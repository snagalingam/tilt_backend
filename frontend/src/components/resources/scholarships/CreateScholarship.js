import React, { useEffect } from "react";
import * as Yup from "yup";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { useMutation } from "@apollo/client";

import { CREATE_SCHOLARSHIP } from "../../../apollo/mutations/scholarship";

const CreateScholarship = () => {
  const MIN_DATE = "2020-01-01";
  const [createScholarship, { error: mutationError }] = useMutation(
    CREATE_SCHOLARSHIP
  );
  if (mutationError) {
    console.log(JSON.stringify(mutationError));
  }

  useEffect(() => {
    document.title = "Tilt: Create Scholarship";
  });

  return (
    <section>
      <div className="container d-flex flex-column">
        <div className="row align-items-center justify-content-center no-gutters min-vh-100">
          <div className="col-12 col-md-6 col-lg-6 py-8 py-md-11">
            {/* Heading */}
            <h2 className="mb-0 font-weight-bold text-center">
              New Scholarship
            </h2>

            {/* Text */}
            <p className="mb-6 text-center text-muted">
              Add a new scholarship to our database
            </p>

            <Formik
              initialValues={{
                name: "",
                amount: "",
                deadline: "",
                url: "",
              }}
              validationSchema={Yup.object().shape({
                name: Yup.string().required("Title is required"),
                amount: Yup.number()
                  .typeError(
                    "Amount must be a number without commas (e.g. 3000)"
                  )
                  .required("Amount is required")
                  .positive("Amount should be a postive number"),
                deadline: Yup.date()
                  .typeError(
                    "Deadline must be a date in the format of 2020-01-01"
                  )
                  .required("Deadline is required")
                  .min(MIN_DATE, "Deadline should be in the future"),
                url: Yup.string().required(
                  "Link to scholarship website is required"
                ),
              })}
              onSubmit={(values, { setSubmitting, resetForm }) => {
                setTimeout(() => {
                  alert(JSON.stringify(values, null, 2));
                  console.log(values);
                  createScholarship({ variables: values });
                  setSubmitting(false);
                  resetForm();
                }, 400);
              }}
            >
              {({ errors, status, touched }) => (
                <Form>
                  {/* Name */}
                  <div className="form-group">
                    <label htmlFor="name">Name</label>
                    <Field
                      name="name"
                      type="text"
                      className={
                        "form-control" +
                        (errors.name && touched.name ? " is-invalid" : "")
                      }
                    />
                    <ErrorMessage
                      name="name"
                      component="div"
                      className="invalid-feedback"
                    />
                  </div>

                  {/* Amount */}
                  <div className="form-group">
                    <label htmlFor="amount">Amount</label>
                    <Field
                      name="amount"
                      type="text"
                      className={
                        "form-control" +
                        (errors.amount && touched.amount ? " is-invalid" : "")
                      }
                    />
                    <ErrorMessage
                      name="amount"
                      component="div"
                      className="invalid-feedback"
                    />
                  </div>

                  {/* Deadline */}
                  <div className="form-group">
                    <label htmlFor="deadline">Deadline</label>
                    <Field
                      name="deadline"
                      type="text"
                      className={
                        "form-control" +
                        (errors.deadline && touched.deadline
                          ? " is-invalid"
                          : "")
                      }
                    />
                    <ErrorMessage
                      name="deadline"
                      component="div"
                      className="invalid-feedback"
                    />
                  </div>

                  {/* URL */}
                  <div className="form-group">
                    <label htmlFor="url">Link to Scholarship Website</label>
                    <Field
                      name="url"
                      type="text"
                      className={
                        "form-control" +
                        (errors.url && touched.url ? " is-invalid" : "")
                      }
                    />
                    <ErrorMessage
                      name="url"
                      component="div"
                      className="invalid-feedback"
                    />
                  </div>

                  {/* Submit */}
                  <button className="btn btn-block btn-primary" type="submit">
                    Add to the database!
                  </button>
                </Form>
              )}
            </Formik>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CreateScholarship;
