const inputText = document.getElementById('senha-gerada');
const copyButton = document.getElementById('copia-senha');

copyButton.addEventListener('click', () => {
    inputText.ariaSelected();
    document.addEventListener('copy')
});
//function copiaSenha() {
    //const inputText = document.getElementById('senha-gerada');
    //const copyButton = document.getElementById('copia-senha');

    //inputText.select();
    //document.addEventListener('copy')

    //copyButton.addEventListener('click', () => {
        //inputText.select();
        //document.addEventListener('copy');
    //});
//}