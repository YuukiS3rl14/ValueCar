document.addEventListener('DOMContentLoaded', function () {
    const toggleFavoriteButtons = document.querySelectorAll('.toggle-favorite');

    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    toggleFavoriteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const autoId = this.getAttribute('data-product-id');
            const isFavorito = this.getAttribute('data-favorito') === 'true';

            if (isFavorito) {
                // Eliminar favorito
                fetch(`/favoritos/remove/${autoId}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        const heartIcon = this.querySelector('use');
                        heartIcon.setAttribute('xlink:href', '#heart');  // Corazón vacío
                        this.setAttribute('data-favorito', 'false');
                    } else {
                        console.error('Error al eliminar el favorito:', response.statusText);
                    }
                })
                .catch(error => console.error('Error:', error));
            } else {
                // Agregar favorito
                fetch(`/favoritos/add/${autoId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        const heartIcon = this.querySelector('use');
                        heartIcon.setAttribute('xlink:href', '#heart-filled');  // Corazón lleno
                        this.setAttribute('data-favorito', 'true');
                    } else {
                        console.error('Error al agregar el favorito:', response.statusText);
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    });
});