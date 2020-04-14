import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

import Footer from './Footer';
import NavBar from './NavBar';

const TermsOfService = () => {
  useEffect(() => {
    document.title = 'Tilt: Terms of Use';
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
                Terms of Service
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

              {/* Introduction */}
              <p class="font-size-lg mb-6 mb-md-8">
                Welcome to Tilt Access, LLC! Tilt Access, LLC (“Tilt”) is excited to support students during the college application process by providing students with a personalized task management tool. The following Terms of Service apply when utilizing Tilt’s services (“Services”). Please review the following contract carefully. Violation of the Terms of Service will result in your loss of access to Tilt’s Services.
              </p>
              <p>
                THS AGREEMENT (“AGREEMENT“) IS A LEGAL AGREEMENT BETWEEN YOU (EITHER AN INDIVIDUAL OR ENTITY) (“YOU” or “YOUR”) AND TILT THAT SETS FORTH THE LEGAL TERMS AND CONDITIONS FOR YOUR USE OF THE SERVICES AND ANY OTHER WEBSITE THAT IS OWNED OR OPERATED BY TILT WHICH LINKS TO THIS AGREEMENT OR OTHER SERVICES OFFERED BY TILT FROM TIME TO TIME.
              </p>
              <p>
                Tilt owns and operates the Services.   By accessing the Services, you agree to be bound by these Terms of Use.  In addition, you represent that you are lawfully able to enter into contracts and agree to be bound by these Terms of Use. If you have agreed to these Terms of Use on behalf of your organization, you represent that you have the authority to bind that organization to this Agreement, and that you have the right to upload or authorize upload of student data.  If you do not have the necessary authority, or if you do not agree with these Terms of Use, then you may not use the Services.
              </p>
              <p>
                Tllt reserves the right to change these Terms of Use at any time, however we will provide you with notice prior to making such changes. Your continued use of the Services constitutes your agreement to any updated terms. Should we make material changes to the Terms of Use impacting the Services, we will provide you with notice prior to making such changes and request your consent in accordance with applicable law.  The “last updated” date indicates when these Terms of Use were last revised.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Intellectual Property
              </h3>
              <p>
                You acknowledge that the Services, including all trademarks, service marks and logos, are owned by or licensed to Tilt and are protected by copyright and other intellectual property rights, and that you have no rights to transfer or reproduce the Services, or prepare any derivative works with respect to, or to disclose confidential information pertaining to, the Services.  This Agreement does not transfer or convey any rights of ownership in or related to the Services, or intellectual property rights owned by Tilt to you.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                License
              </h3>
              <p>
                In order to allow Tilt to provide the Services, you hereby grant to Tilt a limited, non-exclusive, sublicensable (as necessary to use the Services), worldwide, royalty-free, and transferable (only to a successor) right and license to (i) use the information, data, content, reviews, comments and other materials uploaded by you to the Services (“User Content”) solely for purposes of furnishing the services provided by the Services to you and in accordance with these Terms  of Use and our Privacy Policy; (ii) use, copy, store, distribute, publicly perform and display, modify, and create derivative works (such as changes we make so that your content works better with our Services) such content as necessary to provide, improve and make the Services available to you and other users, including through any future media in which the Services may be distributed, (iii) use and disclose metrics and analytics regarding the User Content in an aggregate or other non-personally identifiable manner (including, for use in improving our service or in marketing and business development purposes), (iv) use any User Content that has been de-identified for product development, research or other purposes in accordance with applicable laws; and (v) use for other purposes permitted by the Tilt Privacy Policy. You may not modify, copy, distribute, broadcast, transmit, reproduce, publish, license, transfer, sell, scrape, mirror, frame, or otherwise use any information or material obtained from or through the Services. You are solely responsible for obtaining all rights, permissions, and authorizations to provide the User Content for use as contemplated under this Section. You also warrant to Tilt that you will not use the Services for any purpose that are unlawful, prohibited by any applicable regulation or are otherwise inconsistent with this Agreement.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                User Responsibilities
              </h3>
              <p>
                To use the Services you must create an account (the “Account”). In order to create your Account you will be asked to create an account and provide your name, email address, phone number), account information and password, demographic , User selected University or College, Financial Aid Award Letters, SAT, ACT, and GPA, other information (such as your school, race and ethnicity, gender, age or birthday, and other information about your interests and preferences) (collectively “Personal Information”).  You are solely responsible for all activities that occur in connection with your account, and represent that you will comply with these Terms of Use and all applicable laws.  You agree that you will maintain the confidentiality of your account name and password; notify us immediately of any unauthorized access or use of your account, ensure that your account is used at all times in compliance with the Tilt Terms of Use and Privacy Policy and not impersonate another user or provide false information in an attempt to gain access to the Services.
              </p>
              <p>
                We will add information to the Services provided by your School. This may include information such as Financial Aid Award Letters, SAT and ACT scores, GPA and any other information that the School may provide to us in connection with our Services. Tilt understands that it is important that our partner schools comply with the Family Education Rights and Privacy Act (“FERPA”) and related regulations. Certain information collected through your School that may be provided to Tilt that is directly related to a student and maintained by your School, may be considered an education record (“education record”) under FERPA.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Restrictions
              </h3>
              <p>
                You agree that you will not (and will not allow any third party to):
              </p>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Upload, post, e-mail or otherwise transmit any User Content that is unlawful, harmful, threatening, intimidating, abusive, defamatory, obscene, libelous, invasive of another’s privacy, disrespectful, hateful, or racially, ethnically or otherwise objectionable;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Forge headers or otherwise manipulate identifiers in order to disguise the origin of any materials transmitted through the Services;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Upload, post, e-mail or otherwise transmit any materials that you do not have the right to transmit under any law or under contractual relationships;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Upload, post, e-mail or otherwise transmit any material that infringes any patent, trademark, trade secret, copyright or other proprietary rights of any party;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Upload, post, e-mail or otherwise transmit any material that contains software viruses or worms or any other computer code, files or programs designed to disable, interrupt, destroy, redirect, monitor another user’s usage, limit or otherwise inhibit the functionality of any computer software or hardware or telecommunications equipment;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Interfere with or disrupt the Services or servers or networks connected to the Services, or disobey any requirements, procedures, policies or regulations of networks connected to the Services; or
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Intentionally or unintentionally violate any applicable local, state, national or international law or regulation.
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Provide inaccurate information or impersonate another person or entity.
                </p>
              </div>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Privacy
              </h3>
              <p>
                Tilt represents that it will comply with all applicable laws, including those related to protection of personally identifiable information stored and maintained through the Services.
              </p>
              <p>
                We are committed to maintaining your privacy, and maintain a <Link className="text-reset" to="/privacy-policy">Privacy Policy</Link>. All personally identifiable information you provide to us is subject to the Privacy Policy, and acceptance of these Terms of Use constitutes consent to our collection and use of personal  information as described in the Privacy Policy.
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
                Security
              </h3>
              <p>
                Tilt implements and maintains commercially reasonable security practices appropriate to the nature of the personally identifiable information collected and maintained through the Services, in order to protect such information from unauthorized access, destruction, use, modification or disclosure. Such practices include, but are not limited to use of firewalls, encryption and authentication techniques.  The Internet, however, is not perfectly secure, nor are all security risks reasonably foreseeable, and Tilt shall not be responsible for security incidents not reasonably within its control.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                User Content
              </h3>
              <p>
                The Services may contain areas in which you may post reviews or make comments.  By using these areas, you acknowledge and agree that the User Content  you provide in these areas  may be available to other users.  Tilt is not liable for any statements, representations or comments provided by its users in any public forum.  Although Tilt has no obligation to screen, edit or monitor any of the comments posted to its Services, Tilt reserves the right to remove, edit or refuse to post such User Content you provide in these areas in its sole discretion.
              </p>
              <p>
                You may also provide us with suggestions, comments or other feedback (“Feedback“) about our products and services.  We may use Feedback for any purpose without obligation of any kind in connection with our business, including the enhancement of our products and the  Services.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Our Policy Toward Children
              </h3>
              <p>
                The Tilt Services are not intended for use by children under the age of 13 and does not knowingly collect personal information from children under 13 years of age. If you believe that your child may have provided us with personal information without your consent, you may contact us at <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a>. If we learn that we have collected Personal Information  of a child under 13 we will take steps to delete such information from our files as soon as possible.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Changes to Site
              </h3>
              <p>
                Tilt may add, change, discontinue or remove any portion of the Services at any time, without notice.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Links
              </h3>
              <p>
                The Services may contain links to third party websites, including social networking websites.  These links are provided for your convenience, and inclusion of links on the Services does not suggest an endorsement.  We are not responsible for the contents or transmission of any linked site or for ensuring that the linked sites are error and virus free.  Linked sites are subject to their own terms of use and privacy policies, and we encourage you to read them.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Indemnification
              </h3>
              <p>
                To the extent permissible by law, you will defend and indemnify Tilt and hold it and its affiliates, officers, directors, managers, employees, agents, vendors, merchants sponsors, providers, and licensors harmless from any and all claims, actions, demands, proceedings, losses, deficiencies, damages, liabilities, costs, and expenses (including but not limited to reasonable attorneys’ fees and all related costs and expenses) incurred by them as a result of any claim, judgment, or adjudication related to or arising directly or indirectly from any or all of the following: (i) your use of the Services; (ii) any information you submit, post, or transmit through the Services; (iii) breach of any of your obligations, representations, or warranties in these Terms of Use; or (iv) your violation of any rights of another person.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                DISCLAIMER OF WARRANTIES
              </h3>
              <p>
                THE SERVICES IS PROVIDED “AS IS” AND “AS-AVAILABLE,” WITH ALL FAULTS, AND WITHOUT WARRANTY OF ANY KIND. EXCEPT FOR ANY EXPRESS WARRANTY PROVIDED HEREIN, TILT AND ITS LICENSORS AND SUPPLIERS DISCLAIM ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, QUIET ENJOYMENT, QUALITY OF INFORMATION, OR TITLE/NON-INFRINGEMENT, AND ALL SUCH WARRANTIES ARE HEREBY SPECIFICALLY DISCLAIMED.
              </p>
              <p>
                TILT ASSUMES NO RESPONSIBILITY FOR ANY ERRORS OR OMISSIONS ON THE TILT PLAFORM, ANY FAILURES, DELAYS OR INTERRUPTIONS IN THE SERVICES’ ACCESSIBILITY, ANY LOSSES OR DAMAGES ARISING FROM THE USE OF THE SERVICES, ANY CONDUCT BY OTHER USERS ON THE SERVICES, OR UNAUTHORIZED ACCESS TO OR USE OF THE SERVICES
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                LIMITATION OF LIABILITY
              </h3>
              <p>
                YOU UNDERSTAND AND AGREE THAT TILTWILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES, INCLUDING, BUT NOT LIMITED TO, DAMAGES FOR LOSS OF PRODUCTS, USE, DATA OR OTHER INTANGIBLE LOSSES, EVEN IF TILT HAS BEEN ADVISED OF THE POSSIBILITIES OF THOSE DAMAGES, RESULTING FROM YOUR USE OR INABILITY TO USE THE SERVICES, SERVICES, CONTENT OR SOFTWARE, THE COST OF OBTAINING SUBSTITUTE SERVICES RESULTING FROM ANY LOSS OF DATA, INFORMATION, ENTERED INTO THROUGH THE SERVICES, OR STATEMENTS OR CONDUCT OF ANY THIRD PARTY, OR ANY OTHER MATTER RELATED TO THE SERVICES, CONTENT OR SOFTWARE. YOU UNDERSTAND AND AGREE THAT YOUR USE OF THE SERVICES IS PREDICATED UPON YOUR WAIVER OF ANY RIGHT TO SUE TILT OR ITS AFFILIATES DIRECTLY OR TO PARTICIPATE IN A CLASS ACTION SUIT FOR ANY LOSSES OR DAMAGES RESULTING FROM YOUR USE OF THE SERVICES.
              </p>
              <p>
                CERTAIN STATE JURISDICTIONS DO NOT ALLOW LIMITATIONS ON IMPLIED WARRANTIES OR THE EXCLUSION OR LIMITATION OF CERTAIN DAMAGES. IF THESE LAWS APPLY TO YOU, SOME OR ALL OF THE ABOVE DISCLAIMERS, EXCLUSIONS, OR LIMITATIONS MAY NOT APPLY TO YOU, AND YOU MIGHT HAVE ADDITIONAL RIGHTS.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Notices
              </h3>
              <p>
                We will provide you any notices regarding the Services by posting the notice on the Services, as applicable, or by sending to you by e-mail to the email address you maintain as part of your account.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Applicable Law; Jurisdiction and Venue
              </h3>
              <p>
                We control the Services from our offices within the United States. We make no representation that the Services is appropriate, legal or available for use in other locations. You may not use or export the Content in violation of United States export laws and regulations. Any claim relating to the Services shall be governed by the laws of the State of Illinois, without reference to its choice of law provisions. If there is a dispute between you and us, you expressly agree that exclusive jurisdiction and venue reside in the state and federal courts located in Chicago, IL.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Severability
              </h3>
              <p>
                If any of the part of these Terms of Use are determined to be invalid or unenforceable pursuant to applicable law, they will be severable from the remainder of these Terms of Use and will not cause the invalidity or unenforceability of the remainder of these Terms of Use.
              </p>

              {/* Section */}
              <h3 class="mt-5 mb-5">
                Digital Millennium Copyright Act
              </h3>
              <p>
                If you believe that materials hosted by Tilt infringe your copyright, you (or your agent) may notice requesting that the materials be removed. Notice must be provided in writing and must include the following information:
              </p>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  A signature of the person authorized to act on behalf of the owner of the copyright interest;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Identification  of the copyrighted work that you claim has been infringed
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  The location of the work you claim is infringing (e.g., URL) or enough detail that we may find it;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  Your name, address, telephone number, and e-mail address;
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  A statement by you that you have a good faith belief that the disputed use is not authorized by the copyright owner, its agent, or the law; and
                </p>
              </div>
              <div class="d-flex">
                <span class="badge badge-rounded-circle badge-primary-soft mt-1 mr-4">
                  <i class="fe"></i>
                </span>
                <p>
                  A statement, made under penalty of perjury, that the information in your notice is accurate and that you are the copyright owner or authorized to act on the copyright owner's behalf.
                </p>
              </div>
              <p>
                Notices should be sent to: <a href="mailto:hello@tiltaccess.com" class="text-reset">hello@tiltaccess.com</a>.
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

export default TermsOfService;
