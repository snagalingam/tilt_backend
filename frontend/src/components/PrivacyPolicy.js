import React, { useEffect } from 'react';

import Footer from './Footer';
import NavBar from './NavBar';

const PrivacyPolicy = () => {
  useEffect(() => {
    document.title = 'Tilt: Privacy Policy';
  });

  return (
    <div>
      <NavBar classList=" navbar-light bg-white border-bottom" type="boxed" />

      {/* CONTENT
      ================================================== */}
      <section class="pt-8 pt-md-11 pb-8 pb-md-14">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-12 col-md">

              {/* Heading */}
              <h1 class="display-4 mb-2">
                Privacy Policy
              </h1>

              {/* Text */}
              <p class="font-size-lg text-gray-700 mb-md-0">
                Last Updated: 4/13/2020
              </p>

            </div>
            <div class="col-auto">

              {/* Buttons */}
              <button onClick={() => window.print()} class="btn btn-primary-soft">
                Print
              </button>

            </div>
          </div>
          <div class="row">
            <div class="col-12">

              {/* Divider */}
              <hr class="my-6 my-md-8" />

            </div>
          </div>
          <div class="row">
            <div class="col-12 col-md-8">

              {/* Text */}
              <p class="font-size-lg mb-6 mb-md-8">
                At Tilt Access (“Tilt”) protecting your privacy, data, and personal is very important to Us.  For purposes of this Privacy Policy, “We” or “Us” refers to Tilt and “You” and “Your” refers to You, the individual accessing, browsing, or registering to use the Tilt Access services and website. This policy explains how Tilt collects, uses and shares Your personal information in connection with Your use of www.tiltaccess.com (the “Site”) and  any of the services that Tilt may provide now or in the future (the “Services”). This privacy policy ("Privacy Policy") is incorporated by reference into the Tilt Terms of Use.
              </p>

              {/* Section */}
              <h3 class="mb-5">
                Revisions to this Privacy Policy
              </h3>
              <p>
                Any information collected by the Services is covered by the Privacy Policy in effect at the time such information is collected. We may revise this Privacy Policy from time to time. If we make any material changes to this Privacy Policy, we'll notify you of those changes by posting them on the Services or by sending you other notification, and we'll update the "Last Updated" date above to indicate when those changes will become effective.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Information You Provide to Us
              </h3>
              <p>
                <u>Account Information</u>. We receive and store any information you knowingly provide to us. You must create an account in order to use the  Services (the “Account”). Through the registration process and/or through your Account settings, we may collect personal information including your name, email address, phone number), account information and password, User selected University or College, Financial Aid Award Letters, SAT and ACT scores, GPA and demographic or other information (such as your school, gender, age or birthday, pronoun, proposed major and other information about your interests and preferences) (collectively “Personal Information”). Any other information combined with your Personal Information will be treated together as Personal Information.
              </p>
              <p>
                All information entered by you is voluntary and at your own discretion, though certain information is required in order to create an Account or to use the Services. If you provide such information, you consent to the use of that information in accordance with the policies and practices described in this Privacy Policy. Tilt may, send you notifications, information, materials, or other offers through email, text, or other type of notification. Also, we may receive a confirmation when you open an email from us. This confirmation helps us make our communications with you more interesting and improve our Services. If you do not want to receive communications from us, please indicate your preference by contacting us at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a> or by unsubscribing from our emails.
              </p>
              <p>
                <u>Information Collected Through Your School</u>. We will add information to your Account provided by your School. This may include information such as Financial Aid Award Letters, SAT and ACT scores and GPA that the School may provide to us in connection with our Services. Tilt understands that it is important that our partner Schools comply with the Family Education Rights and Privacy Act (“FERPA”) and related regulations. Certain information collected through your School that may be provided to Tilt that is directly related to a student and maintained by your School, may be considered an education record (“education record”) under FERPA.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Information Collected Automatically
              </h3>
              <p>
                Like many website owners and operators, we use automated data collection tools such as Cookies and Web Beacons to collect certain information.  This information is necessary for the adequate performance of the contract between you and us, to enable us to comply with legal obligations and given our legitimate interest in being able to provide and improve the Services.
              </p>
              <p>
                The technologies and information we automatically collect include:
              </p>
              <p>
                <b>"Cookies"</b> are small text files that are placed on your hard drive by a Web server when you access our Services. We may use Cookies to tell us how and when you interact with our Services , to monitor aggregate usage and web traffic routing on our Services, and to customize and improve our Services. Although most browsers automatically accept Cookies, you can change your browser options to stop automatically accepting Cookies or to prompt you before accepting Cookies. However, if you don't accept Cookies, you may not be able to access all portions or features of the Services. Some third-party services providers that we engage may also place their own Cookies on your hard drive. Note that this Privacy Policy covers only our use of Cookies and does not include use of Cookies by such third parties.
              </p>
              <p>
                <b>"Web Beacons"</b> (also known as Web bugs, pixel tags or clear GIFs) are tiny graphics with a unique identifier that may be included on the Tilt Site for several purposes, including to deliver or communicate with Cookies, to track and measure the performance of the Tilt Site, to monitor how many visitors view the Site.
              </p>
              <p>
                <u>Information Related to Use of the Services</u>. Our servers may automatically record certain information about how a person uses the Site (we refer to this information as "Log Data"). Log Data may include information such as a user's Internet Protocol (IP) address, browser type, operating system, the web page that a user was visiting before accessing our Site, the pages or features of the Site to which a user browsed and the time spent on those pages or features, search terms, the links on the Site that a user clicked on and other statistics. We use Log Data to administer the Site and we analyze (and may engage third parties to analyze) Log Data to improve, customize and enhance the Site by expanding their features and functionality and tailoring them to our user's needs and preferences. We may use a person's IP address to generate aggregate, non-identifying information about how the Site is used.
              </p>
              <p>
                <u>Information Sent by Your Device</u>. We collect certain information that your device from which you are using the Site (such as, mobile phone, iPad, computer, etc.) sends when you use the Site, like a device identifier, user settings and the operating system of your device, as well as information about your use of the Site.
              </p>
              <p>
                <u>Location Information</u>. When you use our Site, we may collect and store information about your location by converting your IP address into a rough geo-location or by accessing your mobile device’s GPS coordinates or coarse location if you enable location services on your device. We may use location information to improve and personalize the Site for you.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                How We Use Your Information
              </h3>

              <p>
                <b>Information You Give To Us and Information Provided By Your School.</b> We will use this information:
              </p>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  to provide you with the information and services that you request from us;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  to provide you with information about goods or services we feel may interest you. We will only contact you by electronic means (e-mail or SMS) where you have consented to this, or where we can otherwise lawfully do so.
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  to notify you about changes to the Site and Services;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  to ensure that content from Tilt is presented in the most effective manner for you and for your computer.
                </p>
              </div>

              <p>
                <b>Information Automatically Collected.</b> We will use this information:
              </p>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  to administer Tilt and for internal operations, including troubleshooting, site traffic, data analysis, testing, research, statistical and survey purposes;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  to improve the Site and Services to ensure that content is presented in the most effective manner;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  as part of our efforts to keep the Site and Services safe and secure.
                </p>
              </div>

              <p class="mt-5">
                Our primary goals in collecting information are to provide and improve our Services, to administer your use of the Site and Services (including your Account, if you are an Account holder), and to enable you to enjoy and easily navigate the Site and Services. We will use your Personal Information to:
              </p>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  administer the Site and Services, communicate with you and provide customer support in relation to the Site and Services;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  resolve disputes, collect fees (if any) and troubleshoot problems;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  customize your experience and otherwise measure and improve the Site and Services;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  send you relevant emails and communications (including keeping you informed about our products, offerings and any promotional offers) that might be of interest to you (If we use your personal information to market to you, you will be able to opt-out of such uses);
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  create data used to improve our services and conduct research, statistical and behavioral analysis; and
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  enforce our agreements, terms, conditions, and policies, and send you notices and alerts.
                </p>
              </div>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Information that We Share with Third Parties
              </h3>
              <p>
                First and foremost, you should know that Tilt does not sell or rent your Personal Information to any third-party for any purpose - including for advertising or marketing purposes. Third-party advertising is not permitted on areas where You are required to log in to the Services and Personal Information is never used for behaviorally-targeted advertising (by us or third-parties). Furthermore, we do not share your Personal Information with any third-parties except in the limited circumstances described in this Privacy Policy and as set forth below:
              </p>
              <p>
                <u>Information Shared with Authorized Viewers</u>. We will share your information, including your Personal Information, with individuals such as principals, teachers and school guidance counselors that you have explicitly authorized us to share your information (“Authorized Viewers”).
              </p>
              <p>
                <u>Information Shared with Our Service Providers</u>. We may engage third-party services providers to work with us to administer and provide the Services (e.g. companies that provide us services such as hosting and maintenance of our Site, data storage and management, etc.). These third-party services providers have access to your Personal Information only to the extent needed to perform services on our behalf.
              </p>
              <p>
                <u>Information Shared with Third Parties</u>. From time to time in the course of our business or operations, we may collaborate with Schools, College Preparation Programs, Colleges, Universities or other educational partners to collect, analyze and process data relating to our student users. Such collaboration enables us to grow and improve our Services. Generally, any such data is collected in an aggregated and anonymized format, which means that Personal Information will not be included in any such collected data. Your use of the Site and Services constitutes your consent to the collection and sharing of aggregated, anonymized data from such third parties in the manner described in this paragraph. In the event that any data is collected from third parties in a manner that contains Personal Information, we will take reasonable efforts to ensure that our users have consented to the collection and sharing of such Personal Information.
              </p>
              <p>
                <u>Analytics Services</u>. We use analytics services, including mobile analytics software, to help us understand and improve how the Site and Services are being used. These services may collect, store and use information in order to help us understand things like how often you use the Site and Services, the events that occur within the application, usage, performance data, and from where the application was downloaded.
              </p>
              <p>
                <u>Aggregated Information and Non-identifying Information</u>. We may share aggregated information (information about our users that we combine together so that it no longer identifies or references an individual user) and other non-personally identifiable information, including with users, partners or the press in order to, for example, demonstrate how the Site and Services are used, spot industry trends, or to provide marketing materials for Tilt. Any aggregated information and non-personalized information shared this way will not contain any personal information.
              </p>
              <p>
                <u>Legal Requirements</u>. We may disclose personal information if we have a good faith belief that doing so is necessary to comply with the law, such as complying with a subpoena or other legal process. We may need to disclose personal information where, in good faith, we think it is necessary to protect the rights, property, or safety of Tilt, our employees, our community, or others, or to prevent violations of our Terms of Use or other agreements. This includes, without limitation, exchanging information with other companies and organizations for fraud protection or responding to law enforcement and government requests. Where appropriate, we may notify users about the legal requests, unless (i) providing notice is prohibited by the legal process itself, by court order we receive, or by applicable law; (ii) we believe that providing notice would be futile, ineffective, create a risk of injury or bodily harm to an individual or group, or create or increase a risk of fraud upon Tilt, or its users. In instances where we comply with legal requests without notice for these reasons, we will attempt to notify that user about the request after the fact where appropriate and where we determine in good faith that we are no longer prevented from doing so.
              </p>
              <p>
                <u>Change of Control</u>. In the event that all or a portion of Tilt or its assets are acquired by or merged with a third-party, personal information that we have collected from users would be one of the assets transferred to or acquired by that third-party. This Privacy Policy will continue to apply to your information, and any acquirer would only be able to handle your personal information as per this policy (unless you give consent to a new policy). We will provide you with notice of an acquisition within thirty (30) days following the completion of such a transaction, by posting on our homepage, or by email to your email address that you provided to us. If you do not consent to the use of your personal information by such a successor company, you may request its deletion from the company.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Family Educational Rights and Privacy Act (“FERPA”)
              </h3>
              <p>
                If you are employed by a school or district subject to FERPA, you agree to appoint Tilt as a “school official” as that term is defined in FERPA and as interpreted by the Family Policy Compliance Office, and determine that Tilt has a “legitimate educational interest” for the purpose of delivering the Services in accordance with these Terms. Tilt agrees that it shall be bound by all relevant provisions of FERPA, including operating under the direct control of your school or district with respect to handling of “personally identifiable information” from “education records,” as those terms are defined in FERPA. Tilt further agrees that personally identifiable information from students will not be disclosed to third parties except as required to provide Services to you contemplated in this Agreement. Any third party users will be bound to manage personally identifiable information in compliance with the Privacy Policy, security policies and all applicable laws, and to use the personally identifiable information for the sole and limited purpose of providing the Services to the user.
              </p>
              <p>
                Tilt may use education records that have been de-identified for product development, research or other purposes permitted by applicable law (“de-Identified data”), including:
              </p>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  To demonstrate the effectiveness of the Services, including in our marketing materials; and
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  To develop and improve our educational products.
                </p>
              </div>
              <p>
                Tilt agrees not to attempt to re-identify the de-Identified data and not to transfer the de-Identified data to a third-party unless that party agrees not to attempt re-identification.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Your Choices
              </h3>
              <p>
                We offer you choices regarding the collection, use and sharing of your Personal Information and we'll respect the choices you make. Please note that if you decide not to provide us with the Personal Information that we request, you may not be able to access all of the features of the Services.
              </p>
              <p>
                <u>Opt-Out</u>. We may periodically send you free newsletters, SMS messages and e-mails that directly promote the Site and Services. When you receive such communications from us, you will have the opportunity to "opt-out" (either through your Account or by following the unsubscribe instructions provided in the e-mail you receive). We do need to send you certain communications regarding use of the Services and you will not be able to opt out of those communications – e.g., communications regarding updates to our Terms of Use or this Privacy Policy or communication in connection with your Account.
              </p>
              <p>
                <u>Modifying Your Information</u>. You can access and modify the Personal Information associated with your Account by sending us an email at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a>. If you want us to delete your Personal Information and your Account, please email us at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a> with your request. We'll take steps to delete your information as soon we can, but some information may remain in archived/backup copies for our records or as otherwise required by law.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                How We Protect Your Information
              </h3>
              <p>
                Tilt uses commercially reasonable information security safeguards to protect its databases and servers against risks of loss, unauthorized access, destruction, misuse, modification, or inadvertent or improper disclosure of data.  Tilt segregates certain personally identifiable and other information about your use of Tilt's services into separate databases, some of which can be accessed only by a limited number of employees.  Your Tilt account is protected by a password. You can help us protect against unauthorized access to your account by keeping your username password secret at all times.
              </p>
              <p>
                We restrict access to personal information to authorized Tilt administrators, agents or independent contractors who need to know that information in order to process it for us, and who are subject to strict confidentiality obligations and may be disciplined or terminated if they fail to meet these obligations.
              </p>
              <p>
                <u>Modifying Your Information</u>. You can access and modify the Personal Information associated with your Account by sending us an email at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a>. If you want us to delete your Personal Information and your Account, please email us at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a> with your request. We'll take steps to delete your information as soon we can, but some information may remain in archived/backup copies for our records or as otherwise required by law.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Links to Other Sites
              </h3>
              <p>
                The Tilt Site and Services may contain links to websites and services that are owned or operated by third parties (each, a "Third-party Service"). Any information that you provide on or to a Third-party Service or that is collected by a Third-party Service is provided directly to the owner or operator of the Third-party Service and is subject to the owner's or operator's privacy policy. Tilt is not responsible for the content, privacy or security practices and policies of any Third-party Service.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                International Transfer
              </h3>
              <p>
                Tilt is operated in the United States. If you are located outside of the United States, please be aware that the information we collect about you, including personal information, will be transferred to the United States. By using Tilt, you consent to the transfer, processing and storage of your information, including personal information, in the United States in accordance with this Privacy Policy.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                How Long We Retain Your Personal Information
              </h3>
              <p>
                We will only access, use, and retain Your personal information for the length of time necessary to provide you access to the Services, in accordance with our data retention policies and applicable law.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Our Policy Toward Children
              </h3>
              <p>
                The Tilt Site and Services are not intended for use by children under the age of 13 and does not knowingly collect personal information from children under 13 years of age. If you believe that your child may have provided us with personal information without your consent, you may contact us at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a>. If we learn that we have collected Personal Information of a child under 13 we will take steps to delete such information from our files as soon as possible.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Responding to Do Not Track Signals
              </h3>
              <p>
                Our Site and Services do not have the capability to respond to "Do Not Track" signals received from various web browsers.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Questions
              </h3>
              <p>
                If You have questions or concerns about the terms of this Privacy Policy, please contact Us at hello@tiltaccess.com.
              </p>

            </div>
            <div class="col-12 col-md-4">

              {/* Card */}
              <div class="card shadow-light-lg">
                <div class="card-body">

                  {/* Heading */}
                  <h4 class="text-gray-800">
                    Have a question?
                  </h4>

                  {/* Text */}
                  <p class="font-size-sm mb-5">
                    Not sure exactly what we’re looking for or just want clarification? We’d be happy to chat with you and clear things up for you. Anytime!
                  </p>

                  {/* Heading */}
                  <h6 class="font-weight-bold text-uppercase text-gray-700 mb-2">
                    Call anytime
                  </h6>

                  {/* Text */}
                  <p class="font-size-sm mb-5">
                    <a href="tel:224-306-9466" class="text-reset">(224) 306-9466</a>
                  </p>

                  {/* Heading */}
                  <h6 class="font-weight-bold text-uppercase text-gray-700 mb-2">
                    Email us
                  </h6>

                  {/* Text */}
                  <p class="font-size-sm mb-0">
                    <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a>
                  </p>

                </div>
              </div>

            </div>
          </div>
        </div>
      </section>

      {/* SHAPE
      ================================================== */}
      <div class="position-relative">
        <div class="shape shape-bottom shape-fluid-x svg-shim text-dark">
          <svg viewBox="0 0 2880 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 48H1437.5H2880V0H2160C1442.5 52 720 0 720 0H0V48Z" fill="currentColor"/>
          </svg>
        </div>
      </div>

      <Footer classList=" bg-dark"/>
    </div>
  );
};

export default PrivacyPolicy;
