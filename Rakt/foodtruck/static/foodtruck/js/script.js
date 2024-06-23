document.addEventListener('DOMContentLoaded', () => {
    const switchers = document.querySelectorAll('.switcher');

    switchers.forEach(item => {
        item.addEventListener('click', function() {
            console.log('Switching form');
            switchers.forEach(item => item.parentElement.classList.remove('is-active'));
            this.parentElement.classList.add('is-active');
        });
    });
});