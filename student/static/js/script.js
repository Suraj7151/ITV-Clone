// (function() {
//     // let list = document.querySelector('#list');
//     let dash = document.getElementById('dash');

//     dash.onclick = () => {
//         dash.classList.add('active');
//         console.log("check");
//     }

//     dash.classList.remove('active');
// })();

document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.sidebarLink');
    const currentPath = window.location.pathname;
  menuItems.forEach(item => {
    const link = item.querySelector('a');
    if (link && link.getAttribute('href') === currentPath) {
      item.classList.add('active');
    }else{
        item.classList.remove('active');
    }
  });
});




function toggleAnswer(button) {
    const answer = button.nextElementSibling;
    const isVisible = answer.style.display === 'block';
    document.querySelectorAll('.faq-answer').forEach(ans => ans.style.display = 'none');
    if (!isVisible) {
        answer.style.display = 'block';
    } else {
        answer.style.display = 'none';
    }
}

var toggleButton = document.getElementById('bars');

    toggleButton.addEventListener('click', function() {
        var sidebar = document.querySelector('#sidebars');
        var block =document.querySelector('.main')
    var otherElements = document.getElementById('MC');
        if (sidebar && toggleButton && otherElements){
            sidebar.classList.toggle('hidden');
            otherElements.classList.toggle('width')
            block.classList.toggle('shifted')
        console.log("Hiii")
        }
        
    });






document.addEventListener('DOMContentLoaded', function() {
    var progressElements = document.querySelectorAll('.moduleprogress');
    
    progressElements.forEach(function(progressElement) {
        var progressValue = progressElement.dataset.progress;
        var progressBars = document.querySelectorAll('.progressbar')
        console.log('Progress:', progressValue); 

        progressBars.forEach(function(progressBar){
            if (progressValue=='25.0'){
                progressBar.classList.add('progressbar25')
            }
            else if (progressValue=='50.0'){
                progressBar.classList.add('progressbar50')
                
            }
            else if (progressValue=='75.0'){
                
                progressBar.classList.add('progressbar75')
            }else if (progressValue=='100.0'){
               
                progressBar.classList.add('progressbar100')
            }
        })
    });
});

var selfToggle = document.getElementById('selfToggle')
var profile = document.querySelector('#profileId')

selfToggle.addEventListener('click',function(event){
    event.preventDefault();
    profile.classList.toggle('visible');
    
    console.log("Toggle");
})


document.addEventListener('DOMContentLoaded', (event) => {
    function moveButterfly() {
        const modules = document.querySelectorAll('.module');
        const butterfly = document.querySelector('.studentJourney .butterfly'); 
        const steps = document.querySelectorAll('.studentJourney > div'); 

        let lastCompletedIndex = -1;

        modules.forEach((module, index) => {
            const progress = parseInt(module.querySelector('.module-progress').getAttribute('data-progress'));

            if (progress === 100) {
                lastCompletedIndex = index;
            }
        });

        let targetStepIndex = 0; // Default to the first step

        if (lastCompletedIndex >= 0 && lastCompletedIndex < modules.length - 1) {
            targetStepIndex = lastCompletedIndex + 2;
        }

        const targetStep = steps[targetStepIndex];

        // Move the butterfly to the target module position
        if (targetStep) {
            butterfly.style.transform = `translateX(${targetStep.offsetLeft}px)`;
        }
    }

    moveButterfly();
    // You can call moveButterfly() whenever a module is completed or on certain events
});
