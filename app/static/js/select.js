const select = document.querySelectorAll('.campo-form select');


select.forEach((element)=> {
    
    element.addEventListener('focus', ()=>{
        const icon = element.parentElement.children[1];
        icon.classList.add('active');
        
    })
})

select.forEach((element)=> {
    element.addEventListener('change', ()=>{
        const icon = element.parentElement.children[1];
        icon.classList.remove('active');
    })
})


select.forEach((element)=> {
    element.addEventListener('blur', ()=>{
        const icon = element.parentElement.children[1];
        icon.classList.remove('active');
    })
})




