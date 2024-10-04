function checkUserPermissions() {
    // Simulación de verificación de permisos
    const userHasPermission = true; 

    if (userHasPermission) {
        document.getElementById('admin-content').style.display = 'block';
    }
}

window.onload = checkUserPermissions;