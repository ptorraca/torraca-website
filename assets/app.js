// Torraca Electrical — minimal interactions
(function(){
  // Mobile nav
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.nav');
  if(burger && nav){
    burger.addEventListener('click', function(){
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded','false');
        document.body.style.overflow = '';
      });
    });
  }

  // Dropdown nav (click to toggle; hover handles desktop via CSS)
  var toggles = document.querySelectorAll('.navtoggle');
  toggles.forEach(function(btn){
    btn.addEventListener('click', function(e){
      e.preventDefault();
      var item = btn.closest('.navitem');
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.navitem.open').forEach(function(i){
        i.classList.remove('open');
        var t = i.querySelector('.navtoggle'); if(t) t.setAttribute('aria-expanded','false');
      });
      document.querySelectorAll('.subitem.open').forEach(function(s){
        s.classList.remove('open');
        var st = s.querySelector('.subtoggle'); if(st) st.setAttribute('aria-expanded','false');
      });
      if(!isOpen){ item.classList.add('open'); btn.setAttribute('aria-expanded','true'); }
    });
  });
  // Second tier: services stay hidden until a customer type is selected
  function closeSubs(scope){
    (scope||document).querySelectorAll('.subitem.open').forEach(function(s){
      s.classList.remove('open');
      var t = s.querySelector('.subtoggle'); if(t) t.setAttribute('aria-expanded','false');
    });
  }
  document.querySelectorAll('.subtoggle').forEach(function(btn){
    btn.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      var item = btn.closest('.subitem');
      var isOpen = item.classList.contains('open');
      closeSubs(item.parentNode);
      if(!isOpen){ item.classList.add('open'); btn.setAttribute('aria-expanded','true'); }
    });
  });
  document.addEventListener('click', function(e){
    if(!e.target.closest('.navitem')){
      document.querySelectorAll('.navitem.open').forEach(function(i){
        i.classList.remove('open');
        var t = i.querySelector('.navtoggle'); if(t) t.setAttribute('aria-expanded','false');
      });
      closeSubs();
    }
  });

  // Home header: solid on scroll, translucent over the hero at the top
  var homeHdr = document.querySelector('body.home header.site');
  if(homeHdr){
    var onScroll = function(){ homeHdr.classList.toggle('scrolled', window.scrollY > 30); };
    window.addEventListener('scroll', onScroll, {passive:true});
    onScroll();
  }

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window && els.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, {threshold:0.12, rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(el){ io.observe(el); });
  } else {
    els.forEach(function(el){ el.classList.add('in'); });
  }

  // Quote form (no backend on the static build) — mailto fallback
  var form = document.getElementById('quoteform');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var d = new FormData(form);
      var body = 'Name: '+(d.get('name')||'')+'\nPhone: '+(d.get('phone')||'')
        +'\nSuburb: '+(d.get('suburb')||'')+'\nService: '+(d.get('service')||'')
        +'\n\n'+(d.get('message')||'');
      window.location.href = 'mailto:info@torracaelectrical.com.au?subject='
        + encodeURIComponent('Website quote request')
        + '&body=' + encodeURIComponent(body);
    });
  }
})();
