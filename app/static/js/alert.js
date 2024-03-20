

if (document.contains(document.querySelector('.alert '))) {
    setTimeout(()=> {
        document.querySelector('.alert ').remove();
    }, 2000);
}