function(t) {
  document.querySelectorAll(".js-section-link.is-active").forEach(function(link) {
    link.classList.remove("is-active");
  });

  if (t) {
    document.querySelectorAll(".js-section-link").forEach(function(link) {
      if (link.href.replace(/^.*\/\/[^\/]+/, "").includes(t)) {
        link.classList.add("is-active");
      }
    });
  }
}