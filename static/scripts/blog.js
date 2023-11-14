document.addEventListener('DOMContentLoaded', () => {
        // Social Buttons
        const socialBtns = document.querySelectorAll('.socials-btn')

        // Triggers the openSocialLink function
        socialBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                        const path = btn.getAttribute('path')
                        window.open(path)
                });
        });
});
