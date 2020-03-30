import AOS from 'aos';
import Typed from 'typed.js';
import SmoothScroll from 'smooth-scroll'

export function initializeAOS() {
  function init() {
    var options = {
      duration: 700,
      easing: 'ease-out-quad',
      once: true,
      startEvent: 'load'
    }
    AOS.init(options);
  }

  if (typeof AOS !== 'undefined') {
    init();
  }
};

export function initializeTyped() {
  var toggle = document.querySelectorAll('[data-toggle="typed"]');

  function init(el) {
    var elementOptions = el.dataset.options;
        elementOptions = elementOptions ? JSON.parse(elementOptions) : {};
    var defaultOptions = {
      typeSpeed: 40,
      backSpeed: 40,
      backDelay: 1000,
      loop: true
    }
    var options = Object.assign(defaultOptions, elementOptions);

    // Init
    new Typed(el, options);
  };

  if (typeof Typed !== 'undefined' && toggle) {
    [].forEach.call(toggle, function(el) {
      init(el);
    });
  };
};

export function initializeSmoothScroll() {
  var toggle = '[data-toggle="smooth-scroll"]';

  function init(toggle) {
    var options = {
      header: '.navbar.fixed-top',
      offset: function(anchor, toggle) {
        return toggle.dataset.offset ? toggle.dataset.offset : 24;
      }
    };

    new SmoothScroll(toggle, options);
  }

  if (typeof SmoothScroll !== 'undefined' && toggle) {
    init(toggle);
  }

};
