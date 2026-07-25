/**
 * app.js — Frontend JavaScript
 * ==============================
 *
 * WHY VANILLA JAVASCRIPT (no jQuery, no React)?
 *   In 2024+, modern browsers have excellent built-in JavaScript APIs.
 *   Learning vanilla JS first gives you a solid foundation before
 *   learning frameworks (React, Vue, etc.).
 *   This also keeps the project lightweight — no dependencies.
 *
 * WHAT THIS FILE DOES:
 *   1. Delete confirmation modal (open, close, submit)
 *   2. Highlight active navigation link based on current URL
 *   3. Mobile hamburger menu toggle
 *   4. Auto-dismiss flash messages after 5 seconds
 *   5. Apply category colors dynamically via data-category attributes
 *   6. Live search debounce (prevents spamming the server on every keystroke)
 *   7. Form validation feedback
 *
 * JAVASCRIPT LESSON — "defer" attribute in <script>:
 *   We put the <script> tag at the BOTTOM of <body> in base.html.
 *   This ensures the HTML is fully loaded before JavaScript runs.
 *   If JavaScript runs before the HTML exists, it can't find elements!
 *
 * JAVASCRIPT LESSON — DOMContentLoaded:
 *   Even with the script at the bottom, best practice is to wrap code
 *   in DOMContentLoaded — it fires when all HTML is parsed and ready.
 */

'use strict';  // Enable strict mode: catches common JavaScript mistakes

// ── Run everything after the DOM is fully loaded ──────────────────────────────
document.addEventListener('DOMContentLoaded', function () {

  initNavActive();       // Highlight current page in nav
  initMobileNav();       // Hamburger menu for mobile
  initFlashMessages();   // Auto-dismiss notifications
  initCategoryColors();  // Apply category badge colors
  initSearchDebounce();  // Debounce the search input

});


/* ════════════════════════════════════════════════════════════════════════════
   1. DELETE CONFIRMATION MODAL
   ════════════════════════════════════════════════════════════════════════════
   Called from HTML onclick attribute:
   onclick="openDeleteModal('42', 'Morning Coffee')"
   ════════════════════════════════════════════════════════════════════════════ */

/**
 * Show the delete confirmation modal.
 *
 * @param {string} expenseId   - The expense's database ID
 * @param {string} expenseName - The expense's title (shown in modal)
 */
function openDeleteModal(expenseId, expenseName) {
  const modal = document.getElementById('deleteModal');
  const nameEl = document.getElementById('deleteExpenseName');
  const form = document.getElementById('deleteForm');

  if (!modal || !nameEl || !form) return;

  // Fill in the expense name so user knows what they're deleting
  nameEl.textContent = expenseName;

  // Set the form action to the correct delete URL
  // Flask's url_for() equivalent in JavaScript:
  form.action = `/delete/${expenseId}`;

  // Show the modal
  modal.classList.add('is-open');

  // Prevent background page from scrolling while modal is open
  document.body.style.overflow = 'hidden';

  // Trap focus inside modal for accessibility
  const firstFocusable = modal.querySelector('button, [href], input');
  if (firstFocusable) firstFocusable.focus();
}

/**
 * Close the delete confirmation modal.
 * Called by the "Cancel" button in the modal.
 */
function closeDeleteModal() {
  const modal = document.getElementById('deleteModal');
  if (!modal) return;

  modal.classList.remove('is-open');
  document.body.style.overflow = '';  // Restore scrolling
}

// Close modal when clicking the dark backdrop
document.addEventListener('click', function (event) {
  const modal = document.getElementById('deleteModal');
  if (modal && event.target === modal) {
    closeDeleteModal();
  }
});

// Close modal with Escape key (accessibility best practice)
document.addEventListener('keydown', function (event) {
  if (event.key === 'Escape') {
    closeDeleteModal();
  }
});


/* ════════════════════════════════════════════════════════════════════════════
   2. ACTIVE NAVIGATION LINK
   ════════════════════════════════════════════════════════════════════════════
   Detects the current URL path and adds 'active' class to the matching
   nav link so users know which page they're on.
   ════════════════════════════════════════════════════════════════════════════ */

function initNavActive() {
  // window.location.pathname = the URL path (e.g. "/expenses", "/create")
  const path = window.location.pathname;

  // data-page attribute maps link to route name
  const navLinks = document.querySelectorAll('.nav-link[data-page]');

  navLinks.forEach(function (link) {
    const page = link.getAttribute('data-page');

    // Determine if this link is "active" based on the current URL
    const isActive =
      (page === 'index'    && (path === '/' || path === '')) ||
      (page === 'expenses' && path.startsWith('/expenses')) ||
      (page === 'summary'  && path.startsWith('/summary'));

    if (isActive) {
      link.classList.add('active');
    }
  });
}


/* ════════════════════════════════════════════════════════════════════════════
   3. MOBILE NAVIGATION (Hamburger Menu)
   ════════════════════════════════════════════════════════════════════════════ */

function initMobileNav() {
  const toggle = document.getElementById('navToggle');
  const links  = document.getElementById('navLinks');

  if (!toggle || !links) return;

  toggle.addEventListener('click', function () {
    const isOpen = links.classList.toggle('is-open');

    // Update aria-expanded for accessibility
    toggle.setAttribute('aria-expanded', String(isOpen));

    // Animate hamburger → X
    const lines = toggle.querySelectorAll('.hamburger-line');
    if (isOpen) {
      lines[0].style.transform = 'translateY(7px) rotate(45deg)';
      lines[1].style.opacity = '0';
      lines[2].style.transform = 'translateY(-7px) rotate(-45deg)';
    } else {
      lines[0].style.transform = '';
      lines[1].style.opacity = '';
      lines[2].style.transform = '';
    }
  });

  // Close nav when a link is clicked (on mobile)
  links.querySelectorAll('.nav-link').forEach(function (link) {
    link.addEventListener('click', function () {
      links.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}


/* ════════════════════════════════════════════════════════════════════════════
   4. AUTO-DISMISS FLASH MESSAGES
   ════════════════════════════════════════════════════════════════════════════
   Flash messages fade out automatically after 5 seconds.
   Users can also close them manually with the × button.
   ════════════════════════════════════════════════════════════════════════════ */

function initFlashMessages() {
  const flashes = document.querySelectorAll('.flash');

  flashes.forEach(function (flash) {
    // Auto-remove after 5 seconds (5000 milliseconds)
    const DISMISS_DELAY = 5000;

    setTimeout(function () {
      // Fade out animation before removing from DOM
      flash.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
      flash.style.opacity = '0';
      flash.style.transform = 'translateX(20px)';

      // Remove from DOM after animation finishes
      setTimeout(function () {
        if (flash.parentNode) {
          flash.remove();
        }
      }, 400);
    }, DISMISS_DELAY);
  });
}


/* ════════════════════════════════════════════════════════════════════════════
   5. CATEGORY COLORS (Applied via CSS, using data-category attribute)
   ════════════════════════════════════════════════════════════════════════════
   CSS handles the badge colors using [data-category="Food"] attribute selectors.
   The mini-card top strips in summary.html need JavaScript for dynamic backgrounds.
   ════════════════════════════════════════════════════════════════════════════ */

// Category color map — matches the CSS variables in style.css
const CATEGORY_COLORS = {
  'Food':           { bg: '#fff7ed', border: '#fed7aa', text: '#c2410c' },
  'Transportation': { bg: '#eff6ff', border: '#bfdbfe', text: '#1d4ed8' },
  'Shopping':       { bg: '#fdf4ff', border: '#f0abfc', text: '#a21caf' },
  'Bills':          { bg: '#fef2f2', border: '#fecaca', text: '#b91c1c' },
  'Entertainment':  { bg: '#f5f3ff', border: '#ddd6fe', text: '#6d28d9' },
  'Education':      { bg: '#ecfeff', border: '#a5f3fc', text: '#0e7490' },
  'Other':          { bg: '#f9fafb', border: '#e5e7eb', text: '#374151' },
};

function initCategoryColors() {
  // Style the mini-card tops in summary.html
  document.querySelectorAll('.mini-card-top[data-category]').forEach(function (el) {
    const category = el.getAttribute('data-category');
    const colors = CATEGORY_COLORS[category];
    if (colors) {
      el.style.backgroundColor = colors.bg;
      el.style.borderBottomColor = colors.border;
    }
  });

  // Add category-specific border-left to summary-category-item
  document.querySelectorAll('.summary-category-item').forEach(function (item) {
    const badge = item.querySelector('[data-category]');
    if (badge) {
      const category = badge.getAttribute('data-category');
      const colors = CATEGORY_COLORS[category];
      if (colors) {
        item.style.borderLeft = `3px solid ${colors.border}`;
        item.style.paddingLeft = '16px';
      }
    }
  });
}


/* ════════════════════════════════════════════════════════════════════════════
   6. SEARCH DEBOUNCE
   ════════════════════════════════════════════════════════════════════════════
   WHAT IS DEBOUNCE?
   Without debounce: Every keystroke sends a server request.
   Typing "coffee" = 6 requests (c, co, cof, coff, coffe, coffee)

   With debounce:    Wait 400ms after the user STOPS typing, then search.
   Typing "coffee" = 1 request (after they finish typing)

   This saves server resources and makes the search feel smoother.

   REAL-WORLD USE:
   Google Search, GitHub search, Notion search — all use debounce.
   ════════════════════════════════════════════════════════════════════════════ */

function initSearchDebounce() {
  const searchInput = document.getElementById('search');
  if (!searchInput) return;

  let debounceTimer;
  const DEBOUNCE_DELAY = 400; // milliseconds

  searchInput.addEventListener('input', function () {
    // Cancel the previous timer if user keeps typing
    clearTimeout(debounceTimer);

    // Set a new timer — only fires if user pauses for 400ms
    debounceTimer = setTimeout(function () {
      // Submit the parent form to trigger a search
      const form = searchInput.closest('form');
      if (form) form.submit();
    }, DEBOUNCE_DELAY);
  });
}


/* ════════════════════════════════════════════════════════════════════════════
   7. FORM VALIDATION FEEDBACK
   ════════════════════════════════════════════════════════════════════════════
   Adds visual feedback (red border + shake animation) when the user
   tries to submit an empty required field.

   We use novalidate on the form to disable browser's default validation
   UI, so we can provide our own styled version.
   ════════════════════════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('expenseForm');
  if (!form) return;

  form.addEventListener('submit', function (event) {
    const requiredFields = form.querySelectorAll('[required]');
    let hasError = false;

    requiredFields.forEach(function (field) {
      if (!field.value.trim()) {
        // Visual feedback: red border
        field.classList.add('input-error');
        hasError = true;

        // Remove error styling when user starts typing
        field.addEventListener('input', function () {
          field.classList.remove('input-error');
        }, { once: true });
      }
    });

    if (hasError) {
      // Prevent form submission
      event.preventDefault();

      // Scroll to first error
      const firstError = form.querySelector('.input-error');
      if (firstError) {
        firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        firstError.focus();
      }
    }
  });
});

// Add CSS for error state (injected via JS to keep style.css clean)
(function addErrorStyles() {
  const style = document.createElement('style');
  style.textContent = `
    .input-error {
      border-color: #ef4444 !important;
      box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.12) !important;
      animation: shake 0.3s ease;
    }
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      25%       { transform: translateX(-4px); }
      75%       { transform: translateX(4px); }
    }
  `;
  document.head.appendChild(style);
})();
