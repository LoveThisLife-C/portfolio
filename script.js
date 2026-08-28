(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".nav-toggle");
  const mobileNav = document.querySelector("#mobile-nav");
  const progress = document.querySelector("#progress-fill");
  const progressRadial = document.querySelector("#progress-radial");
  const year = document.querySelector("#year");
  const heroScroll = document.querySelector(".hero-scroll");
  const heroCanvas = document.querySelector("#hero-canvas");
  const hero = document.querySelector("#hero");
  const heroCycle = document.querySelector("#hero-cycle");
  const skillNavBtns = [...document.querySelectorAll(".skill-nav__btn")];
  const skillDomains = [...document.querySelectorAll(".skill-domain")];
  const statValues = [...document.querySelectorAll(".stat__value [data-count]")];
  const workFilterBtns = [...document.querySelectorAll(".work-filter__btn")];
  const projectCards = [...document.querySelectorAll(".project[data-category]")];

  if (year) year.textContent = String(new Date().getFullYear());

  /* Hero load sequence */
  requestAnimationFrame(() => {
    document.body.classList.add("is-loaded");
  });

  /* Hero cycling specialties */
  const cyclePhrases = [
    "AI & Automation",
    "Full Stack Apps",
    "Shopify Stores",
    "Odoo ERP Systems",
    "Python Pipelines",
    "Bubble MVPs",
  ];
  let cycleIndex = 0;
  if (heroCycle && !reduceMotion) {
    setInterval(() => {
      heroCycle.classList.add("is-changing");
      setTimeout(() => {
        cycleIndex = (cycleIndex + 1) % cyclePhrases.length;
        heroCycle.textContent = cyclePhrases[cycleIndex];
        heroCycle.classList.remove("is-changing");
      }, 350);
    }, 3200);
  }

  /* Hero particle canvas — full viewport */
  if (heroCanvas && hero && !reduceMotion) {
    const ctx = heroCanvas.getContext("2d");
    let particles = [];
    let w = 0;
    let h = 0;
    let mouse = { x: -999, y: -999 };

    const resizeCanvas = () => {
      const rect = hero.getBoundingClientRect();
      w = heroCanvas.width = Math.floor(rect.width * devicePixelRatio);
      h = heroCanvas.height = Math.floor(rect.height * devicePixelRatio);
      heroCanvas.style.width = `${rect.width}px`;
      heroCanvas.style.height = `${rect.height}px`;
      const count = Math.min(56, Math.floor((rect.width * rect.height) / 18000));
      particles = Array.from({ length: count }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.25 * devicePixelRatio,
        vy: (Math.random() - 0.5) * 0.25 * devicePixelRatio,
        r: (Math.random() * 1.2 + 0.4) * devicePixelRatio,
      }));
    };

    const drawParticles = () => {
      if (!ctx) return;
      ctx.clearRect(0, 0, w, h);
      const mx = mouse.x * devicePixelRatio;
      const my = mouse.y * devicePixelRatio;

      particles.forEach((p) => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > w) p.vx *= -1;
        if (p.y < 0 || p.y > h) p.vy *= -1;

        const dx = p.x - mx;
        const dy = p.y - my;
        const dist = Math.hypot(dx, dy);
        if (dist < 120 * devicePixelRatio) {
          p.x += dx * 0.012;
          p.y += dy * 0.012;
        }

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(26, 92, 82, 0.35)";
        ctx.fill();
      });

      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const a = particles[i];
          const b = particles[j];
          const d = Math.hypot(a.x - b.x, a.y - b.y);
          if (d > 140 * devicePixelRatio) continue;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(26, 92, 82, ${0.12 * (1 - d / (140 * devicePixelRatio))})`;
          ctx.lineWidth = devicePixelRatio;
          ctx.stroke();
        }
      }
      requestAnimationFrame(drawParticles);
    };

    resizeCanvas();
    drawParticles();
    window.addEventListener("resize", resizeCanvas);
    hero.addEventListener("mousemove", (e) => {
      const rect = hero.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });
    hero.addEventListener("mouseleave", () => {
      mouse.x = -999;
      mouse.y = -999;
    });
  }

  /* Skill domain tabs */
  skillNavBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const target = btn.dataset.target;
      if (!target) return;
      skillNavBtns.forEach((b) => b.classList.toggle("is-active", b === btn));
      skillDomains.forEach((domain) => {
        domain.classList.toggle("is-active", domain.dataset.domain === target);
      });
    });
  });

  /* Stat counters */
  const animateCount = (el) => {
    const end = Number(el.dataset.count || 0);
    const suffix = el.dataset.suffix || "";
    const duration = 1200;
    const start = performance.now();
    const tick = (now) => {
      const p = Math.min(1, (now - start) / duration);
      const eased = 1 - (1 - p) ** 3;
      el.textContent = `${Math.round(end * eased)}${suffix}`;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  if (statValues.length && "IntersectionObserver" in window) {
    const statIo = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          animateCount(entry.target);
          statIo.unobserve(entry.target);
        });
      },
      { threshold: 0.5 }
    );
    statValues.forEach((el) => statIo.observe(el));
  } else {
    statValues.forEach((el) => {
      el.textContent = `${el.dataset.count}${el.dataset.suffix || ""}`;
    });
  }

  /* Work category filters */
  workFilterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const filter = btn.dataset.filter || "all";
      workFilterBtns.forEach((b) => b.classList.toggle("is-active", b === btn));
      projectCards.forEach((card) => {
        const match = filter === "all" || card.dataset.category === filter;
        card.classList.toggle("is-filtered-out", !match);
      });
    });
  });

  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  /* Kinetic word stagger */
  document.querySelectorAll("[data-kinetic]").forEach((el) => {
    if (el.dataset.kineticReady) return;
    const text = el.textContent.trim();
    el.textContent = "";
    el.classList.add("kinetic");
    text.split(/\s+/).forEach((token, i) => {
      const word = document.createElement("span");
      word.className = "word";
      word.style.setProperty("--i", String(i));
      word.textContent = token;
      el.appendChild(word);
      el.appendChild(document.createTextNode(" "));
    });
    el.dataset.kineticReady = "1";
  });

  document.querySelectorAll(".project").forEach((el, i) => {
    el.classList.remove("reveal--left", "reveal--right");
    el.classList.add("reveal");
    const media = el.querySelector(".project-media");
    const result = el.querySelector(".work-meta .work-result");
    if (media && result && !media.querySelector(".work-result")) {
      const badge = document.createElement("span");
      badge.className = "work-result";
      badge.textContent = result.textContent;
      media.appendChild(badge);
    }
  });

  document.querySelectorAll(".manifesto-card, .pillar, .skill-group").forEach((el, i) => {
    el.style.setProperty("--delay", `${(i % 4) * 90}ms`);
  });

  document.querySelectorAll(".solutions-flow .solution-card").forEach((el, i) => {
    el.style.setProperty("--delay", `${(i % 6) * 65}ms`);
  });

  document.querySelectorAll(".part-divider").forEach((el) => {
    if ("IntersectionObserver" in window) {
      const divIo = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) entry.target.classList.add("is-visible");
          });
        },
        { threshold: 0.6 }
      );
      divIo.observe(el);
    }
  });

  const onScroll = () => {
    const y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 16);
    if (heroScroll) heroScroll.style.opacity = String(clamp(1 - y / 260, 0, 1));

    const max = document.documentElement.scrollHeight - window.innerHeight;
    const pageP = max > 0 ? y / max : 0;
    if (progress) progress.style.width = `${pageP * 100}%`;
    if (progressRadial) progressRadial.style.strokeDashoffset = String(97.4 * (1 - pageP));

    let current = "";
    document.querySelectorAll("section[id], .part-block[id]").forEach((section) => {
      if (y >= section.offsetTop - 130) current = section.id;
    });
    document.querySelectorAll('.nav a[href^="#"]').forEach((link) => {
      link.classList.toggle("is-active", link.getAttribute("href") === `#${current}`);
    });

    if (!reduceMotion) {
      document.querySelectorAll(".hero-bg .hero-mesh, .hero-bg .hero-grid, .hero-bg .hero-aurora").forEach((layer, i) => {
        const speed = [0.08, 0.04, 0.02][i] || 0.04;
        layer.style.transform = `translate3d(0, ${y * speed}px, 0)`;
      });

      const portrait = document.querySelector("#hero-portrait img");
      if (portrait && hero) {
        const rect = hero.getBoundingClientRect();
        const p = clamp(-rect.top / rect.height, 0, 1);
        portrait.style.transform = `translateY(${p * 24}px)`;
      }

      document.querySelectorAll(".project.is-visible .project-media img").forEach((img) => {
        const parent = img.closest(".project");
        if (!parent) return;
        const rect = parent.getBoundingClientRect();
        const mid = rect.top + rect.height / 2 - window.innerHeight / 2;
        img.style.translate = `0 ${clamp(mid * -0.04, -18, 18)}px`;
      });
    }
  };

  let ticking = false;
  window.addEventListener(
    "scroll",
    () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        onScroll();
        ticking = false;
      });
    },
    { passive: true }
  );

  window.addEventListener("resize", () => {
    onScroll();
  });

  onScroll();

  if (toggle && mobileNav) {
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      toggle.setAttribute("aria-label", open ? "Open menu" : "Close menu");
      mobileNav.hidden = open;
    });
    mobileNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.hidden = true;
      });
    });
  }

  const reveals = [...document.querySelectorAll(".reveal")];
  reveals.forEach((el) => {
    const siblings = [...(el.parentElement?.children || [])].filter((c) =>
      c.classList.contains("reveal")
    );
    const i = Math.max(0, siblings.indexOf(el));
    el.style.setProperty("--delay", `${Math.min(i, 4) * 80}ms`);
  });

  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          if (entry.target.classList.contains("kinetic")) {
            entry.target.classList.add("is-inview");
          }
          io.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    reveals.forEach((el) => io.observe(el));

    const kineticIo = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) entry.target.classList.add("is-inview");
        });
      },
      { threshold: 0.35 }
    );
    document.querySelectorAll(".kinetic").forEach((el) => kineticIo.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
    document.querySelectorAll(".kinetic").forEach((el) => el.classList.add("is-inview"));
  }
})();
