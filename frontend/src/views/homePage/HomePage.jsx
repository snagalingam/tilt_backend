import React, { useEffect } from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";
import CheckCircleIcon from "@material-ui/icons/CheckCircle";

import Banner from "../../components/banner/Banner";
import CommunityCard from "./communityCard/CommunityCard";
import FaqSection from "./faqSection/FaqSection";
import Footer from "../../components/footer/Footer";
import NavBar from "../../components/navBar/NavBar";
import Testimonial from "./testimonial/Testimonial";
import TiltButton from "../../components/tiltButton/TiltButton";

import "./home-page.scss";
import dog from "../../img/dog.png";
import butler from "../../img/clients/butler.svg";
import hfs from "../../img/clients/hfs.svg";
import solorio from "../../img/clients/solorio.svg";
import westinghouse from "../../img/clients/westinghouse.svg";

const emailSchema = yup.object().shape({
  email: yup.string().email().required("Please enter a valid email"),
});

const HomePage = () => {
  function handleSubmit(values) {
    console.log(values);
  }

  useEffect(() => {
    document.title = "Financial aid help for high school students - Tilt";
  }, []);

  return (
    <>
      <NavBar />
      <div className="home-page-container">
        <Banner />

        <div className="tilt-clients">
          <h2>Our Clients</h2>
          <div className="client-logos">
            <div className="butler-logo">
              <img src={butler} alt="butler logo" />
            </div>
            <div>
              <img src={hfs} className="hfs-logo" alt="hfs logo" />
            </div>
            <div>
              <img src={solorio} className="solorio-logo" alt="solorio logo" />
            </div>
            <div>
              <img
                src={westinghouse}
                className="westinghouse-logo"
                alt="westinghouse logo"
              />
            </div>
          </div>
        </div>

        <div className="tilt-join">
          <div className="tilt-join-header">
            <h2>Join the Tilt community</h2>
          </div>
          <div className="community-cards">
            <CommunityCard
              step="1"
              img="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAACiCAMAAAD84hF6AAABa1BMVEUAoZvoso48PDr9/f1f0dwagqcol7Xz9Pbdo4sAnZeYzcvf5+rrtpcApJ5Wz9ruyLNOu88dHRs9OTc+NjQvLy02NjQ9OTQAfKP5/f1Ct8znrogYhaty1uDmsI3ttpHko4rl9/nU8vWc4eiB2uOt5uzH7vK56u/hqYyP3ubh9vgrKyk3Q0AvNDTw+vuz6O16enlaWlgqYV4xUk8uWVVCQj+9vbzS0tHf6e0Qj4o4Qj80SkchdG8Vh4Edena51+JaUEg/qsNtbWuBgYCenpyurq1SUlDswqYidJAoaYEzUVonaWVaobyYwtM3SU94sMcsYHIshp7NsJCohW6W1eFrxdUvnbmUlJO/o43So4tPoZaMopHy2Me4o4347OSUv9EtXW97sKCvrZHK4Oh2saa+lnsveYzKwbCeuaqIcF9tXVFFhpFCmqmYwMeViHOerJN1nKNTubWUdWaCjH21ineioo/gzsbetqV0wsAAAAC6blrpAAAYlElEQVR4nO2djV8aR7fHhUWQoqgIAeVFgd0FDaBJVNSkaIzaNlhSY1Qw0Rqb3ie5vTe3uUn79M+/Z2Zf2J3Zl9ndUdP76fk8nzRqHl2+/s7M+Z0zu4yM/BOeI/7NXV/B3zL+weYr/sHmK/7B5iu4Y5uYiMfhDyWGnzR+9P8gOGObiD/e2ty8v/XwwfPH3z55srEBDEcmRh49Qh/HAVxcYcj1h95B8MU2sbE1kwqHw6lUagZHKry59fDRI+Xj5/F4/D4gffRg4+/OjS+2+BaCZg5Apn9y8z7+xMwDJEM6l/8+wRXbxPMZipplpDQdqrn8t2PIV20WYnOCp+UyILyvMVSXw6+cIVdscS/Q7BgCxPtfvQ65YtsIgM2SYYrS4VeCkC82fWnbDIfvKeEpbR0ZmtbDO95TeGKbeKJiS/04mv3uu++/f/HzDz/8+OOmTjA4QpMOt+5OhzeD7Yf86OhoXgn42+h3APHFzz9jhhrEe/wYmtZDkw75vThzcMX2rYbtZwzLGEOEQx3e13XIIZWHOgwjHT4y2JQb0CFXbI9VbPdobBYMMUVjLnOEqMtQ1SEwNNU2QV8qV2zP1dd774UZWxaFM0MtlVUd8kQYpsvDJyMBwXHF9kDD9r0JW7Z73e50R0e7XVeMQxlmLXXIhSFA3HwSjBvXAuSRhu07MzWhfd0UutlOOzua7bXzo4edw143OxpV1jqMkVmHfNbD1My3gbjxwnb19u3V4GFGvSgztk4zm833RrPX14DtsDmaz7XbC0JH+bjbiXYve91uVN0w7JLZuBxa6NB7cRO/e2zxXw5KpVLo3bbKjcSG9ZRtdxC2hWw+18uOdoUuEIQvLmQPhVxOEC6vLwHZYc92EbRAGI3+9NNPv/764oW+Hs6wMpx5HERufLBNTE6GIEo1lZvppWe7uWanl1exQaZGIWERu64Qzeabl/CpfLTbzR+CKHtC146VVUS1OMF/GhgactmaYerh3WP7DwVbqNTHl7RpfnGQiAvC9eho8zCLM7UrXHa7nVwUqa6Xy6NPoYjmupisH2x0YIS6DlP3yJZWaivIC+aBLf6vycmDUKiIuL1vwCX9SGDLYhnlmz0lU7tCMyfAB9n2Yfa6kwVseGWDv/eazgUfEXkHbKQOf9382tT2y+Tk5HhIiX4DW1LTi+vlISeFHl7SsguHSGFRrLzOdR4Ulm3D2pa7zEIy51hWNm/Y9CCxPbpbbPEBUJsMabGNLKlJa1B/HF62c9Fsu50H1fWyl808bBMgr17zsA3/oHkIa1sU/ulC2xM1b9jILeHB3WLD1DSxhUofMuF7PxDVbqeZa/ewmppCBzbTNmIJwsrnBNg90a6AqrdRlLQ3hu0nYmeYeX6n2IDagQ5NxfYz6a3QygX/jR52evCfw2uECOmsnYN/mRcu1ZoN8bsxbITDuNsC5LwUMgXG9sJuYVftAPpyFJUkl0he0RwKQJn3uLQ5baTu2ALZhGDYBkcENby2zfzn7M7OzgnsYbgmtUGB0xJ/DYq23iXIMH/dvTlsv5LYArnSANiu3hbnKGo1dEW/TRliVmMYVQ2mFUJFht6gBcQWaMTtG9vVUYliBjn6soGwzc5OWQfJ0KmjxBfbC6LeTW0EoOYb21taaEqOgrtK/9fx8SsIREkJN4h5eyFyw0Y2ne7CytNrmiK2d8gkpBOCgCrY5sJiWZLEYwRxyo3hLCVE95z1gu0HogDZvH1sFjuBGh+Qlc/EBCpyTQyxhRkyQjQtiFYMA2BL3Q9CzR82O2qK2MKrFthMCEGIi+Wy1BFVhrNuDHfMyawtiF6w/UhgC+TkfWGz1VpI6RvtO1Oz1qEskjq0hqgmMyKRP/GA7T6xIwSypH6wkRWueRuFHF3xhI0QorIg6snsuqlgJYIUT1wYkk4+kCX1g81OaqHaKr6izFMjiNZxGUvKF8TmgmlBdGc4a8uQ2EeDWVIf2N7aiu2D0trNLBte+eLxQlloCuVj5cOFnH8d5mySmUmIlJMPZEl9YLPTWum/G8oVpU+Nr/b4eEE6Ppbk8nG5KS4i6fkSHgnRbkG0Y/gbV0vqHdtHG7HNfdRm8ulnhtfXbJYhxY5b0iv4U5IAW/nV8eLxcXNR5IFPYQgQEUMqmQ0QSWz3bhlb0YbaW/0EanrP8JLKr15BwSu15Fegt5yA/tc8lkWMkRc2AiLokF4QfyO9VbD5sldsV5ZiK5XOhzP5pTXzqwB2oLny8aL0SjpeFESkOsAmSjeDjWCoJvP/pAlsgSypZ2xHllI7GowMZ/LpddsXgQaiOQn2R2lBBIK3GM8IbOFbxTaYs6B2dIW/9tAV2x3GKYktkCX1is2i+jjSvqYdE88k7pqRRexmzNSCOXmP2AZWWtO+k1aHI0taiRSq1XqlJUnlxYVmLue7XOMVTwlswSypR2yW1cdA/U7aFe3HhGYygiKJAv5bKABCUZSBYbN5NwhXzNhSD28Tm1X1MXeufE0/XQ+WVME2FY3uRLRIqqFBBIa3CXGf2EiDOXlv2K6sNoSSmqUbakGJLOkCwraTv+z08q8iVpE0C7EFEBeA4Y1Ri60S2II5eW/YrDtGRfw1/Zg4wlYGIsnRa7jey6glNhqhArFahwVRVhdEjtgSBLaATt4TtoFNJxwvbvox8cyuIEjAYKeLrredBxqyXEm60jNDxDqsVjSGQYW4TuwIAZ28J2w2vY/SFcamW1Jw8jLC1lOwwV+lQqReLdQLkUKkVSkgJXqDGDEsiItIiN6xEWVbQCfvCZslNGTiMbbnBiffglc6NdoW1CSVKoWWXGnVZakuioVWpSoWxDorOXuGaEH0i+32jjyfW20IKN5gbJolRU5eVLYEdORjCl5luVKQWmK1UG5VKmJFksSKLFa9Y7NgmGQ0tmt3h61vQ00peCd0SwpOXlnKZqPRE/wXWKUK1UKrWmkVWq2KXG8V5FYhIDYVXoUN2x6JLZgl9YDtquaMzWhJy2qla1rDtA+qhUKkWg2qNvV7imzYSCcfsAHiAVvfptOmViATW0Ynr/YNxUodQRpuj7wjKbNh2+Xr5Nmxnc87YxvRJmqkk1dmAGUJ1jXMMMmTIevatszXybNj64/ZUQuF8DfSL8lxuKz3DYEhByEmy2zYCCcfcLjMjm0wb48Nqy2ujYZQA2QB1Qau9RWeAWgMDTr0wDDJ2OuknPwt3ar2Zd52R1Cw6Td878PKpvU+hkWqe/dIH6RoC2KEhSFb4Rbj7OSZsfXH7LGhnfTjmTruQzP5ReNrNZolnaGLEHP6gogZRuyFyDb+4u3kWbFBjtruCKHQx7faqZmhk49ETvL5/BSRUybXrnaP3F27w4LI5rNipCUN6ORZsZ07YiuVtPMfQycfiXav24ejU6Q8LHRo6B65G06UywtljSHjRpogq92ATp4V25sxJ2yh0BAbcvII22wUXe8hsqQFFv+ZJCAiIS7wamPydvKs2PpjDvUHxvZJw/ZMcfInl+h6cd8IPCjqeoBpqLJaKkMuGxn6xba2RGALaEkZscXHHHYEBdt7DdueYkmVvtE1YKuK9booVVtypCL5cqLmdnqlpS6IXrCR3up2sMGO4IZNPW6EZ/IV3De6hkqkuwPYWnVZrsqiWBElP9QcGIqM7EgnH9SSMmI7d8UW+qBeEbKkeC2bHe328rglLsqFllSV5LrMAZuZIaMlxU4+jSKj/HZvB9sXV2zFbSM2vCwld3amVIGgP6BwqPvoTXLBdgqw9tfW1vaenS6jyjeoJWXEdua2kQ6xISffJDsfN9D7ULCxO/mMdupuHR0Tvx1sfXdsWh2uHxNXzZJWpN5I98iDk0c7PL60RDjwTJ4RG2ykbthq2mq7b90AUU+dyYQOA0JkxQZOHnb43f2Vp6doiBXYybNhg43UpWwL9bUcXVGU5vgqtGO4WgvOvxDZnXx6LQbbQSadgNI3sJNnw3Y176o2oyXNVXB9JbKNic0MI94Ysjv59HoCb6IxqOECO3k2bOeuahs6+WW1AZI0FViIIdPBGew4pWEyO3ePCmzY0HKWWccOaxVhC+zk2bC51x8mJ1/WDs7MDhchwrUzjdq17pF9G7PAVu6imXwmsY4c1j4qfQM7eTZsb9y9FenkIyf5w8Ou5QGQJCHEFlsbU2iqbUzDglhnooadPMhsCS+9p+ngTp4N25k3S4pn8nlYrXPdHStuFhRVHXptYzJ6KwUbcliw9O5mgjt5Nmx9BmyZITZRb4B0UAOkitXHtMTTCyJTG9MtkJPfF54tZTLpZVTDBbvhmxnbmDs2zclrM/noIbpe1ABJgiWFercCICIF3D5iLDTIDpx2CM47Q9AZZGdi+enK6hqq4YLO5NmwDRiwaY8gUywp6lKiTa53gk6ASFVZroqiLNbhb1K1UmHDZguxqi2IrPfRwHI2vH8OarhUUG/Fhs29bCvplhSw4XMK0W6n00WntCpQwkkVWRblSEuuiJVKuRz4/IfGkPHAESxnw7s1kQu8FWwM1W5IHw0lhJxCZSeaP1FfJTr0IVYrEdQ+KtclX2qzpOdhJp9ZWd59tre2jnpIm0Gp8cJW1KghJy9aGU51W2hJEU6nZiKeLClwy6TT6aV0msNMng3buTu2WsPo5NHNs9SYWIFY4HNAS8WGZ/IXrw8ODl5fOGAjh8uBnTwTti/u2PoaNuKGb/N4bljpc8KG1rbXobnx8fFi6LUtNWq4HNjJs2Fz7xsZnbx9qDdxI4beXbtVwFb6em4cPQlt8mBu0hZbmMAW2MkzYXvjis3k5IUy04hT73wEOATXFC5Uaoibnd6o4XJgJ8+E7cwdm9HJL6oFrTLi9ODaF7UzH6wMwclPhia1CM3ZrG8Jckoa2MkzYQNv5dY3opw8uNIkbZb0W9dcIDIegisIQmhcx3YwN2797dZJbIGdPC9s7w0zeXRTAlh5u4MzEW9nPgiGxl9FsmrIUSw36zTlPpPnh80wXEZOfirbaTY7+OCMTaZZunaWBXF4CK5a1jcEBVvIWm57BLbUk6DUWLChAYwbNn0mv644+RN8lAFZ0ojcYljbDTr0cAhOMGMbt5Eb95k8E7aBO7aQabgMLz/aQdfbiaKjDNVWoZD0UuUaXXu9Ljrdy/t6LnRgUFvowAobdZ98YEvKhG3eFZtpJo+8UxS329CdQ9WyDD6+LomBzs1EbBbEi7nhnoCfx2q1mXK+4ZsjNoOTFxAdfHDmGq1t9UoStXn43PdibsHJgA1+uMrtAF2IZZYSp+uDz+SZsP3ijq1mmMkrDZBZ9F4csxHFhLYqVanCssR5hAhOHv948KTao3+tspTzffKM2M7dsWnDZeTkcwVl75walh83cf+Liu2AvBQ6S2MrxI4Q3MmzYDtz3xLeqb9P3Awscz2v4BSLeE8whUWWcj9dz4QNL23O2Eq0kze4drp7xCsW8J5gxkYberIBEuwh7KzYkJFnxrZMXbRgfPQa7nzwEyKaJYwT10JXvAmi/ODg5N2xXc0zYNOd/CkNjYom0fnwLUQ8k58k5UYtbrzvk2fC1h9jwGY8Jt6s6mc+mLpH/g/BYWxUllJ7KffT9QzYvihic+kbGYfL8vDgTMR05oPFtXtaEKv4/0RmKSU33jd8M2AbjDFQM2BTnTyak57oBYhpxGl4RoWLEJtuh+CUEyBUlpKbAoWNw/uMu2A7Y6FGz+Qj0ejhpT7vM4eh8WG4/c9FhwJxCA5/D+WG7wtq8k3IjbSkwWfybthwpet6tn44k8+oM/mdLnBYQP02F0dFdY88HILTpn1/Er9VsnQjH90WfCbvgi3OsB3gMM7kEbY8boBcnkSSlWqlynrsw8K1s9wxdEFeIFGDkE6eQwPEGdubeZYUJZw8aoDk0eON8H1q1YpcRwdA6qA7ZUbK9tAZrbJjOQT3J5EOhNxISxrsIezu2H5hS1HzTB47edylzHWRlS9XJLkiFdDzUsroVpiCXK+KnpshVguiDvCC/M2a5Ube8L3F4W1xnbD1mfaDkHkm38RI8r3rDj5LmZQLoliQk6KULKCDM2ILHT/ySs1SiMMTqJTcTJsC/5m8I7YvrGLTZ/LIyTeVl3aSz+snKSE9k2I9WSjLBXTjVUsORG2ITz9vdEFepbHkvYGZvBO2AYOrUsLk5HN1yxK1AvSUR/gU3HZX79iEP4mcMMqNvOGbw0zeFtvvrCWbGdsuWtIWyxbjuZtoHw1PBV4Qv15jyXsDM3kbbPHfY9K/mFPUPFw2xnDEeSMtOMOmSsrNUPLewEzeBtvEYiwW+4NVbGYnbxv6O0jwuu2qYPjmk8Qv2FCD3MBM3hpb/JsYios/2cQWqhmdPGNo7yARoHtUNXw7MksNNQjrTH4wGATCBimqxh9MYquN6ZZ0L+by7jk2OsxZHoJzYUhgIzYFXW7UTF6zpIOrqyGoj0X05tFH5/6xjSxq2GIXB3ZPCDRS07FBvbu/8nR593RvbX09kfCDkFwQ7XVovgWGWtx0uVk/hP3qqBgqzc33v+BXfFVUHrtZKhXZJEdji38jxIbxmoHa2LZhj89k0CHZpaWldAYzPH22t7a2noj50qF+5oO8DzVCPijwNbmg6DWI1UPYB0fKm8IVx+bPRszvZlBi4kZgg7T/PWYKZ8EVcZXygTTLZob4xn7EcBcx9K9D8728VdPp+gvqiV9ayWsxkx8+Gr02Nv+FeFZp0Tu2+OP4RDlGxOuQHbhiTWmRaDupcygIzTpc961DMqhdX5Ob5uQbcJGNDFjSuPFNH4Bb3Pyk9NJHr9gmHs9s/SKQ2KwFV6upzFCsOgNz1OGqUYf+EdLb/qQRW2P1/bt+//OHRnjL9IxvSJcz4q0zxhnS1IhtYiMVTqV3ExS32OtxGtyYIT6H7dKUlSGWYRAdUr5ULXnxTL6x+gl2SrQOfw4/GnlrfDE1ykCW3npUG36YaXp/jUlwRY1ZrVYM9bcbKDKB6BkYIh1q2zJimHDVYYzOUiw3NJNvvK+VNEafHkwckS+DAM4gNwM2/fHWS8sWgrugBIe51ZRrLZX6715+ev/hw/Y2JGyGL0MrHbJkaQhjWw033pWG1zz/v8TbF9QobuNvvGDT3/AgnF61EFyMHBHBNdQMV1BCAZ8s1vrv3r1UGK6uKgS5IHTRIZ2luORNhBsvS8ZrHiOehFukTOS4u9wM2B4a3q+NUXB2UVID9tr+588vP+k6TM1ApCA4IFT25bRe29BNLlTyrqe3TUyKJKQi1R8bH3dd3XRs+oP71cta3csxCM4tiobtduw8vrHx5NvHz58/erh1X0WIIQZliHW49JlqPCC5rS+9Nz94v0Zyg5qgRqjNVW46tg3yUpaeJiy2BmbBkdDmz9ClTGgxElcZPkAMN8OpwDrMfKAXt/7+05XGZ+KTNbd+2Li73DRs+pPUDdcR3qP15kVwRmh9C5OsIyQZ+pPhap+SW+lDI9P4TEJy7SMCNzZsRIqqkX7qf4UzKW3si8tlODBMzTDqsPGSxvYuE6axUcubBTYXq6Bii29aXolvwZnWtPk3HjpZJoiY4ROdYXjI0Opqt2kR1bYBG7VVuKXpuKvcFGwWKaoLbt37CmeGduYZmhVBSoeGbVm9+MY7SkTFz43GJ1paDNiu3LFZp6gquMwzC8E59JNMzGBRc/75fiFSOgSC6ff0E7zHthvvLRg591/HXTcFjM0mRTXBrbALzsyMOzR7hApD+jH7tZeNbcaRCMHNMUcQNvsUZRdcEdxBzcwM0vMmoZGBANJv6lAc287QBR0LNsdNAbA5paij4Az2vjhGxe1CU2JA5+P8+ca5w9P37bEdOf0gwOacoqrg0qeWgtPAkdig5Ai2EfiMN/MkgVp/cO7wXg/22ByzFLA9ZKoqnQVnxgbFLYczZH5iQAlLuTLeWQrYGGvxzJKF4Np/KIIz1bbeyzR+cUYJC18U7ywFbGzUkOD2KcEl2utYcBq2+fk3V3ckNCWuLDYFFD6wOWWpF2ywwu0S1BKJNhacho11PHtzQRvTmt8sdXgxnrCRHfMEjnbiYE7V2t1TG6G3zSLVKmLE5pClHrEhwen2vp1QubX/ULD1b4+OfdByQ1WlR2pKltqfsfGKzSi4hB7txJ/zILar24NjH96rNKsoAjXlHUQtwzs2AKcIrp0wcAPBzbtPLm4lnN7IjD2cSxA/2NCIxiQ2VXB3uoUOw+Ft8zxis1/cfGEDcMuJdoKI9jcczttxiLjnKs0Om33TzSc22BqeUdwS/75FOA5Bl7x+sV3Z/Qi/2NLTfz1dJ8B1bhGNU/DLUtvFzSe2zPT09F/ThOC+jhy17IP4xGa7uPnEtjSN4q8Vo+D+/ZVsCZClN764+cOWnlYCBKdvDV9Lio5wytIbwDathy649teSoiNW7SPPUcTYbAteX9iWpg3cpk+x4L6eFB3hs5eOOw1ifLmEaVP8tb/2VaXoCMcsPbD5AfFv/g8UvUk9v0nBCwAAAABJRU5ErkJggg=="
              header="Sign up for free"
              text="We will always provide our services free of charge to students and families."
            />
            <CommunityCard
              step="2"
              img="https://specials-images.forbesimg.com/imageserve/1157006349/960x0.jpg?fit=scale"
              header="Apply to affordable colleges"
              text="We will find you colleges that are likely to offer you the most money."
            />
            <CommunityCard
              step="3"
              img="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIQEBISEhMVEBIQDxYQFxUQEBASFREQFRUXFhcVFxUYHSggGhonGxUXITEhJiktLi4uFx8zODMsNygtLisBCgoKDg0OGhAQGysiICUtLTAtMC4tLTEuLystLS0tMistMS0tKy0tLS0tLS0tLS0uLS8tLS0tLy0tLS0tLS0tLf/AABEIALYBFQMBEQACEQEDEQH/xAAbAAEAAQUBAAAAAAAAAAAAAAAABAECAwUGB//EADsQAAIBAgMEBwYEBQUBAAAAAAABAgMRBBIhBTFBUQYyYXGBkaETIkKxwdEUUmJyB4KS4fAzQ1Nz8SP/xAAbAQEAAgMBAQAAAAAAAAAAAAAABAUBAwYCB//EADIRAQACAQIDBAkFAQEBAQAAAAABAgMEEQUhMRJBUXETIjJhgZGh0fAGQrHB4RTxUhX/2gAMAwEAAhEDEQA/AOqKJUgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC6na+pH1UZZxT6Lr+dPek6ScUZY9L0/OvuVq2voeNFGWMUek+Hjt73vXTinNPovj4b+5YS0MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK04OTtFXfy7zVmz48Ne1edm3Fhvlnakbp0Nnq3vPXs3L7lLk4veb+pG0e/rP2XGPhdIr687z/CDZxdmtYvVPcXmPJXJWL16SpslJx2mtusL8RUUndK3zZ7eJYwwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYmYiN5ZiJmdoSKOEb1louS3/ANim1XF619XDznx7vh4/nVb6bhcz62Xl7k+mlFWSsiivmtkt2rzvK5pjrSOzWNoXqRjd62Q9o0brOt6393PwLjheq7NvRW6T08/9/lVcS03ar6SvWOvl/iCdAoQAAAAAAAAAAAAAAAAAAAAAAAAAAABqx5reLRvD1ak0nazLTw8mm/LtPTGzEGAC6nScuxc39CDquIYsHLrbwj+/BP0vD8ufn0jx+yZSpKO7fze85zU6zLqJ9aeXh3Og0+jx4I9WOfj3styIk7K3DGytwxsrmMxMwxMbtZXp5ZW4PVd3I67Qar/oxbz1jlP3+LltbpvQZNo6T0+3wWE1DAMlKi5JtcF5vkGdmMMAAAAAAAAAAAAAAAAAAAAAAF1O19SLq4zTjn0PX6/BM0c4IyR6bf8Ar4s+Jcf5uz6lZwmuo25ex7/6WHFZwb7T7fu/tgjUaTS3MvVItir6LU1Zs+PDXtXnZtw6fJmt2aRuz06C46/IoNVxTJk9XH6sfX/HQ6XhePF62T1p+jMVS0VuNmNlbmNjZIw2EqVOrFtc3ovNk7TcN1Oo9is7eM8oacmamP2pYsbjsJhv9aupzX+3Q9+V+TfDxsdDpf03SOee2/ujp8//ABTavjuHFyiefzn/AD4q7K2tRxtKs6VL2MsO1KzleU6T4t+D013Lmb+KcKwxpJnFSImvP37d/nyauF8V/wCrJMT+eDHiKeaNuK1XeclotTOnyxbu7/Jb6vTRnxzXv7vNr0dhExMbw5OYmJ2lVeZlhscPWi4/ly71yMvcShV6ik7pW+ph5ljDAAAAAAAAAAAAAAAAAAAAAAAbMVrFY2h6tabTvKK8fTVeNGTyynHMuT1tlvwbs/I16uuopppzYo3iJ5+737fm3ksOH6Omed7zy/ltoxS3HH5Mlslu1ed5dNTHXHXs1jaFTW9roQcnaKcnySbZsx4r5bdmkTM+5iZisbzOyTUwSpRz4ipDDx/XJZn3LiXum/T2e/PLMVj5z9vqr9RxPBhjeZ/ppsZ0vwtHTD0niJL463uw71He/JHQ6Xg+lwc4rvPjPP8Axzer/Ukzyx/aPu5vavSfFYm6nVcYP4KfuQtystWu9stNnPZ9fnze1bl4Q05lDb3oVtH8PjKbfUq//GfLLPRX/my+piYiY2lP4bn9FqInunl+fF2uKo+znKH5XZd29elj5nrtNOn1FsfhPLy7n03Fft0i3igYqFnmXHf38y04Tqt49Dbu6fZS8V0u0+mr8fuwl2pBP1DIGAAAAAAAAAAAAAAAAAAAAAAAAA896TYjPiZtPqNQVuGX+9zpNDj7OCInv5/P/F/o6dnDHv5uu6F7beKaoTaVaMbqU2oqpFcf3LivHnbkuJ/pu/pu1ptuzPj+2ft4fJY/9Va13u6DGbVwOG69V4ma+ChrG/bO9vXwNmm/TuGnPLM2nw6R91Nq/wBQ4sfKn05/40O0OnNeSccPCGFh+hKU33yat6X7S+xYMeKvZx1iI9zmtTxrPlnly+suZr1p1JZpylUm+MpOUn4vU2Km1rXne0zMvRsR0S/GYTCWjHB1YRtNezSvdatxjxbinr+Zh0V9B/0YacuxMdeTmelPRN4GnCbrKrnnksqbhbRu/WfIKzW8P/5qRbtb7z4NNsyn7zm3aNNXel+eh5tPcr6q7QhTj7sVJSundvRxa4aiu8k7Q9Dp4v8AE4Whid8nH2VT/shx8dX4o5b9Sab2c8eU/wBf2+i8E1XpsEb9f76SwyV1Z8TlqXmlotXrC4vSL1mtukoTjZ25eqOw02eM+OLx8fdLj9Vp5wZJpPw8hI23tFY3n6NVKTe0Vj68madHTu39pU6biXpM01mJ2np37ef5yW2q4b6PDFomN4692/kwlwpgAAAAAAAAAAAAAAAAAAAAACytUUYuT3RTk+5K5mtZtMRDMRMztDy2tUcm5PfJuT727s62tYrERHc6aIiI2juYGzMxvG0lqxaJraN4ls8Fi8ys96IWTH2J9ziOKcNnTX7VfZnp7vd+dU6UGrXVrq6vxXM1Kh0n8O6MJ4+GezywlOCfGorW8k2/ALPhNa21Edrujl5vQZOvUxOIoVYyWGq0EqVSC6rtad5LVSbldX/IrBfT6S2W+O0erMcpj6/H7PMsbsHHK6nSrTjCT1SnNaaZkuXaHOZdJqulomYj4tbhK8qcnlV82ji03fw5mJiJQ43htqE3UUc1Nb3GScbWSV01fga55d71DcdAsUpPEYS/u1E6tP8AfD7pR8Is063T/wDRgtjnvj6931X3ANV6LLNJ8/6n6NofNZiYnaX0BixFO6ut69VyLDh2q9Dk2t7M9fur+I6X0+PevtR0+yMmdQ5Rc5XSXI1Uw0pa1qxznq3ZM970rS08q9Pz6KG1pAAAAAAAAAAAAAAAAAAAAAANV0nr5MNU5ytD+p6+lyZoadrPX3c/klaOnazR7ubzyTOjXzEzIpGTTut6MTETG0teXFTLSaXjeJdVs7aanSWWClKFo2kszt2eJXZMU0tzcPr9DfS326x3T4/74rKFadGpGcW6dSDzJrRp+JhX0valotXlMOtw/wDEbEqynTpSs1dqM02uPxWuFtTjOWPaiHZ4nbFSOLwsIxjUw+Lg2pRUs0ZJZr3vbLZx4cwuL6i8ZqViN62hw38R8PGljlOn7sqlKNSVvz3lHN4pL15hR8Xx1pn3r3xvLnfx82pKTzKUbcFZ89EY7Mdys7RsnHPD16VaO+nNS04x3SXim14mWzT5ZxZK3jul6PtmUITc8yVOpFVYttJWlrv9fE4TjOitTVz2I37fONvHv+r6jos0ZMMTv0/I+jlsf0voU7qF60v0aR/qf0uSNJ+mdXm55NqR7+vy++zbbPWOnNJ2XipVqUakoqDneVk20lfTUub4IwT6KLTbs8t5cprOz6e3Zjb85pZ4RQAAAAAAAAAAAAAAAAAAAAAAByvTjEaUqfa5vw0XzZb8Kpztf4LPh1OdrfBx8mXK1Y2BaBkw1eVOWaLs93ejzekWjaWjU6emoxzS/wD5Pi389oqrGnreSjZtq2vJ/wCcSvnHNJmJcLrdJfT5Jpb/ANjxdtsTEbJlh6UMTFKrCLUnkqxcndu+anv8TCbp76GcVa5Y5x7p/p1uB21h3harwS9r+Ep6QftI6WbSTkszWj8rBaY9TinFPoOfZjpz/vm8k2ptOeIqyq1ZXnN37EuCS4JIy5bLkvmvN7dWtq42MT1WlrdISdPw3Pn9ivLx7kOrtCT3aEiun8V9pv0/SvPNbf3R9/8AxZXxtSqoxnUlNQWWKlJtQiuCW5G6KRXpC/x46Y6xWkbQrSi20lvbsu9mZnbnL1vtzl6hhaShCMVujFR8lY5K9u3abT3uatbtWm3iynl5AAAAAAAAAAAAAAAAAAAAAAAHn/SzEZ8TNcIJQ8ld+rOi4fTs4I9/Ne6KnZwx7+bRyJyWsYFGAAy4bNfRX5ni9IvGyJrNHXVY+zPXunw/zxbDM1rcjzgtEbqDLwHLTH2omJnwj+vFlwnSKth8/sajh7SOWWSyur33vd3oxXBaevJ60PCdTTeZt2In4z+fFqZ15PjbuJFcVYW+n4Xp8PPbefGef+MaNixAPWtn06OJwtL3ITpunG0XGLUWlZpcmmmvA5fLOTFmtzmJ3WFYrasIUuiVBVI1IZoZZKWW+aLs78dV5m7/APQyzSaW57x172jNpYvSa1nbdtpUmu0guezcM1GPnEdqPd9uqwIAGAAAAAAAAAAAAAAAAAAAAAFs5WTb3JX8DMRvyZjm8txVbPOU38c3LzdzrKV7FYr4Rs6WlezWK+CMz29LQLqdJy3L7A2SqeES36/Iy9bJCVgyqBBxdGzutz9GHmYRzDAgKoDb7F25Wwt1TacG7uE1eN+a4p9xG1Glx5va6+L3TJanR6JsDaTxNFVHDJ7zjbNmvbitOfyKDVYIw5OxE7puO/bjdsSM2I9eNn3mXNcXwRTJGSP3fzDEFQAAAAAAAAAAAAAAAAAAAAA1vSPEezw1V8XHIu+Ty/UlaOnbz1j4/LmkaWnay1j85PN5M6Z0BToSluWnN7gylU8Ilv1foZNmewZLAUsADKklfRga6vSyu3DgYeJhjAuQGSAHo3QepfC5eMKkvJu6fq/I5ziMxOefh/Cdg9h0JBbltSF0ZRtVpq6jH2LfDzcPtLGSdeUoyas8qcW1otP87y4xYojHFZh8v1GW3p7TWe/aJjwj79WbDbeqR6yVRf0vzX2NV9HSfZ5NuPX5K+1zbXDbbpT3twf693nuIt9Lkr05puPW4r9Z282xjJNXTunxTuiPMbdUuJiecKmAAAAAAAAAAAAAAAAAaLpbh6lSlCME2vaZpWTdkk7aLvLHhtqVyTNp25ct0/QWpXJM2nbk5OODUd6u+1fQ6CNp5wuo26wy5TL0plMMKWApYClgFgFgMdakpKz/APGBrZRadnvRh5EBlgB6Z0ewjp0YW35VftOTzX7d5t4ysaRtEQ3MZXNT0i7WxPs6M5cbWXe9EbsFO3eIV3F9V/zaS+SOu20ec8vp1cC2XL5coAAy0MRODvCTj3Pf3riebUrb2oe6ZL0nes7NphukE1pOKmua91/Yi30dZ9mdk3HxC8e3G7a4ba9GfxZHynp67iJfTZK92/knY9Xiv37eacmaElUAAAAAAAAAAAAJEJQyO6d7+N+FgyjgY6tCM+tFS70me6XtTnWZh6re1fZnZAr7Coy3Jwf6X9HoS6cRz179/NJprs1e/fza+v0bfwTv2SVvVfYmU4tH76/JKpxOP3V+TX19jVo/BmXOLT9N5Mpr8F/3bef5sl01uG3ft5/myFOk1o00+1NEqtotG8TukxMWjeOazKemVMoFMphhSwEfFYfMrrevVcgTCAjDynbKoe0rU485LyWv0I+qv2MNre7+eT1jje0Q9Xw0MsUuw5ZYstgy5rpdiepTX7n8l9fMsdFTlNnE/qrVb3pp47vWnz6R/fzc0TnJAAAAAozDLLh8ZUp9Sbj2X08noeL4639qG7HmvT2ZbTDdJZLSpFS7YaPyenyIt9HH7ZTcevn98fJtaO2qElfOo9k00yNbT5I7kyupxWjq2BobwAAAAAAAAADLPQp63fApeIcQr2JxY53mesrnh/Dr9qMmSNojpClajrdbvkbdDxGmSsUyTtb+f9a9dw69LTfHG9f4/wAYS1VIAAtlRU9GlK+lmkz1W01neJ2eqzMTyQsRsSi21kytflbXpuJVNfnp+7fz5/6k01uavfv5tdX6Ofkn4SX1RMpxaf31+SVTic/ur8kCvsStH4VL9rv8yZTiOC3ft5pVNdht37eaBVoSj1k496aJlL1vzrMT5JVb1t7M7sbgenpBxuGt7y8fuYl5luuhOHzVpTe6ELfzSf2T8yr4pfbHFfGf4QdZnviivYnad3dKsyiaY4vn225ee3+qKqw104pqazvNt/OI/rZxW1cT7StOXbbwWiLrFTsUiHI63U21Oovmt3z9I5QiGxFAAAABazDK1h6WSD1Cxh6ejlE6AAAAAAAAAAAMlGdn2Ffr9JXNSbRHrR9fcseH6y2HJFZn1Z+nv+6lSd+426TSUwUjl63fP53Nes1d9Reefq90fnesJaEAAM+EqJPVb9L8gzCuLqpvRbtLglHDABbKCe9X7zMTMc4ZidkOtsmjL4Ev2+78iTTW56dLfPmkU1eavS3z5oFfo5F9WbXZJJkynFrR7dYny5fdKpxK37q7/nxSdg7K/DRkr5nOebTgrWS/zmRNZqYz3iYjaIRtVnjNaJiNobQiIoBHxOCp1OvFN89z81qbKZb09mWvJhpk9qGqxPR5b6c7dk9fVEqmtn90IOTh0fsn5tVidm1afWg7c4+8vTd4kqmel+koWTTZadYRDcjgBgWsw9LGGYY5B7hYwy9JKJ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARcTs+lU60FfmtH5o20zXp0lpyafHk9qGqxPR7/jn4T+6+xKprf/qPkhZOHf8AxPzanFYGpT60GlzWq80SqZqX6ShX0+TH7UIjNjUsYeoY2HqFjD09KKJfgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOK2TRqb4JPnD3X6aM3Uz5K9JaL6bHfrDT4vo1Ja05qXZLR+e5+hKprI/dCJfQTHsy0uLwdSl14OPa1p5rQlUyVv7MotsV6e1CIz28vSyiXwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAo0Br6+xMPN3dNJ/pbj6LQ3V1GSve020+OesNiaW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH/9k="
              header="Get the most amount of aid"
              text="Our advisors will help you apply to financial aid and scholarships."
            />
          </div>
        </div>

        <div className="tilt-couple" style={{ marginTop: "10rem" }}>
          <div className="text">
            <h2>Find &#38; select affordable colleges</h2>
            <p>
              Based on your background, we can help you find colleges that will
              offer you the most amount of grants and scholarships.
            </p>
            <div className="get-started">
              <button className="tilt-button dark">Get Started</button>
              <div>
                <p>"We tripled our direct orders with Tilt"</p>
                <span>Tamer, Owner of Harvard University</span>
              </div>
            </div>
          </div>
          <div className="image">
            <img src={dog} />
          </div>
        </div>
        <div className="tilt-couple" style={{ marginTop: "10rem" }}>
          <div className="image">
            <img src={dog} />
          </div>
          <div className="text">
            <h2>Get help applying to financial aid</h2>
            <p>
              We will walk you through how to fill out financial aid forms and
              compare your financial aid packages once you have been accepted.
            </p>
            <div className="get-started">
              <TiltButton classes={["dark"]}>Get Started</TiltButton>
              <div>
                <p>"We tripled our direct orders with Tilt"</p>
                <span>Tamer, Owner of Harvard University</span>
              </div>
            </div>
          </div>
        </div>

        <div className="tilt-couple" style={{ marginTop: "10rem" }}>
          <div className="text">
            <h2>On-demand advisors to answer questions</h2>
            <p>
              We know that figuring out how to pay for college can be confusing
              and overwhelming—that's why you'll always have access to our
              advisors who are ready to answer your questions.
            </p>
            <div className="get-started">
              <TiltButton classes={["dark"]}>Get Started</TiltButton>
              <div>
                <p>"We tripled our direct orders with Tilt"</p>
                <span>Tamer, Owner of Harvard University</span>
              </div>
            </div>
          </div>
          <div className="image">
            <img src={dog} />
          </div>
        </div>

        <div className="tilt-couple" style={{ marginTop: "10rem" }}>
          <div className="image">
            <img src={dog} />
          </div>
          <div className="text">
            <h2>Database of vetted scholarships</h2>
            <p>
              We find and evaluate scholarships offered across the country, so
              you don't have to.
            </p>
            <div className="get-started">
              <TiltButton classes={["dark"]}>Get Started</TiltButton>
              <div>
                <p>"We tripled our direct orders with Tilt"</p>
                <span>Tamer, Owner of Harvard University</span>
              </div>
            </div>
          </div>
        </div>

        <div className="tilt-couple" style={{ marginTop: "10rem" }}>
          <div classSName="text">
            <h2>Financial aid for students</h2>
          </div>
        </div>

        <Testimonial />

        <FaqSection />

        <div className="black-box" style={{ marginTop: "5rem" }}>
          <div className="organization">
            <div className="text">
              <h2>Become a partner</h2>
              <p>
                Interested in bring Tilt to your school or community
                organization?
              </p>
            </div>

            <div className="form">
              <Formik
                initialValues={{
                  email: "",
                }}
                validationSchema={emailSchema}
                onSubmit={handleSubmit}
              >
                {(state) => (
                  <Form className="tilt-email-input">
                    <Field name="email" placeholder="Enter your email"></Field>
                    {/* {state.errors && state.touched && (
            <span className="custom-text-input-error">
              {state.errors[field]}
            </span>
          )} */}
                    <TiltButton classes={["light"]} type="submit">
                      Get Started
                    </TiltButton>
                  </Form>
                )}
              </Formik>
            </div>
          </div>

          <div
            style={{
              margin: "2rem 0",
              width: "100%",
              border: "1px solid gray",
            }}
          />

          <div className="benefits">
            <span>
              <CheckCircleIcon /> Access to student accounts
            </span>
            <span>
              <CheckCircleIcon /> Customized reporting
            </span>
            <span>
              <CheckCircleIcon /> Satisfaction guarantee
            </span>
          </div>
        </div>

        <Footer />
      </div>
    </>
  );
};

export default HomePage;
