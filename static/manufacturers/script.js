  document.addEventListener('DOMContentLoaded', function () {
    const utilitySelect = document.getElementById('id_utility_type');
    const otherFieldDiv = document.getElementById('other-field');

    function toggleOtherField() {
      if (utilitySelect.value === 'other') {
        otherFieldDiv.style.display = 'block';
      } else {
        otherFieldDiv.style.display = 'none';
        const input = otherFieldDiv.querySelector('input');
        if (input) input.value = ''; // Optional: clear input if hidden
      }
    }

    // Run on page load and on change
    toggleOtherField();
    utilitySelect.addEventListener('change', toggleOtherField);
  });
