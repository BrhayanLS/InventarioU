let productTable;
let productForm;
let productIdField;
let submitButton;

function loadProducts() {
    fetch('/product')
    .then(response => response.json())
    .then(data => {
        productTable.innerHTML = '';
        data.forEach(product => {
            const row = productTable.insertRow();
            row.innerHTML = `
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>${product.quantity}</td>
                <td>${product.price}</td>
                <td>
                    <button onclick="editProduct(${product.id}, '${product.name}', ${product.quantity}, ${product.price})">Editar</button>
                    <button onclick="deleteProduct(${product.id})">Eliminar</button>
                </td>
            `;
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function resetForm() {
    productForm.reset();
    productIdField.value = '';
    btnProducto.textContent = 'Añadir Producto';
}

function editProduct(id, name, quantity, price) {
    productIdField.value = id;
    document.getElementById('name').value = name;
    document.getElementById('quantity').value = quantity;
    document.getElementById('price').value = price;
    btnProducto.textContent = 'Actualizar Producto';
}

function deleteProduct(id) {
    if (confirm('¿Estás seguro de que quieres eliminar este producto?')) {
        fetch(`/product/${id}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            console.log('Product deleted:', data);
            loadProducts();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    productForm = document.getElementById('product-form');
    productTable = document.getElementById('product-table').getElementsByTagName('tbody')[0];
    productIdField = document.getElementById('product-id');
    submitButton = document.querySelector('button[type="submit"]');

    loadProducts();

    productForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const id = productIdField.value;
        const name = document.getElementById('name').value;
        const quantity = document.getElementById('quantity').value;
        const price = document.getElementById('price').value;

        if (id) {
            fetch(`/product/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, quantity, price }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Product updated:', data);
                loadProducts();
                resetForm();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        } else {
            fetch('/product', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, quantity, price }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Product created:', data);
                loadProducts();
                resetForm();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    });
});