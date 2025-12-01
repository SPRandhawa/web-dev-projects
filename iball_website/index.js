alert("welcome to iball");

 window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('intro').style.display = 'none';
    const content = document.getElementById('main-content');
    content.style.display = 'block';
    content.classList.add('visible');
    document.body.style.overflow = 'auto';
  }, 6000);
});
 const toggleBtn = document.getElementById('search-toggle');
  const wrapper = document.querySelector('.search-wrapper');
  const searchBar = document.getElementById('search-bar');

  toggleBtn.addEventListener('click', (e) => {
    e.preventDefault(); // Prevent anchor default
    wrapper.classList.toggle('active');
    if (wrapper.classList.contains('active')) {
      searchBar.focus();
    }
  });

  searchBar.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      const query = searchBar.value.trim();
      if (query) {
        alert('Searching for: ' + query); // You can trigger your search logic here
      }
    }
  });
const products = [
  {
    id: 1,
    name: "iBall Wireless Mouse",
    description: "Ergonomic wireless mouse with high precision tracking.",
    price: "₹599",
    image: "download.jfif"
  },
  {
    id: 2,
    name: "iBall Over-Ear Headphones",
    description: "Comfortable headphones with deep bass and noise isolation.",
    price: "₹1,299",
    image: "download (1).jfif"
  },
  {
    id: 3,
    name: "iBall Keyboard & Mouse Combo",
    description: "Wireless combo with smooth typing and quick response.",
    price: "₹999",
    image: "download1.jfif"
  },
  {
    id: 4,
    name: "iBall Portable Bluetooth Speaker",
    description: "Compact speaker with powerful sound and 8-hour battery.",
    price: "₹1,499",
    image: "images.jfif"
  }
];

function renderProducts() {
  const grid = document.getElementById('productGrid');
  grid.innerHTML = '';

  products.forEach(product => {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.innerHTML = `
      <img src="${product.image}" alt="${product.name}">
      <div class="product-card-content">
        <h3>${product.name}</h3>
        <p>${product.description}</p>
        <div class="product-card-footer">
          <span class="price">${product.price}</span>
          <div>
            <button class="add-to-cart-button" onclick='addToCart(${JSON.stringify(product)})'>Add to Cart</button>
            <span class="favorite-icon" onclick='toggleFavorite(this, ${JSON.stringify(product)})'>♥</span>
          </div>
        </div>
      </div>
    `;
    grid.appendChild(card);
  });
}

function addToCart(product) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart.push(product);
  localStorage.setItem("cart", JSON.stringify(cart));
  updateCartCount();
}

function toggleFavorite(el, product) {
  el.classList.toggle('active');
  let favorites = JSON.parse(localStorage.getItem("favorites")) || [];

  const exists = favorites.find(p => p.id === product.id);
  if (exists) {
    favorites = favorites.filter(p => p.id !== product.id);
  } else {
    favorites.push(product);
  }

  localStorage.setItem("favorites", JSON.stringify(favorites));
}

function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  document.getElementById("cartCount").textContent = cart.length;
}

document.addEventListener('DOMContentLoaded', () => {
  renderProducts();
  updateCartCount();
});


 
const chatbotIcon = document.getElementById("chatbotIcon");
const chatbotWindow = document.getElementById("chatbotWindow");
const closeChat = document.getElementById("closeChat");

chatbotIcon.addEventListener("click", () => {
  chatbotWindow.style.display = "flex";
});

closeChat.addEventListener("click", () => {
  chatbotWindow.style.display = "none";
});

function sendMessage() {
  const input = document.getElementById("userInput");
  const chatBox = document.getElementById("chatBox");
  const userText = input.value.trim();

  if (userText === "") return;

  const userMessage = `<div class="message user"><span>${userText}</span></div>`;
  chatBox.innerHTML += userMessage;

  const botResponse = getBotResponse(userText);
  const botMessage = `<div class="message bot"><span>${botResponse}</span></div>`;
  chatBox.innerHTML += botMessage;

  chatBox.scrollTop = chatBox.scrollHeight;
  input.value = "";
}

function getBotResponse(input) {
  input = input.toLowerCase();
  if (input.includes("hello") || input.includes("hi")) {
    return "Hi there! How can I help you today?";
  } else if (input.includes("product")) {
    return "You can check our products on the Products page.";
  } else if (input.includes("email")) {
    return "You can reach us at support@example.com.";
  }
  else if (input.includes("customer care number")) {
    return "You can reach our customer care at +91 8008008008. We're available 24/7 to assist you.";
  }
   else if (input.includes("bye")) {
    return "Goodbye! Feel free to reach out if you need anything else. Have a great day!";
  }
   else {
    return "Sorry, I didn’t understand that. Please try again!";
  }
}
let generatedOTP = "";

function getOTP() {
  generatedOTP = Math.floor(100000 + Math.random() * 900000).toString();
  alert("Your OTP is: " + generatedOTP);
}

document.getElementById("signupForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const enteredOTP = document.getElementById("otp").value.trim();

  if (enteredOTP === generatedOTP) {
    alert("Signup successful!");
    this.reset();
  } else {
    alert("Invalid OTP. Please try again.");
  }
});

