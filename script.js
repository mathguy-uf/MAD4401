const menuButton = document.getElementById('menuButton');
const siteNav = document.getElementById('siteNav');

if (menuButton && siteNav) {
  menuButton.addEventListener('click', () => {
    const isOpen = siteNav.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });

  siteNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      siteNav.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
    });
  });
}

const courseModules = {
  module1Resources: [
    {
      number: '01',
      title: 'Taylor Series and Error',
      description: 'Taylor polynomials, Lagrange remainder, error bounds, and choosing a degree for a target tolerance.',
      path: 'module_1/01_taylor_series.ipynb',
    },
    {
      number: '02',
      title: 'Floating-Point Arithmetic',
      description: 'Finite-digit arithmetic, fl notation, chopping, rounding, IEEE-754, ULPs, and cancellation.',
      path: 'module_1/02_floating_point_and_error.ipynb',
    },
    {
      number: '03',
      title: 'Bisection Method',
      description: 'IVT, Rolle and uniqueness ideas, the bisection algorithm, error bounds, and iteration counts.',
      path: 'module_1/03_bisection_method.ipynb',
    },
    {
      number: '04',
      title: 'Fixed Points and Cobwebs',
      description: 'Fixed-point iteration, convergence hypotheses, derivative bounds, and cobweb diagrams.',
      path: 'module_1/04_fixed_point_cobwebs.ipynb',
    },
    {
      number: '05',
      title: "Newton's Method",
      description: 'Tangent-line derivation, implementation, graphical interpretation, and common failure modes.',
      path: 'module_1/05_newton_method.ipynb',
    },
    {
      number: '06',
      title: 'Order of Convergence',
      description: 'Big-O notation, linear and quadratic convergence, asymptotic constants, and observed order.',
      path: 'module_1/06_order_of_convergence.ipynb',
    },
  ],

  module2Resources: [
    {
      number: '01',
      title: 'Lagrange Interpolation',
      description: 'Lagrange basis polynomials, uniqueness, degree at most n, and interpolation error.',
      path: 'module_2/01_lagrange_interpolation.ipynb',
    },
    {
      number: '02',
      title: 'Degree-10 LIP vs. Taylor',
      description: 'Compare two degree-10 approximations of 1/(1+x²) on [-1, 1] and inspect their errors.',
      path: 'module_2/02_lip_vs_taylor.ipynb',
    },
    {
      number: '03',
      title: 'Newton Divided Differences',
      description: 'Build and evaluate Newton-form interpolation using a divided-difference table.',
      path: 'module_2/03_newton_divided_differences.ipynb',
    },
    {
      number: '04',
      title: "Neville's Method",
      description: 'Construct the recursive Neville table step by step and connect it to the unique interpolant.',
      path: 'module_2/04_neville_method.ipynb',
    },
    {
      number: '05',
      title: 'Least-Squares Best Fit',
      description: 'Normal equations, constrained models, residual sums of squares, and R² model comparison.',
      path: 'module_2/05_least_squares_best_fit.ipynb',
    },
    {
      number: '06',
      title: 'Numerical Differentiation',
      description: 'Forward, backward, and centered differences plus differentiation of an interpolating polynomial.',
      path: 'module_2/06_numerical_differentiation.ipynb',
    },
    {
      number: '07',
      title: 'Riemann Sums',
      description: 'Left, right, and midpoint rules with geometric visualization and convergence behavior.',
      path: 'module_2/07_riemann_sums.ipynb',
    },
    {
      number: '08',
      title: "Trapezoidal and Simpson's Rules",
      description: 'Single and composite quadrature rules, error bounds, and choosing n for a target accuracy.',
      path: 'module_2/08_trapezoidal_simpson.ipynb',
    },
  ],

  module3Resources: [
    {
      number: '00',
      title: 'IVP Foundations',
      description: 'Lipschitz conditions, existence and uniqueness, perturbations, and well-posedness.',
      path: 'module_3/00_ivp_foundations.ipynb',
    },
    {
      number: '01',
      title: 'Direction Fields and Autonomous ODEs',
      description: 'Direction fields, equilibria, stability, basins of attraction, and phase-line behavior.',
      path: 'module_3/01_direction_fields_autonomous_odes.ipynb',
    },
    {
      number: '02',
      title: "Euler's Method",
      description: 'Derive Euler geometrically, implement it, compare with exact solutions, and reuse Euler data.',
      path: 'module_3/02_euler_method.ipynb',
    },
    {
      number: '03',
      title: "Error in Euler's Method",
      description: 'One-step defect, local truncation error, global error, and first-order convergence.',
      path: 'module_3/03_euler_error.ipynb',
    },
    {
      number: '04',
      title: 'Higher-Order Taylor Methods',
      description: 'Taylor methods of orders 2, 3, and 4 with local truncation error and convergence studies.',
      path: 'module_3/04_taylor_methods.ipynb',
    },
    {
      number: '05',
      title: 'Runge–Kutta: RK2 and RK3',
      description: 'Improved Euler, midpoint RK2, Heun RK3, and numerical order comparisons.',
      path: 'module_3/05_rk2_rk3.ipynb',
    },
    {
      number: '06',
      title: 'Classical RK4',
      description: 'The four-stage RK4 method, a full worked step, and fourth-order convergence.',
      path: 'module_3/06_rk4.ipynb',
    },
    {
      number: '07',
      title: 'Adaptive RK23 and Method Comparison',
      description: 'Brin-style adaptive RK23 plus a common-IVP comparison of all major methods in the course.',
      path: 'module_3/07_rk23_and_method_comparison.ipynb',
    },
  ],
};

function notebookLinks(path) {
  const encodedPath = path
    .split('/')
    .map(encodeURIComponent)
    .join('/');

  return {
    github: `https://github.com/mathguy-uf/MAD4401/blob/main/${encodedPath}`,
    colab: `https://colab.research.google.com/github/mathguy-uf/MAD4401/blob/main/${encodedPath}`,
    binder: `https://mybinder.org/v2/gh/mathguy-uf/MAD4401/main?urlpath=lab/tree/${encodedPath}`,
  };
}

function makeResourceCard(resource) {
  const links = notebookLinks(resource.path);
  const card = document.createElement('article');

  card.className = 'resource-card';
  card.innerHTML = `
    <div class="resource-top">
      <span class="chapter">${resource.number}</span>
      <span class="available-label">Available</span>
    </div>
    <h3>${resource.title}</h3>
    <p>${resource.description}</p>
    <div class="notebook-actions">
      <a href="${links.github}">View on GitHub</a>
      <a href="${links.colab}">Run in Colab</a>
      <a href="${links.binder}">Launch Binder</a>
    </div>
  `;

  return card;
}

Object.entries(courseModules).forEach(([containerId, resources]) => {
  const container = document.getElementById(containerId);

  if (!container) {
    return;
  }

  resources.forEach((resource) => {
    container.appendChild(makeResourceCard(resource));
  });
});
