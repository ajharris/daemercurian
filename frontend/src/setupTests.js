// src/setupTests.js
import '@testing-library/jest-dom';


// Mock `window.matchMedia` with `addEventListener` and `removeEventListener`
beforeAll(() => {
    Object.defineProperty(window, 'matchMedia', {
      writable: true,
      value: (query) => ({
        matches: query === '(prefers-color-scheme: dark)', // Default to dark for testing
        media: query,
        onchange: null,
        addEventListener: function (event, handler) {
          if (event === 'change') this.onchange = handler;
        },
        removeEventListener: function (event) {
          if (event === 'change') this.onchange = null;
        },
        addListener: function (handler) { // For older APIs, mock with same behavior
          this.onchange = handler;
        },
        removeListener: function () {
          this.onchange = null;
        },
        dispatchEvent: function (event) {
          if (event.type === 'change' && typeof this.onchange === 'function') {
            this.onchange(event);
          }
        }
      }),
    });
  });
  