// Main frontend logic
function loadPage(page) {
    fetch(`/templates/${page}.html`)
        .then(res => res.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
            attachToggleHandlers();
        });
}

function attachToggleHandlers() {
    const gpu = document.getElementById('gpu-toggle');
    const transfer = document.getElementById('transfer-toggle');
    // restore toggle state
    if (gpu) {
        gpu.checked = localStorage.getItem('gpu-toggle') === 'true';
    // persist GPU toggle
        gpu.addEventListener('change', () => {
            localStorage.setItem('gpu-toggle', gpu.checked);
        });
    // restore transfer toggle state
    }
    // persist transfer toggle
    if (transfer) {
        transfer.checked = localStorage.getItem('transfer-toggle') === 'true';
        transfer.addEventListener('change', () => {
            localStorage.setItem('transfer-toggle', transfer.checked);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadPage('train');
});
