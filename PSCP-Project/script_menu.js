document.getElementById('start-button').addEventListener('click', function() {
    window.open('https://justtype.vercel.app', '_self');
});

let cartoon = document.getElementById('cartoon');
let runspeed = 0;

function animateCartoon() {
    runspeed += 0.18;
    cartoon.style.left = runspeed + 'px';
    requestAnimationFrame(animateCartoon);
}

animateCartoon();