/*
🎓 iBall Educational JavaScript File

📌 PURPOSE:
This file adds INTERACTIVITY to the website:
- dynamic content
- events
- logic
- storage (cart system)

⚠️ IMPORTANT RULES:
- Do NOT write HTML here
- Do NOT write CSS here
- Only logic and behavior should be written
*/

// ===============================
// 🔥 Intro Screen Logic
// ===============================

/*
WHY THIS IS USED:
We show intro first, then load website after delay.
This improves UI experience.
*/

window.addEventListener("load", () => {
    setTimeout(() => {
        document.getElementById("intro").style.display = "none";
        document.getElementById("main-content").style.display = "block";
    }, 3000);
});


// ===============================
// 🛍️ PRODUCT DATA
// ===============================

/*
WHY ARRAY IS USED:
We store products in array so we can:
- loop them
- display dynamically
- update easily
*/

const products = [
    {
        id: 1,
        name: "iBall Mouse",
        price: "₹599"
    },
    {
        id: 2,
        name: "iBall Keyboard",
        price: "₹999"
    },
    {
        id: 3,
        name: "iBall Headphones",
        price: "₹1299"
    }
];


// ===============================
// 🖥️ RENDER PRODUCTS
// ===============================

/*
WHY THIS FUNCTION:
It creates product cards dynamically instead of writing HTML manually.
*/

function renderProducts() {
    const grid = document.getElementById("productGrid");
    grid.innerHTML = "";

    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("product");

        div.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;

        grid.appendChild(div);
    });
}


// ===============================
// 🛒 CART SYSTEM
// ===============================

/*
WHY LOCALSTORAGE IS USED:
- data remains saved even after refresh
- simulates real e-commerce cart
*/

let cart = JSON.parse(localStorage.getItem("cart")) || [];

function addToCart(id) {
    cart.push(id);
    localStorage.setItem("cart", JSON.stringify(cart));

    updateCartCount();
}

/*
WHY THIS FUNCTION:
It updates UI cart number live
*/

function updateCartCount() {
    document.getElementById("cartCount").innerText = cart.length;
}


// ===============================
// 🚀 INITIAL LOAD
// ===============================

/*
WHY THIS IS IMPORTANT:
Runs everything when page loads
*/

document.addEventListener("DOMContentLoaded", () => {
    renderProducts();
    updateCartCount();
});
