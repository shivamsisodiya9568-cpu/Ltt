
Action: file_editor create /app/website/script.js --file-text "/* =====================================================================
   TAAU DAARU BAAZ BEER SHOP — Interactive Script
   Features: Loader, Nav, Mobile menu, Search, Filter, Sliders,
             Animated counters, Scroll reveal, Scroll-top, Form validation,
             FAQ accordion, Age gate, Toast, Modal
   ===================================================================== */
(function () {
  'use strict';

  /* ---------------- Helpers ---------------- */
  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  const on = (el, ev, fn, opt) => el && el.addEventListener(ev, fn, opt);

  /* ---------------- Loader ---------------- */
  window.addEventListener('load', () => {
    const loader = $('.loader');
    if (!loader) return;
    setTimeout(() => loader.classList.add('hidden'), 2200);
  });

  /* ---------------- Age Gate ---------------- */
  function initAgeGate() {
    const gate = $('.age-gate');
    if (!gate) return;
    const accepted = localStorage.getItem('tdb_age_ok');
    if (accepted === '1') { gate.classList.add('hidden'); return; }

    on($('[data-age-yes]'), 'click', () => {
      localStorage.setItem('tdb_age_ok', '1');
      gate.classList.add('hidden');
      toast('Welcome back, connoisseur.', 'check');
    });
    on($('[data-age-no]'), 'click', () => {
      window.location.href = 'https://www.google.com';
    });
  }

  /* ---------------- Header scroll ---------------- */
  function initHeader() {
    const header = $('.header');
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 30);
    onScroll();
    on(window, 'scroll', onScroll, { passive: true });
  }

  /* ---------------- Mobile Menu ---------------- */
  function initMobileMenu() {
    const burger = $('.hamburger');
    const menu = $('.mobile-menu');
    if (!burger || !menu) return;
    on(burger, 'click', () => {
      const open = menu.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    $$('.mobile-menu a').forEach(a => on(a, 'click', () => {
      menu.classList.remove('is-open');
      burger.classList.remove('is-open');
      document.body.style.overflow = '';
    }));
  }

  /* ---------------- Smooth Scroll ---------------- */
  function initSmoothScroll() {
    $$('a[href^=\"#\"]').forEach(a => on(a, 'click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = $(id);
      if (target) {
        e.preventDefault();
        const top = target.getBoundingClientRect().top + window.scrollY - 70;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    }));
  }

  /* ---------------- Scroll-Top ---------------- */
  function initScrollTop() {
    const btn = $('.scroll-top');
    if (!btn) return;
    on(window, 'scroll', () => btn.classList.toggle('visible', window.scrollY > 400), { passive: true });
    on(btn, 'click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ---------------- Reveal on Scroll ---------------- */
  function initReveal() {
    const els = $$('.reveal, .reveal-left, .reveal-right, .reveal-stagger');
    if (!('IntersectionObserver' in window)) {
      els.forEach(el => el.classList.add('is-visible'));
      return;
    }
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    els.forEach(el => io.observe(el));
  }

  /* ---------------- Animated Counters ---------------- */
  function initCounters() {
    const counters = $$('[data-counter]');
    if (!counters.length) return;
    const animate = (el) => {
      const end = parseFloat(el.dataset.counter);
      const dur = parseInt(el.dataset.duration || '2000', 10);
      const start = performance.now();
      const update = (now) => {
        const p = Math.min((now - start) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        const val = end * eased;
        el.textContent = end >= 100 ? Math.floor(val).toLocaleString() : val.toFixed(1);
        if (p < 1) requestAnimationFrame(update);
        else el.textContent = end >= 100 ? Math.floor(end).toLocaleString() : end.toString();
      };
      requestAnimationFrame(update);
    };
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { animate(entry.target); io.unobserve(entry.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(el => io.observe(el));
  }

  /* ---------------- Product Search + Filter ---------------- */
  function initProductFilter() {
    const grid = $('#productGrid');
    if (!grid) return;
    const products = $$('.product', grid);
    const chips = $$('.chip[data-filter]');
    const searchInput = $('#productSearch');
    const empty = $('#productEmpty');

    let activeFilter = 'all';
    let query = '';

    const apply = () => {
      let shown = 0;
      products.forEach(p => {
        const cat = (p.dataset.category || '').toLowerCase();
        const name = (p.dataset.name || '').toLowerCase();
        const matchCat = activeFilter === 'all' || cat.includes(activeFilter);
        const matchQuery = !query || name.includes(query) || cat.includes(query);
        const visible = matchCat && matchQuery;
        p.style.display = visible ? '' : 'none';
        if (visible) shown++;
      });
      if (empty) empty.style.display = shown === 0 ? 'block' : 'none';
    };

    chips.forEach(chip => on(chip, 'click', () => {
      chips.forEach(c => c.classList.remove('is-active'));
      chip.classList.add('is-active');
      activeFilter = chip.dataset.filter;
      apply();
    }));

    if (searchInput) {
      on(searchInput, 'input', (e) => {
        query = e.target.value.trim().toLowerCase();
        apply();
      });
    }
  }

  /* ---------------- Favorite toggle ---------------- */
  function initFavorites() {
    $$('.product-fav').forEach(btn => on(btn, 'click', e => {
      e.preventDefault(); e.stopPropagation();
      const active = btn.classList.toggle('is-active');
      const icon = btn.querySelector('i');
      if (icon) icon.className = active ? 'fa-solid fa-heart' : 'fa-regular fa-heart';
      toast(active ? 'Added to favorites' : 'Removed from favorites', active ? 'heart' : 'xmark');
    }));
  }

  /* ---------------- Add to Cart ---------------- */
  function initCart() {
    let count = 0;
    const counter = $('[data-cart-count]');
    $$('[data-add-cart]').forEach(btn => on(btn, 'click', e => {
      e.preventDefault(); e.stopPropagation();
      count++;
      if (counter) { counter.textContent = count; counter.classList.add('pulse'); setTimeout(() => counter.classList.remove('pulse'), 400); }
      toast('Added to cart', 'cart-plus');
    }));
  }

  /* ---------------- Testimonial Slider ---------------- */
  function initTestiSlider() {
    const track = $('.testi-track');
    const dotsWrap = $('.testi-controls');
    if (!track || !dotsWrap) return;
    const cards = $$('.testi-card', track);
    const perView = () => window.innerWidth < 768 ? 1 : window.innerWidth < 1024 ? 2 : 3;
    let slides = Math.max(1, Math.ceil(cards.length / perView()));
    let i = 0;
    let timer;

    const buildDots = () => {
      dotsWrap.innerHTML = '';
      slides = Math.max(1, Math.ceil(cards.length / perView()));
      for (let n = 0; n < slides; n++) {
        const d = document.createElement('span');
        d.className = 'testi-dot' + (n === 0 ? ' is-active' : '');
        d.setAttribute('role', 'button');
        d.setAttribute('aria-label', 'Slide ' + (n + 1));
        on(d, 'click', () => go(n));
        dotsWrap.appendChild(d);
      }
    };
    const update = () => {
      const cardW = cards[0].getBoundingClientRect().width + 26;
      track.style.transform = `translateX(-${i * cardW * perView()}px)`;
      $$('.testi-dot', dotsWrap).forEach((d, idx) => d.classList.toggle('is-active', idx === i));
    };
    const go = (n) => { i = (n + slides) % slides; update(); };
    const next = () => go(i + 1);

    buildDots(); update();
    const start = () => { stop(); timer = setInterval(next, 5500); };
    const stop = () => timer && clearInterval(timer);
    start();
    on(track, 'mouseenter', stop); on(track, 'mouseleave', start);

    let resizeT;
    on(window, 'resize', () => { clearTimeout(resizeT); resizeT = setTimeout(() => { i = 0; buildDots(); update(); }, 200); });
  }

  /* ---------------- FAQ Accordion ---------------- */
  function initFAQ() {
    $$('.faq-item').forEach(item => {
      const q = $('.faq-q', item);
      on(q, 'click', () => {
        const isOpen = item.classList.contains('is-open');
        $$('.faq-item.is-open').forEach(i => i.classList.remove('is-open'));
        if (!isOpen) item.classList.add('is-open');
      });
    });
  }

  /* ---------------- Contact Form Validation ---------------- */
  function initContactForm() {
    const form = $('#contactForm');
    if (!form) return;
    const status = $('.form-status', form);

    const validators = {
      name: v => v.trim().length >= 2 || 'Please enter your full name.',
      email: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || 'Please enter a valid email.',
      phone: v => /^\+?\d[\d\s-]{7,15}$/.test(v) || 'Please enter a valid phone number.',
      subject: v => v.trim().length >= 2 || 'Please select a subject.',
      message: v => v.trim().length >= 10 || 'Message must be at least 10 characters.'
    };

    const validateField = (input) => {
      const name = input.name;
      const errEl = input.parentElement.querySelector('.form-error');
      const result = validators[name] ? validators[name](input.value) : true;
      const ok = result === true;
      if (errEl) errEl.textContent = ok ? '' : result;
      input.style.borderColor = ok ? '' : 'var(--danger)';
      return ok;
    };

    $$('input, select, textarea', form).forEach(inp => {
      on(inp, 'blur', () => validateField(inp));
      on(inp, 'input', () => { if (inp.style.borderColor) validateField(inp); });
    });

    on(form, 'submit', e => {
      e.preventDefault();
      let ok = true;
      $$('input, select, textarea', form).forEach(inp => { if (!validateField(inp)) ok = false; });
      if (!ok) {
        if (status) { status.className = 'form-status error'; status.textContent = 'Please fix the highlighted fields.'; }
        return;
      }
      if (status) { status.className = 'form-status success'; status.textContent = 'Cheers! Your message has been received. We will reach out within 24 hours.'; }
      form.reset();
      toast('Message sent — Cheers!', 'check');
      setTimeout(() => { if (status) status.style.display = 'none'; }, 6000);
    });
  }

  /* ---------------- Newsletter ---------------- */
  function initNewsletter() {
    const form = $('#newsletterForm');
    if (!form) return;
    on(form, 'submit', e => {
      e.preventDefault();
      const email = form.querySelector('input').value.trim();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        toast('Please enter a valid email.', 'triangle-exclamation');
        return;
      }
      form.reset();
      toast('Subscribed! Welcome to the Daaru club.', 'champagne-glasses');
    });
  }

  /* ---------------- Quick View Modal ---------------- */
  function initModal() {
    const modal = $('#productModal');
    if (!modal) return;
    const img = $('.modal-img img', modal);
    const title = $('[data-mt-name]', modal);
    const cat = $('[data-mt-cat]', modal);
    const price = $('[data-mt-price]', modal);
    const desc = $('[data-mt-desc]', modal);

    $$('[data-quick-view]').forEach(btn => on(btn, 'click', e => {
      e.preventDefault(); e.stopPropagation();
      const card = btn.closest('.product');
      if (!card) return;
      img.src = card.querySelector('img').src;
      title.textContent = card.dataset.name || '';
      cat.textContent = card.dataset.category || '';
      price.textContent = card.dataset.price || '';
      desc.textContent = card.dataset.desc || '';
      modal.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }));
    const close = () => { modal.classList.remove('is-open'); document.body.style.overflow = ''; };
    on($('.modal-close', modal), 'click', close);
    on(modal, 'click', e => { if (e.target === modal) close(); });
    on(document, 'keydown', e => { if (e.key === 'Escape') close(); });
  }

  /* ---------------- Toast ---------------- */
  let toastEl;
  function toast(msg, icon = 'circle-info') {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      document.body.appendChild(toastEl);
    }
    toastEl.innerHTML = `<i class=\"fa-solid fa-${icon}\"></i> <span>${msg}</span>`;
    toastEl.classList.add('show');
    clearTimeout(toast._t);
    toast._t = setTimeout(() => toastEl.classList.remove('show'), 2600);
  }

  /* ---------------- Year stamp ---------------- */
  function initYear() {
    const y = new Date().getFullYear();
    $$('[data-year]').forEach(el => el.textContent = y);
  }

  /* ---------------- Parallax on hero ---------------- */
  function initParallax() {
    const art = $('.hero-art');
    if (!art) return;
    on(window, 'mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 18;
      const y = (e.clientY / window.innerHeight - 0.5) * 18;
      art.style.transform = `translate3d(${x}px, ${y}px, 0)`;
    });
  }

  /* ---------------- Init ---------------- */
  document.addEventListener('DOMContentLoaded', () => {
    initAgeGate();
    initHeader();
    initMobileMenu();
    initSmoothScroll();
    initScrollTop();
    initReveal();
    initCounters();
    initProductFilter();
    initFavorites();
    initCart();
    initTestiSlider();
    initFAQ();
    initContactForm();
    initNewsletter();
    initModal();
    initYear();
    initParallax();
  });
})();
"
Observation: Create successful: /app/website/script.js
