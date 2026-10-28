(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---- Theme (light / dark, remembered) ---- */
  var themeBtn = $(".theme-btn");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem("eb-theme", next); } catch (e) {}
      themeBtn.setAttribute("aria-pressed", next === "dark");
      drawChart();
    });
  }

  /* ---- Mobile navigation + dropdown menus ---- */
  var toggle = $(".nav-toggle"), nav = $("#site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.addEventListener("click", function (e) {
    $$("details.more[open], details.account[open]").forEach(function (d) { if (!d.contains(e.target)) d.removeAttribute("open"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") $$("details[open]").forEach(function (d) { d.removeAttribute("open"); });
  });

  /* ---- Toast messages: dismiss; successes and info fade, errors stay until closed ---- */
  function closeToast(f) { f.classList.add("out"); setTimeout(function () { f.remove(); }, 260); }
  $$(".flash").forEach(function (f) {
    var close = $(".flash-close", f);
    if (close) close.addEventListener("click", function () { closeToast(f); });
    if (!f.classList.contains("flash-error") && !f.classList.contains("static")) setTimeout(function () { closeToast(f); }, 7000);
  });

  /* ---- Page loading bar on navigation ---- */
  var loader = $(".page-loader");
  function loadingOn() { if (loader) loader.classList.add("on"); }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    if (a.target === "_blank" || a.hasAttribute("download")) return;
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#" || a.origin !== location.origin) return;
    loadingOn();
  });
  window.addEventListener("pageshow", function () { if (loader) loader.classList.remove("on"); });

  /* ---- Confirm destructive actions ---- */
  $$("form[data-confirm]").forEach(function (f) {
    f.addEventListener("submit", function (e) { if (!window.confirm(f.getAttribute("data-confirm"))) e.preventDefault(); });
  });

  /* ---- Reveal buttons (interview answers) ---- */
  $$("[data-reveal]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var el = document.getElementById(btn.getAttribute("data-reveal"));
      if (!el) return;
      el.hidden = !el.hidden;
      btn.textContent = el.hidden ? "Show sample answer" : "Hide sample answer";
      btn.setAttribute("aria-expanded", String(!el.hidden));
    });
  });

  /* ---- Prevent double submits and show progress ---- */
  $$("form").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      if (e.defaultPrevented || f.id === "chat-form") return;
      var b = $("button[type=submit].btn", f);
      if (b && !b.classList.contains("loading")) {
        b.classList.add("loading"); loadingOn(); f.setAttribute("aria-busy", "true");
        var label = b.getAttribute("data-loading");
        if (label) b.textContent = label;
        setTimeout(function () { b.setAttribute("disabled", "disabled"); }, 0);
      }
    });
  });
  window.addEventListener("pageshow", function () {   // back button: re-enable
    $$("button.loading").forEach(function (b) { b.classList.remove("loading"); b.removeAttribute("disabled"); });
    $$("form[aria-busy]").forEach(function (f) { f.removeAttribute("aria-busy"); });
  });

  /* ---- Inline form validation with clear messages ---- */
  var ALERT = '<svg class="icon" aria-hidden="true"><use href="#i-alert"/></svg>';
  function labelOf(el) {
    var l = el.closest("label"); if (!l) return "This field";
    var t = (l.childNodes[0] && l.childNodes[0].textContent || "").trim();
    return t || "This field";
  }
  function messageFor(el) {
    var v = el.validity;
    if (v.customError) return el.validationMessage;
    if (v.valueMissing) return "Please fill in " + labelOf(el).toLowerCase() + ".";
    if (v.typeMismatch && el.type === "email") return "Enter a valid email address, like name@example.com.";
    if (v.typeMismatch && el.type === "url") return "Enter a full web address starting with https://";
    if (v.tooShort) return labelOf(el) + " needs at least " + el.minLength + " characters (you typed " + el.value.length + ").";
    if (v.tooLong) return labelOf(el) + " can be at most " + el.maxLength + " characters.";
    if (v.rangeUnderflow || v.rangeOverflow) return "Enter a number between " + el.min + " and " + el.max + ".";
    return "Please check this field.";
  }
  function showError(el, msg) {
    clearError(el);
    el.setAttribute("aria-invalid", "true");
    var span = document.createElement("span");
    span.className = "field-error js-error"; span.setAttribute("role", "alert");
    span.id = "jserr-" + (el.id || el.name);
    span.innerHTML = ALERT + "<span></span>"; span.lastChild.textContent = msg;
    var host = el.closest(".pw-wrap") || el;
    var after = host.nextElementSibling && host.nextElementSibling.classList.contains("pw-meter") ? host.nextElementSibling : host;
    after.parentNode.insertBefore(span, after.nextSibling);
    el.setAttribute("aria-describedby", span.id);
  }
  function clearError(el) {
    el.removeAttribute("aria-invalid");
    var l = el.closest("label") || el.parentNode;
    $$(".js-error", l).forEach(function (n) { n.remove(); });
  }
  $$("form.form").forEach(function (form) {
    form.noValidate = true;
    var pw = $("input[name=password], input[name=new_password]", form);
    var confirm = $("input[name=confirm], input[name=confirm_password]", form);
    function matchCheck() { if (confirm && pw) confirm.setCustomValidity(confirm.value && confirm.value !== pw.value ? "Passwords do not match. Type the same password again." : ""); }
    if (pw && confirm) { pw.addEventListener("input", matchCheck); confirm.addEventListener("input", matchCheck); }
    var fields = $$("input:not([type=hidden]):not([type=checkbox]):not([type=radio]), select, textarea", form);
    fields.forEach(function (el) {
      el.addEventListener("blur", function () { if (el.value !== "" || el.dataset.touched) { el.dataset.touched = "1"; el.checkValidity() ? clearError(el) : showError(el, messageFor(el)); } });
      el.addEventListener("input", function () { if (el.dataset.touched && el.checkValidity()) clearError(el); });
    });
    form.addEventListener("submit", function (e) {
      matchCheck();
      var bad = fields.filter(function (el) { return !el.disabled && !el.checkValidity(); });
      if (!bad.length) return;
      e.preventDefault();
      bad.forEach(function (el) { showError(el, messageFor(el)); });
      bad[0].focus();
      var b = $("button[type=submit].btn", form);
      if (b) { b.classList.remove("loading"); b.removeAttribute("disabled"); }
      $(".page-loader") && $(".page-loader").classList.remove("on");
    }, true);
  });

  /* ---- Password: show/hide and strength meter ---- */
  function strength(pw) {
    var s = 0;
    if (pw.length >= 8) s++;
    if (pw.length >= 12) s++;
    if (/[A-Za-z]/.test(pw) && /\d/.test(pw)) s++;
    if (/[^A-Za-z0-9]/.test(pw) || (/[a-z]/.test(pw) && /[A-Z]/.test(pw) && pw.length >= 10)) s++;
    if (pw.length < 8 || !/[A-Za-z]/.test(pw) || !/\d/.test(pw)) s = Math.min(s, 1);
    return pw ? Math.max(s, 1) : 0;
  }
  $$(".form input[type=password]").forEach(function (input) {
    var wrap = document.createElement("div");
    wrap.className = "pw-wrap";
    input.parentNode.insertBefore(wrap, input);
    wrap.appendChild(input);
    var btn = document.createElement("button");
    btn.type = "button"; btn.className = "pw-toggle"; btn.textContent = "Show";
    btn.setAttribute("aria-label", "Show password");
    btn.addEventListener("click", function () {
      var show = input.type === "password";
      input.type = show ? "text" : "password";
      btn.textContent = show ? "Hide" : "Show";
      btn.setAttribute("aria-label", show ? "Hide password" : "Show password");
    });
    wrap.appendChild(btn);
    if (input.autocomplete === "new-password" && input.name !== "confirm" && input.name !== "confirm_password") {
      var meter = document.createElement("div");
      meter.className = "pw-meter"; meter.setAttribute("aria-live", "polite");
      meter.innerHTML = "<i></i><i></i><i></i><i></i><span></span>";
      wrap.parentNode.insertBefore(meter, wrap.nextSibling);
      var words = ["", "Weak", "Okay", "Good", "Strong"];
      input.addEventListener("input", function () {
        var sc = strength(input.value);
        meter.dataset.score = sc;
        $("span", meter).textContent = words[sc];
      });
    }
  });

  /* ---- Lesson reader: reading progress + copy buttons ---- */
  var body = $(".lesson-body");
  if (body) {
    var bar = $(".read-bar");
    var onScroll = function () {
      var r = body.getBoundingClientRect();
      var total = r.height - window.innerHeight * 0.6;
      var pct = total <= 0 ? 100 : Math.min(100, Math.max(0, (-r.top / total) * 100));
      if (bar) bar.style.width = pct + "%";
    };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
    $$("pre", body).forEach(function (pre) {
      var b = document.createElement("button");
      b.type = "button"; b.className = "code-copy"; b.textContent = "Copy";
      b.addEventListener("click", function () {
        var text = pre.innerText.replace(/\s*Copy\s*$/, "");
        (navigator.clipboard ? navigator.clipboard.writeText(text) : Promise.reject()).then(function () {
          b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1500);
        }).catch(function () { b.textContent = "Press Ctrl+C"; });
      });
      pre.appendChild(b);
    });
  }

  /* ---- Quiz: answered counter and unanswered warning ---- */
  var quiz = $("#quiz-form");
  if (quiz) {
    var total = $$("fieldset.question", quiz).length;
    var count = $("#answered"), fill = $("#quiz-fill");
    var update = function () {
      var names = {};
      $$("input[type=radio]:checked", quiz).forEach(function (r) { names[r.name] = 1; });
      var n = Object.keys(names).length;
      count.textContent = n;
      fill.style.width = (n * 100 / total) + "%";
      return n;
    };
    quiz.addEventListener("change", update);
    quiz.addEventListener("submit", function (e) {
      var left = total - update();
      if (left > 0 && !window.confirm(left + " question" + (left === 1 ? " is" : "s are") + " unanswered and will count as wrong. Submit anyway?")) {
        e.preventDefault();
        var b = $("button[type=submit]", quiz); b.classList.remove("loading"); b.removeAttribute("disabled");
      }
    });
  }

  /* ---- Dashboard charts (theme aware, accessible) ---- */
  var charts = [];
  function drawChart() {
    var canvases = $$("canvas[data-chart]");
    if (!canvases.length || !window.Chart) return;
    charts.forEach(function (c) { c.destroy(); }); charts = [];
    var cs = getComputedStyle(document.documentElement);
    var brand = cs.getPropertyValue("--brand").trim(), muted = cs.getPropertyValue("--muted").trim(),
        line = cs.getPropertyValue("--line").trim(), hi = cs.getPropertyValue("--hi").trim();
    canvases.forEach(function (canvas) {
      var kind = canvas.dataset.chart, max = canvas.dataset.max ? Number(canvas.dataset.max) : undefined;
      var horizontal = kind === "hbar";
      var type = kind === "line" ? "line" : "bar";
      var color = kind === "week" ? hi : brand;
      var valueAxis = { min: 0, max: max, beginAtZero: true, ticks: { color: muted, precision: 0 }, grid: { color: line } };
      var labelAxis = { ticks: { color: muted }, grid: { display: false } };
      charts.push(new Chart(canvas, {
        type: type,
        data: { labels: JSON.parse(canvas.dataset.labels),
                datasets: [{ label: canvas.dataset.label || "", data: JSON.parse(canvas.dataset.values),
                             borderColor: kind === "week" ? cs.getPropertyValue("--ink-2").trim() : brand,
                             backgroundColor: kind === "line" ? brand + "22" : color,
                             borderWidth: kind === "week" ? 1.5 : 2, fill: kind === "line", tension: .3, pointRadius: 4,
                             borderRadius: kind === "line" ? 0 : 6, maxBarThickness: 36 }] },
        options: { indexAxis: horizontal ? "y" : "x", responsive: true, maintainAspectRatio: true,
                   plugins: { legend: { display: false } },
                   scales: horizontal ? { x: valueAxis, y: labelAxis } : { y: valueAxis, x: labelAxis } }
      }));
      var sk = canvas.closest(".skeleton"); if (sk) sk.classList.add("ready");
    });
  }
  if ($("canvas[data-chart]")) {
    window.addEventListener("load", drawChart);
    // If the chart library is blocked or offline, stop the placeholder shimmer.
    setTimeout(function () { if (!window.Chart) $$(".skeleton").forEach(function (n) { n.classList.add("ready"); }); }, 6000);
  }

  /* ---- AI tutor chat (text via textContent, never innerHTML) ---- */
  var form = $("#chat-form");
  if (form) {
    var log = $("#chat-log"), input = $("#chat-input");
    var token = $('meta[name="csrf-token"]').content;
    var history = [], busy = false;

    var add = function (role, text) {
      var d = document.createElement("div");
      d.className = "msg " + role; d.textContent = text || "";
      log.appendChild(d); log.scrollTop = log.scrollHeight; return d;
    };
    add("bot", "Hi! I'm your study assistant. Ask about any lesson, or pick a question below.");

    var send = function (message) {
      message = (message || "").trim();
      if (!message || busy) return;
      busy = true;
      add("user", message); input.value = ""; input.style.height = "auto";
      var pending = add("bot");
      pending.innerHTML = '<span class="typing" role="status" aria-label="Thinking"><i></i><i></i><i></i></span>';
      fetch(form.dataset.url, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRFToken": token },
        body: JSON.stringify({ message: message, level: $("#chat-level").value, language: $("#chat-language").value, history: history.slice(-6) })
      }).then(function (r) { return r.json().then(function (data) { return { ok: r.ok, data: data }; }); })
        .then(function (res) {
          pending.textContent = res.ok ? res.data.reply : (res.data.error || "Something went wrong. Please try again.");
          if (res.ok) {
            (res.data.suggestions || []).forEach(function (s) {
              if (typeof s.url === "string" && s.url.charAt(0) === "/") {
                var a = document.createElement("a"); a.href = s.url; a.textContent = s.title;
                pending.appendChild(document.createElement("br")); pending.appendChild(a);
              }
            });
            history.push({ role: "user", content: message }, { role: "assistant", content: res.data.reply });
          }
        })
        .catch(function () { pending.textContent = "No connection. Check your internet and try again."; })
        .then(function () { busy = false; log.scrollTop = log.scrollHeight; input.focus(); });
    };

    form.addEventListener("submit", function (e) { e.preventDefault(); send(input.value); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(input.value); }
    });
    input.addEventListener("input", function () { input.style.height = "auto"; input.style.height = Math.min(input.scrollHeight, 160) + "px"; });
    $$(".chip[data-q]").forEach(function (c) { c.addEventListener("click", function () { send(c.dataset.q); }); });
  }
})();
