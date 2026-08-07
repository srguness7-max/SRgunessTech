// Particles.js - Neon Devre / Ağ Efekti Yapılandırması
document.addEventListener("DOMContentLoaded", function () {
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 75, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#00f3ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5 },
                "size": { "value": 3, "random": true },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#0066ff",
                    "opacity": 0.35,
                    "width": 1.2
                },
                "move": { "enable": true, "speed": 1.8 }
            },
            "interactivity": {
                "events": {
                    "onhover": { "enable": true, "mode": "grab" },
                    "onclick": { "enable": true, "mode": "push" }
                },
                "modes": {
                    "grab": { "distance": 180, "line_linked": { "opacity": 0.8 } }
                }
            }
        });
    }
});