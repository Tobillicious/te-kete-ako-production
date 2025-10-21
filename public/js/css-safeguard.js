(function ensureProfessionalCss(){
  try {
    var hasProfessionalCss = !!document.querySelector('link[rel="stylesheet"][href="/css/te-kete-professional.css"], link[rel="stylesheet"][href$="te-kete-professional.css"]');
    if (!hasProfessionalCss) {
      var link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = '/css/te-kete-professional.css';
      (document.head || document.documentElement).appendChild(link);
    }
  } catch (e) {
    // no-op safeguard
  }
})();


