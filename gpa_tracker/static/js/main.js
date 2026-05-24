// ===== 1. Auto hide alerts after 3 seconds =====
setTimeout(function () {
  var alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    alert.style.transition = 'opacity 0.6s ease';
    alert.style.opacity = '0';
    setTimeout(function () {
      alert.remove();
    }, 600);
  });
}, 3000);


// ===== 2. Live grade preview when typing marks =====
var marksInput = document.querySelector('input[name="marks"]');

if (marksInput) {
  marksInput.addEventListener('input', function () {
    var marks = parseFloat(this.value);
    var text = '';
    var color = '';

    if (marks >= 85) {
      text = 'Grade A — Excellent!';
      color = '#10b981';
    } else if (marks >= 70) {
      text = 'Grade B — Good';
      color = '#4f46e5';
    } else if (marks >= 55) {
      text = 'Grade C — Average';
      color = '#f59e0b';
    } else if (marks >= 40) {
      text = 'Grade D — Pass';
      color = '#6b7280';
    } else if (marks >= 0) {
      text = 'Grade F — Fail';
      color = '#ef4444';
    }

    // find or create the tip element
    var tip = document.getElementById('grade-tip');
    if (!tip) {
      tip = document.createElement('small');
      tip.id = 'grade-tip';
      tip.style.display = 'block';
      tip.style.marginTop = '4px';
      tip.style.fontWeight = '600';
      marksInput.parentNode.appendChild(tip);
    }

    tip.style.color = color;
    tip.textContent = text ? '→ ' + text : '';
  });
}


// ===== 3. Confirm before deleting =====
var deleteButtons = document.querySelectorAll('.btn-danger');
deleteButtons.forEach(function (btn) {
  btn.addEventListener('click', function (e) {
    var confirmed = confirm('Are you sure you want to delete this?');
    if (!confirmed) {
      e.preventDefault();
    }
  });
});