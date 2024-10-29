function confirmDelete(id) {

    Swal.fire({
        title: "Estas seguro?",
        text: "No es posible revertir el cambio!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Eliminado!",
                text: "El empleado a sido eliminado.",
                icon: "success"
            }).then(function() {
                window.location.href = "/deleteuser/"+id+"/";
            });
        }
    });
}