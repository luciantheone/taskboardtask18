(function () {
  "use strict";
  var root = document.documentElement;
  var btn = document.getElementById("theme");
  var brand = document.querySelector(".brand");
  var dark = document.querySelector(".logo-dark");
  var light = document.querySelector(".logo-light");

  function loaded(img) { return !!img && img.complete && img.naturalWidth > 0; }

  function syncLogo() {
    var isLight = root.getAttribute("data-theme") === "light";
    if (dark) dark.hidden = !(!isLight && loaded(dark));
    if (light) light.hidden = !(isLight && loaded(light));
    if (brand) brand.classList.toggle("has-logo", isLight ? loaded(light) : loaded(dark));
  }

  function syncLabel() {
    if (btn) btn.textContent = root.getAttribute("data-theme") === "light" ? "Dark theme" : "Light theme";
  }

  if (btn) {
    btn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("kyc-theme", next); } catch (e) { /* storage can be blocked */ }
      syncLabel();
      syncLogo();
    });
  }
  [dark, light].forEach(function (img) { if (img) img.addEventListener("load", syncLogo); });
  syncLabel();
  syncLogo();

  var copyBtn = document.getElementById("copy");
  var pre = document.getElementById("pintext");
  var note = document.getElementById("copied");

  function done(msg) {
    if (!note) return;
    note.textContent = msg;
    setTimeout(function () { note.textContent = ""; }, 2500);
  }

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    done(ok ? "Copied" : "Select the text and copy it by hand");
  }

  if (copyBtn && pre) {
    copyBtn.addEventListener("click", function () {
      var text = pre.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done("Copied"); }, function () { fallbackCopy(text); });
      } else {
        fallbackCopy(text);
      }
    });
  }
})();
