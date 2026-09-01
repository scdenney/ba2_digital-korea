(function () {
  var button = document.querySelector('.nav-toggle');
  var navigation = document.querySelector('.site-nav');
  var dropdowns = document.querySelectorAll('.nav-dropdown');

  if (button && navigation) {
    button.addEventListener('click', function () {
      var isOpen = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!isOpen));
      navigation.classList.toggle('is-open', !isOpen);
      if (isOpen) {
        dropdowns.forEach(function (dropdown) { dropdown.removeAttribute('open'); });
      }
    });
  }

  document.addEventListener('click', function (event) {
    dropdowns.forEach(function (dropdown) {
      if (dropdown.hasAttribute('open') && !dropdown.contains(event.target)) {
        dropdown.removeAttribute('open');
      }
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    dropdowns.forEach(function (dropdown) {
      if (dropdown.hasAttribute('open')) {
        dropdown.removeAttribute('open');
        dropdown.querySelector('summary').focus();
      }
    });
  });

  document.querySelectorAll('main table').forEach(function (table) {
    if (table.parentElement && table.parentElement.classList.contains('table-wrap')) return;
    var wrapper = document.createElement('div');
    wrapper.className = 'table-wrap';
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });

  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.page-toc a[href^="#"]'));
  if (tocLinks.length === 0) return;

  var linkById = {};
  tocLinks.forEach(function (link) {
    var id = decodeURIComponent(link.getAttribute('href').slice(1));
    if (id) linkById[id] = link;
  });

  var headings = Array.prototype.slice
    .call(document.querySelectorAll('h1[id], h2[id], h3[id], h4[id]'))
    .filter(function (heading) { return Object.prototype.hasOwnProperty.call(linkById, heading.id); });
  if (headings.length === 0) return;

  var activeLink = null;
  function updateToc() {
    var current = headings[0];
    headings.forEach(function (heading) {
      if (heading.getBoundingClientRect().top <= 120) current = heading;
    });
    if (linkById[current.id] === activeLink) return;
    activeLink = linkById[current.id];
    tocLinks.forEach(function (link) { link.classList.toggle('is-active', link === activeLink); });
  }

  window.addEventListener('scroll', updateToc, { passive: true });
  window.addEventListener('resize', updateToc, { passive: true });
  updateToc();
})();
