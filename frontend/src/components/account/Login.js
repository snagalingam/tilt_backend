import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../../img/tilt_logo.png';


const Login = () => {
  const [login, setLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const BG_LIGHT = "bg-light";

  useEffect(() => {
    document.title = 'Tilt: Login';
    document.body.classList.add(BG_LIGHT);
  });

  return (
    <div>
      <section>
        <div class="container d-flex flex-column">
          <div class="row align-items-center justify-content-center no-gutters min-vh-100">
            <div class="col-12 col-md-6 col-lg-5 py-8 py-md-11">

              {/* Brand */}
              <div class="row align-items-center justify-content-center mb-2">
                <Link class="mb-5" to="/">
                  <img src={logo} class="navbar-brand-img" alt="..." />
                </Link>
              </div>

              <div class="card card-row shadow-light">
                <div class="row no-gutters">
                  <div class="col-12">
                    <div class="card-body">

                      {/* Heading */}
                      <h3 class="mb-5">
                        Sign in to your account
                      </h3>

                      {/* Form */}
                      <form class="mb-6" method="post">
                        {% csrf_token %}
                        {{ form|crispy }}

                        {/* Submit */}
                        <button class="btn btn-block btn-primary" type="submit">
                          Continue
                        </button>

                      </form>
                    </div>
                  </div>
                </div>
              </div>

              {/* Text */}
              <p class="mt-5 mb-5 font-size-sm text-center text-muted">
                Don't have an account? <a href="{% url 'account_signup' %}">Sign up</a>.
              </p>

              {/* Text */}
              <div class="col-10 offset-1">
                <div class="container d-flex flex-column">
                  <div class="row align-items-center justify-content-between no-gutters mt-3">
                    <div class="col-4 text-center">
                      <p>
                        <a class="font-size-sm text-center text-muted" href="{% url 'home' %}">
                          © Tilt
                        </a>
                      </p>
                    </div>
                    <div class="col-4 text-center">
                      <p>
                        <a class="font-size-sm text-center text-muted" href="{% url 'contact' %}">
                          Contact
                        </a>
                      </p>
                    </div>
                    <div class="col-4 text-center">
                      <p class="font-size-sm text-center text-muted">
                        <a class="font-size-sm text-center text-muted" href="{% url 'privacy-policy' %}">Privacy</a>
                      </p>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Login;
