document.addEventListener('DOMContentLoaded', function() {
    
    var refreshButton = document.getElementById('refresh-btn');

    
    refreshButton.addEventListener('click', function() {
        
        fetch('/refresh-data/')
            .then(response => response.json())
            .then(data => {
                
                updateCard(data);
            })
            .catch(error => console.error('Error refreshing data:', error));
    });

    
    function updateCard(data) {
        document.querySelector('.card-img').src = data.dog_image_url;
        document.querySelector('.card-text').textContent = data.breed_name;
        document.querySelector('.card-text').textContent = data.repo;
        document.querySelector('.card-text').textContent = data.activity;
    }
});

