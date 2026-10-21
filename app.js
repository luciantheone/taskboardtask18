(function () {
  "use strict";
  var DATA = [
    { s: "no", l: "NOT NEEDED", w: "Hold or buy RBNT on an exchange", r: "Nothing is signed on Redbelly Network. Any ID check the exchange asks for is the exchange's own and separate.", src: "S1, S6" },
    { s: "no", l: "NOT NEEDED", w: "Hold wrapped RBNT on another chain", r: "The token lives on another chain. Redbelly access applies to your account on Redbelly Network.", src: "S1, S7" },
    { s: "unc", l: "UNCONFIRMED", w: "Bridge into Redbelly mainnet", r: "No official page says if a wallet must be enabled to receive bridged tokens. Enable the wallet first to be safe.", src: "S7" },
    { s: "yes", l: "NEEDED", w: "Bridge out of Redbelly mainnet", r: "You sign a transaction on Redbelly Network, and that needs write access.", src: "S1, S7" },
    { s: "yes", l: "NEEDED", w: "Send, swap or use apps on mainnet", r: "Users must claim an access credential, then enable their account with write access.", src: "S1, S2" },
    { s: "yes", l: "NEEDED", w: "Stake RBNT", r: "Staking is a deposit call on a mainnet contract, which is a transaction.", src: "S1, S5" }
  ];
  var btns = document.querySelectorAll(".chips button");
  var out = document.getElementById("result");

  function show(i) {
    var d = DATA[i];
    btns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-k") === String(i) ? "true" : "false"); });
    out.innerHTML = "";
    var big = document.createElement("p");
    big.className = "big status s-" + d.s;
    var dot = document.createElement("i");
    big.appendChild(dot);
    big.appendChild(document.createTextNode(d.l));
    var why = document.createElement("p");
    why.textContent = d.r;
    var src = document.createElement("p");
    src.className = "note";
    src.textContent = "Sources: " + d.src;
    out.appendChild(big);
    out.appendChild(why);
    out.appendChild(src);
  }
  btns.forEach(function (b) {
    b.addEventListener("click", function () { show(Number(b.getAttribute("data-k"))); });
  });


  // Logo slot: show the logo only if the file loaded, otherwise keep the text wordmark.
  var brand = document.querySelector(".brand");
  var logoImg = brand && brand.querySelector("img");
  function logoOk() { if (brand && logoImg && logoImg.currentSrc && logoImg.naturalWidth > 0) brand.classList.add("has-logo"); }
  if (logoImg) {
    if (logoImg.complete) logoOk(); else logoImg.addEventListener("load", logoOk);
    // picture source can change with the colour scheme
    if (window.matchMedia) {
      var mq = window.matchMedia("(prefers-color-scheme: light)");
      var re = function () { setTimeout(function () { brand.classList.remove("has-logo"); logoOk(); }, 50); };
      if (mq.addEventListener) mq.addEventListener("change", re);
    }
  }

  var copy = document.getElementById("copyShort");
  if (copy) {
    copy.addEventListener("click", function () {
      var t = document.getElementById("shortText").textContent;
      var done = function () { copy.textContent = "Copied"; setTimeout(function () { copy.textContent = "Copy text"; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(t).then(done, function () {});
      }
    });
  }
})();
