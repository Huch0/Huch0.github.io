---
title: CV
permalink: /cv/
---

{%- assign en = '/assets/files/cv.pdf' | relative_url -%}
{%- assign kr = '/assets/files/cv-kr.pdf' | relative_url -%}

<p class="page-eyebrow">Curriculum Vitae</p>

<div class="cv-toolbar">
  <div class="cv-langs" role="group" aria-label="CV language">
    <button class="cv-lang-btn is-active" type="button" data-cv-lang="en">English</button>
    <button class="cv-lang-btn" type="button" data-cv-lang="kr">한국어</button>
  </div>
  <a class="btn-cv" id="cv-download" href="{{ en }}" target="_blank" rel="noopener">
    {% include icon.html name="download" %} Download PDF
  </a>
</div>

<div id="cv-viewer">
  <object class="cv-embed" data="{{ en }}" type="application/pdf" aria-label="Curriculum Vitae (PDF)">
    <div class="cv-fallback">
      <p>This browser can't display the embedded PDF (common on mobile).</p>
      <p><a href="{{ en }}">Download the CV as a PDF&nbsp;&rarr;</a></p>
    </div>
  </object>
</div>

<script>
  (function () {
    var urls = { en: "{{ en }}", kr: "{{ kr }}" };
    var viewer = document.getElementById('cv-viewer');
    var dl = document.getElementById('cv-download');
    var btns = document.querySelectorAll('.cv-lang-btn');
    function set(lang) {
      var url = urls[lang] || urls.en;
      // Recreate the <object> so the PDF actually reloads across browsers.
      viewer.innerHTML =
        '<object class="cv-embed" data="' + url + '" type="application/pdf" aria-label="Curriculum Vitae (PDF)">' +
        '<div class="cv-fallback"><p>This browser can\'t display the embedded PDF.</p>' +
        '<p><a href="' + url + '">Download the CV as a PDF &rarr;</a></p></div></object>';
      dl.setAttribute('href', url);
      btns.forEach(function (b) { b.classList.toggle('is-active', b.getAttribute('data-cv-lang') === lang); });
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function () { set(b.getAttribute('data-cv-lang')); });
    });
  })();
</script>
