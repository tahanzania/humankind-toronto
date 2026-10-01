/* humanKIND toronto — small progressive enhancements. Everything works without JS. */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Sticky header shadow */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Desktop dropdowns (click/keyboard support on top of :hover/:focus-within) */
  var toggles = document.querySelectorAll(".nav__toggle");
  toggles.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      toggles.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
      btn.setAttribute("aria-expanded", open ? "false" : "true");
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav__item")) toggles.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
  });

  /* Mobile menu */
  var menu = document.getElementById("mobile-menu");
  var openBtn = document.querySelector("[data-menu-open]");
  var closeBtn = document.querySelector("[data-menu-close]");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("is-open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    if (open) menu.removeAttribute("inert"); else menu.setAttribute("inert", "");
    document.body.classList.toggle("menu-open", open);
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    setTimeout(function () {
      if (open && closeBtn) closeBtn.focus();
      if (!open && openBtn) openBtn.focus();
    }, 60);
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (menu && menu.classList.contains("is-open")) setMenu(false);
    toggles.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
  });

  /* Reveal on scroll */
  var revealables = document.querySelectorAll(".reveal, .packing, .tl-item, .script-underline, [data-reveal]");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* Timeline progress line */
  var timeline = document.querySelector(".timeline");
  var progress = document.querySelector(".timeline__progress");
  if (timeline && progress) {
    var ticking = false;
    var update = function () {
      var r = timeline.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = (vh * 0.6 - r.top) / r.height;
      progress.style.height = Math.max(0, Math.min(1, p)) * 100 + "%";
      ticking = false;
    };
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* Team card flip */
  document.querySelectorAll(".team-card").forEach(function (card) {
    card.querySelectorAll(".team-card__btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var flipped = card.classList.toggle("is-flipped");
        var front = card.querySelector(".team-card__front");
        var back = card.querySelector(".team-card__back");
        front.setAttribute("aria-hidden", flipped ? "true" : "false");
        back.setAttribute("aria-hidden", flipped ? "false" : "true");
        if (flipped) { front.setAttribute("inert", ""); back.removeAttribute("inert"); }
        else { back.setAttribute("inert", ""); front.removeAttribute("inert"); }
        var target = card.querySelector(flipped ? ".team-card__back .team-card__btn" : ".team-card__front .team-card__btn");
        if (target) target.focus();
      });
    });
  });

  /* Button ripple */
  if (!reduceMotion) {
    document.addEventListener("pointerdown", function (e) {
      var btn = e.target.closest(".btn");
      if (!btn) return;
      var rect = btn.getBoundingClientRect();
      var size = Math.max(rect.width, rect.height);
      var dot = document.createElement("span");
      dot.className = "ripple-dot";
      dot.style.width = dot.style.height = size + "px";
      dot.style.left = e.clientX - rect.left - size / 2 + "px";
      dot.style.top = e.clientY - rect.top - size / 2 + "px";
      btn.appendChild(dot);
      setTimeout(function () { dot.remove(); }, 700);
    });
  }

  /* Countdown (Create for a Cause) */
  document.querySelectorAll("[data-countdown]").forEach(function (el) {
    var target = new Date(el.getAttribute("data-countdown")).getTime();
    var parts = {
      days: el.querySelector("[data-days]"),
      hours: el.querySelector("[data-hours]"),
      mins: el.querySelector("[data-mins]")
    };
    function tick() {
      var diff = Math.max(0, target - Date.now());
      var d = Math.floor(diff / 86400000);
      var h = Math.floor((diff % 86400000) / 3600000);
      var m = Math.floor((diff % 3600000) / 60000);
      if (parts.days) parts.days.textContent = d;
      if (parts.hours) parts.hours.textContent = String(h).padStart(2, "0");
      if (parts.mins) parts.mins.textContent = String(m).padStart(2, "0");
      if (diff === 0) {
        var wrap = el.closest("[data-countdown-wrap]");
        if (wrap) wrap.hidden = true;
      }
    }
    tick();
    setInterval(tick, 30000);
  });

  /* Contact form: pre-select topic from ?topic= and compose an email */
  var form = document.getElementById("contact-form");
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var topic = params.get("topic");
    var select = form.querySelector("#topic");
    if (topic && select) {
      Array.prototype.forEach.call(select.options, function (opt) {
        if (opt.value === topic) select.value = topic;
      });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form);
      var topicLabel = select ? select.options[select.selectedIndex].text : "General enquiry";
      var subject = "[Website] " + topicLabel + " — " + data.get("name");
      var body =
        "Name: " + data.get("name") + "\n" +
        "Email: " + data.get("email") + "\n" +
        (data.get("phone") ? "Phone: " + data.get("phone") + "\n" : "") +
        "Topic: " + topicLabel + "\n\n" +
        data.get("message");
      var href = "mailto:" + form.getAttribute("data-to") +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
      var status = form.querySelector(".form__status");
      if (status) status.textContent = "Opening your email app… If nothing happens, email us directly at " + form.getAttribute("data-to") + ".";
      window.location.href = href;
    });
  }
})();
