/*
document.addEventListener('DOMContentLoaded', function() {
    const favoriteButtons = document.querySelectorAll('.toggle-favorite');

    favoriteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            const productId = this.getAttribute('data-product-id');

            fetch("{% url 'toggle_favorito' %}", { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}' 
                },
                body: JSON.stringify({ 'producto_id': productId })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else if (response.status === 401) {
                    window.location.href = "{% url 'login' %}";
                } else {
                    throw new Error('Network response was not ok.');
                }
            })
            .then(data => {
                if (data.status === 'added') {
                    this.querySelector('svg').classList.add('marked');
                    this.querySelector('svg').classList.remove('normal');
                } else if (data.status === 'deleted') {
                    this.querySelector('svg').classList.remove('marked');
                    this.querySelector('svg').classList.add('normal');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
*/

/*
$(document).ready(function() {
    $('#submitComment').click(function() {
        const formData = $('#commentForm').serialize();
        const productoId = {{ producto.id }}; 

        $.post("{% url 'detail' producto.id %}", formData + '&csrfmiddlewaretoken={{ csrf_token }}')
        .done(function(response) {
            if (response.status === 'success') {
                alert('Comentario añadido con éxito!');
                $('#commentOffcanvas').collapse('hide');
            }
        })
        .fail(function() {
            alert('Error al añadir el comentario. Por favor intenta de nuevo.');
        });
    });
});
*/