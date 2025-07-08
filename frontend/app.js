// app.js

// Check if user logged in; otherwise redirect to login page
const username = localStorage.getItem('nutriUser');
if (!username) {
  window.location.href = 'login.html';
}

document.getElementById('usernameDisplay').textContent = username;
document.getElementById('profileUsername').textContent = username;

const userId = username; // demo user_id from login

// Sidebar menu buttons
document.getElementById('menuProfile').addEventListener('click', () => {
  showSection('profileSection');
});
document.getElementById('menuHistory').addEventListener('click', () => {
  showSection('historySection');
  loadHistory();
});
document.getElementById('menuHelp').addEventListener('click', () => {
  showSection('helpSection');
});
document.getElementById('menuLogout').addEventListener('click', () => {
  localStorage.removeItem('nutriUser');
  window.location.href = 'login.html';
});

function showSection(id) {
  ['profileSection', 'historySection', 'helpSection'].forEach(s => {
    document.getElementById(s).classList.add('hidden');
  });
  document.getElementById(id).classList.remove('hidden');
  document.getElementById('result').textContent = '';
}

// Search functionality
document.getElementById('searchBtn').addEventListener('click', () => {
  const query = document.getElementById('searchInput').value.trim();
  if (!query) return alert('Please enter a product name!');
  analyzeProduct(query);
});

// Barcode scanning (simulate input)
document.getElementById('scanBtn').addEventListener('click', () => {
  const barcode = document.getElementById('barcodeInput').value.trim();
  if (!barcode) return alert('Please enter a barcode!');
  analyzeProductByBarcode(barcode);
});

// Simulate product analysis (replace with real API)
function analyzeProduct(name) {
  // Save to history
  saveHistory(name);

  // Fake response for demo
  const resultText = `Analyzing: ${name}\n\nNutrition Facts:\n- Calories: 120\n- Sugar: 8g\n- Fat: 5g\n\nRecommendation:\nTry to avoid excess sugar and fats. Prefer fresh fruits and veggies.`;
  document.getElementById('result').textContent = resultText;
  showSection(''); // hide other sections to show result
}

// Fake barcode analysis
function analyzeProductByBarcode(barcode) {
  // Save to history
  saveHistory(`Barcode: ${barcode}`);

  // Fake response
  const resultText = `Barcode: ${barcode}\n\nProduct: Sample Snack\nCalories: 150\nSugars: 10g\nFats: 7g\n\nSuggestion: Consume moderately, prefer healthier alternatives.`;
  document.getElementById('result').textContent = resultText;
  showSection('');
}

// History saved in localStorage (simple demo)
function saveHistory(item) {
  let history = JSON.parse(localStorage.getItem('nutriHistory') || '[]');
  history.unshift(`${new Date().toLocaleString()}: ${item}`);
  if (history.length > 10) history.pop();
  localStorage.setItem('nutriHistory', JSON.stringify(history));
}

// Load and show history
function loadHistory() {
  let history = JSON.parse(localStorage.getItem('nutriHistory') || '[]');
  const list = document.getElementById('historyList');
  list.innerHTML = '';
  if (history.length === 0) {
    list.innerHTML = '<li>No history found.</li>';
    return;
  }
  history.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    list.appendChild(li);
  });
}
