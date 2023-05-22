function password(){
    let text = document.getElementById('sign-in-password')
    let hide1 = document.getElementById('hide1');
    let hide2 = document.getElementById('hide2');

    if(text.type === 'password'){
        text.type = 'text';
        hide2.style.display = 'block';
        hide1.style.display = 'none';
    }
    else{
        text.type = 'password';
        hide2.style.display = 'none';
        hide1.style.display = 'block';
    }
}

// more class toggle
let more = document.querySelector('.more');
let navButton = document.querySelector('.nav-button');

navButton.addEventListener('click', () =>{
    more.classList.toggle('active')
})

// light/dark mode toggle
let toggleDark = document.getElementById('toggleDark');
let iconToggle = document.querySelector('.icon-toggle');
let body = document.querySelector('body');

toggleDark.addEventListener('click', () =>{
    iconToggle.classList.toggle('fa-moon')
    if(iconToggle.classList.toggle('fa-sun')){
        // body.style.background = '#fff';
        // body.style.color = '#000';
        body.style.transition = '.2s';
        more.style.background = '#fff';
        body.classList.remove('dark')
    }else{
        // body.style.background = '#000';
        // body.style.color = '#fff';
        body.style.transition = '.2s';
        more.style.background = '#000';
        body.classList.add('dark')
    }
})

let postContainer = document.querySelector('.post-container')
let postClick = document.querySelector('.create-post-click')
let cancel = document.querySelector('.cancel a')

function post(){
    if (postContainer.classList.contains('active')){
        cancel.addEventListener('click', () =>{
            postContainer.classList.remove('active')
        })
    }else{
        postClick.addEventListener('click', () =>{
            postContainer.classList.add('active')
        })
    }
    
}

let postUser = document.querySelector('.post-user .drop')
let dropdown = document.querySelector('.dropdown')

postUser.addEventListener('click', () =>{
    dropdown.classList.toggle('active')
})

let search = document.getElementById('search')
let transform = document.querySelector('.search')

search.addEventListener('click', () =>{
    transform.classList.toggle('translate')
})