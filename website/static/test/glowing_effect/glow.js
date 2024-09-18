// create an array of colors used for glow effects
const colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A1'];

// select the elements with the class glow
// iterate over each selected elements, with div being the current element
document.querySelectorAll('.glow').forEach((div, index) => {
    div.addEventListener('click', () => {
        // Remove existing glow class if present
        div.classList.remove('glowing');
        
        // Applies a glow effect using boxshadow css property
        div.style.boxShadow = `0 0 20px ${colors[index % colors.length]}, 0 0 30px ${colors[index % colors.length]}`;
        
        // Add glowing class to trigger the effect
        div.classList.add('glowing');
        
        // Optionally reset the glow after a short time
        setTimeout(() => {
            div.style.boxShadow = '';
        }, 1000);
    });
});
